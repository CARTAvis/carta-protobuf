.. _data-cube-navigation:

Data cube navigation
--------------------

The frontend can change the displayed channel and Stokes parameter by issuing the :carta:ref:`SET_IMAGE_CHANNELS` command. When an image is opened, the frontend will send a :carta:ref:`SET_IMAGE_CHANNELS` with the first channel and Stokes parameter. The frontend subscribes to all :carta:ref:`RASTER_TILE_DATA` messages.

Tiled rendering splits the image into individual square tiles (defaulting to 256 pixels in width), and renders the image progressively as tiles arrive from the backend. This is more efficient when exploring a large image, as it reuses data when panning and zooming around the image. Images are downsampled by a power of 2.

In addition, contour rendering can be used on files. The contours for an entire channel are generated when the frontend sends the :carta:ref:`SET_CONTOUR_PARAMETERS` command. The frontend subscribes to all :carta:ref:`CONTOUR_IMAGE_DATA` messages. Currently, contour renders are automatically updated when the user changes channel or plays an animation. Contours are delivered in separate chunks by the backend, so that the user can see the contours as they are delivered to the frontend, and can get an idea of how long the contour fetching will take.

.. _Zooming and panning:

Zooming and panning
~~~~~~~~~~~~~~~~~~~

The frontend can request specific tiles of an image to be delivered. Tiles are specified using the widely used a `tiled web map <https://en.wikipedia.org/wiki/Tiled_web_map>`__ convention (commonly used in GIS and online image viewer software). Each tile is defined by three coordinates: The layer, x and y coordinates. The zeroth layer consists of the entire image, down-sampled until it is stored in a single tile, with both width and height less than or equal to a chosen tile size (defaulting to 256 pixels, but this may increase in future to 512 pixels for large format screens). The tile size must be a multiple of four, due to the ZFP algorithm’s block size. Each subsequent layer doubles in width and height, to the point where the highest layer (*N*) contains the entire image in full resolution, split into fixed-size tiles (tiles along the right and top edges of the image will have reduced width and height respectively).

Tile coordinates (``layer``, ``x`` and ``y``) are encoded into a single 32-bit integer before sending. There are two primary reasons for this:

-  Using a struct as a key in a map on either frontend or backend would be more complicated, and require a custom hash function. JavaScript ``Map`` objects do not support this. Storing tiles within a map-of-maps-of-maps would be less efficient.
-  Encoding and decoding an array of structs in a protocol buffer object would be less efficient in terms of CPU time and network storage

The encoded integer consists of:

-  12 bits for the X and Y coordinate. This limits the implementation to at most 4096 tiles along either axis. With a default tile size of 256 pixels, this means images must be smaller than 1.04 million pixels in width and height.
-  7 bits for the layer coordinate. This limits the implementation to 128 layers. However, this limitation is artificial, since at most 12 layers will be required, given the above limitation of 4096 tiles
-  1 bit left over, because JavaScript bit shifting is done on signed integers, rather than unsigned

Encoding and decoding is a simple and lightweight process using some bit shifting. A single line JavaScript function to encode is:

``(x, y, layer) => (layer << 24) | (y << 12) | x;``

When a user zooms or pans, the frontend sends the :carta:ref:`ADD_REQUIRED_TILES` command to the backend. The frontend may debounce, throttle or delay sending tiles to the backend, in order to optimise delivery and avoid sending stale tiles. The order of the list of tiles supplied to :carta:ref:`ADD_REQUIRED_TILES` determines the order in which the backend delivers tiles. If subsequent :carta:ref:`ADD_REQUIRED_TILES` messages arrive while the backend is still delivering tiles, the most recent tile list is prioritised.

Another route for optimisation available to the frontend is :carta:ref:`REMOVE_REQUIRED_TILES`, which allows the frontend to explicitly indicate that certain tiles are no longer required. If any of these tiles are yet to be delivered to the frontend, the backend can optimise tile delivery by removing them from the queue of titles to be delivered.

Tile data is delivered by the backend using the :carta:ref:`RASTER_TILE_DATA` stream. This allows the backend to send one or more raster tiles with the same compression format and quality to the frontend. Each time a tile is delivered to the frontend, the image is re-rendered.

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Altering image view
    
    actor User
    box "Client-side" #EDEDED	
            participant Frontend
    end box
    
    box "Server-side" #lightblue
    	participant Backend
    end box
    User -> Frontend: Pans or zooms image
    activate Frontend
    Frontend -> Backend : ADD_REQUIRED_TILES
    activate Backend
    Frontend <-- Backend : RASTER_TILE_DATA
    User <-- Frontend: Displays updated image
    Frontend <-- Backend : RASTER_TILE_DATA
    User <-- Frontend: Displays updated image
    Frontend <-- Backend : RASTER_TILE_DATA
    User <-- Frontend: Displays updated image
    deactivate Backend
    deactivate Frontend
    

.. _Channel navigation:

Channel navigation
~~~~~~~~~~~~~~~~~~

When changing channels via a :carta:ref:`SET_IMAGE_CHANNELS` message, the frontend includes an initial list of required tiles. These tiles are then delivered individually by the backend. Unlike the case when zooming and panning, the frontend will wait for all required tiles to be delivered before displaying an image when switching channels. When receiving a :carta:ref:`SET_IMAGE_CHANNELS` message, the backend will also send the new channel histogram via the :carta:ref:`REGION_HISTOGRAM_DATA` stream.

