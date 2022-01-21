.. _application-layer:

Application Layer
-----------------

Interface communication messages fall into three overall categories:

-  **Control messages** (along with any associated acknowledgement responses), which are used to modify the state of the backend from the frontend. Example of this would be starting a new session, moving the cursor or updating region parameters. Each message from the frontend correspond to zero or one acknowledgement response from the backend. Message names for this category follow the naming convention :f2b:`MESSAGE_NAME` and :b2f:`MESSAGE_NAME_ACK`
-  **Request messages** (along with the required responses), which are used to explicitly request information from the backend without explicitly changing the backend state. Examples of this would be requesting a file list. The frontend will wait for a response for each request of this type, and callbacks or promises will be used to execute code based on the returned response. As each request needs to be mapped to response, messages in this category must include a unique requestID entry. Each message from the frontend in this category corresponds to exactly one response from the backend. Message names for this category follow the naming convention :f2b:`MESSAGE_NAME_REQUEST` and :b2f:`MESSAGE_NAME_RESPONSE`
-  **Data flow messages**, which flow from the backend to the frontend without an originating front end request. These messages are used for pushing updated data from the backend to the frontend. Examples of this type would be image data, region statistics, profile data and cursor values. The appropriate mechanism for dealing with these messages in the frontend is a observable/subscription-based approach. As there is no request/response combination for messages in this category, there is no prescribed message naming convention.

**Implementation note:** The backend should implement a command queue for control messages, so that high priority messages are executed first, and cause the backend to disregard any queued-up control messages that are no longer relevant. As an example: moving the cursor across the image will result in a large number of control messages being sent to the backend. Each of these control messages could result in a data flow message with new cursor and profile information, which may take some time to calculate. If a file is closed by the frontend, the backend no longer needs to process any remaining cursor messages relating to this file, and those messages should be removed from the queue.

**Message definitions shown in** :f2b:`blue` **are used for frontend ->backend communication. Message definitions shown in** :b2f:`red` **are used for backend->frontend communication.**

