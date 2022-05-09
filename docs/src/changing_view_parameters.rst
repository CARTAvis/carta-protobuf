.. _changing-view-parameters:

Changing view parameters
------------------------

Contours must be re-calculated by the server when the contour parameters (levels, mode or smoothness) change. However, as contour rendering is done on the frontend, any changes to the contour rendering parameters (visibility, opacity, thickness, colour, line style) do not require any server interaction.

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Updating contour parameters
    
    actor User
    box "Client-side" #EDEDED
            participant Frontend
    end box
    
    box "Server-side" #lightblue
    	participant Backend
    end box
    User -> Frontend: Changes contour\nparameters
    activate Frontend
    Frontend -> Backend : SET_CONTOUR_PARAMETERS
    activate Backend
    Frontend <-- Backend : CONTOUR_IMAGE_DATA
    deactivate Backend
    User <-- Frontend: Displays updated image
    User -> Frontend: Changes rendering\nparameters
    User <-- Frontend: Displays updated image
    deactivate Frontend
    

Similarly for raster images: As all the rendering is done on the frontend, any changes to the raster rendering configuration (colour map, range, scaling type) do not require any interaction between frontend and backend:

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Changing colour maps, range or scaling type\n(no server interaction required)
    
    actor User
    box "Client-side"	
            participant "GPU"
            participant Frontend
    end box
    
    box "Server-side" #lightblue
    	participant Backend
    end box
    
    User -> Frontend : Changes parameter
    activate Frontend
    Frontend -> GPU : Shader parameters
    deactivate Frontend
    activate GPU
    GPU -> GPU : Render image\n(Color mapping,\ncomposition etc)
    User <-- GPU : Display image
    deactivate GPU
    
Vector overlay rendering requires image data for both the vector angle (normally calculated from polarization angle *PA*) and length/intensity (normally calculated from polarized intensity *PI*). The image data is first downsampled on the backend using block downsampling with an even block width, and then masked with a threshold value. Adjusting the block width or threshold value will require the data to be recalculated and streamed by the backend. The backend streams data tile-by-tile.

.. uml::

    skinparam style strictuml
        hide footbox
        title Updating vector overlay parameters

        actor User
        box "Client-side" #EDEDED
                participant Frontend
        end box

        box "Server-side" #lightblue
            participant Backend
        end box
        User -> Frontend: Changes vector overlay\nparameters
        activate Frontend
        Frontend -> Backend: SET_VECTOR_OVERLAY_PARAMETERS
        activate Backend
        Backend -> Backend: Reads required\ndata from disk
        Backend -> Backend: Generates PA/PI tiles
        Backend -> Backend: Compresses using ZFP
        Frontend <-- Backend: VECTOR_OVERLAY_TILE_DATA\n(progress < 1.0)
        Frontend -> Frontend: Processes tile and\ngenerates vertices
        User <-- Frontend: Displays partial\noverlay image
        Frontend <-- Backend: VECTOR_OVERLAY_TILE_DATA\n(progress < 1.0)
        Frontend -> Frontend: Processes tile and\ngenerates vertices
        User <-- Frontend: Displays partial\noverlay image
        Frontend <-- Backend: VECTOR_OVERLAY_TILE_DATA\n(progress = 1.0)
        deactivate Backend
        Frontend -> Frontend: Processes tile and\ngenerates vertices
        User <-- Frontend: Dispalys complete\noverlay image
        deactivate Frontend