In general, one image view command will correspond to a subsequent image data stream message. However, changing the image channel will result in a subsequent image data stream message, as well as any relevant updated statistics, histograms or profile data.

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Altering image channel
    
    actor User
    box "Client-side" #EDEDED	
            participant Frontend
    end box
    
    box "Server-side" #lightblue
    	participant Backend
    end box
    User -> Frontend: Changes channel\nor Stokes
    activate Frontend
    Frontend -> Backend : SET_IMAGE_CHANNELS
    activate Backend
    Backend -> Backend: Calculates which\nanalytics need\nupdates
    Backend -> Backend: Calculates\nchannel histogram
    Frontend <-- Backend : REGION_HISTOGRAM_DATA
    Frontend <-- Backend : RASTER_TILE_DATA
    Frontend <-- Backend : RASTER_TILE_DATA
    Frontend <-- Backend : RASTER_TILE_DATA
    User <-- Frontend: Displays updated\nimage
    Backend -> Backend: Calculates\nremaining analytics
    Frontend <-- Backend : SPATIAL_PROFILE_DATA
    deactivate Backend
    User <-- Frontend: Displays updated\nplots
    deactivate Frontend
    

.. _Animation:

Animation
~~~~~~~~~

An animation can be played back by issuing the :carta:ref:`START_ANIMATION` command. This command encapsulates all the different animation stepping and bounds parameters, in order to allow the backend to perform frame calculations and deliver image data to the front. After the the :carta:ref:`START_ANIMATION` command has been issued, the backend sends required images and analysis results of the active and spectrally matched images to the frontend at a regular interval. When the user stops an animation, the frontend sends the :carta:ref:`STOP_ANIMATION` command, which includes information on the current image’s channels, so that the backend can be sure that the frontend channel state is the same as that of the backend. If the last sent frame does match the frontend channel state, the backend adjusts channels again. In order to prevent the backend from sending too many animation frames, some basic flow control is provided through :carta:ref:`ANIMATION_FLOW_CONTROL` message. This is sent from the frontend to the backend to indicate the latest frame of the active image received, preventing the backend from queuing up too many frames. The :carta:ref:`START_ANIMATION` command includes an :carta:ref:`ADD_REQUIRED_TILES` sub-message, specifying the required tiles and compression type to be used in the animation. The backend includes an animation ID field in :carta:ref:`START_ANIMATION_ACK` in order to allow the frontend to differentiate between frames of previous animations and the latest animation.

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Animation playback
    
    actor User
    box "Client-side" #EDEDED
            participant Frontend
    end box
    
    box "Server-side" #lightblue
    	participant Backend
    end box
    User -> Frontend: Requests animation\nplayback
    activate Frontend
    Frontend -> Backend : START_ANIMATION
    activate Backend
    Frontend <-- Backend : START_ANIMATION_ACK
    Group For each image
        Frontend <-- Backend : Required contours, vectors, analytics...
        alt Visible image
            Frontend <-- Backend : RASTER_TILE_SYNC
            Frontend <-- Backend : RASTER_TILE_DATA
            Frontend <-- Backend : RASTER_TILE_SYNC
        end
    end
    Frontend -> Backend: ANIMATION_FLOW_CONTROL (active image)
    User <-- Frontend: Displays updated image
    Group For each image
        Frontend <-- Backend : Required contours, vectors, analytics...
        alt Visible image
            Frontend <-- Backend : RASTER_TILE_SYNC
            Frontend <-- Backend : RASTER_TILE_DATA
            Frontend <-- Backend : RASTER_TILE_SYNC
        end
    end
    Frontend -> Backend: ANIMATION_FLOW_CONTROL (active image)
    User <-- Frontend: Displays updated image
    Group For each image
        Frontend <-- Backend : Required contours, vectors, analytics...
        alt Visible image
            Frontend <-- Backend : RASTER_TILE_SYNC
            Frontend <-- Backend : RASTER_TILE_DATA
            Frontend <-- Backend : RASTER_TILE_SYNC
        end
    end
    Frontend -> Backend: ANIMATION_FLOW_CONTROL (active image)
    User <-- Frontend: Displays updated image
    User -> Frontend : Stops playback
    Frontend -> Backend : STOP_ANIMATION
    Frontend -> Backend : SET_IMAGE_CHANNELS
    Frontend <-- Backend : RASTER_TILE_DATA
    Frontend <-- Backend : RASTER_TILE_DATA
    deactivate Frontend
    deactivate Backend
    

Active and visible spectrally matched images are sent as tiled data. For each image, the backend first sends the :carta:ref:`RASTER_TILE_SYNC` message with `end_sync` false. Tiled data are then sent with :carta:ref:`RASTER_TILE_DATA`. After all the tiles are sent, the backend sends the :carta:ref:`RASTER_TILE_SYNC` message again with `end_sync` true. In order to keep the image view channel and full image histogram synchronised, :carta:ref:`REGION_HISTOGRAM_DATA` messages are sent to the frontend, containing the channel histogram for the new channel. During animation playback, each animation step will result in image data stream messages, as well as any relevant analytics updates, including :carta:ref:`SPATIAL_PROFILE_DATA`, :carta:ref:`REGION_STATS_DATA`, :carta:ref:`CONTOUR_IMAGE_DATA`, and :carta:ref:`VECTOR_OVERLAY_TILE_DATA`. If zooming or panning occurs during animation, or if an image becomes visible or invisible in the image view panel, :carta:ref:`ADD_REQUIRED_TILES` messages of the frames are sent to the backend, updating the requirements. These new requirements are used in the next frame generated by the backend.

