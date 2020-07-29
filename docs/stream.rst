.. _title:

Protocol Documentation
======================

Table of Contents
-----------------

.. container::
   :name: toc-container

   -  `catalog_filter.proto <#catalog_filter.proto>`__

      -  `MCatalogFilterRequest <#CARTA.CatalogFilterRequest>`__
      -  `MCatalogFilterResponse <#CARTA.CatalogFilterResponse>`__
      -  `MCatalogFilterResponse.ColumnsEntry <#CARTA.CatalogFilterResponse.ColumnsEntry>`__

   -  `contour_image.proto <#contour_image.proto>`__

      -  `MContourImageData <#CARTA.ContourImageData>`__
      -  `MContourSet <#CARTA.ContourSet>`__

   -  `error.proto <#error.proto>`__

      -  `MErrorData <#CARTA.ErrorData>`__

   -  `raster_tile.proto <#raster_tile.proto>`__

      -  `MRasterTileData <#CARTA.RasterTileData>`__
      -  `MRasterTileSync <#CARTA.RasterTileSync>`__
      -  `MTileData <#CARTA.TileData>`__

   -  `region_histogram.proto <#region_histogram.proto>`__

      -  `MRegionHistogramData <#CARTA.RegionHistogramData>`__

   -  `region_stats.proto <#region_stats.proto>`__

      -  `MRegionStatsData <#CARTA.RegionStatsData>`__

   -  `spatial_profile.proto <#spatial_profile.proto>`__

      -  `MSpatialProfileData <#CARTA.SpatialProfileData>`__

   -  `spectral_profile.proto <#spectral_profile.proto>`__

      -  `MSpectralProfileData <#CARTA.SpectralProfileData>`__

   -  `Scalar Value Types <#scalar-value-types>`__

.. container:: file-heading

   .. rubric:: catalog_filter.proto
      :name: catalog_filter.proto

   `Top <#title>`__

.. _CARTA.CatalogFilterRequest:

CatalogFilterRequest
~~~~~~~~~~~~~~~~~~~~

+--------------------+--------------------+----------+-------------+
| Field              | Type               | Label    | Description |
+====================+====================+==========+=============+
| file_id            | `sfixe             |          |             |
|                    | d32 <#sfixed32>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| column_indices     | `int32 <#int32>`__ | repeated |             |
+--------------------+--------------------+----------+-------------+
| filter_configs     | `F                 | repeated |             |
|                    | ilterConfig <#CART |          |             |
|                    | A.FilterConfig>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| subset_data_size   | `sfixe             |          |             |
|                    | d32 <#sfixed32>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| subset_start_index | `sfixe             |          |             |
|                    | d32 <#sfixed32>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| image_bounds       | `CatalogImageB     |          |             |
|                    | ounds <#CARTA.Cata |          |             |
|                    | logImageBounds>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| image_file_id      | `sfixe             |          |             |
|                    | d32 <#sfixed32>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| region_id          | `sfixe             |          |             |
|                    | d32 <#sfixed32>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| sort_column        | `s                 |          |             |
|                    | tring <#string>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| sorting_type       | `SortingType <#CAR |          |             |
|                    | TA.SortingType>`__ |          |             |
+--------------------+--------------------+----------+-------------+

.. _CARTA.CatalogFilterResponse:

CatalogFilterResponse
~~~~~~~~~~~~~~~~~~~~~

+-------------------+--------------------+----------+-------------+
| Field             | Type               | Label    | Description |
+===================+====================+==========+=============+
| file_id           | `sfixe             |          |             |
|                   | d32 <#sfixed32>`__ |          |             |
+-------------------+--------------------+----------+-------------+
| image_file_id     | `sfixe             |          |             |
|                   | d32 <#sfixed32>`__ |          |             |
+-------------------+--------------------+----------+-------------+
| region_id         | `sfixe             |          |             |
|                   | d32 <#sfixed32>`__ |          |             |
+-------------------+--------------------+----------+-------------+
| columns           | `CatalogFi         | repeated |             |
|                   | lterResponse.Colum |          |             |
|                   | nsEntry <#CARTA.Ca |          |             |
|                   | talogFilterRespons |          |             |
|                   | e.ColumnsEntry>`__ |          |             |
+-------------------+--------------------+----------+-------------+
| subset_data_size  | `sfixe             |          |             |
|                   | d32 <#sfixed32>`__ |          |             |
+-------------------+--------------------+----------+-------------+
| subset_end_index  | `sfixe             |          |             |
|                   | d32 <#sfixed32>`__ |          |             |
+-------------------+--------------------+----------+-------------+
| progress          | `float <#float>`__ |          |             |
+-------------------+--------------------+----------+-------------+
| filter_data_size  | `sfixe             |          |             |
|                   | d32 <#sfixed32>`__ |          |             |
+-------------------+--------------------+----------+-------------+
| request_end_index | `sfixe             |          |             |
|                   | d32 <#sfixed32>`__ |          |             |
+-------------------+--------------------+----------+-------------+

