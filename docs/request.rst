.. _title:

Protocol Documentation
======================

Table of Contents
-----------------

.. container::
   :name: toc-container

   -  `catalog_file_info.proto <#catalog_file_info.proto>`__

      -  `MCatalogFileInfoRequest <#CARTA.CatalogFileInfoRequest>`__
      -  `MCatalogFileInfoResponse <#CARTA.CatalogFileInfoResponse>`__

   -  `catalog_list.proto <#catalog_list.proto>`__

      -  `MCatalogListRequest <#CARTA.CatalogListRequest>`__
      -  `MCatalogListResponse <#CARTA.CatalogListResponse>`__

   -  `file_info.proto <#file_info.proto>`__

      -  `MFileInfoRequest <#CARTA.FileInfoRequest>`__
      -  `MFileInfoResponse <#CARTA.FileInfoResponse>`__

   -  `file_list.proto <#file_list.proto>`__

      -  `MFileListRequest <#CARTA.FileListRequest>`__
      -  `MFileListResponse <#CARTA.FileListResponse>`__

   -  `region_file_info.proto <#region_file_info.proto>`__

      -  `MRegionFileInfoRequest <#CARTA.RegionFileInfoRequest>`__
      -  `MRegionFileInfoResponse <#CARTA.RegionFileInfoResponse>`__

   -  `region_list.proto <#region_list.proto>`__

      -  `MRegionListRequest <#CARTA.RegionListRequest>`__
      -  `MRegionListResponse <#CARTA.RegionListResponse>`__

   -  `scripting.proto <#scripting.proto>`__

      -  `MScriptingRequest <#CARTA.ScriptingRequest>`__
      -  `MScriptingResponse <#CARTA.ScriptingResponse>`__

   -  `Scalar Value Types <#scalar-value-types>`__

.. container:: file-heading

   .. rubric:: catalog_file_info.proto
      :name: catalog_file_info.proto

   `Top <#title>`__

.. _CARTA.CatalogFileInfoRequest:

CatalogFileInfoRequest
~~~~~~~~~~~~~~~~~~~~~~

========= ==================== ===== ===========
Field     Type                 Label Description
========= ==================== ===== ===========
directory `string <#string>`__       
name      `string <#string>`__       
========= ==================== ===== ===========

.. _CARTA.CatalogFileInfoResponse:

CatalogFileInfoResponse
~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------+----------+-------------+
| Field     | Type                                         | Label    | Description |
+===========+==============================================+==========+=============+
| success   | `bool <#bool>`__                             |          |             |
+-----------+----------------------------------------------+----------+-------------+
| message   | `string <#string>`__                         |          |             |
+-----------+----------------------------------------------+----------+-------------+
| file_info | `CatalogFileInfo <#CARTA.CatalogFileInfo>`__ |          |             |
+-----------+----------------------------------------------+----------+-------------+
| headers   | `CatalogHeader <#CARTA.CatalogHeader>`__     | repeated |             |
+-----------+----------------------------------------------+----------+-------------+

.. container:: file-heading

   .. rubric:: catalog_list.proto
      :name: catalog_list.proto

   `Top <#title>`__

.. _CARTA.CatalogListRequest:

CatalogListRequest
~~~~~~~~~~~~~~~~~~

========= ==================== ===== ===========
Field     Type                 Label Description
========= ==================== ===== ===========
directory `string <#string>`__       
========= ==================== ===== ===========

.. _CARTA.CatalogListResponse:

CatalogListResponse
~~~~~~~~~~~~~~~~~~~

+----------------+--------------------+----------+-------------+
| Field          | Type               | Label    | Description |
+================+====================+==========+=============+
| success        | `bool <#bool>`__   |          |             |
+----------------+--------------------+----------+-------------+
| message        | `s                 |          |             |
|                | tring <#string>`__ |          |             |
+----------------+--------------------+----------+-------------+
| directory      | `s                 |          |             |
|                | tring <#string>`__ |          |             |
+----------------+--------------------+----------+-------------+
| parent         | `s                 |          |             |
|                | tring <#string>`__ |          |             |
+----------------+--------------------+----------+-------------+
| files          | `Catalog           | repeated |             |
|                | FileInfo <#CARTA.C |          |             |
|                | atalogFileInfo>`__ |          |             |
+----------------+--------------------+----------+-------------+
| subdirectories | `s                 | repeated |             |
|                | tring <#string>`__ |          |             |
+----------------+--------------------+----------+-------------+

