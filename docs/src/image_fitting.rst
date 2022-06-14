.. _image-fitting:

Image fitting
-----------------

Users can fit multiple 2D Gaussian components to the selected file with the image fitting widget. Frontend sends :carta:ref:`FITTING_REQUEST` with ``file_id``, ``region_id``, and initial values. Backend fits the current channel and polarization of the file and responds with :carta:ref:`FITTING_RESPONSE`. The sequence diagram is shown below:

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Image Fitting
    
    actor User
    box "Client-side"
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box

    User -> Frontend : Set fitting parameters
    activate Frontend
    Frontend -> Backend : FITTING_REQUEST
    activate Backend
    Backend -> Backend : 2D Gaussian fitting
    Frontend <-- Backend : FITTING_RESPONSE
    deactivate Backend
    User <-- Frontend : Displays fitting results
    deactivate Frontend
    