.. _CARTA.CatalogFilterResponse.ColumnsEntry:

CatalogFilterResponse.ColumnsEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ================================== ===== ===========
Field Type                               Label Description
===== ================================== ===== ===========
key   `fixed32 <#fixed32>`__                   
value `ColumnData <#CARTA.ColumnData>`__       
===== ================================== ===== ===========

.. container:: file-heading

   .. rubric:: contour_image.proto
      :name: contour_image.proto

   `Top <#title>`__

.. _CARTA.ContourImageData:

ContourImageData
~~~~~~~~~~~~~~~~

CONTOUR_IMAGE_DATA:

Data for an image rendered in contour mode.

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| file_id          | `sfixed3         |          | The file ID that |
|                  | 2 <#sfixed32>`__ |          | the contour      |
|                  |                  |          | image            |
|                  |                  |          | corresponds to   |
+------------------+------------------+----------+------------------+
| r                | `fixed           |          | The file ID of   |
| eference_file_id | 32 <#fixed32>`__ |          | the reference    |
|                  |                  |          | image that the   |
|                  |                  |          | contour vertices |
|                  |                  |          | are mapped to    |
+------------------+------------------+----------+------------------+
| image_bounds     | `Ima             |          | The bounding box |
|                  | geBounds <#CARTA |          | in the XY plane  |
|                  | .ImageBounds>`__ |          | corresponding to |
|                  |                  |          | the image data   |
|                  |                  |          | in pixel         |
|                  |                  |          | coordinates      |
+------------------+------------------+----------+------------------+
| channel          | `sfixed3         |          | The image        |
|                  | 2 <#sfixed32>`__ |          | channel used to  |
|                  |                  |          | generate the     |
|                  |                  |          | contours         |
+------------------+------------------+----------+------------------+
| stokes           | `sfixed3         |          | The image stokes |
|                  | 2 <#sfixed32>`__ |          | parameter used   |
|                  |                  |          | to generate the  |
|                  |                  |          | contours         |
+------------------+------------------+----------+------------------+
| contour_sets     | `C               | repeated | Each contour set |
|                  | ontourSet <#CART |          | consists of the  |
|                  | A.ContourSet>`__ |          | contour level    |
|                  |                  |          | value, as well   |
|                  |                  |          | as a list of     |
|                  |                  |          | coordinates. The |
|                  |                  |          | start_indices    |
|                  |                  |          | list is used to  |
|                  |                  |          | determine how to |
|                  |                  |          | subdivide the    |
|                  |                  |          | coordinates list |
|                  |                  |          | into separate    |
|                  |                  |          | poly-lines when  |
|                  |                  |          | rendering.       |
+------------------+------------------+----------+------------------+
| progress         | `dou             |          | Progress of the  |
|                  | ble <#double>`__ |          | contour sets     |
|                  |                  |          | being sent. If   |
|                  |                  |          | this is zero,    |
|                  |                  |          | the message is   |
|                  |                  |          | assumed to       |
|                  |                  |          | contain the      |
|                  |                  |          | entire contour   |
|                  |                  |          | sets             |
+------------------+------------------+----------+------------------+