.. container:: file-heading

   .. rubric:: file_info.proto
      :name: file_info.proto

   `Top <#title>`__

.. _CARTA.FileInfoRequest:

FileInfoRequest
~~~~~~~~~~~~~~~

FILE_INFO_REQUEST:

Requests the file info for a specific file.

Backend responds with FILE_INFO_RESPONSE

+-----------+----------------------+-------+-----------------------+
| Field     | Type                 | Label | Description           |
+===========+======================+=======+=======================+
| directory | `string <#string>`__ |       | Required directory    |
|           |                      |       | name                  |
+-----------+----------------------+-------+-----------------------+
| file      | `string <#string>`__ |       | Required file name    |
+-----------+----------------------+-------+-----------------------+
| hdu       | `string <#string>`__ |       | Required HDU name (if |
|           |                      |       | applicable). If left  |
|           |                      |       | empty, the first HDU  |
|           |                      |       | is selected           |
+-----------+----------------------+-------+-----------------------+

.. _CARTA.FileInfoResponse:

FileInfoResponse
~~~~~~~~~~~~~~~~

FILE_INFO_RESPONSE

Response for FILE_INFO_REQUEST.

Gives information on the requested file

+-------------------+-------------------+-------+-------------------+
| Field             | Type              | Label | Description       |
+===================+===================+=======+===================+
| success           | `bool <#bool>`__  |       | Defines whether   |
|                   |                   |       | the               |
|                   |                   |       | FILE_INFO_REQUEST |
|                   |                   |       | was successful    |
+-------------------+-------------------+-------+-------------------+
| message           | `st               |       | Error message (if |
|                   | ring <#string>`__ |       | applicable)       |
+-------------------+-------------------+-------+-------------------+
| file_info         | `FileInfo <#C     |       | Basic file info   |
|                   | ARTA.FileInfo>`__ |       | (type, size)      |
+-------------------+-------------------+-------+-------------------+
| f                 | `FileInfoExt      |       | Extended file     |
| ile_info_extended | ended <#CARTA.Fil |       | info (WCS, header |
|                   | eInfoExtended>`__ |       | info)             |
+-------------------+-------------------+-------+-------------------+

.. container:: file-heading

   .. rubric:: file_list.proto
      :name: file_list.proto

   `Top <#title>`__

.. _CARTA.FileListRequest:

FileListRequest
~~~~~~~~~~~~~~~

FILE_LIST_REQUEST:

Requests the list of available files for a given directory.

Backend responds with FILE_LIST_RESPONSE

========= ==================== ===== =======================
Field     Type                 Label Description
========= ==================== ===== =======================
directory `string <#string>`__       Required directory name
========= ==================== ===== =======================

.. _CARTA.FileListResponse:

FileListResponse
~~~~~~~~~~~~~~~~

FILE_LIST_RESPONSE

Response for FILE_LIST_REQUEST.

Gives a list of available files (and their types), as well as
subdirectories

+----------------+------------------+----------+------------------+
| Field          | Type             | Label    | Description      |
+================+==================+==========+==================+
| success        | `bool <#bool>`__ |          | Defines whether  |
|                |                  |          | the              |
|                |                  |          | F                |
|                |                  |          | ILE_LIST_REQUEST |
|                |                  |          | was successful   |
+----------------+------------------+----------+------------------+
| message        | `str             |          | Error message    |
|                | ing <#string>`__ |          | (if applicable)  |
+----------------+------------------+----------+------------------+
| directory      | `str             |          | Directory of     |
|                | ing <#string>`__ |          | listing          |
+----------------+------------------+----------+------------------+
| parent         | `str             |          | Directory parent |
|                | ing <#string>`__ |          | (null/empty if   |
|                |                  |          | top-level)       |
+----------------+------------------+----------+------------------+
| files          | `FileInfo <#CA   | repeated | List of          |
|                | RTA.FileInfo>`__ |          | available image  |
|                |                  |          | files, with file |
|                |                  |          | type information |
|                |                  |          | and size         |
|                |                  |          | information.     |
+----------------+------------------+----------+------------------+
| subdirectories | `str             | repeated | List of          |
|                | ing <#string>`__ |          | available        |
|                |                  |          | subdirectories   |
+----------------+------------------+----------+------------------+

