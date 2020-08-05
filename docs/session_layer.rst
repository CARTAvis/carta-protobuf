.. _session-layer:

Session Layer
-------------

Sessions will utilise the the WebSocket protocol, as the frontend will be browser-based. Initial session establishment will occur using HTTP, and then be upgraded to WebSocket. Session management will be handled by a session ID being passed from backend to frontend on initial connection. If the frontend is disconnected without closing the session explicitly, the session ID can be passed to the backend upon reconnection to resume the session, although this is not currently supported.