.. _CARTA.ContourSet:

ContourSet
~~~~~~~~~~

============================= ==================== ===== ===========
Field                         Type                 Label Description
============================= ==================== ===== ===========
level                         `double <#double>`__       
decimation_factor             `int32 <#int32>`__         
raw_coordinates               `bytes <#bytes>`__         
raw_start_indices             `bytes <#bytes>`__         
uncompressed_coordinates_size `int32 <#int32>`__         
============================= ==================== ===== ===========

.. container:: file-heading

   .. rubric:: error.proto
      :name: error.proto

   `Top <#title>`__

.. _CARTA.ErrorData:

ErrorData
~~~~~~~~~

ERROR_DATA:

Stream of error/warning/info data. This stream is used to present the
frontend with additional information on

the state of the backend, and is not used in place of returning
success=false on requests or commands.

+----------+----------------------+----------+----------------------+
| Field    | Type                 | Label    | Description          |
+==========+======================+==========+======================+
| severity | `ErrorSeverity <#CAR |          | The severity of the  |
|          | TA.ErrorSeverity>`__ |          | error. Critical      |
|          |                      |          | errors are reserved  |
|          |                      |          | for errors that      |
|          |                      |          | would normally       |
|          |                      |          | require the user to  |
|          |                      |          | restart the program  |
|          |                      |          | or reload the page   |
+----------+----------------------+----------+----------------------+
| tags     | `string <#string>`__ | repeated | A list of strings    |
|          |                      |          | describing the error |
|          |                      |          | type, that the       |
|          |                      |          | frontend can         |
|          |                      |          | interpret and react  |
|          |                      |          | to. For example,     |
|          |                      |          | “file_io” or         |
|          |                      |          | “memory”.            |
+----------+----------------------+----------+----------------------+
| message  | `string <#string>`__ |          | The error message    |
+----------+----------------------+----------+----------------------+
| data     | `string <#string>`__ |          | Accompanying error   |
|          |                      |          | data. For example,   |
|          |                      |          | if an error has the  |
|          |                      |          | “file_io” tag, the   |
|          |                      |          | frontend would       |
|          |                      |          | expect the data      |
|          |                      |          | field to contain the |
|          |                      |          | file ID of the       |
|          |                      |          | offending file.      |
+----------+----------------------+----------+----------------------+

.. container:: file-heading

   .. rubric:: raster_tile.proto
      :name: raster_tile.proto

   `Top <#title>`__

.. _CARTA.RasterTileData:

RasterTileData
~~~~~~~~~~~~~~

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| file_id          | `sfixed3         |          | The file ID that |
|                  | 2 <#sfixed32>`__ |          | the raster image |
|                  |                  |          | corresponds to   |
+------------------+------------------+----------+------------------+
| channel          | `sfixed3         |          | The image        |
|                  | 2 <#sfixed32>`__ |          | channel          |
|                  |                  |          | (z-coordinate)   |
+------------------+------------------+----------+------------------+
| stokes           | `sfixed3         |          | The image stokes |
|                  | 2 <#sfixed32>`__ |          | coordinate       |
+------------------+------------------+----------+------------------+
| compression_type | `Compression     |          | The compression  |
|                  | Type <#CARTA.Com |          | algorithm used.  |
|                  | pressionType>`__ |          |                  |
+------------------+------------------+----------+------------------+
| com              | `f               |          | Compression      |
| pression_quality | loat <#float>`__ |          | quality switch   |
+------------------+------------------+----------+------------------+
| animation_id     | `sfixed3         |          | The ID of the    |
|                  | 2 <#sfixed32>`__ |          | animation (if    |
|                  |                  |          | any)             |
+------------------+------------------+----------+------------------+
| tiles            | `TileData <#CA   | repeated | List of tile     |
|                  | RTA.TileData>`__ |          | data             |
+------------------+------------------+----------+------------------+