.. container:: file-heading

   .. rubric:: region_file_info.proto
      :name: region_file_info.proto

   `Top <#title>`__

.. _CARTA.RegionFileInfoRequest:

RegionFileInfoRequest
~~~~~~~~~~~~~~~~~~~~~

REGION_FILE_INFO_REQUEST:

Requests contents for a specific region file on the server

Backend responds with REGION_FILE_INFO_RESPONSE

========= ==================== ===== =======================
Field     Type                 Label Description
========= ==================== ===== =======================
directory `string <#string>`__       Required directory name
file      `string <#string>`__       Required file name
========= ==================== ===== =======================

.. _CARTA.RegionFileInfoResponse:

RegionFileInfoResponse
~~~~~~~~~~~~~~~~~~~~~~

REGION_FILE_INFO_RESPONSE

Response for REGION_FILE_INFO_REQUEST.

Gives information on the requested file

+-----------+---------------------+----------+---------------------+
| Field     | Type                | Label    | Description         |
+===========+=====================+==========+=====================+
| success   | `bool <#bool>`__    |          | Defines whether the |
|           |                     |          | REGION_INFO_REQUEST |
|           |                     |          | was successful      |
+-----------+---------------------+----------+---------------------+
| message   | `                   |          | Error message (if   |
|           | string <#string>`__ |          | applicable)         |
+-----------+---------------------+----------+---------------------+
| file_info | `FileInfo <         |          | Basic info about    |
|           | #CARTA.FileInfo>`__ |          | region file         |
+-----------+---------------------+----------+---------------------+
| contents  | `                   | repeated | Contents of file;   |
|           | string <#string>`__ |          | each string is a    |
|           |                     |          | line                |
+-----------+---------------------+----------+---------------------+

.. container:: file-heading

   .. rubric:: region_list.proto
      :name: region_list.proto

   `Top <#title>`__

.. _CARTA.RegionListRequest:

RegionListRequest
~~~~~~~~~~~~~~~~~

REGION_LIST_REQUEST:

Requests the list of available region files for a given directory.

Backend responds with REGION_LIST_RESPONSE

========= ==================== ===== =======================
Field     Type                 Label Description
========= ==================== ===== =======================
directory `string <#string>`__       Required directory name
========= ==================== ===== =======================

.. _CARTA.RegionListResponse:

RegionListResponse
~~~~~~~~~~~~~~~~~~

REGION_LIST_RESPONSE

Response for REGION_LIST_REQUEST.

Gives a list of available region files (and their types), as well as
subdirectories

+----------------+------------------+----------+------------------+
| Field          | Type             | Label    | Description      |
+================+==================+==========+==================+
| success        | `bool <#bool>`__ |          | Defines whether  |
|                |                  |          | the              |
|                |                  |          | REG              |
|                |                  |          | ION_LIST_REQUEST |
|                |                  |          | was successful   |
+----------------+------------------+----------+------------------+
| message        | `str             |          | Error message    |
|                | ing <#string>`__ |          | (if applicable)  |
+----------------+------------------+----------+------------------+
| directory      | `str             |          | Directory of     |
|                | ing <#string>`__ |          | listing          |
+----------------+------------------+----------+------------------+
| parent         | `str             |          | Directory parent |
|                | ing <#string>`__ |          | (null/empty if   |
|                |                  |          | top-level)       |
+----------------+------------------+----------+------------------+
| files          | `FileInfo <#CA   | repeated | List of          |
|                | RTA.FileInfo>`__ |          | available image  |
|                |                  |          | files, with file |
|                |                  |          | type information |
|                |                  |          | and size         |
|                |                  |          | information.     |
+----------------+------------------+----------+------------------+
| subdirectories | `str             | repeated | List of          |
|                | ing <#string>`__ |          | available        |
|                |                  |          | subdirectories   |
+----------------+------------------+----------+------------------+

