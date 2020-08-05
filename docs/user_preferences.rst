.. _user-preferences:

User preferences
----------------

If the backend supports the :ref:`USER_PREFERENCES <serverfeatureflags>` server feature flag, the frontend will expect all the user’s preferences (default settings, color maps, interaction preferences and others) to be included in the :ref:`REGISTER_VIEWER_ACK <registerviewerack>` message. Changes to the user preferences can be made by the frontend through the :ref:`SET_USER_PREFERENCES <setuserpreferences>` control message. Each preference to be updated, along with the updated value, is stored as a map. User preference entries can be removed from the server by sending a :ref:`SET_USER_PREFERENCES <setuserpreferences>` message with a map of preference keys with empty values.

If the backend supports the :ref:`USER_LAYOUTS <serverfeatureflags>` server feature flag, the frontend will expect all the user’s custom UI layouts to be included in the :ref:`REGISTER_VIEWER_ACK <registerviewerack>` message. Changes to individual layouts (adding, updating or removing) are updated through the :ref:`SET_USER_LAYOUT <setuserlayout>` control message.

