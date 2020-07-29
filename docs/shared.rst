.. _title:

Protocol Documentation
======================

Table of Contents
-----------------

.. container::
   :name: toc-container

   -  `defs.proto <#defs.proto>`__

      -  `MAnimationFrame <#CARTA.AnimationFrame>`__
      -  `MCatalogFileInfo <#CARTA.CatalogFileInfo>`__
      -  `MCatalogHeader <#CARTA.CatalogHeader>`__
      -  `MCatalogImageBounds <#CARTA.CatalogImageBounds>`__
      -  `MColumnData <#CARTA.ColumnData>`__
      -  `MCoosys <#CARTA.Coosys>`__
      -  `MDoubleBounds <#CARTA.DoubleBounds>`__
      -  `MFileInfo <#CARTA.FileInfo>`__
      -  `MFileInfoExtended <#CARTA.FileInfoExtended>`__
      -  `MFilterConfig <#CARTA.FilterConfig>`__
      -  `MHeaderEntry <#CARTA.HeaderEntry>`__
      -  `MHistogram <#CARTA.Histogram>`__
      -  `MImageBounds <#CARTA.ImageBounds>`__
      -  `MPoint <#CARTA.Point>`__
      -  `MRegionInfo <#CARTA.RegionInfo>`__
      -  `MRegionStyle <#CARTA.RegionStyle>`__
      -  `MSpatialProfile <#CARTA.SpatialProfile>`__
      -  `MSpectralProfile <#CARTA.SpectralProfile>`__
      -  `MStatisticsValue <#CARTA.StatisticsValue>`__

   -  `enums.proto <#enums.proto>`__

      -  `ECatalogFileType <#CARTA.CatalogFileType>`__
      -  `EClientFeatureFlags <#CARTA.ClientFeatureFlags>`__
      -  `EColumnType <#CARTA.ColumnType>`__
      -  `EComparisonOperator <#CARTA.ComparisonOperator>`__
      -  `ECompressionType <#CARTA.CompressionType>`__
      -  `ECoordinateType <#CARTA.CoordinateType>`__
      -  `EEntryType <#CARTA.EntryType>`__
      -  `EErrorSeverity <#CARTA.ErrorSeverity>`__
      -  `EEventType <#CARTA.EventType>`__
      -  `EFileFeatureFlags <#CARTA.FileFeatureFlags>`__
      -  `EFileType <#CARTA.FileType>`__
      -  `ERegionType <#CARTA.RegionType>`__
      -  `ERenderMode <#CARTA.RenderMode>`__
      -  `EServerFeatureFlags <#CARTA.ServerFeatureFlags>`__
      -  `ESessionType <#CARTA.SessionType>`__
      -  `ESmoothingMode <#CARTA.SmoothingMode>`__
      -  `ESortingType <#CARTA.SortingType>`__
      -  `EStatsType <#CARTA.StatsType>`__

   -  `Scalar Value Types <#scalar-value-types>`__

.. container:: file-heading

   .. rubric:: defs.proto
      :name: defs.proto

   `Top <#title>`__

.. _CARTA.AnimationFrame:

AnimationFrame
~~~~~~~~~~~~~~

======= ======================== ===== ===========
Field   Type                     Label Description
======= ======================== ===== ===========
channel `sfixed32 <#sfixed32>`__       
stokes  `sfixed32 <#sfixed32>`__       
======= ======================== ===== ===========

.. _CARTA.CatalogFileInfo:

CatalogFileInfo
~~~~~~~~~~~~~~~