.. container:: file-heading

   .. rubric:: scripting.proto
      :name: scripting.proto

   `Top <#title>`__

.. _CARTA.ScriptingRequest:

ScriptingRequest
~~~~~~~~~~~~~~~~

+-------------------+-------------------+-------+-------------------+
| Field             | Type              | Label | Description       |
+===================+===================+=======+===================+
| scr               | `sfixed           |       | Used to connect a |
| ipting_request_id | 32 <#sfixed32>`__ |       | single scripting  |
|                   |                   |       | request to its    |
|                   |                   |       | response          |
+-------------------+-------------------+-------+-------------------+
| target            | `st               |       | the path of the   |
|                   | ring <#string>`__ |       | target object.    |
|                   |                   |       | e.g.              |
|                   |                   |       | activeF           |
|                   |                   |       | rame.renderConfig |
+-------------------+-------------------+-------+-------------------+
| action            | `st               |       | the name of the   |
|                   | ring <#string>`__ |       | function to call. |
|                   |                   |       | e.g. setColorMap  |
+-------------------+-------------------+-------+-------------------+
| parameters        | `st               |       | JSON array of     |
|                   | ring <#string>`__ |       | paramters. e.g.   |
|                   |                   |       | '["viridis"]'     |
+-------------------+-------------------+-------+-------------------+
| async             | `bool <#bool>`__  |       | flag indicating   |
|                   |                   |       | whether the       |
|                   |                   |       | frontend should   |
|                   |                   |       | execute this      |
|                   |                   |       | asynchronously,   |
|                   |                   |       | or only return    |
|                   |                   |       | once the call is  |
|                   |                   |       | complete          |
+-------------------+-------------------+-------+-------------------+

.. _CARTA.ScriptingResponse:

ScriptingResponse
~~~~~~~~~~~~~~~~~

+-------------------+-------------------+-------+-------------------+
| Field             | Type              | Label | Description       |
+===================+===================+=======+===================+
| scr               | `sfixed           |       | should match the  |
| ipting_request_id | 32 <#sfixed32>`__ |       | incoming request  |
|                   |                   |       | ID                |
+-------------------+-------------------+-------+-------------------+
| success           | `bool <#bool>`__  |       | indicates whether |
|                   |                   |       | the call was      |
|                   |                   |       | correctly         |
|                   |                   |       | executed          |
+-------------------+-------------------+-------+-------------------+
| message           | `st               |       | optional error    |
|                   | ring <#string>`__ |       | message           |
+-------------------+-------------------+-------+-------------------+
| response          | `st               |       | JSON-parsable     |
|                   | ring <#string>`__ |       | response. e.g.    |
|                   |                   |       | "true", or the    |
|                   |                   |       | base64-encoded    |
|                   |                   |       | string            |
+-------------------+-------------------+-------+-------------------+

Scalar Value Types
------------------

