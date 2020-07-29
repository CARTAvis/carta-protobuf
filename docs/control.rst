

.. CARTA.AnimationFlowControl:

AnimationFlowControl
^^^^^^^^^^^^^

ANIMATION_FLOW_CONTROL
Used for informing the backend of which frames have been received


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| received_frame `AnimationFrame <CARTA.AnimationFrame>`__  | The latest flow control frame received |
+-------+------+-------+-------------+
| animation_id | sfixed32 |  | The animation ID that the flow control message belongs to |
+-------+------+-------+-------------+
| timestamp | sfixed64 |  | Timestamp at which the frame was received |
+-------+------+-------+-------------+



.. CARTA.StartAnimation:

StartAnimation
^^^^^^^^^^^^^

START_ANIMATION:
Starts an animation, as defined by the start, stop and step definitions.
Backend responds with START_ANIMATION_ACK


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | Which file slot the animation describes. |
+-------+------+-------+-------------+
| first_frame `AnimationFrame <CARTA.AnimationFrame>`__  | The lower bound of the animation when looping. |
+-------+------+-------+-------------+
| start_frame `AnimationFrame <CARTA.AnimationFrame>`__  | The starting point of the animation. |
+-------+------+-------+-------------+
| last_frame `AnimationFrame <CARTA.AnimationFrame>`__  | The upper bound of the animation. |
+-------+------+-------+-------------+
| delta_frame `AnimationFrame <CARTA.AnimationFrame>`__  | The frame change step for the animation. For example, a delta frame of {channel=1, stokes=0} would step through each channel in the file. |
+-------+------+-------+-------------+
| frame_rate | sfixed32 |  | Frame rate per second |
+-------+------+-------+-------------+
| looping | bool |  | Whether to loop the animation indefinitely. |
+-------+------+-------+-------------+
| reverse | bool |  | Whether to reverse the animation direction when endFrame is reached. |
+-------+------+-------+-------------+
| required_tiles `AddRequiredTiles <CARTA.AddRequiredTiles>`__  | Required tiles when changing channels |
+-------+------+-------+-------------+



.. CARTA.StartAnimationAck:

StartAnimationAck
^^^^^^^^^^^^^

START_ANIMATION_ACK
Response for START_ANIMATION


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether START_ANIMATION was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| animation_id | sfixed32 |  | The animation ID of the new animation |
+-------+------+-------+-------------+



.. CARTA.StopAnimation:

StopAnimation
^^^^^^^^^^^^^

STOP_ANIMATION
Stops the playing animation


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | Which file slot the animation describes. |
+-------+------+-------+-------------+
| end_frame `AnimationFrame <CARTA.AnimationFrame>`__  | The ending point of the animation. |
+-------+------+-------+-------------+






.. CARTA.CloseFile:

CloseFile
^^^^^^^^^^^^^

CLOSE_FILE:
Instructs the backend to close a file with a given file ID


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | Which "file" slot to close |
+-------+------+-------+-------------+






.. CARTA.SetContourParameters:

SetContourParameters
^^^^^^^^^^^^^

SET_CONTOUR_PARAMETERS
Sets the contour parameters for a file


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | fixed32 |  | The file ID that the contour corresponds to |
+-------+------+-------+-------------+
| reference_file_id | fixed32 |  | The file ID of the reference image that the contour vertices should be mapped to |
+-------+------+-------+-------------+
| image_bounds `ImageBounds <CARTA.ImageBounds>`__  | The XY bounds corresponding to the image data in pixel coordinates |
+-------+------+-------+-------------+
| levels | double | repeated | Contour levels |
+-------+------+-------+-------------+
| smoothing_mode `SmoothingMode <CARTA.SmoothingMode>`__  | Pre-contouring smoothing mode |
+-------+------+-------+-------------+
| smoothing_factor | int32 |  | Contour smoothness factor. For block averaging, this is the block width For Gaussian smoothing, this defines both the Gaussian width, and the kernel size |
+-------+------+-------+-------------+
| decimation_factor | int32 |  | Decimation factor, indicates to what 1/Nth of a pixel the contour vertices should be rounded to |
+-------+------+-------+-------------+
| compression_level | int32 |  | Zstd compression level |
+-------+------+-------+-------------+
| contour_chunk_size | int32 |  | Size of contour chunks, in number of vertices. If this is set to zero, partial contour results are not used |
+-------+------+-------+-------------+