.. _CARTA.RasterTileSync:

RasterTileSync
~~~~~~~~~~~~~~

+--------------+---------------------+-------+---------------------+
| Field        | Type                | Label | Description         |
+==============+=====================+=======+=====================+
| file_id      | `sfix               |       | The file ID that    |
|              | ed32 <#sfixed32>`__ |       | the raster image    |
|              |                     |       | corresponds to      |
+--------------+---------------------+-------+---------------------+
| channel      | `sfix               |       | The image channel   |
|              | ed32 <#sfixed32>`__ |       | (z-coordinate)      |
+--------------+---------------------+-------+---------------------+
| stokes       | `sfix               |       | The image stokes    |
|              | ed32 <#sfixed32>`__ |       | coordinate          |
+--------------+---------------------+-------+---------------------+
| animation_id | `sfix               |       | The ID of the       |
|              | ed32 <#sfixed32>`__ |       | animation (if any)  |
+--------------+---------------------+-------+---------------------+
| end_sync     | `bool <#bool>`__    |       | Is this a start or  |
|              |                     |       | end sync message?   |
+--------------+---------------------+-------+---------------------+

.. _CARTA.TileData:

TileData
~~~~~~~~

+---------------+---------------------+-------+---------------------+
| Field         | Type                | Label | Description         |
+===============+=====================+=======+=====================+
| layer         | `sfix               |       | Tile layer          |
|               | ed32 <#sfixed32>`__ |       | coordinate          |
+---------------+---------------------+-------+---------------------+
| x             | `sfix               |       | Tile x coordinate   |
|               | ed32 <#sfixed32>`__ |       |                     |
+---------------+---------------------+-------+---------------------+
| y             | `sfix               |       | Tile y coordinate   |
|               | ed32 <#sfixed32>`__ |       |                     |
+---------------+---------------------+-------+---------------------+
| width         | `sfix               |       | Width of the tile   |
|               | ed32 <#sfixed32>`__ |       | data. If this is    |
|               |                     |       | left as zero, the   |
|               |                     |       | default tile size   |
|               |                     |       | should be used      |
+---------------+---------------------+-------+---------------------+
| height        | `sfix               |       | Height of the tile  |
|               | ed32 <#sfixed32>`__ |       | data. If this is    |
|               |                     |       | left as zero, the   |
|               |                     |       | default tile size   |
|               |                     |       | should be used      |
+---------------+---------------------+-------+---------------------+
| image_data    | `bytes <#bytes>`__  |       | Image data. For     |
|               |                     |       | uncompressed data,  |
|               |                     |       | this is converted   |
|               |                     |       | into FP32, while    |
|               |                     |       | for compressed      |
|               |                     |       | data, this is       |
|               |                     |       | passed to the       |
|               |                     |       | compression library |
|               |                     |       | for decompression.  |
+---------------+---------------------+-------+---------------------+
| nan_encodings | `bytes <#bytes>`__  |       | Run-length          |
|               |                     |       | encodings of NaN    |
|               |                     |       | values. These       |
|               |                     |       | values are used to  |
|               |                     |       | restore the NaN     |
|               |                     |       | values after        |
|               |                     |       | decompression.      |
+---------------+---------------------+-------+---------------------+

.. container:: file-heading

   .. rubric:: region_histogram.proto
      :name: region_histogram.proto

   `Top <#title>`__

.. _CARTA.RegionHistogramData:

RegionHistogramData
~~~~~~~~~~~~~~~~~~~

REGION_HISTOGRAM_DATA:

Stats data for a specific region

