.. _connection:

Connection
----------

Connection takes place via the WebSockets protocol, and is initiated as soon as the frontend page is successfully loaded. Upon connection, the frontend registers itself to the backend using the :carta:ref:`REGISTER_VIEWER` message and retrieves a new session ID, server capabilities and user preferences through :carta:ref:`REGISTER_VIEWER_ACK`. It then requests the list of files in the default directory. If the connection is dropped, the frontend re-registers itself to the server, but passes through the original session ID. The server should attempt to resume this session, but if not possible, will generate a new session ID for the client. In addition to the session ID, the frontend can pass through an optional API key, which can be used to determine basic permissions and user-related settings.

A connection heartbeat is established by the server-initiated ping/pong sequence defined by the WebSocket protocol. In addition to this, a client-initiated ping/pong sequence is produced by empty messages being sent by the frontend periodically. The backend keeps track of the time since each connected client last initiated the ping/pong sequence, and makes timeout decisions based on this value.

When the frontend is intentionally closed, by closing the associated app or web page, the frontend closes the WebSocket connection gracefully, and the backend can then remove the associated session. When the frontend is closed in error, or the backend determines that a connection is timed out, the backend should maintain the session for an appropriate period, so that it can be resumed when the frontend reconnects. The frontend should attempt to reconnect with the same session ID when a connection is dropped. If the backend responds with a session type set to ``RESUMED``, the frontend will attempt to resume the session by sending a list of files, along with their associated regions in a :carta:ref:`RESUME_SESSION` message.

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Initial connection
    
    actor User
    box "Client-side"
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    User -> Frontend : Loads app/page
    activate Frontend
    Frontend -> Backend : Connects to backend (WS)
    activate Backend
    Frontend <-- Backend : Connection response (WS)
    Frontend -> Backend : REGISTER_VIEWER
    Frontend <-- Backend : REGISTER_VIEWER_ACK
    User <-- Frontend : Connection info\nupdated
    deactivate Frontend
    deactivate Backend
    

.. uml::
    
    skinparam style strictuml
    hide footbox
    title Reconnection (after dropped connection)
    
    actor User
    box "Client-side"
    participant Frontend
    end box
    
    box "Server-side" #lightblue
    participant Backend
    end box
    activate Frontend
    Frontend -> Backend : Connects to backend (WS)
    activate Backend
    Frontend <-- Backend : Connection response (WS)
    Frontend -> Backend : REGISTER_VIEWER\n(using existing sessionID)
    Frontend <-- Backend : REGISTER_VIEWER_ACK
    deactivate Frontend
    deactivate Backend
    

If the scripting interface is enabled, the backend HTTP server accepts scripting requests, acting as a proxy between a scripting client, such as a python package, and the frontend. The frontend parses a scripting command from each ``SCRIPTING_REQUEST`` message sent by the backend, executes the required code, and responds with a ``SCRIPTING_RESPONSE`` message, which includes the success state of the command, as well as a possible response in JSON format. Each incoming scripting request includes a unique ID, which is passed back in the scripting response, so that the backend can uniquely match scripting requests to their responses.

