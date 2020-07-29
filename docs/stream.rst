

.. CARTA.CatalogFilterRequest:

CatalogFilterRequest
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| column_indices | int32 | repeated |  |
+-------+------+-------+-------------+
| filter_configs `FilterConfig <CARTA.FilterConfig>`__ repeated |  |
+-------+------+-------+-------------+
| subset_data_size | sfixed32 |  |  |
+-------+------+-------+-------------+
| subset_start_index | sfixed32 |  |  |
+-------+------+-------+-------------+
| image_bounds `CatalogImageBounds <CARTA.CatalogImageBounds>`__  |  |
+-------+------+-------+-------------+
| image_file_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| region_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| sort_column | string |  |  |
+-------+------+-------+-------------+
| sorting_type `SortingType <CARTA.SortingType>`__  |  |
+-------+------+-------+-------------+



.. CARTA.CatalogFilterResponse:

CatalogFilterResponse
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| image_file_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| region_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| columns `CatalogFilterResponse.ColumnsEntry <CARTA.CatalogFilterResponse.ColumnsEntry>`__ repeated |  |
+-------+------+-------+-------------+
| subset_data_size | sfixed32 |  |  |
+-------+------+-------+-------------+
| subset_end_index | sfixed32 |  |  |
+-------+------+-------+-------------+
| progress | float |  |  |
+-------+------+-------+-------------+
| filter_data_size | sfixed32 |  |  |
+-------+------+-------+-------------+
| request_end_index | sfixed32 |  |  |
+-------+------+-------+-------------+



.. CARTA.CatalogFilterResponse.ColumnsEntry:

CatalogFilterResponse.ColumnsEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | fixed32 |  |  |
+-------+------+-------+-------------+
| value `ColumnData <CARTA.ColumnData>`__  |  |
+-------+------+-------+-------------+






.. CARTA.ContourImageData:

ContourImageData
^^^^^^^^^^^^^

CONTOUR_IMAGE_DATA:
Data for an image rendered in contour mode.


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the contour image corresponds to |
+-------+------+-------+-------------+
| reference_file_id | fixed32 |  | The file ID of the reference image that the contour vertices are mapped to |
+-------+------+-------+-------------+
| image_bounds `ImageBounds <CARTA.ImageBounds>`__  | The bounding box in the XY plane corresponding to the image data in pixel coordinates |
+-------+------+-------+-------------+
| channel | sfixed32 |  | The image channel used to generate the contours |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | The image stokes parameter used to generate the contours |
+-------+------+-------+-------------+
| contour_sets `ContourSet <CARTA.ContourSet>`__ repeated | Each contour set consists of the contour level value, as well as a list of coordinates. The start_indices list is used to determine how to subdivide the coordinates list into separate poly-lines when rendering. |
+-------+------+-------+-------------+
| progress | double |  | Progress of the contour sets being sent. If this is zero, the message is assumed to contain the entire contour sets |
+-------+------+-------+-------------+



.. CARTA.ContourSet:

ContourSet
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| level | double |  |  |
+-------+------+-------+-------------+
| decimation_factor | int32 |  |  |
+-------+------+-------+-------------+
| raw_coordinates | bytes |  |  |
+-------+------+-------+-------------+
| raw_start_indices | bytes |  |  |
+-------+------+-------+-------------+
| uncompressed_coordinates_size | int32 |  |  |
+-------+------+-------+-------------+






.. CARTA.ErrorData:

ErrorData
^^^^^^^^^^^^^

ERROR_DATA:
Stream of error/warning/info data. This stream is used to present the frontend with additional information on
the state of the backend, and is not used in place of returning success=false on requests or commands.


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| severity `ErrorSeverity <CARTA.ErrorSeverity>`__  | The severity of the error. Critical errors are reserved for errors that would normally require the user to restart the program or reload the page |
+-------+------+-------+-------------+
| tags | string | repeated | A list of strings describing the error type, that the frontend can interpret and react to. For example, “file_io” or “memory”. |
+-------+------+-------+-------------+
| message | string |  | The error message |
+-------+------+-------+-------------+
| data | string |  | Accompanying error data. For example, if an error has the “file_io” tag, the frontend would expect the data field to contain the file ID of the offending file. |
+-------+------+-------+-------------+






.. CARTA.RasterTileData:

RasterTileData
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the raster image corresponds to |
+-------+------+-------+-------------+
| channel | sfixed32 |  | The image channel (z-coordinate) |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | The image stokes coordinate |
+-------+------+-------+-------------+
| compression_type `CompressionType <CARTA.CompressionType>`__  | The compression algorithm used. |
+-------+------+-------+-------------+
| compression_quality | float |  | Compression quality switch |
+-------+------+-------+-------------+
| animation_id | sfixed32 |  | The ID of the animation (if any) |
+-------+------+-------+-------------+
| tiles `TileData <CARTA.TileData>`__ repeated | List of tile data |
+-------+------+-------+-------------+