+------------+---------------------+----------+---------------------+
| Field      | Type                | Label    | Description         |
+============+=====================+==========+=====================+
| file_id    | `sfix               |          | The file ID that    |
|            | ed32 <#sfixed32>`__ |          | the profile         |
|            |                     |          | corresponds to      |
+------------+---------------------+----------+---------------------+
| region_id  | `sfix               |          | The region_id       |
|            | ed32 <#sfixed32>`__ |          | corresponding to    |
|            |                     |          | these histograms.   |
|            |                     |          | If the histograms   |
|            |                     |          | correspond to the   |
|            |                     |          | entire current 2D   |
|            |                     |          | image, the region   |
|            |                     |          | ID has a value of   |
|            |                     |          | -1.                 |
+------------+---------------------+----------+---------------------+
| stokes     | `sfix               |          | The image stokes    |
|            | ed32 <#sfixed32>`__ |          | parameter used to   |
|            |                     |          | generate the        |
|            |                     |          | profiles            |
+------------+---------------------+----------+---------------------+
| histograms | `Histogram <#       | repeated | array of histograms |
|            | CARTA.Histogram>`__ |          | of the current      |
|            |                     |          | region              |
+------------+---------------------+----------+---------------------+
| progress   | `float <#float>`__  |          | Progress indicator, |
|            |                     |          | in the case of      |
|            |                     |          | partial histogram   |
|            |                     |          | results being sent  |
+------------+---------------------+----------+---------------------+

.. container:: file-heading

   .. rubric:: region_stats.proto
      :name: region_stats.proto

   `Top <#title>`__

.. _CARTA.RegionStatsData:

RegionStatsData
~~~~~~~~~~~~~~~

REGION_STATS_DATA:

Stats data for a specific region

+------------+---------------------+----------+---------------------+
| Field      | Type                | Label    | Description         |
+============+=====================+==========+=====================+
| file_id    | `sfix               |          | The file ID that    |
|            | ed32 <#sfixed32>`__ |          | the profile         |
|            |                     |          | corresponds to      |
+------------+---------------------+----------+---------------------+
| region_id  | `sfix               |          | The region_id       |
|            | ed32 <#sfixed32>`__ |          | corresponding to    |
|            |                     |          | this profile. If    |
|            |                     |          | the statistics data |
|            |                     |          | corresponds to the  |
|            |                     |          | entire current 2D   |
|            |                     |          | image, the region   |
|            |                     |          | ID has a value of   |
|            |                     |          | -1.                 |
+------------+---------------------+----------+---------------------+
| channel    | `sfix               |          | The image channel   |
|            | ed32 <#sfixed32>`__ |          | used to generate    |
|            |                     |          | the statistics      |
+------------+---------------------+----------+---------------------+
| stokes     | `sfix               |          | The image stokes    |
|            | ed32 <#sfixed32>`__ |          | parameter used to   |
|            |                     |          | generate the        |
|            |                     |          | profiles            |
+------------+---------------------+----------+---------------------+
| statistics | `Stati              | repeated | Array of statistics |
|            | sticsValue <#CARTA. |          | values, each        |
|            | StatisticsValue>`__ |          | corresponding to a  |
|            |                     |          | particular          |
|            |                     |          | measurement, such   |
|            |                     |          | as max, min, mean,  |
|            |                     |          | etc                 |
+------------+---------------------+----------+---------------------+

.. container:: file-heading

   .. rubric:: spatial_profile.proto
      :name: spatial_profile.proto

   `Top <#title>`__

.. _CARTA.SpatialProfileData:

SpatialProfileData
~~~~~~~~~~~~~~~~~~

SPATIAL_PROFILE_DATA:

Data for spatial profile set for a specific file