+-------------+----------------------------+----------+-------------+
| Field       | Type                       | Label    | Description |
+=============+============================+==========+=============+
| name        | `string <#string>`__       |          |             |
+-------------+----------------------------+----------+-------------+
| type        | `CatalogFileType <         |          |             |
|             | #CARTA.CatalogFileType>`__ |          |             |
+-------------+----------------------------+----------+-------------+
| file_size   | `sfixed64 <#sfixed64>`__   |          |             |
+-------------+----------------------------+----------+-------------+
| description | `string <#string>`__       |          |             |
+-------------+----------------------------+----------+-------------+
| coosys      | `Coosys <#CARTA.Coosys>`__ | repeated |             |
+-------------+----------------------------+----------+-------------+
| date        | `sfixed64 <#sfixed64>`__   |          |             |
+-------------+----------------------------+----------+-------------+

.. _CARTA.CatalogHeader:

CatalogHeader
~~~~~~~~~~~~~

============ ================================== ===== ===========
Field        Type                               Label Description
============ ================================== ===== ===========
name         `string <#string>`__                     
data_type    `ColumnType <#CARTA.ColumnType>`__       
column_index `sfixed32 <#sfixed32>`__                 
description  `string <#string>`__                     
units        `string <#string>`__                     
============ ================================== ===== ===========

.. _CARTA.CatalogImageBounds:

CatalogImageBounds
~~~~~~~~~~~~~~~~~~

============= ==================================== ===== ===========
Field         Type                                 Label Description
============= ==================================== ===== ===========
x_column_name `string <#string>`__                       
y_column_name `string <#string>`__                       
image_bounds  `ImageBounds <#CARTA.ImageBounds>`__       
============= ==================================== ===== ===========

.. _CARTA.ColumnData:

ColumnData
~~~~~~~~~~

+-------------+--------------------+----------+--------------------+
| Field       | Type               | Label    | Description        |
+=============+====================+==========+====================+
| data_type   | `ColumnType <#CA   |          |                    |
|             | RTA.ColumnType>`__ |          |                    |
+-------------+--------------------+----------+--------------------+
| string_data | `s                 | repeated | All data types     |
|             | tring <#string>`__ |          | other than string  |
|             |                    |          | sent as binary     |
+-------------+--------------------+----------+--------------------+
| binary_data | `bytes <#bytes>`__ |          | binary data will   |
|             |                    |          | get converted to a |
|             |                    |          | TypedArray         |
+-------------+--------------------+----------+--------------------+

.. _CARTA.Coosys:

Coosys
~~~~~~

======= ==================== ===== ===========
Field   Type                 Label Description
======= ==================== ===== ===========
equinox `string <#string>`__       
epoch   `string <#string>`__       
system  `string <#string>`__       
======= ==================== ===== ===========

.. _CARTA.DoubleBounds:

DoubleBounds
~~~~~~~~~~~~

===== ==================== ===== ===========
Field Type                 Label Description
===== ==================== ===== ===========
min   `double <#double>`__       
max   `double <#double>`__       
===== ==================== ===== ===========

.. _CARTA.FileInfo:

FileInfo
~~~~~~~~

File info message structure (internal use only)

======== ============================== ======== ===========
Field    Type                           Label    Description
======== ============================== ======== ===========
name     `string <#string>`__                    
type     `FileType <#CARTA.FileType>`__          
size     `sfixed64 <#sfixed64>`__                
HDU_list `string <#string>`__           repeated 
date     `sfixed64 <#sfixed64>`__                
======== ============================== ======== ===========

.. _CARTA.FileInfoExtended:

FileInfoExtended
~~~~~~~~~~~~~~~~

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| dimensions       | `sfixed3         |          | Number of        |
|                  | 2 <#sfixed32>`__ |          | dimensions of    |
|                  |                  |          | the image file   |
+------------------+------------------+----------+------------------+
| width            | `sfixed3         |          | Width of the XY  |
|                  | 2 <#sfixed32>`__ |          | plane            |
+------------------+------------------+----------+------------------+
| height           | `sfixed3         |          | Height of the XY |
|                  | 2 <#sfixed32>`__ |          | plane            |
+------------------+------------------+----------+------------------+
| depth            | `sfixed3         |          | Number of        |
|                  | 2 <#sfixed32>`__ |          | channels         |
+------------------+------------------+----------+------------------+
| stokes           | `sfixed3         |          | Number of Stokes |
|                  | 2 <#sfixed32>`__ |          | parameters       |
+------------------+------------------+----------+------------------+
| stokes_vals      | `str             | repeated | List of Stokes   |
|                  | ing <#string>`__ |          | parameters       |
|                  |                  |          | contained in the |
|                  |                  |          | file (if         |
|                  |                  |          | applicable). For |
|                  |                  |          | files that do    |
|                  |                  |          | not explicitly   |
|                  |                  |          | specify Stokes   |
|                  |                  |          | files, this will |
|                  |                  |          | be blank.        |
+------------------+------------------+----------+------------------+
| header_entries   | `Hea             | repeated | Header entries   |
|                  | derEntry <#CARTA |          | from header      |
|                  | .HeaderEntry>`__ |          | string or        |
|                  |                  |          | attributes       |
+------------------+------------------+----------+------------------+
| computed_entries | `Hea             | repeated |                  |
|                  | derEntry <#CARTA |          |                  |
|                  | .HeaderEntry>`__ |          |                  |
+------------------+------------------+----------+------------------+

.. _CARTA.FilterConfig:

FilterConfig
~~~~~~~~~~~~

+---------------------+----------------------+-------+-------------+
| Field               | Type                 | Label | Description |
+=====================+======================+=======+=============+
| column_name         | `string <#string>`__ |       |             |
+---------------------+----------------------+-------+-------------+
| comparison_operator | `Compariso           |       |             |
|                     | nOperator <#CARTA.Co |       |             |
|                     | mparisonOperator>`__ |       |             |
+---------------------+----------------------+-------+-------------+
| value               | `double <#double>`__ |       |             |
+---------------------+----------------------+-------+-------------+
| secondary_value     | `double <#double>`__ |       |             |
+---------------------+----------------------+-------+-------------+
| sub_string          | `string <#string>`__ |       |             |
+---------------------+----------------------+-------+-------------+

.. _CARTA.HeaderEntry:

HeaderEntry
~~~~~~~~~~~

============= ================================ ===== ===========
Field         Type                             Label Description
============= ================================ ===== ===========
name          `string <#string>`__                   
value         `string <#string>`__                   
entry_type    `EntryType <#CARTA.EntryType>`__       
numeric_value `double <#double>`__                   
comment       `string <#string>`__                   
============= ================================ ===== ===========

.. _CARTA.Histogram:

Histogram
~~~~~~~~~

================ ======================== ======== ===========
Field            Type                     Label    Description
================ ======================== ======== ===========
channel          `sfixed32 <#sfixed32>`__          
num_bins         `sfixed32 <#sfixed32>`__          
bin_width        `double <#double>`__              
first_bin_center `double <#double>`__              
bins             `sfixed32 <#sfixed32>`__ repeated 
mean             `double <#double>`__              
std_dev          `double <#double>`__              
================ ======================== ======== ===========

.. _CARTA.ImageBounds:

ImageBounds
~~~~~~~~~~~

===== ======================== ===== ===========
Field Type                     Label Description
===== ======================== ===== ===========
x_min `sfixed32 <#sfixed32>`__       
x_max `sfixed32 <#sfixed32>`__       
y_min `sfixed32 <#sfixed32>`__       
y_max `sfixed32 <#sfixed32>`__       
===== ======================== ===== ===========

.. _CARTA.Point:

Point
~~~~~

===== ================== ===== ===========
Field Type               Label Description
===== ================== ===== ===========
x     `float <#float>`__       
y     `float <#float>`__       
===== ================== ===== ===========

.. _CARTA.RegionInfo:

RegionInfo
~~~~~~~~~~