.. CARTA.RasterTileSync:

RasterTileSync
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the raster image corresponds to |
+-------+------+-------+-------------+
| channel | sfixed32 |  | The image channel (z-coordinate) |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | The image stokes coordinate |
+-------+------+-------+-------------+
| animation_id | sfixed32 |  | The ID of the animation (if any) |
+-------+------+-------+-------------+
| end_sync | bool |  | Is this a start or end sync message? |
+-------+------+-------+-------------+



.. CARTA.TileData:

TileData
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| layer | sfixed32 |  | Tile layer coordinate |
+-------+------+-------+-------------+
| x | sfixed32 |  | Tile x coordinate |
+-------+------+-------+-------------+
| y | sfixed32 |  | Tile y coordinate |
+-------+------+-------+-------------+
| width | sfixed32 |  | Width of the tile data. If this is left as zero, the default tile size should be used |
+-------+------+-------+-------------+
| height | sfixed32 |  | Height of the tile data. If this is left as zero, the default tile size should be used |
+-------+------+-------+-------------+
| image_data | bytes |  | Image data. For uncompressed data, this is converted into FP32, while for compressed data, this is passed to the compression library for decompression. |
+-------+------+-------+-------------+
| nan_encodings | bytes |  | Run-length encodings of NaN values. These values are used to restore the NaN values after decompression. |
+-------+------+-------+-------------+






.. CARTA.RegionHistogramData:

RegionHistogramData
^^^^^^^^^^^^^

REGION_HISTOGRAM_DATA:
Stats data for a specific region


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the profile corresponds to |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | The region_id corresponding to these histograms. If the histograms correspond to the entire current 2D image, the region ID has a value of -1. |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | The image stokes parameter used to generate the profiles |
+-------+------+-------+-------------+
| histograms `Histogram <CARTA.Histogram>`__ repeated | array of histograms of the current region |
+-------+------+-------+-------------+
| progress | float |  | Progress indicator, in the case of partial histogram results being sent |
+-------+------+-------+-------------+






.. CARTA.RegionStatsData:

RegionStatsData
^^^^^^^^^^^^^

REGION_STATS_DATA:
Stats data for a specific region


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the profile corresponds to |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | The region_id corresponding to this profile. If the statistics data corresponds to the entire current 2D image, the region ID has a value of -1. |
+-------+------+-------+-------------+
| channel | sfixed32 |  | The image channel used to generate the statistics |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | The image stokes parameter used to generate the profiles |
+-------+------+-------+-------------+
| statistics `StatisticsValue <CARTA.StatisticsValue>`__ repeated | Array of statistics values, each corresponding to a particular measurement, such as max, min, mean, etc |
+-------+------+-------+-------------+






.. CARTA.SpatialProfileData:

SpatialProfileData
^^^^^^^^^^^^^

SPATIAL_PROFILE_DATA:
Data for spatial profile set for a specific file


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the profile corresponds to |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | The region_id corresponding to this profile. If the profile corresponds to the cursor position, the region ID is zero. |
+-------+------+-------+-------------+
| x | sfixed32 |  | The pixel X-coordinate of the profile set |
+-------+------+-------+-------------+
| y | sfixed32 |  | The pixel Y-coordinate of the profile set |
+-------+------+-------+-------------+
| channel | sfixed32 |  | The image channel used to generate the profiles |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | The image stokes parameter used to generate the profiles |
+-------+------+-------+-------------+
| value | float |  | The value of the image at the given coordinates |
+-------+------+-------+-------------+
| profiles `SpatialProfile <CARTA.SpatialProfile>`__ repeated | Spatial profiles for each required profile type |
+-------+------+-------+-------------+






.. CARTA.SpectralProfileData:

SpectralProfileData
^^^^^^^^^^^^^

SPECTRAL_PROFILE_DATA:
Data for spectral profile set for a specific file


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the profile corresponds to |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | The region ID that the stats data corresponds to. If the profile corresponds to the cursor position, the region ID has a value of 0. |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | The image stokes parameter used to generate the profiles |
+-------+------+-------+-------------+
| progress | float |  | Progress indicator, in the case of partial profile results being sent. If the profile calculations are time-consuming, regular updates should be sent to the frontend. If the data is complete, progress >= 1. |
+-------+------+-------+-------------+
| profiles `SpectralProfile <CARTA.SpectralProfile>`__ repeated | Spatial profiles for each required profile type |
+-------+------+-------+-------------+





