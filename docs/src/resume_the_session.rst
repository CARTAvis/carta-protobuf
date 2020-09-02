.. _resume-the-session:

Resume the session
------------------

The basic idea is that, when the frontend reconnects to the backend (with :carta:ref:`REGISTER_VIEWER`), it would also send some state information, such as:

-  list of open files, along with their IDs and the current channels and stokes
-  list of regions for each file, along with all their properties

Users can choose whether to resume the session while reconnected. If yes, then the backend would then reconstruct the session based on the frontend's message, by opening files again, changing to the appropriate channels, and so on, and then adding the regions and then set requirements.

There are two use cases for resuming with an existing session ID, and a third where resume is not possible.

#. Backend is restarted, frontend connects, frontend sends state information.

   #. Frontend sends :carta:ref:`REGISTER_VIEWER` with session_id > 0.
   #. Restarted backend has no session_ids, :carta:ref:`REGISTER_VIEWER_ACK` sets session_type=RESUMED\ *.* Backend creates new Session with given session_id (On Connect).
   #. Frontend sends state to backend, i.e., sends :carta:ref:`RESUME_SESSION` message with state information, backend responds with :carta:ref:`RESUME_SESSION_ACK`.
   #. Backend sets state in newly-created Session.

#. Network connection drops, frontend reconnects to backend with existing session id.

   #. While the network connection drops. It seems the uWebsocket has a default timeout setting for 15,000 ms (need to verify). For the new version of uWebsocket, we can set the timeout via the variable “\ *.idleTimeout”*. On Disconnect is called after the timeout and then backend deletes Session.
   #. Frontend sends :carta:ref:`REGISTER_VIEWER` with session_id > 0.
   #. Backend has session_id, :carta:ref:`REGISTER_VIEWER_ACK` sets session_type=RESUMED. Frontend sends state to backend with :carta:ref:`RESUME_SESSION`, and backend responses with :carta:ref:`RESUME_SESSION_ACK`.
   #. Backend sets state in existing Session, requirements trigger sending data streams (possibly cached).

#. Frontend is restarted, has no existing session id so cannot resume even though backend continues.

   #. Frontend sends :carta:ref:`REGISTER_VIEWER` with session_id = 0.
   #. Backend creates a new Session, :carta:ref:`REGISTER_VIEWER_ACK` sets session_type=NEW.
   #. The Session will be deleted immediately while the frontend is restarted.

