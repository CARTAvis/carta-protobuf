.. _image-fitting:

Image fitting
-----------------

Users can fit multiple 2D Gaussian components to the selected file with the image fitting widget. Frontend sends :carta:ref:`FITTING_REQUEST` with ``file_id``, ``region_id``, ``initial_values``, and other settings. Backend fits the current channel and polarization of the file. For each fitting iteration, backend sends back :carta:ref:`FITTING_PROGRESS` to update the progress. When the fitting is complete, backend responds with :carta:ref:`FITTING_RESPONSE`.
Users can cancel the requested fitting with the progress widget. Frontend sends :carta:ref:`STOP_FITTING`, and backend sents back :carta:ref:`FITTING_RESPONSE` after the fitting is canceled.
The sequence diagram is shown below:

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
    Backend -> Backend : Setup 2D Gaussian fitting
    loop
        Backend -> Backend : One fitting iteration
        Frontend <-- Backend : FITTING_PROGRESS
    end
    User -> Frontend : (Cancels the requested fitting)
    Frontend -> Backend : (STOP_FITTING)
    Frontend <-- Backend : FITTING_RESPONSE
    deactivate Backend
    User <-- Frontend : Displays fitting results
    deactivate Frontend

