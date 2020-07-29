

.. CARTA.CatalogFileInfoRequest:

CatalogFileInfoRequest
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  |  |
+-------+------+-------+-------------+
| name | string |  |  |
+-------+------+-------+-------------+



.. CARTA.CatalogFileInfoResponse:

CatalogFileInfoResponse
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  |  |
+-------+------+-------+-------------+
| message | string |  |  |
+-------+------+-------+-------------+
| file_info `CatalogFileInfo <CARTA.CatalogFileInfo>`__  |  |
+-------+------+-------+-------------+
| headers `CatalogHeader <CARTA.CatalogHeader>`__ repeated |  |
+-------+------+-------+-------------+






.. CARTA.CatalogListRequest:

CatalogListRequest
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  |  |
+-------+------+-------+-------------+



.. CARTA.CatalogListResponse:

CatalogListResponse
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  |  |
+-------+------+-------+-------------+
| message | string |  |  |
+-------+------+-------+-------------+
| directory | string |  |  |
+-------+------+-------+-------------+
| parent | string |  |  |
+-------+------+-------+-------------+
| files `CatalogFileInfo <CARTA.CatalogFileInfo>`__ repeated |  |
+-------+------+-------+-------------+
| subdirectories | string | repeated |  |
+-------+------+-------+-------------+






.. CARTA.FileInfoRequest:

FileInfoRequest
^^^^^^^^^^^^^

FILE_INFO_REQUEST:
Requests the file info for a specific file.
Backend responds with FILE_INFO_RESPONSE


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  | Required directory name |
+-------+------+-------+-------------+
| file | string |  | Required file name |
+-------+------+-------+-------------+
| hdu | string |  | Required HDU name (if applicable). If left empty, the first HDU is selected |
+-------+------+-------+-------------+



.. CARTA.FileInfoResponse:

FileInfoResponse
^^^^^^^^^^^^^

FILE_INFO_RESPONSE
Response for FILE_INFO_REQUEST.
Gives information on the requested file


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether the FILE_INFO_REQUEST was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| file_info `FileInfo <CARTA.FileInfo>`__  | Basic file info (type, size) |
+-------+------+-------+-------------+
| file_info_extended `FileInfoExtended <CARTA.FileInfoExtended>`__  | Extended file info (WCS, header info) |
+-------+------+-------+-------------+






.. CARTA.FileListRequest:

FileListRequest
^^^^^^^^^^^^^

FILE_LIST_REQUEST:
Requests the list of available files for a given directory.
Backend responds with FILE_LIST_RESPONSE


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  | Required directory name |
+-------+------+-------+-------------+



.. CARTA.FileListResponse:

FileListResponse
^^^^^^^^^^^^^

FILE_LIST_RESPONSE
Response for FILE_LIST_REQUEST.
Gives a list of available files (and their types), as well as subdirectories


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether the FILE_LIST_REQUEST was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| directory | string |  | Directory of listing |
+-------+------+-------+-------------+
| parent | string |  | Directory parent (null/empty if top-level) |
+-------+------+-------+-------------+
| files `FileInfo <CARTA.FileInfo>`__ repeated | List of available image files, with file type information and size information. |
+-------+------+-------+-------------+
| subdirectories | string | repeated | List of available subdirectories |
+-------+------+-------+-------------+






.. CARTA.RegionFileInfoRequest:

RegionFileInfoRequest
^^^^^^^^^^^^^

REGION_FILE_INFO_REQUEST:
Requests contents for a specific region file on the server
Backend responds with REGION_FILE_INFO_RESPONSE


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  | Required directory name |
+-------+------+-------+-------------+
| file | string |  | Required file name |
+-------+------+-------+-------------+



.. CARTA.RegionFileInfoResponse:

RegionFileInfoResponse
^^^^^^^^^^^^^

REGION_FILE_INFO_RESPONSE
Response for REGION_FILE_INFO_REQUEST.
Gives information on the requested file


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether the REGION_INFO_REQUEST was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| file_info `FileInfo <CARTA.FileInfo>`__  | Basic info about region file |
+-------+------+-------+-------------+
| contents | string | repeated | Contents of file; each string is a line |
+-------+------+-------+-------------+






.. CARTA.RegionListRequest:

RegionListRequest
^^^^^^^^^^^^^

REGION_LIST_REQUEST:
Requests the list of available region files for a given directory.
Backend responds with REGION_LIST_RESPONSE


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  | Required directory name |
+-------+------+-------+-------------+



.. CARTA.RegionListResponse:

RegionListResponse
^^^^^^^^^^^^^

REGION_LIST_RESPONSE
Response for REGION_LIST_REQUEST.
Gives a list of available region files (and their types), as well as subdirectories


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether the REGION_LIST_REQUEST was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| directory | string |  | Directory of listing |
+-------+------+-------+-------------+
| parent | string |  | Directory parent (null/empty if top-level) |
+-------+------+-------+-------------+
| files `FileInfo <CARTA.FileInfo>`__ repeated | List of available image files, with file type information and size information. |
+-------+------+-------+-------------+
| subdirectories | string | repeated | List of available subdirectories |
+-------+------+-------+-------------+






.. CARTA.ScriptingRequest:

ScriptingRequest
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| scripting_request_id | sfixed32 |  | Used to connect a single scripting request to its response |
+-------+------+-------+-------------+
| target | string |  | the path of the target object. e.g. activeFrame.renderConfig |
+-------+------+-------+-------------+
| action | string |  | the name of the function to call. e.g. setColorMap |
+-------+------+-------+-------------+
| parameters | string |  | JSON array of paramters. e.g. '["viridis"]' |
+-------+------+-------+-------------+
| async | bool |  | flag indicating whether the frontend should execute this asynchronously, or only return once the call is complete |
+-------+------+-------+-------------+



.. CARTA.ScriptingResponse:

ScriptingResponse
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| scripting_request_id | sfixed32 |  | should match the incoming request ID |
+-------+------+-------+-------------+
| success | bool |  | indicates whether the call was correctly executed |
+-------+------+-------+-------------+
| message | string |  | optional error message |
+-------+------+-------+-------------+
| response | string |  | JSON-parsable response. e.g. "true", or the base64-encoded string |
+-------+------+-------+-------------+





