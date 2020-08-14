.. _presentation-layer:

Presentation layer
------------------

Messages are encoded using the Protocol Buffers message format, which encodes into a binary format. Each message is prepended by a 64-bit structure, consisting of:

-  16-bit unsigned integer, used to identify the message type, specified by :carta:ref:`EventType`
-  16-bit unsigned integer, used to determine the ICD version
-  32-bit unsigned integer, used to uniquely identify requests and corresponding responses. In the case of messages with no corresponding request, such as data stream messages, this integer will be ignored.

Using an 8-byte header prevents byte alignment issues from cropping up. End points decode the message by splitting it into two sections: the 8-byte identifier header and the payload. The identifier header is used to determine which Protocol Buffer definition should be used to decode the payload, and which request corresponds to which response. The ICD version integer (shown at the top of this document) should match the major version of this document (also shown at the top of this document). Any changes to the protocol buffer definitions that would render older backend or frontend implementations incompatible should result in incrementing the ICD version number, and a corresponding change to this document’s version number.

**Implementation note:** The protocol buffer style guide [`6 <https://developers.google.com/protocol-buffers/docs/style>`__] expects snake_case for field names. The protobuf c++ compiler leaves names in snake_case, while the javascript compiler leaves field names in camelCase. So a field accessed via ``msg.min_val() in c++`` would be accessed by ``msg.minVal`` in javascript.