+----------------+------------------+----------+------------------+
| Field          | Type             | Label    | Description      |
+================+==================+==========+==================+
| region_type    | `R               |          | The type of      |
|                | egionType <#CART |          | region described |
|                | A.RegionType>`__ |          | by the control   |
|                |                  |          | points. The      |
|                |                  |          | meaning of the   |
|                |                  |          | control points   |
|                |                  |          | will differ,     |
|                |                  |          | depending on the |
|                |                  |          | type of region   |
|                |                  |          | being defined.   |
+----------------+------------------+----------+------------------+
| control_points | `Point <         | repeated | Control points   |
|                | #CARTA.Point>`__ |          | for the region   |
+----------------+------------------+----------+------------------+
| rotation       | `f               |          | (Only applicable |
|                | loat <#float>`__ |          | for ellipse and  |
|                |                  |          | rectangle)       |
|                |                  |          | Rotation of the  |
|                |                  |          | region in the xy |
|                |                  |          | plane (radians). |
+----------------+------------------+----------+------------------+

.. _CARTA.RegionStyle:

RegionStyle
~~~~~~~~~~~

+------------+---------------------+----------+---------------------+
| Field      | Type                | Label    | Description         |
+============+=====================+==========+=====================+
| name       | `                   |          | The name of the     |
|            | string <#string>`__ |          | region, displayed   |
|            |                     |          | as an annotation    |
|            |                     |          | label.              |
+------------+---------------------+----------+---------------------+
| color      | `                   |          | Color as a name     |
|            | string <#string>`__ |          | ("blue"), RGB       |
|            |                     |          | string, or hex      |
|            |                     |          | string              |
+------------+---------------------+----------+---------------------+
| line_width | `sfix               |          | Width in pixels     |
|            | ed32 <#sfixed32>`__ |          |                     |
+------------+---------------------+----------+---------------------+
| dash_list  | `sfix               | repeated | Dash length: on,    |
|            | ed32 <#sfixed32>`__ |          | off                 |
+------------+---------------------+----------+---------------------+

.. _CARTA.SpatialProfile:

SpatialProfile
~~~~~~~~~~~~~~

=============== ======================== ===== ===========
Field           Type                     Label Description
=============== ======================== ===== ===========
start           `sfixed32 <#sfixed32>`__       
end             `sfixed32 <#sfixed32>`__       
raw_values_fp32 `bytes <#bytes>`__             
coordinate      `string <#string>`__           
=============== ======================== ===== ===========

.. _CARTA.SpectralProfile:

SpectralProfile
~~~~~~~~~~~~~~~

=============== ================================ ===== ===========
Field           Type                             Label Description
=============== ================================ ===== ===========
coordinate      `string <#string>`__                   
stats_type      `StatsType <#CARTA.StatsType>`__       
raw_values_fp32 `bytes <#bytes>`__                     
raw_values_fp64 `bytes <#bytes>`__                     
=============== ================================ ===== ===========

.. _CARTA.StatisticsValue:

StatisticsValue
~~~~~~~~~~~~~~~

========== ================================ ===== ===========
Field      Type                             Label Description
========== ================================ ===== ===========
stats_type `StatsType <#CARTA.StatsType>`__       
value      `double <#double>`__                   
========== ================================ ===== ===========

.. container:: file-heading

   .. rubric:: enums.proto
      :name: enums.proto

   `Top <#title>`__

.. _CARTA.CatalogFileType:

CatalogFileType
~~~~~~~~~~~~~~~

========= ====== ===========
Name      Number Description
========= ====== ===========
FITSTable 0      
VOTable   1      
========= ====== ===========

.. _CARTA.ClientFeatureFlags:

ClientFeatureFlags
~~~~~~~~~~~~~~~~~~

==================== ====== ===========
Name                 Number Description
==================== ====== ===========
CLIENT_FEATURE_NONE  0      
WEB_GL               1      
WEB_GL_2             2      
WEB_ASSEMBLY         4      
WEB_ASSEMBLY_THREADS 8      
OFFSCREEN_CANVAS     16     
==================== ====== ===========