.. CARTA.ExportRegion:

ExportRegion
^^^^^^^^^^^^^

EXPORT_REGION:
Requests exporting the specified regions to a file on the server.
If directory and file are blank, return file contents for export on client.
Backend responds with  EXPORT_REGION_ACK


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| type `FileType <CARTA.FileType>`__  | Required file type |
+-------+------+-------+-------------+
| coord_type `CoordinateType <CARTA.CoordinateType>`__  | Required coordinate type pixel/world |
+-------+------+-------+-------------+
| file_id | sfixed32 |  | File id for the coordinate system to use |
+-------+------+-------+-------------+
| region_styles `ExportRegion.RegionStylesEntry <CARTA.ExportRegion.RegionStylesEntry>`__ repeated | Region ids and style params to export |
+-------+------+-------+-------------+
| directory | string |  | Optional directory name of server file |
+-------+------+-------+-------------+
| file | string |  | Optional file name of server file |
+-------+------+-------+-------------+



.. CARTA.ExportRegion.RegionStylesEntry:

ExportRegion.RegionStylesEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | sfixed32 |  |  |
+-------+------+-------+-------------+
| value `RegionStyle <CARTA.RegionStyle>`__  |  |
+-------+------+-------+-------------+



.. CARTA.ExportRegionAck:

ExportRegionAck
^^^^^^^^^^^^^

EXPORT_REGION_ACK
Response for EXPORT_REGION to indicate success and file contents if on client.


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether EXPORT_REGION was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| contents | string | repeated | File contents for client export (one line per string) |
+-------+------+-------+-------------+






.. CARTA.ImportRegion:

ImportRegion
^^^^^^^^^^^^^

IMPORT_REGION:
Requests the opening and applying of a specific region file.
Backend responds with  IMPORT_REGION_ACK


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| group_id | sfixed32 |  | Required WCS group id (may be a single file id) |
+-------+------+-------+-------------+
| type `FileType <CARTA.FileType>`__  | Required file type |
+-------+------+-------+-------------+
| directory | string |  | Optional directory name of server file |
+-------+------+-------+-------------+
| file | string |  | Optional file name of server file |
+-------+------+-------+-------------+
| contents | string | repeated | Optional file contents of client file (1 line per string) |
+-------+------+-------+-------------+



.. CARTA.ImportRegionAck:

ImportRegionAck
^^^^^^^^^^^^^

IMPORT_REGION_ACK
Response for IMPORT_REGION. Also supplies region properties


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether IMPORT_REGION was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| regions `ImportRegionAck.RegionsEntry <CARTA.ImportRegionAck.RegionsEntry>`__ repeated | Map region id to parameters |
+-------+------+-------+-------------+
| region_styles `ImportRegionAck.RegionStylesEntry <CARTA.ImportRegionAck.RegionStylesEntry>`__ repeated | Map region id to style parameters |
+-------+------+-------+-------------+



.. CARTA.ImportRegionAck.RegionStylesEntry:

ImportRegionAck.RegionStylesEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | sfixed32 |  |  |
+-------+------+-------+-------------+
| value `RegionStyle <CARTA.RegionStyle>`__  |  |
+-------+------+-------+-------------+



.. CARTA.ImportRegionAck.RegionsEntry:

ImportRegionAck.RegionsEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | sfixed32 |  |  |
+-------+------+-------+-------------+
| value `RegionInfo <CARTA.RegionInfo>`__  |  |
+-------+------+-------+-------------+






.. CARTA.CloseCatalogFile:

CloseCatalogFile
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  |  |
+-------+------+-------+-------------+



.. CARTA.OpenCatalogFile:

OpenCatalogFile
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  |  |
+-------+------+-------+-------------+
| name | string |  |  |
+-------+------+-------+-------------+
| file_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| preview_data_size | sfixed32 |  |  |
+-------+------+-------+-------------+



.. CARTA.OpenCatalogFileAck:

OpenCatalogFileAck
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  |  |
+-------+------+-------+-------------+
| message | string |  |  |
+-------+------+-------+-------------+
| file_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| file_info `CatalogFileInfo <CARTA.CatalogFileInfo>`__  |  |
+-------+------+-------+-------------+
| data_size | sfixed32 |  |  |
+-------+------+-------+-------------+
| headers `CatalogHeader <CARTA.CatalogHeader>`__ repeated |  |
+-------+------+-------+-------------+
| preview_data `OpenCatalogFileAck.PreviewDataEntry <CARTA.OpenCatalogFileAck.PreviewDataEntry>`__ repeated |  |
+-------+------+-------+-------------+



.. CARTA.OpenCatalogFileAck.PreviewDataEntry:

OpenCatalogFileAck.PreviewDataEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | fixed32 |  |  |
+-------+------+-------+-------------+
| value `ColumnData <CARTA.ColumnData>`__  |  |
+-------+------+-------+-------------+






.. CARTA.OpenFile:

OpenFile
^^^^^^^^^^^^^

OPEN_FILE:
Requests the opening of a specific file.
Backend responds with  OPEN_FILE_ACK


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  | Required directory name |
+-------+------+-------+-------------+
| file | string |  | Required file name |
+-------+------+-------+-------------+
| hdu | string |  | Which HDU to load (if applicable). If left blank, the first HDU will be used |
+-------+------+-------+-------------+
| file_id | sfixed32 |  | Which "file" slot to load the file into (when viewing multiple files) |
+-------+------+-------+-------------+
| render_mode `RenderMode <CARTA.RenderMode>`__  | The render mode to use. Additional modes will be added in subsequent versions. |
+-------+------+-------+-------------+



.. CARTA.OpenFileAck:

OpenFileAck
^^^^^^^^^^^^^

OPEN_FILE_ACK
Response for OPEN_FILE. Also supplies file information


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether OPEN_FILE was successful |
+-------+------+-------+-------------+
| file_id | sfixed32 |  | Which file slot the file was loaded into (when viewing multiple files) |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| file_info `FileInfo <CARTA.FileInfo>`__  | Basic file info (type, size) |
+-------+------+-------+-------------+
| file_info_extended `FileInfoExtended <CARTA.FileInfoExtended>`__  | Extended file info (WCS, header info) |
+-------+------+-------+-------------+
| file_feature_flags | fixed32 |  | Optional bitflags specifying feature flags of the file being opened. |
+-------+------+-------+-------------+






.. CARTA.RemoveRegion:

RemoveRegion
^^^^^^^^^^^^^

REMOVE_REGION:
Removes a region


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| region_id | sfixed32 |  | Unique region ID of the region to be removed |
+-------+------+-------+-------------+



.. CARTA.SetRegion:

SetRegion
^^^^^^^^^^^^^

SET_REGION:
Creates or updates a region. Backend responds with SET_REGION_ACK


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | File slot of the reference image |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | Unique region ID. <=0 if a new region is being created. |
+-------+------+-------+-------------+
| region_info `RegionInfo <CARTA.RegionInfo>`__  | Region parameters |
+-------+------+-------+-------------+



.. CARTA.SetRegionAck:

SetRegionAck
^^^^^^^^^^^^^

SET_REGION_ACK:
Response for SET_REGION


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether SET_REGION was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | The unique region ID. If the region is updated, this will be the same as the region ID specified in SET_REGION. If a new region is being created, the ID of the new region will be passed back. |
+-------+------+-------+-------------+






.. CARTA.SetHistogramRequirements:

SetHistogramRequirements
^^^^^^^^^^^^^

SET_HISTOGRAM_REQUIREMENTS:
Sets which histogram data needs to be streamed to the frontend when the region is updated


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | Which file slot the requirements describe |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | ID of the region that is having requirements defined. If a region ID of -1 is given, this corresponds to the entire 2D image. |
+-------+------+-------+-------------+
| histograms `SetHistogramRequirements.HistogramConfig <CARTA.SetHistogramRequirements.HistogramConfig>`__ repeated | List of required histograms, along with the number of bins. If the channel is -1, the current channel is used. If the channel is -2, the histogram is constructed over all channels. If the number of bins is less than zero, an automatic bin size is used, based on the number of values. |
+-------+------+-------+-------------+



.. CARTA.SetHistogramRequirements.HistogramConfig:

SetHistogramRequirements.HistogramConfig
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| channel | sfixed32 |  |  |
+-------+------+-------+-------------+
| num_bins | sfixed32 |  |  |
+-------+------+-------+-------------+



.. CARTA.SetRegionRequirements:

SetRegionRequirements
^^^^^^^^^^^^^

SET_REGION_REQUIREMENTS:
Sets which spatial profile data needs to be streamed to the frontend when the region is updated


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | fixed32 |  |  |
+-------+------+-------+-------------+
| region_id | fixed32 |  | ID of the region that is having requirements defined. If a region ID of 0 is given, this corresponds to the point region defined by the cursor position. |
+-------+------+-------+-------------+
| x | bool |  | Is the X-profile (of the current Stokes parameter) required? |
+-------+------+-------+-------------+
| y | bool |  | Is the Y-profile (of the current Stokes parameter) required? |
+-------+------+-------+-------------+
| z | bool |  | Is the Z-profile (of the current Stokes parameter) required? |
+-------+------+-------+-------------+
| additional_profiles | string | repeated | List of additional profiles needed (for example, [“Qz”, “Uz”]) will include the Z-profile of the Q and U Stokes cube, regardless of which Stokes parameter is currently in use. |
+-------+------+-------+-------------+



.. CARTA.SetSpatialRequirements:

SetSpatialRequirements
^^^^^^^^^^^^^

SET_SPATIAL_REQUIREMENTS:
Sets which information needs to be streamed to the frontend when the region is updated


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | Which file slot the requirements describe |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | ID of the region that is having requirements defined. If a region ID of 0 is given, this corresponds to the point region defined by the cursor position. |
+-------+------+-------+-------------+
| spatial_profiles | string | repeated | List of spatial profiles needed. If no Stokes parameter is specified (i.e. just “x” or “y”), the active Stokes parameter is used. |
+-------+------+-------+-------------+



.. CARTA.SetSpectralRequirements:

SetSpectralRequirements
^^^^^^^^^^^^^

SET_SPECTRAL_REQUIREMENTS:
Sets which spectral profile data needs to be streamed to the frontend when the region is updated


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | Which file slot the requirements describe |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | ID of the region that is having requirements defined. If a region ID of 0 is given, this corresponds to the point region defined by the cursor position. |
+-------+------+-------+-------------+
| spectral_profiles `SetSpectralRequirements.SpectralConfig <CARTA.SetSpectralRequirements.SpectralConfig>`__ repeated | List of spectral profiles needed, along with which stats types are needed for each profile. If no Stokes parameter is specified (i.e. just “z”) or if the coordinate is empty, the active Stokes parameter is used. If the region is a point region, the statsTypes field is ignored. |
+-------+------+-------+-------------+



.. CARTA.SetSpectralRequirements.SpectralConfig:

SetSpectralRequirements.SpectralConfig
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| coordinate | string |  |  |
+-------+------+-------+-------------+
| stats_types `StatsType <CARTA.StatsType>`__ repeated |  |
+-------+------+-------+-------------+



.. CARTA.SetStatsRequirements:

SetStatsRequirements
^^^^^^^^^^^^^

SET_STATS_REQUIREMENTS:
Sets which stats data needs to be streamed to the frontend when the region is updated


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | Which file slot the requirements describe |
+-------+------+-------+-------------+
| region_id | sfixed32 |  | ID of the region that is having requirements defined. If a region ID of -1 is given, this corresponds to the entire 2D image. |
+-------+------+-------+-------------+
| stats `StatsType <CARTA.StatsType>`__ repeated | List of required stats |
+-------+------+-------+-------------+






.. CARTA.RegisterViewer:

RegisterViewer
^^^^^^^^^^^^^

REGISTER_VIEWER:
Registers the viewer with the backend.
Responds with REGISTER_VIEWER_ACK


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| session_id | fixed32 |  | Unique session ID parameter (can be generated using UUID libraries). Passing in an existing session ID can be used for resuming sessions |
+-------+------+-------+-------------+
| api_key | string |  | Optional user-specific API key to be used for basic authentication. Could be an encrypted JWT for secure authentication. |
+-------+------+-------+-------------+
| client_feature_flags | fixed32 |  | Optional feature bitflag specifying client-side feature set |
+-------+------+-------+-------------+