+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| .     | Notes | C++   | Java  | P     | Go    | C#    | PHP   | Ruby  |
| proto |       |       |       | ython |       |       |       |       |
| Type  |       |       |       |       |       |       |       |       |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| d     |       | d     | d     | float | fl    | d     | float | Float |
| ouble |       | ouble | ouble |       | oat64 | ouble |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| float |       | float | float | float | fl    | float | float | Float |
|       |       |       |       |       | oat32 |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| int32 | Uses  | int32 | int   | int   | int32 | int   | in    | B     |
|       | varia |       |       |       |       |       | teger | ignum |
|       | ble-l |       |       |       |       |       |       | or    |
|       | ength |       |       |       |       |       |       | F     |
|       | enco  |       |       |       |       |       |       | ixnum |
|       | ding. |       |       |       |       |       |       | (as   |
|       | I     |       |       |       |       |       |       | requ  |
|       | neffi |       |       |       |       |       |       | ired) |
|       | cient |       |       |       |       |       |       |       |
|       | for   |       |       |       |       |       |       |       |
|       | enc   |       |       |       |       |       |       |       |
|       | oding |       |       |       |       |       |       |       |
|       | neg   |       |       |       |       |       |       |       |
|       | ative |       |       |       |       |       |       |       |
|       | nu    |       |       |       |       |       |       |       |
|       | mbers |       |       |       |       |       |       |       |
|       | – if  |       |       |       |       |       |       |       |
|       | your  |       |       |       |       |       |       |       |
|       | field |       |       |       |       |       |       |       |
|       | is    |       |       |       |       |       |       |       |
|       | l     |       |       |       |       |       |       |       |
|       | ikely |       |       |       |       |       |       |       |
|       | to    |       |       |       |       |       |       |       |
|       | have  |       |       |       |       |       |       |       |
|       | neg   |       |       |       |       |       |       |       |
|       | ative |       |       |       |       |       |       |       |
|       | va    |       |       |       |       |       |       |       |
|       | lues, |       |       |       |       |       |       |       |
|       | use   |       |       |       |       |       |       |       |
|       | s     |       |       |       |       |       |       |       |
|       | int32 |       |       |       |       |       |       |       |
|       | ins   |       |       |       |       |       |       |       |
|       | tead. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| int64 | Uses  | int64 | long  | int   | int64 | long  | inte  | B     |
|       | varia |       |       | /long |       |       | ger/s | ignum |
|       | ble-l |       |       |       |       |       | tring |       |
|       | ength |       |       |       |       |       |       |       |
|       | enco  |       |       |       |       |       |       |       |
|       | ding. |       |       |       |       |       |       |       |
|       | I     |       |       |       |       |       |       |       |
|       | neffi |       |       |       |       |       |       |       |
|       | cient |       |       |       |       |       |       |       |
|       | for   |       |       |       |       |       |       |       |
|       | enc   |       |       |       |       |       |       |       |
|       | oding |       |       |       |       |       |       |       |
|       | neg   |       |       |       |       |       |       |       |
|       | ative |       |       |       |       |       |       |       |
|       | nu    |       |       |       |       |       |       |       |
|       | mbers |       |       |       |       |       |       |       |
|       | – if  |       |       |       |       |       |       |       |
|       | your  |       |       |       |       |       |       |       |
|       | field |       |       |       |       |       |       |       |
|       | is    |       |       |       |       |       |       |       |
|       | l     |       |       |       |       |       |       |       |
|       | ikely |       |       |       |       |       |       |       |
|       | to    |       |       |       |       |       |       |       |
|       | have  |       |       |       |       |       |       |       |
|       | neg   |       |       |       |       |       |       |       |
|       | ative |       |       |       |       |       |       |       |
|       | va    |       |       |       |       |       |       |       |
|       | lues, |       |       |       |       |       |       |       |
|       | use   |       |       |       |       |       |       |       |
|       | s     |       |       |       |       |       |       |       |
|       | int64 |       |       |       |       |       |       |       |
|       | ins   |       |       |       |       |       |       |       |
|       | tead. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| u     | Uses  | u     | int   | int   | u     | uint  | in    | B     |
| int32 | varia | int32 |       | /long | int32 |       | teger | ignum |
|       | ble-l |       |       |       |       |       |       | or    |
|       | ength |       |       |       |       |       |       | F     |
|       | enco  |       |       |       |       |       |       | ixnum |
|       | ding. |       |       |       |       |       |       | (as   |
|       |       |       |       |       |       |       |       | requ  |
|       |       |       |       |       |       |       |       | ired) |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| u     | Uses  | u     | long  | int   | u     | ulong | inte  | B     |
| int64 | varia | int64 |       | /long | int64 |       | ger/s | ignum |
|       | ble-l |       |       |       |       |       | tring | or    |
|       | ength |       |       |       |       |       |       | F     |
|       | enco  |       |       |       |       |       |       | ixnum |
|       | ding. |       |       |       |       |       |       | (as   |
|       |       |       |       |       |       |       |       | requ  |
|       |       |       |       |       |       |       |       | ired) |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| s     | Uses  | int32 | int   | int   | int32 | int   | in    | B     |
| int32 | varia |       |       |       |       |       | teger | ignum |
|       | ble-l |       |       |       |       |       |       | or    |
|       | ength |       |       |       |       |       |       | F     |
|       | enco  |       |       |       |       |       |       | ixnum |
|       | ding. |       |       |       |       |       |       | (as   |
|       | S     |       |       |       |       |       |       | requ  |
|       | igned |       |       |       |       |       |       | ired) |
|       | int   |       |       |       |       |       |       |       |
|       | v     |       |       |       |       |       |       |       |
|       | alue. |       |       |       |       |       |       |       |
|       | These |       |       |       |       |       |       |       |
|       | more  |       |       |       |       |       |       |       |
|       | e     |       |       |       |       |       |       |       |
|       | ffici |       |       |       |       |       |       |       |
|       | ently |       |       |       |       |       |       |       |
|       | e     |       |       |       |       |       |       |       |
|       | ncode |       |       |       |       |       |       |       |
|       | neg   |       |       |       |       |       |       |       |
|       | ative |       |       |       |       |       |       |       |
|       | nu    |       |       |       |       |       |       |       |
|       | mbers |       |       |       |       |       |       |       |
|       | than  |       |       |       |       |       |       |       |
|       | re    |       |       |       |       |       |       |       |
|       | gular |       |       |       |       |       |       |       |
|       | in    |       |       |       |       |       |       |       |
|       | t32s. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| s     | Uses  | int64 | long  | int   | int64 | long  | inte  | B     |
| int64 | varia |       |       | /long |       |       | ger/s | ignum |
|       | ble-l |       |       |       |       |       | tring |       |
|       | ength |       |       |       |       |       |       |       |
|       | enco  |       |       |       |       |       |       |       |
|       | ding. |       |       |       |       |       |       |       |
|       | S     |       |       |       |       |       |       |       |
|       | igned |       |       |       |       |       |       |       |
|       | int   |       |       |       |       |       |       |       |
|       | v     |       |       |       |       |       |       |       |
|       | alue. |       |       |       |       |       |       |       |
|       | These |       |       |       |       |       |       |       |
|       | more  |       |       |       |       |       |       |       |
|       | e     |       |       |       |       |       |       |       |
|       | ffici |       |       |       |       |       |       |       |
|       | ently |       |       |       |       |       |       |       |
|       | e     |       |       |       |       |       |       |       |
|       | ncode |       |       |       |       |       |       |       |
|       | neg   |       |       |       |       |       |       |       |
|       | ative |       |       |       |       |       |       |       |
|       | nu    |       |       |       |       |       |       |       |
|       | mbers |       |       |       |       |       |       |       |
|       | than  |       |       |       |       |       |       |       |
|       | re    |       |       |       |       |       |       |       |
|       | gular |       |       |       |       |       |       |       |
|       | in    |       |       |       |       |       |       |       |
|       | t64s. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| fi    | A     | u     | int   | int   | u     | uint  | in    | B     |
| xed32 | lways | int32 |       |       | int32 |       | teger | ignum |
|       | four  |       |       |       |       |       |       | or    |
|       | b     |       |       |       |       |       |       | F     |
|       | ytes. |       |       |       |       |       |       | ixnum |
|       | More  |       |       |       |       |       |       | (as   |
|       | effi  |       |       |       |       |       |       | requ  |
|       | cient |       |       |       |       |       |       | ired) |
|       | than  |       |       |       |       |       |       |       |
|       | u     |       |       |       |       |       |       |       |
|       | int32 |       |       |       |       |       |       |       |
|       | if    |       |       |       |       |       |       |       |
|       | v     |       |       |       |       |       |       |       |
|       | alues |       |       |       |       |       |       |       |
|       | are   |       |       |       |       |       |       |       |
|       | often |       |       |       |       |       |       |       |
|       | gr    |       |       |       |       |       |       |       |
|       | eater |       |       |       |       |       |       |       |
|       | than  |       |       |       |       |       |       |       |
|       | 2^28. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| fi    | A     | u     | long  | int   | u     | ulong | inte  | B     |
| xed64 | lways | int64 |       | /long | int64 |       | ger/s | ignum |
|       | eight |       |       |       |       |       | tring |       |
|       | b     |       |       |       |       |       |       |       |
|       | ytes. |       |       |       |       |       |       |       |
|       | More  |       |       |       |       |       |       |       |
|       | effi  |       |       |       |       |       |       |       |
|       | cient |       |       |       |       |       |       |       |
|       | than  |       |       |       |       |       |       |       |
|       | u     |       |       |       |       |       |       |       |
|       | int64 |       |       |       |       |       |       |       |
|       | if    |       |       |       |       |       |       |       |
|       | v     |       |       |       |       |       |       |       |
|       | alues |       |       |       |       |       |       |       |
|       | are   |       |       |       |       |       |       |       |
|       | often |       |       |       |       |       |       |       |
|       | gr    |       |       |       |       |       |       |       |
|       | eater |       |       |       |       |       |       |       |
|       | than  |       |       |       |       |       |       |       |
|       | 2^56. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| sfi   | A     | int32 | int   | int   | int32 | int   | in    | B     |
| xed32 | lways |       |       |       |       |       | teger | ignum |
|       | four  |       |       |       |       |       |       | or    |
|       | b     |       |       |       |       |       |       | F     |
|       | ytes. |       |       |       |       |       |       | ixnum |
|       |       |       |       |       |       |       |       | (as   |
|       |       |       |       |       |       |       |       | requ  |
|       |       |       |       |       |       |       |       | ired) |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| sfi   | A     | int64 | long  | int   | int64 | long  | inte  | B     |
| xed64 | lways |       |       | /long |       |       | ger/s | ignum |
|       | eight |       |       |       |       |       | tring |       |
|       | b     |       |       |       |       |       |       |       |
|       | ytes. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| bool  |       | bool  | bo    | bo    | bool  | bool  | bo    | TrueC |
|       |       |       | olean | olean |       |       | olean | lass/ |
|       |       |       |       |       |       |       |       | False |
|       |       |       |       |       |       |       |       | Class |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| s     | A     | s     | S     | s     | s     | s     | s     | S     |
| tring | s     | tring | tring | tr/un | tring | tring | tring | tring |
|       | tring |       |       | icode |       |       |       | (U    |
|       | must  |       |       |       |       |       |       | TF-8) |
|       | a     |       |       |       |       |       |       |       |
|       | lways |       |       |       |       |       |       |       |
|       | co    |       |       |       |       |       |       |       |
|       | ntain |       |       |       |       |       |       |       |
|       | UTF-8 |       |       |       |       |       |       |       |
|       | en    |       |       |       |       |       |       |       |
|       | coded |       |       |       |       |       |       |       |
|       | or    |       |       |       |       |       |       |       |
|       | 7-bit |       |       |       |       |       |       |       |
|       | ASCII |       |       |       |       |       |       |       |
|       | text. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| bytes | May   | s     | ByteS | str   | [     | ByteS | s     | S     |
|       | co    | tring | tring |       | ]byte | tring | tring | tring |
|       | ntain |       |       |       |       |       |       | (A    |
|       | any   |       |       |       |       |       |       | SCII- |
|       | arbi  |       |       |       |       |       |       | 8BIT) |
|       | trary |       |       |       |       |       |       |       |
|       | seq   |       |       |       |       |       |       |       |
|       | uence |       |       |       |       |       |       |       |
|       | of    |       |       |       |       |       |       |       |
|       | b     |       |       |       |       |       |       |       |
|       | ytes. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
