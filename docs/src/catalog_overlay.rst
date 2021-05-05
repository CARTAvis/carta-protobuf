.. _catalog-overlay:

Catalog overlay
---------------

.. _Sequence Diagrams:

Sequence Diagrams
~~~~~~~~~~~~~~~~~

Catalog file list

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Changing Catalog File browser sub-directory
    
    actor User
    box "Client-side" #EDEDED
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    activate Frontend
    User -> Frontend : Selects sub-directory
    Frontend -> Backend : CATALOG_FILE_LIST_REQUEST
    activate Backend
    Backend -> Backend : Finds file in \n sub-directory
    Frontend <-- Backend : CATALOG_LIST_PROGRESS
    User -> Frontend : (Cancels the Catalog file list)
    Frontend -> Backend : (STOP_CATALOG_LIST)
    Frontend <-- Backend : CATALOG_FILE_LIST_RESPONSE
    deactivate Backend
    User <-- Frontend : Displays updated \n file browser
    deactivate Frontend
    

Catalog file info

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Fetching Catalog File Info
    
    actor User
    box "Client-side" #EDEDED
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    activate Frontend
    User -> Frontend : Selects file
    Frontend -> Backend : CATALOG_FILE_INFO_REQUEST
    activate Backend
    Backend -> Backend : Analyzes XML file
    Frontend <-- Backend : CATALOG_FILE_INFO_RESPONSE
    deactivate Backend
    User <-- Frontend : Displays catalog info\n for user selected file
    deactivate Frontend
    

Opening catalog file

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Opening Catalog File
    
    actor User
    box "Client-side" #EDEDED
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    activate Frontend
    group File Load
        alt Loads file 
            User -> Frontend : Loads catalog file
            Frontend -> Backend : OPEN_CATALOG_FILE
            activate Backend
            Backend -> Backend : Analyzes XML file
            Backend --> Frontend : OPEN_CATALOG_FILE_AFK
            deactivate Backend
            Frontend -> Frontend : Loads preview data \n into catalog widget
            Frontend -> User : Opens catalog widget \n with selected file
        else can not catalog open file
            User -> Frontend : Loads catalog file
            Frontend -> Backend : OPEN_CATALOG_FILE
            activate Backend
            Backend -> Backend : Analyzes XML file
            Backend --> Frontend : OPEN_CATALOG_FILE_AFK
            deactivate Backend 
            Frontend -> User : Displays error message
        end
    end
    deactivate Frontend
    

Catalog file data stream

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Catalog data stream
    
    actor User
    box "Client-side" #EDEDED
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    activate Frontend
        group Catalog Widget
        User -> Frontend : Applies filters
        Frontend -> Backend : CATALOG_FILTER_REQUEST
        activate Backend
        Backend -> Backend : Filters catalog data
        Backend --> Frontend : CATALOG_FILTER_RESPONSE (preview data)
        deactivate Backend
        Frontend -> User : updates catalog table \n view with preview data
    
        User -> Frontend : Applies sort
        Frontend -> Backend : CATALOG_FILTER_REQUEST
        activate Backend
        Backend -> Backend : sorts catalog data
        Backend --> Frontend : CATALOG_FILTER_RESPONSE (preview data)
        deactivate Backend
        Frontend -> User : updates catalog table \n view with preview data
    
        User -> Frontend : addes displayed column
        Frontend -> Backend : CATALOG_FILTER_REQUEST
        activate Backend
        Backend -> Backend : addes column data
        Backend --> Frontend : CATALOG_FILTER_RESPONSE (preview data)
        deactivate Backend
        Frontend -> User : updates catalog table \n view with preview data
    
        User -> Frontend : requests more data \n (scroll in table view)
        Frontend -> Backend : CATALOG_FILTER_REQUEST
        activate Backend
        Backend -> Backend : addes more data
        Backend --> Frontend : CATALOG_FILTER_RESPONSE (request data)
        deactivate Backend
        Frontend -> User : updates catalog table
    
        User -> Frontend : loads all catalog \n data into image \n viewer or subplots
        Frontend -> Backend : CATALOG_FILTER_REQUEST
        activate Backend
        Backend -> Backend : begins calculation
        Backend --> Frontend : CATALOG_FILTER_RESPONSE (partial)
        Frontend -> User : updates catalog table, \n image viewer or subplots
        Backend -> Backend : continues calculation
        Backend --> Frontend : CATALOG_FILTER_RESPONSE (partial)
        Frontend -> User : updates catalog table, \n image viewer or subplots
        Backend -> Backend : completes calculation
        Backend --> Frontend : CATALOG_FILTER_RESPONSE (complete)
        deactivate Backend
        Frontend -> User : updates catalog table, \n image viewer or subplots
        end
    deactivate Frontend
    

Closing catalog file

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Closing Catalog File
    
    actor User
    box "Client-side" #EDEDED
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    activate Frontend
    User -> Frontend : Closes catalog file
    Frontend -> Backend : CATALOG_CLOSE_FILE
    activate Backend
    Backend -> Backend : Closes file
    deactivate Backend 
    Frontend <-- Frontend : Removes catalog \n table view, \n image view and \n subplots view
    User <-- Frontend : Displays next \n avaliable catalog file \n which associated with \n current actived frame
    deactivate Frontend
    