.. CARTA.RegisterViewerAck:

RegisterViewerAck
^^^^^^^^^^^^^

REGISTER_VIEWER_ACK
Acknowledgement response for REGISTER_VIEWER.
Informs the frontend whether the session was correctly.


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| session_id | fixed32 |  | Unique session ID |
+-------+------+-------+-------------+
| success | bool |  | Defines whether the REGISTER_VIEWER command was successful |
+-------+------+-------+-------------+
| message | string |  | Error message (if applicable) |
+-------+------+-------+-------------+
| session_type `SessionType <CARTA.SessionType>`__  | Defines the type of session established |
+-------+------+-------+-------------+
| server_feature_flags | fixed32 |  | Optional feature bitflag specifying server-side feature set |
+-------+------+-------+-------------+
| user_preferences `RegisterViewerAck.UserPreferencesEntry <CARTA.RegisterViewerAck.UserPreferencesEntry>`__ repeated | Map of user preferences retrieved from the server database. If this is empty and the server does not have the USER_PREFERENCES feature flag set, then the user preferences are read from localStorage instead. |
+-------+------+-------+-------------+
| user_layouts `RegisterViewerAck.UserLayoutsEntry <CARTA.RegisterViewerAck.UserLayoutsEntry>`__ repeated | Map of user layouts retrieved from the server database |
+-------+------+-------+-------------+



.. CARTA.RegisterViewerAck.UserLayoutsEntry:

RegisterViewerAck.UserLayoutsEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | string |  |  |
+-------+------+-------+-------------+
| value | string |  |  |
+-------+------+-------+-------------+



.. CARTA.RegisterViewerAck.UserPreferencesEntry:

RegisterViewerAck.UserPreferencesEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | string |  |  |
+-------+------+-------+-------------+
| value | string |  |  |
+-------+------+-------+-------------+






.. CARTA.ImageProperties:

ImageProperties
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| directory | string |  |  |
+-------+------+-------+-------------+
| file | string |  |  |
+-------+------+-------+-------------+
| hdu | string |  |  |
+-------+------+-------+-------------+
| file_id | sfixed32 |  |  |
+-------+------+-------+-------------+
| render_mode `RenderMode <CARTA.RenderMode>`__  |  |
+-------+------+-------+-------------+
| channel | sfixed32 |  |  |
+-------+------+-------+-------------+
| stokes | sfixed32 |  |  |
+-------+------+-------+-------------+
| regions `ImageProperties.RegionsEntry <CARTA.ImageProperties.RegionsEntry>`__ repeated |  |
+-------+------+-------+-------------+
| contour_settings `SetContourParameters <CARTA.SetContourParameters>`__  |  |
+-------+------+-------+-------------+



.. CARTA.ImageProperties.RegionsEntry:

ImageProperties.RegionsEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | sfixed32 |  |  |
+-------+------+-------+-------------+
| value `RegionInfo <CARTA.RegionInfo>`__  |  |
+-------+------+-------+-------------+



.. CARTA.ResumeSession:

ResumeSession
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| images `ImageProperties <CARTA.ImageProperties>`__ repeated |  |
+-------+------+-------+-------------+
| catalog_files `OpenCatalogFile <CARTA.OpenCatalogFile>`__ repeated |  |
+-------+------+-------+-------------+



.. CARTA.ResumeSessionAck:

ResumeSessionAck
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  |  |
+-------+------+-------+-------------+
| message | string |  |  |
+-------+------+-------+-------------+






.. CARTA.SetCursor:

SetCursor
^^^^^^^^^^^^^

SET_CURSOR:
Sets the current cursor position in image space coordinates.
The cursor defines a special case of a region, with a single control point.


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | Which file slot the cursor is moving over |
+-------+------+-------+-------------+
| point `Point <CARTA.Point>`__  | XY-coordinates of cursor in image space |
+-------+------+-------+-------------+
| spatial_requirements `SetSpatialRequirements <CARTA.SetSpatialRequirements>`__  | Optional accompanying spatial requirements message to be processed prior to cursor update |
+-------+------+-------+-------------+






.. CARTA.SetImageChannels:

SetImageChannels
^^^^^^^^^^^^^

