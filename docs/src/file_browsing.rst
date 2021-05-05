.. _file-browsing:

File browsing
-------------

The file browser displays a list of files in the selected directory, along with some basic information on each file (type, size) and a list of subdirectories. If a file contains multiple HDUs (or equivalent), a list of HDU names is included. If a file is selected in the file browser, additional information is shown. A specific HDU of a file can be selected. When a subdirectory is selected, the file list is fetched for that subdirectory. When a file is loaded, the default image view is requested. A file can be loaded as a raster or contour image (not currently implemented), and can be appended to the current list of open files, or can replace all open files, in which case the frontend must first close all files using the :carta:ref:`CLOSE_FILE` message with ``file_id = -1``. Individual open files can be removed from the file list by calling :carta:ref:`CLOSE_FILE` with an appropriate ``file_id`` field.

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Change file browser sub-directory
    
    actor User
    box "Client-side" #EDEDED
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    activate Frontend
    User -> Frontend : Selects sub-directory
    Frontend -> Backend : FILE_LIST_REQUEST/ \n REGION_LIST_REQUEST
    activate Backend
    Backend -> Backend : Finds file in sub-directory
    Frontend <-- Backend : FILE_LIST_PROGRESS
    User -> Frontend : (Cancels the file/region list)
    Frontend -> Backend : (STOP_FILE_LIST)
    Frontend <-- Backend : FILE_LIST_RESPONSE/ \n REGION_LIST_RESPONSE
    deactivate Backend
    User <-- Frontend : Displays updated\n file browser
    deactivate Frontend
    

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Fetching file info
    
    actor User
    box "Client-side"  #EDEDED
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    activate Frontend
    User -> Frontend : Selects file
    Frontend -> Backend : FILE_INFO_REQUEST
    activate Backend
    Backend -> Backend : Determines file info\n from header
    Frontend <-- Backend : FILE_INFO_RESPONSE
    deactivate Backend
    User <-- Frontend : Displays info\n for selected file
    deactivate Frontend
    

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Opening a file as a new frame (appending)
    
    actor User
    box "Client-side"  #EDEDED	
            participant Frontend
    end box
    
    box "Server-side" #lightblue
    	participant Backend
    end box
    group File load
    User -> Frontend : Loads file\n(as new frame)
    activate Frontend
    Frontend -> Backend : OPEN_FILE
    activate Backend
    Backend -> Backend : Loads file
    Frontend <-- Backend : OPEN_FILE_ACK
    Frontend <-- Backend : REGION_HISTOGRAM_DATA
    deactivate Backend
    end
    group Image view
    Frontend -> Backend : SET_IMAGE_CHANNELS
    activate Backend
    Frontend <-- Backend : RASTER_TILE_DATA
    deactivate Backend
    User <-- Frontend: Displays image
    deactivate Frontend
    end
    

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Opening a file\n(replacing open files)
    
    actor User
    box "Client-side"  #EDEDED	
            participant Frontend
    end box
    
    box "Server-side" #lightblue
    	participant Backend
    end box
    group File load
    User -> Frontend : Loads file\n(replace existing\nframes)
    activate Frontend
    Frontend -> Backend : CLOSE_FILE
    Frontend -> Frontend : Removes regions
    Backend -> Backend : Closes files and\n removes regions
    Frontend -> Backend : OPEN_FILE
    activate Backend
    Backend -> Backend : Loads file
    Frontend <-- Backend : OPEN_FILE_ACK
    Frontend <-- Backend : REGION_HISTOGRAM_DATA
    deactivate Backend
    end
    group Image view
    Frontend -> Backend : SET_IMAGE_CHANNELS
    activate Backend
    Frontend <-- Backend : RASTER_TILE_DATA
    deactivate Backend
    User <-- Frontend: Displays image
    deactivate Frontend
    end
    