.. _CARTA.ColumnType:

ColumnType
~~~~~~~~~~

=============== ====== ===========
Name            Number Description
=============== ====== ===========
UnsupportedType 0      
String          1      
Uint8           2      
Int8            3      
Uint16          4      
Int16           5      
Uint32          6      
Int32           7      
Uint64          8      
Int64           9      
Float           10     
Double          11     
Bool            12     
=============== ====== ===========

.. _CARTA.ComparisonOperator:

ComparisonOperator
~~~~~~~~~~~~~~~~~~

============== ====== ===========
Name           Number Description
============== ====== ===========
Equal          0      
NotEqual       1      
Lesser         2      
Greater        3      
LessorOrEqual  4      
GreaterOrEqual 5      
RangeOpen      6      
RangeClosed    7      
============== ====== ===========

.. _CARTA.CompressionType:

CompressionType
~~~~~~~~~~~~~~~

==== ====== ===========
Name Number Description
==== ====== ===========
NONE 0      
ZFP  1      
SZ   2      
==== ====== ===========

.. _CARTA.CoordinateType:

CoordinateType
~~~~~~~~~~~~~~

===== ====== ===========
Name  Number Description
===== ====== ===========
PIXEL 0      
WORLD 1      
===== ====== ===========

.. _CARTA.EntryType:

EntryType
~~~~~~~~~

====== ====== ===========
Name   Number Description
====== ====== ===========
STRING 0      
FLOAT  1      
INT    2      
====== ====== ===========

.. _CARTA.ErrorSeverity:

ErrorSeverity
~~~~~~~~~~~~~

======== ====== ===========
Name     Number Description
======== ====== ===========
DEBUG    0      
INFO     1      
WARNING  2      
ERROR    3      
CRITICAL 4      
======== ====== ===========

.. _CARTA.EventType:

EventType
~~~~~~~~~

========================== ====== ===========
Name                       Number Description
========================== ====== ===========
EMPTY_EVENT                0      
REGISTER_VIEWER            1      
FILE_LIST_REQUEST          2      
FILE_INFO_REQUEST          3      
OPEN_FILE                  4      
SET_IMAGE_CHANNELS         6      
SET_CURSOR                 7      
SET_SPATIAL_REQUIREMENTS   8      
SET_HISTOGRAM_REQUIREMENTS 9      
SET_STATS_REQUIREMENTS     10     
SET_REGION                 11     
REMOVE_REGION              12     
CLOSE_FILE                 13     
SET_SPECTRAL_REQUIREMENTS  14     
START_ANIMATION            15     
START_ANIMATION_ACK        16     
STOP_ANIMATION             17     
REGISTER_VIEWER_ACK        18     
FILE_LIST_RESPONSE         19     
FILE_INFO_RESPONSE         20     
OPEN_FILE_ACK              21     
SET_REGION_ACK             22     
REGION_HISTOGRAM_DATA      23     
SPATIAL_PROFILE_DATA       25     
SPECTRAL_PROFILE_DATA      26     
REGION_STATS_DATA          27     
ERROR_DATA                 28     
ANIMATION_FLOW_CONTROL     29     
ADD_REQUIRED_TILES         30     
REMOVE_REQUIRED_TILES      31     
RASTER_TILE_DATA           32     
REGION_LIST_REQUEST        33     
REGION_LIST_RESPONSE       34     
REGION_FILE_INFO_REQUEST   35     
REGION_FILE_INFO_RESPONSE  36     
IMPORT_REGION              37     
IMPORT_REGION_ACK          38     
EXPORT_REGION              39     
EXPORT_REGION_ACK          40     
SET_USER_PREFERENCES       41     
SET_USER_PREFERENCES_ACK   42     
SET_USER_LAYOUT            43     
SET_USER_LAYOUT_ACK        44     
SET_CONTOUR_PARAMETERS     45     
CONTOUR_IMAGE_DATA         46     
RESUME_SESSION             47     
RESUME_SESSION_ACK         48     
RASTER_TILE_SYNC           49     
CATALOG_LIST_REQUEST       50     
CATALOG_LIST_RESPONSE      51     
CATALOG_FILE_INFO_REQUEST  52     
CATALOG_FILE_INFO_RESPONSE 53     
OPEN_CATALOG_FILE          54     
OPEN_CATALOG_FILE_ACK      55     
CLOSE_CATALOG_FILE         56     
CATALOG_FILTER_REQUEST     57     
CATALOG_FILTER_RESPONSE    58     
SCRIPTING_REQUEST          59     
SCRIPTING_RESPONSE         60     
SPECTRAL_LINE_REQUEST      67     
SPECTRAL_LINE_RESPONSE     68     
========================== ====== ===========

