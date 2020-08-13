.. _changing-view-parameters:

Changing view parameters
------------------------

Contours must be re-calculated by the server when the contour parameters (levels, mode or smoothness) change.

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
    User <-- Frontend: Displays updated image
    deactivate Backend
    deactivate Frontend
    

However, as contour rendering is done on the frontend, any changes to the contour rendering configuration (visibility, opacity, thickness, colour, line style) do not require any server interaction. Similarly for raster images: As all the rendering is done on the frontend, any changes to the raster rendering configuration (colour map, range, scaling type) do not require any interaction between frontend and backend:

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
    