+-----------+---------------------+----------+---------------------+
| Field     | Type                | Label    | Description         |
+===========+=====================+==========+=====================+
| file_id   | `sfix               |          | The file ID that    |
|           | ed32 <#sfixed32>`__ |          | the profile         |
|           |                     |          | corresponds to      |
+-----------+---------------------+----------+---------------------+
| region_id | `sfix               |          | The region_id       |
|           | ed32 <#sfixed32>`__ |          | corresponding to    |
|           |                     |          | this profile. If    |
|           |                     |          | the profile         |
|           |                     |          | corresponds to the  |
|           |                     |          | cursor position,    |
|           |                     |          | the region ID is    |
|           |                     |          | zero.               |
+-----------+---------------------+----------+---------------------+
| x         | `sfix               |          | The pixel           |
|           | ed32 <#sfixed32>`__ |          | X-coordinate of the |
|           |                     |          | profile set         |
+-----------+---------------------+----------+---------------------+
| y         | `sfix               |          | The pixel           |
|           | ed32 <#sfixed32>`__ |          | Y-coordinate of the |
|           |                     |          | profile set         |
+-----------+---------------------+----------+---------------------+
| channel   | `sfix               |          | The image channel   |
|           | ed32 <#sfixed32>`__ |          | used to generate    |
|           |                     |          | the profiles        |
+-----------+---------------------+----------+---------------------+
| stokes    | `sfix               |          | The image stokes    |
|           | ed32 <#sfixed32>`__ |          | parameter used to   |
|           |                     |          | generate the        |
|           |                     |          | profiles            |
+-----------+---------------------+----------+---------------------+
| value     | `float <#float>`__  |          | The value of the    |
|           |                     |          | image at the given  |
|           |                     |          | coordinates         |
+-----------+---------------------+----------+---------------------+
| profiles  | `Spa                | repeated | Spatial profiles    |
|           | tialProfile <#CARTA |          | for each required   |
|           | .SpatialProfile>`__ |          | profile type        |
+-----------+---------------------+----------+---------------------+

.. container:: file-heading

   .. rubric:: spectral_profile.proto
      :name: spectral_profile.proto

   `Top <#title>`__

.. _CARTA.SpectralProfileData:

SpectralProfileData
~~~~~~~~~~~~~~~~~~~

SPECTRAL_PROFILE_DATA:

Data for spectral profile set for a specific file

+-----------+---------------------+----------+---------------------+
| Field     | Type                | Label    | Description         |
+===========+=====================+==========+=====================+
| file_id   | `sfix               |          | The file ID that    |
|           | ed32 <#sfixed32>`__ |          | the profile         |
|           |                     |          | corresponds to      |
+-----------+---------------------+----------+---------------------+
| region_id | `sfix               |          | The region ID that  |
|           | ed32 <#sfixed32>`__ |          | the stats data      |
|           |                     |          | corresponds to. If  |
|           |                     |          | the profile         |
|           |                     |          | corresponds to the  |
|           |                     |          | cursor position,    |
|           |                     |          | the region ID has a |
|           |                     |          | value of 0.         |
+-----------+---------------------+----------+---------------------+
| stokes    | `sfix               |          | The image stokes    |
|           | ed32 <#sfixed32>`__ |          | parameter used to   |
|           |                     |          | generate the        |
|           |                     |          | profiles            |
+-----------+---------------------+----------+---------------------+
| progress  | `float <#float>`__  |          | Progress indicator, |
|           |                     |          | in the case of      |
|           |                     |          | partial profile     |
|           |                     |          | results being sent. |
|           |                     |          | If the profile      |
|           |                     |          | calculations are    |
|           |                     |          | time-consuming,     |
|           |                     |          | regular updates     |
|           |                     |          | should be sent to   |
|           |                     |          | the frontend. If    |
|           |                     |          | the data is         |
|           |                     |          | complete, progress  |
|           |                     |          | >= 1.               |
+-----------+---------------------+----------+---------------------+
| profiles  | `Spect              | repeated | Spatial profiles    |
|           | ralProfile <#CARTA. |          | for each required   |
|           | SpectralProfile>`__ |          | profile type        |
+-----------+---------------------+----------+---------------------+

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