.. _CARTA.FileFeatureFlags:

FileFeatureFlags
~~~~~~~~~~~~~~~~

================== ====== ===========
Name               Number Description
================== ====== ===========
FILE_FEATURE_NONE  0      
ROTATED_DATASET    1      
CHANNEL_HISTOGRAMS 2      
CUBE_HISTOGRAMS    4      
CHANNEL_STATS      8      
MEAN_IMAGE         16     
MIP_DATASET        32     
================== ====== ===========

.. _CARTA.FileType:

FileType
~~~~~~~~

======= ====== ===========
Name    Number Description
======= ====== ===========
CASA    0      
CRTF    1      
DS9_REG 2      
FITS    3      
HDF5    4      
MIRIAD  5      
UNKNOWN 6      
======= ====== ===========

.. _CARTA.RegionType:

RegionType
~~~~~~~~~~

========= ====== ===========
Name      Number Description
========= ====== ===========
POINT     0      
LINE      1      
POLYLINE  2      
RECTANGLE 3      
ELLIPSE   4      
ANNULUS   5      
POLYGON   6      
========= ====== ===========

.. _CARTA.RenderMode:

RenderMode
~~~~~~~~~~

======= ====== ===========
Name    Number Description
======= ====== ===========
RASTER  0      
CONTOUR 1      
======= ====== ===========

.. _CARTA.ServerFeatureFlags:

ServerFeatureFlags
~~~~~~~~~~~~~~~~~~

=================== ====== ===========
Name                Number Description
=================== ====== ===========
SERVER_FEATURE_NONE 0      
SZ_COMPRESSION      1      
HEVC_COMPRESSION    2      
NVENC_COMPRESSION   4      
REGION_WRITE_ACCESS 8      
USER_PREFERENCES    16     
USER_LAYOUTS        32     
=================== ====== ===========

.. _CARTA.SessionType:

SessionType
~~~~~~~~~~~

======= ====== ===========
Name    Number Description
======= ====== ===========
NEW     0      
RESUMED 1      
======= ====== ===========

.. _CARTA.SmoothingMode:

SmoothingMode
~~~~~~~~~~~~~

============ ====== ===========
Name         Number Description
============ ====== ===========
NoSmoothing  0      
BlockAverage 1      
GaussianBlur 2      
============ ====== ===========

.. _CARTA.SortingType:

SortingType
~~~~~~~~~~~

========== ====== ===========
Name       Number Description
========== ====== ===========
Ascending  0      
Descending 1      
========== ====== ===========

.. _CARTA.StatsType:

StatsType
~~~~~~~~~

=========== ====== ===========
Name        Number Description
=========== ====== ===========
NumPixels   0      
NanCount    1      
Sum         2      
FluxDensity 3      
Mean        4      
RMS         5      
Sigma       6      
SumSq       7      
Min         8      
Max         9      
Blc         10     
Trc         11     
MinPos      12     
MaxPos      13     
Blcf        14     
Trcf        15     
MinPosf     16     
MaxPosf     17     
=========== ====== ===========

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