SET_IMAGE_CHANNELS
Sets the current image channel and Stokes parameter


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the view corresponds to |
+-------+------+-------+-------------+
| channel | sfixed32 |  | The image channel (Z-coordinate) |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | The image stokes parameter |
+-------+------+-------+-------------+
| required_tiles `AddRequiredTiles <CARTA.AddRequiredTiles>`__  | Required tiles when changing channels |
+-------+------+-------+-------------+






.. CARTA.SpectralLineRequest:

SpectralLineRequest
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| frequency_range `DoubleBounds <CARTA.DoubleBounds>`__  |  |
+-------+------+-------+-------------+



.. CARTA.SpectralLineResponse:

SpectralLineResponse
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  |  |
+-------+------+-------+-------------+
| message | string |  |  |
+-------+------+-------+-------------+
| data_size | sfixed32 |  |  |
+-------+------+-------+-------------+
| headers `CatalogHeader <CARTA.CatalogHeader>`__ repeated |  |
+-------+------+-------+-------------+
| spectral_line_data `SpectralLineResponse.SpectralLineDataEntry <CARTA.SpectralLineResponse.SpectralLineDataEntry>`__ repeated |  |
+-------+------+-------+-------------+



.. CARTA.SpectralLineResponse.SpectralLineDataEntry:

SpectralLineResponse.SpectralLineDataEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | fixed32 |  |  |
+-------+------+-------+-------------+
| value `ColumnData <CARTA.ColumnData>`__  |  |
+-------+------+-------+-------------+






.. CARTA.AddRequiredTiles:

AddRequiredTiles
^^^^^^^^^^^^^

ADD_REQUIRED_TILES
Provides a list of tiles that are required for the specified file


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the view corresponds to |
+-------+------+-------+-------------+
| tiles | sfixed32 | repeated | The list of tiles required, in encoded coordinate |
+-------+------+-------+-------------+
| compression_type `CompressionType <CARTA.CompressionType>`__  | The compression algorithm used |
+-------+------+-------+-------------+
| compression_quality | float |  | Compression quality switch |
+-------+------+-------+-------------+



.. CARTA.RemoveRequiredTiles:

RemoveRequiredTiles
^^^^^^^^^^^^^

REMOVE_REQUIRED_TILES
Provides a list of tiles that are required for the specified file


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| file_id | sfixed32 |  | The file ID that the view corresponds to |
+-------+------+-------+-------------+
| tiles | sfixed32 | repeated | The list of tiles required, in encoded coordinate |
+-------+------+-------+-------------+






.. CARTA.SetUserLayout:

SetUserLayout
^^^^^^^^^^^^^

SET_USER_LAYOUT:
Sets or clears a user layout.
Backend responds with  SET_USER_LAYOUT_ACK


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| name | string |  | Name of the layout to update. If no layout with the given name is present in the server database, a new layout is created |
+-------+------+-------+-------------+
| value | string |  | JSON string representing the layout. If the value is empty, the user layout is cleared from the server database. |
+-------+------+-------+-------------+



.. CARTA.SetUserLayoutAck:

SetUserLayoutAck
^^^^^^^^^^^^^

SET_USER_LAYOUT_ACK
Response for SET_USER_LAYOUT


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether SET_USER_LAYOUT was successful

Error message (if applicable) |
+-------+------+-------+-------------+






.. CARTA.SetUserPreferences:

SetUserPreferences
^^^^^^^^^^^^^

SET_USER_PREFERENCES:
Sets or clears one or more user preferences.
Backend responds with  SET_USER_PREFERENCES_ACK


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| preference_map `SetUserPreferences.PreferenceMapEntry <CARTA.SetUserPreferences.PreferenceMapEntry>`__ repeated |  |
+-------+------+-------+-------------+



.. CARTA.SetUserPreferences.PreferenceMapEntry:

SetUserPreferences.PreferenceMapEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| key | string |  |  |
+-------+------+-------+-------------+
| value | string |  |  |
+-------+------+-------+-------------+



.. CARTA.SetUserPreferencesAck:

SetUserPreferencesAck
^^^^^^^^^^^^^

SET_USER_PREFERENCES_ACK
Response for SET_USER_PREFERENCES


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| success | bool |  | Defines whether SET_USER_PREFERENCES was successful

Error message (if applicable) |
+-------+------+-------+-------------+





