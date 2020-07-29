.. _title:

Protocol Documentation
======================

Table of Contents
-----------------

.. container::
   :name: toc-container

   -  `animation.proto <#animation.proto>`__

      -  `MAnimationFlowControl <#CARTA.AnimationFlowControl>`__
      -  `MStartAnimation <#CARTA.StartAnimation>`__
      -  `MStartAnimationAck <#CARTA.StartAnimationAck>`__
      -  `MStopAnimation <#CARTA.StopAnimation>`__

   -  `close_file.proto <#close_file.proto>`__

      -  `MCloseFile <#CARTA.CloseFile>`__

   -  `contour.proto <#contour.proto>`__

      -  `MSetContourParameters <#CARTA.SetContourParameters>`__

   -  `export_region.proto <#export_region.proto>`__

      -  `MExportRegion <#CARTA.ExportRegion>`__
      -  `MExportRegion.RegionStylesEntry <#CARTA.ExportRegion.RegionStylesEntry>`__
      -  `MExportRegionAck <#CARTA.ExportRegionAck>`__

   -  `import_region.proto <#import_region.proto>`__

      -  `MImportRegion <#CARTA.ImportRegion>`__
      -  `MImportRegionAck <#CARTA.ImportRegionAck>`__
      -  `MImportRegionAck.RegionStylesEntry <#CARTA.ImportRegionAck.RegionStylesEntry>`__
      -  `MImportRegionAck.RegionsEntry <#CARTA.ImportRegionAck.RegionsEntry>`__

   -  `open_catalog_file.proto <#open_catalog_file.proto>`__

      -  `MCloseCatalogFile <#CARTA.CloseCatalogFile>`__
      -  `MOpenCatalogFile <#CARTA.OpenCatalogFile>`__
      -  `MOpenCatalogFileAck <#CARTA.OpenCatalogFileAck>`__
      -  `MOpenCatalogFileAck.PreviewDataEntry <#CARTA.OpenCatalogFileAck.PreviewDataEntry>`__

   -  `open_file.proto <#open_file.proto>`__

      -  `MOpenFile <#CARTA.OpenFile>`__
      -  `MOpenFileAck <#CARTA.OpenFileAck>`__

   -  `region.proto <#region.proto>`__

      -  `MRemoveRegion <#CARTA.RemoveRegion>`__
      -  `MSetRegion <#CARTA.SetRegion>`__
      -  `MSetRegionAck <#CARTA.SetRegionAck>`__

   -  `region_requirements.proto <#region_requirements.proto>`__

      -  `MSetHistogramRequirements <#CARTA.SetHistogramRequirements>`__
      -  `MSetHistogramRequirements.HistogramConfig <#CARTA.SetHistogramRequirements.HistogramConfig>`__
      -  `MSetRegionRequirements <#CARTA.SetRegionRequirements>`__
      -  `MSetSpatialRequirements <#CARTA.SetSpatialRequirements>`__
      -  `MSetSpectralRequirements <#CARTA.SetSpectralRequirements>`__
      -  `MSetSpectralRequirements.SpectralConfig <#CARTA.SetSpectralRequirements.SpectralConfig>`__
      -  `MSetStatsRequirements <#CARTA.SetStatsRequirements>`__

   -  `register_viewer.proto <#register_viewer.proto>`__

      -  `MRegisterViewer <#CARTA.RegisterViewer>`__
      -  `MRegisterViewerAck <#CARTA.RegisterViewerAck>`__
      -  `MRegisterViewerAck.UserLayoutsEntry <#CARTA.RegisterViewerAck.UserLayoutsEntry>`__
      -  `MRegisterViewerAck.UserPreferencesEntry <#CARTA.RegisterViewerAck.UserPreferencesEntry>`__

   -  `resume_session.proto <#resume_session.proto>`__

      -  `MImageProperties <#CARTA.ImageProperties>`__
      -  `MImageProperties.RegionsEntry <#CARTA.ImageProperties.RegionsEntry>`__
      -  `MResumeSession <#CARTA.ResumeSession>`__
      -  `MResumeSessionAck <#CARTA.ResumeSessionAck>`__

   -  `set_cursor.proto <#set_cursor.proto>`__

      -  `MSetCursor <#CARTA.SetCursor>`__

   -  `set_image_channels.proto <#set_image_channels.proto>`__

      -  `MSetImageChannels <#CARTA.SetImageChannels>`__

   -  `spectral_line_request.proto <#spectral_line_request.proto>`__

      -  `MSpectralLineRequest <#CARTA.SpectralLineRequest>`__
      -  `MSpectralLineResponse <#CARTA.SpectralLineResponse>`__
      -  `MSpectralLineResponse.SpectralLineDataEntry <#CARTA.SpectralLineResponse.SpectralLineDataEntry>`__

   -  `tiles.proto <#tiles.proto>`__

      -  `MAddRequiredTiles <#CARTA.AddRequiredTiles>`__
      -  `MRemoveRequiredTiles <#CARTA.RemoveRequiredTiles>`__

   -  `user_layout.proto <#user_layout.proto>`__

      -  `MSetUserLayout <#CARTA.SetUserLayout>`__
      -  `MSetUserLayoutAck <#CARTA.SetUserLayoutAck>`__

   -  `user_preferences.proto <#user_preferences.proto>`__

      -  `MSetUserPreferences <#CARTA.SetUserPreferences>`__
      -  `MSetUserPreferences.PreferenceMapEntry <#CARTA.SetUserPreferences.PreferenceMapEntry>`__
      -  `MSetUserPreferencesAck <#CARTA.SetUserPreferencesAck>`__

   -  `Scalar Value Types <#scalar-value-types>`__

.. container:: file-heading

   .. rubric:: animation.proto
      :name: animation.proto

   `Top <#title>`__

.. _CARTA.AnimationFlowControl:

AnimationFlowControl
~~~~~~~~~~~~~~~~~~~~

ANIMATION_FLOW_CONTROL

Used for informing the backend of which frames have been received

+----------------+-------------------+-------+-------------------+
| Field          | Type              | Label | Description       |
+================+===================+=======+===================+
| file_id        | `sfixed           |       |                   |
|                | 32 <#sfixed32>`__ |       |                   |
+----------------+-------------------+-------+-------------------+
| received_frame | `Animati          |       | The latest flow   |
|                | onFrame <#CARTA.A |       | control frame     |
|                | nimationFrame>`__ |       | received          |
+----------------+-------------------+-------+-------------------+
| animation_id   | `sfixed           |       | The animation ID  |
|                | 32 <#sfixed32>`__ |       | that the flow     |
|                |                   |       | control message   |
|                |                   |       | belongs to        |
+----------------+-------------------+-------+-------------------+
| timestamp      | `sfixed           |       | Timestamp at      |
|                | 64 <#sfixed64>`__ |       | which the frame   |
|                |                   |       | was received      |
+----------------+-------------------+-------+-------------------+

.. _CARTA.StartAnimation:

StartAnimation
~~~~~~~~~~~~~~

START_ANIMATION:

Starts an animation, as defined by the start, stop and step definitions.

Backend responds with START_ANIMATION_ACK

+----------------+-------------------+-------+-------------------+
| Field          | Type              | Label | Description       |
+================+===================+=======+===================+
| file_id        | `sfixed           |       | Which file slot   |
|                | 32 <#sfixed32>`__ |       | the animation     |
|                |                   |       | describes.        |
+----------------+-------------------+-------+-------------------+
| first_frame    | `Animati          |       | The lower bound   |
|                | onFrame <#CARTA.A |       | of the animation  |
|                | nimationFrame>`__ |       | when looping.     |
+----------------+-------------------+-------+-------------------+
| start_frame    | `Animati          |       | The starting      |
|                | onFrame <#CARTA.A |       | point of the      |
|                | nimationFrame>`__ |       | animation.        |
+----------------+-------------------+-------+-------------------+
| last_frame     | `Animati          |       | The upper bound   |
|                | onFrame <#CARTA.A |       | of the animation. |
|                | nimationFrame>`__ |       |                   |
+----------------+-------------------+-------+-------------------+
| delta_frame    | `Animati          |       | The frame change  |
|                | onFrame <#CARTA.A |       | step for the      |
|                | nimationFrame>`__ |       | animation. For    |
|                |                   |       | example, a delta  |
|                |                   |       | frame of          |
|                |                   |       | {channel=1,       |
|                |                   |       | stokes=0} would   |
|                |                   |       | step through each |
|                |                   |       | channel in the    |
|                |                   |       | file.             |
+----------------+-------------------+-------+-------------------+
| frame_rate     | `sfixed           |       | Frame rate per    |
|                | 32 <#sfixed32>`__ |       | second            |
+----------------+-------------------+-------+-------------------+
| looping        | `bool <#bool>`__  |       | Whether to loop   |
|                |                   |       | the animation     |
|                |                   |       | indefinitely.     |
+----------------+-------------------+-------+-------------------+
| reverse        | `bool <#bool>`__  |       | Whether to        |
|                |                   |       | reverse the       |
|                |                   |       | animation         |
|                |                   |       | direction when    |
|                |                   |       | endFrame is       |
|                |                   |       | reached.          |
+----------------+-------------------+-------+-------------------+
| required_tiles | `AddRequired      |       | Required tiles    |
|                | Tiles <#CARTA.Add |       | when changing     |
|                | RequiredTiles>`__ |       | channels          |
+----------------+-------------------+-------+-------------------+

.. _CARTA.StartAnimationAck:

StartAnimationAck
~~~~~~~~~~~~~~~~~

START_ANIMATION_ACK

Response for START_ANIMATION

+--------------+---------------------+-------+---------------------+
| Field        | Type                | Label | Description         |
+==============+=====================+=======+=====================+
| success      | `bool <#bool>`__    |       | Defines whether     |
|              |                     |       | START_ANIMATION was |
|              |                     |       | successful          |
+--------------+---------------------+-------+---------------------+
| message      | `                   |       | Error message (if   |
|              | string <#string>`__ |       | applicable)         |
+--------------+---------------------+-------+---------------------+
| animation_id | `sfix               |       | The animation ID of |
|              | ed32 <#sfixed32>`__ |       | the new animation   |
+--------------+---------------------+-------+---------------------+

.. _CARTA.StopAnimation:

StopAnimation
~~~~~~~~~~~~~

STOP_ANIMATION

Stops the playing animation

+-----------+-----------------------+-------+-----------------------+
| Field     | Type                  | Label | Description           |
+===========+=======================+=======+=======================+
| file_id   | `sf                   |       | Which file slot the   |
|           | ixed32 <#sfixed32>`__ |       | animation describes.  |
+-----------+-----------------------+-------+-----------------------+
| end_frame | `AnimationFrame <#CAR |       | The ending point of   |
|           | TA.AnimationFrame>`__ |       | the animation.        |
+-----------+-----------------------+-------+-----------------------+

.. container:: file-heading

   .. rubric:: close_file.proto
      :name: close_file.proto

   `Top <#title>`__

.. _CARTA.CloseFile:

CloseFile
~~~~~~~~~

CLOSE_FILE:

Instructs the backend to close a file with a given file ID

======= ======================== ===== ==========================
Field   Type                     Label Description
======= ======================== ===== ==========================
file_id `sfixed32 <#sfixed32>`__       Which "file" slot to close
======= ======================== ===== ==========================

.. container:: file-heading

   .. rubric:: contour.proto
      :name: contour.proto

   `Top <#title>`__

.. _CARTA.SetContourParameters:

SetContourParameters
~~~~~~~~~~~~~~~~~~~~

SET_CONTOUR_PARAMETERS

Sets the contour parameters for a file

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| file_id          | `fixed           |          | The file ID that |
|                  | 32 <#fixed32>`__ |          | the contour      |
|                  |                  |          | corresponds to   |
+------------------+------------------+----------+------------------+
| r                | `fixed           |          | The file ID of   |
| eference_file_id | 32 <#fixed32>`__ |          | the reference    |
|                  |                  |          | image that the   |
|                  |                  |          | contour vertices |
|                  |                  |          | should be mapped |
|                  |                  |          | to               |
+------------------+------------------+----------+------------------+
| image_bounds     | `Ima             |          | The XY bounds    |
|                  | geBounds <#CARTA |          | corresponding to |
|                  | .ImageBounds>`__ |          | the image data   |
|                  |                  |          | in pixel         |
|                  |                  |          | coordinates      |
+------------------+------------------+----------+------------------+
| levels           | `dou             | repeated | Contour levels   |
|                  | ble <#double>`__ |          |                  |
+------------------+------------------+----------+------------------+
| smoothing_mode   | `Smoothi         |          | Pre-contouring   |
|                  | ngMode <#CARTA.S |          | smoothing mode   |
|                  | moothingMode>`__ |          |                  |
+------------------+------------------+----------+------------------+
| smoothing_factor | `i               |          | Contour          |
|                  | nt32 <#int32>`__ |          | smoothness       |
|                  |                  |          | factor. For      |
|                  |                  |          | block averaging, |
|                  |                  |          | this is the      |
|                  |                  |          | block width For  |
|                  |                  |          | Gaussian         |
|                  |                  |          | smoothing, this  |
|                  |                  |          | defines both the |
|                  |                  |          | Gaussian width,  |
|                  |                  |          | and the kernel   |
|                  |                  |          | size             |
+------------------+------------------+----------+------------------+
| d                | `i               |          | Decimation       |
| ecimation_factor | nt32 <#int32>`__ |          | factor,          |
|                  |                  |          | indicates to     |
|                  |                  |          | what 1/Nth of a  |
|                  |                  |          | pixel the        |
|                  |                  |          | contour vertices |
|                  |                  |          | should be        |
|                  |                  |          | rounded to       |
+------------------+------------------+----------+------------------+
| c                | `i               |          | Zstd compression |
| ompression_level | nt32 <#int32>`__ |          | level            |
+------------------+------------------+----------+------------------+
| co               | `i               |          | Size of contour  |
| ntour_chunk_size | nt32 <#int32>`__ |          | chunks, in       |
|                  |                  |          | number of        |
|                  |                  |          | vertices. If     |
|                  |                  |          | this is set to   |
|                  |                  |          | zero, partial    |
|                  |                  |          | contour results  |
|                  |                  |          | are not used     |
+------------------+------------------+----------+------------------+

.. container:: file-heading

   .. rubric:: export_region.proto
      :name: export_region.proto

   `Top <#title>`__

.. _CARTA.ExportRegion:

ExportRegion
~~~~~~~~~~~~

EXPORT_REGION:

Requests exporting the specified regions to a file on the server.

If directory and file are blank, return file contents for export on
client.

Backend responds with EXPORT_REGION_ACK

+---------------+-------------------+----------+-------------------+
| Field         | Type              | Label    | Description       |
+===============+===================+==========+===================+
| type          | `FileType <#C     |          | Required file     |
|               | ARTA.FileType>`__ |          | type              |
+---------------+-------------------+----------+-------------------+
| coord_type    | `Coordin          |          | Required          |
|               | ateType <#CARTA.C |          | coordinate type   |
|               | oordinateType>`__ |          | pixel/world       |
+---------------+-------------------+----------+-------------------+
| file_id       | `sfixed           |          | File id for the   |
|               | 32 <#sfixed32>`__ |          | coordinate system |
|               |                   |          | to use            |
+---------------+-------------------+----------+-------------------+
| region_styles | `Expor            | repeated | Region ids and    |
|               | tRegion.RegionSty |          | style params to   |
|               | lesEntry <#CARTA. |          | export            |
|               | ExportRegion.Regi |          |                   |
|               | onStylesEntry>`__ |          |                   |
+---------------+-------------------+----------+-------------------+
| directory     | `st               |          | Optional          |
|               | ring <#string>`__ |          | directory name of |
|               |                   |          | server file       |
+---------------+-------------------+----------+-------------------+
| file          | `st               |          | Optional file     |
|               | ring <#string>`__ |          | name of server    |
|               |                   |          | file              |
+---------------+-------------------+----------+-------------------+

.. _CARTA.ExportRegion.RegionStylesEntry:

ExportRegion.RegionStylesEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ==================================== ===== ===========
Field Type                                 Label Description
===== ==================================== ===== ===========
key   `sfixed32 <#sfixed32>`__                   
value `RegionStyle <#CARTA.RegionStyle>`__       
===== ==================================== ===== ===========

.. _CARTA.ExportRegionAck:

ExportRegionAck
~~~~~~~~~~~~~~~

EXPORT_REGION_ACK

Response for EXPORT_REGION to indicate success and file contents if on
client.

+----------+----------------------+----------+----------------------+
| Field    | Type                 | Label    | Description          |
+==========+======================+==========+======================+
| success  | `bool <#bool>`__     |          | Defines whether      |
|          |                      |          | EXPORT_REGION was    |
|          |                      |          | successful           |
+----------+----------------------+----------+----------------------+
| message  | `string <#string>`__ |          | Error message (if    |
|          |                      |          | applicable)          |
+----------+----------------------+----------+----------------------+
| contents | `string <#string>`__ | repeated | File contents for    |
|          |                      |          | client export (one   |
|          |                      |          | line per string)     |
+----------+----------------------+----------+----------------------+

.. container:: file-heading

   .. rubric:: import_region.proto
      :name: import_region.proto

   `Top <#title>`__

.. _CARTA.ImportRegion:

ImportRegion
~~~~~~~~~~~~

IMPORT_REGION:

Requests the opening and applying of a specific region file.

Backend responds with IMPORT_REGION_ACK

+-----------+---------------------+----------+---------------------+
| Field     | Type                | Label    | Description         |
+===========+=====================+==========+=====================+
| group_id  | `sfix               |          | Required WCS group  |
|           | ed32 <#sfixed32>`__ |          | id (may be a single |
|           |                     |          | file id)            |
+-----------+---------------------+----------+---------------------+
| type      | `FileType <         |          | Required file type  |
|           | #CARTA.FileType>`__ |          |                     |
+-----------+---------------------+----------+---------------------+
| directory | `                   |          | Optional directory  |
|           | string <#string>`__ |          | name of server file |
+-----------+---------------------+----------+---------------------+
| file      | `                   |          | Optional file name  |
|           | string <#string>`__ |          | of server file      |
+-----------+---------------------+----------+---------------------+
| contents  | `                   | repeated | Optional file       |
|           | string <#string>`__ |          | contents of client  |
|           |                     |          | file (1 line per    |
|           |                     |          | string)             |
+-----------+---------------------+----------+---------------------+

.. _CARTA.ImportRegionAck:

ImportRegionAck
~~~~~~~~~~~~~~~

IMPORT_REGION_ACK

Response for IMPORT_REGION. Also supplies region properties

+---------------+-------------------+----------+-------------------+
| Field         | Type              | Label    | Description       |
+===============+===================+==========+===================+
| success       | `bool <#bool>`__  |          | Defines whether   |
|               |                   |          | IMPORT_REGION was |
|               |                   |          | successful        |
+---------------+-------------------+----------+-------------------+
| message       | `st               |          | Error message (if |
|               | ring <#string>`__ |          | applicable)       |
+---------------+-------------------+----------+-------------------+
| regions       | `I                | repeated | Map region id to  |
|               | mportRegionAck.Re |          | parameters        |
|               | gionsEntry <#CART |          |                   |
|               | A.ImportRegionAck |          |                   |
|               | .RegionsEntry>`__ |          |                   |
+---------------+-------------------+----------+-------------------+
| region_styles | `ImportRegio      | repeated | Map region id to  |
|               | nAck.RegionStyles |          | style parameters  |
|               | Entry <#CARTA.Imp |          |                   |
|               | ortRegionAck.Regi |          |                   |
|               | onStylesEntry>`__ |          |                   |
+---------------+-------------------+----------+-------------------+

.. _CARTA.ImportRegionAck.RegionStylesEntry:

ImportRegionAck.RegionStylesEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ==================================== ===== ===========
Field Type                                 Label Description
===== ==================================== ===== ===========
key   `sfixed32 <#sfixed32>`__                   
value `RegionStyle <#CARTA.RegionStyle>`__       
===== ==================================== ===== ===========

.. _CARTA.ImportRegionAck.RegionsEntry:

ImportRegionAck.RegionsEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ================================== ===== ===========
Field Type                               Label Description
===== ================================== ===== ===========
key   `sfixed32 <#sfixed32>`__                 
value `RegionInfo <#CARTA.RegionInfo>`__       
===== ================================== ===== ===========

.. container:: file-heading

   .. rubric:: open_catalog_file.proto
      :name: open_catalog_file.proto

   `Top <#title>`__

.. _CARTA.CloseCatalogFile:

CloseCatalogFile
~~~~~~~~~~~~~~~~

======= ======================== ===== ===========
Field   Type                     Label Description
======= ======================== ===== ===========
file_id `sfixed32 <#sfixed32>`__       
======= ======================== ===== ===========

.. _CARTA.OpenCatalogFile:

OpenCatalogFile
~~~~~~~~~~~~~~~

================= ======================== ===== ===========
Field             Type                     Label Description
================= ======================== ===== ===========
directory         `string <#string>`__           
name              `string <#string>`__           
file_id           `sfixed32 <#sfixed32>`__       
preview_data_size `sfixed32 <#sfixed32>`__       
================= ======================== ===== ===========

.. _CARTA.OpenCatalogFileAck:

OpenCatalogFileAck
~~~~~~~~~~~~~~~~~~

+--------------+---------------------------+----------+-------------+
| Field        | Type                      | Label    | Description |
+==============+===========================+==========+=============+
| success      | `bool <#bool>`__          |          |             |
+--------------+---------------------------+----------+-------------+
| message      | `string <#string>`__      |          |             |
+--------------+---------------------------+----------+-------------+
| file_id      | `sfixed32 <#sfixed32>`__  |          |             |
+--------------+---------------------------+----------+-------------+
| file_info    | `CatalogFileInfo <#       |          |             |
|              | CARTA.CatalogFileInfo>`__ |          |             |
+--------------+---------------------------+----------+-------------+
| data_size    | `sfixed32 <#sfixed32>`__  |          |             |
+--------------+---------------------------+----------+-------------+
| headers      | `CatalogHeader            | repeated |             |
|              | <#CARTA.CatalogHeader>`__ |          |             |
+--------------+---------------------------+----------+-------------+
| preview_data | `OpenCata                 | repeated |             |
|              | logFileAck.PreviewDataEnt |          |             |
|              | ry <#CARTA.OpenCatalogFil |          |             |
|              | eAck.PreviewDataEntry>`__ |          |             |
+--------------+---------------------------+----------+-------------+

.. _CARTA.OpenCatalogFileAck.PreviewDataEntry:

OpenCatalogFileAck.PreviewDataEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ================================== ===== ===========
Field Type                               Label Description
===== ================================== ===== ===========
key   `fixed32 <#fixed32>`__                   
value `ColumnData <#CARTA.ColumnData>`__       
===== ================================== ===== ===========

.. container:: file-heading

   .. rubric:: open_file.proto
      :name: open_file.proto

   `Top <#title>`__

.. _CARTA.OpenFile:

OpenFile
~~~~~~~~

OPEN_FILE:

Requests the opening of a specific file.

Backend responds with OPEN_FILE_ACK

+-------------+----------------------+-------+----------------------+
| Field       | Type                 | Label | Description          |
+=============+======================+=======+======================+
| directory   | `string <#string>`__ |       | Required directory   |
|             |                      |       | name                 |
+-------------+----------------------+-------+----------------------+
| file        | `string <#string>`__ |       | Required file name   |
+-------------+----------------------+-------+----------------------+
| hdu         | `string <#string>`__ |       | Which HDU to load    |
|             |                      |       | (if applicable). If  |
|             |                      |       | left blank, the      |
|             |                      |       | first HDU will be    |
|             |                      |       | used                 |
+-------------+----------------------+-------+----------------------+
| file_id     | `sfi                 |       | Which "file" slot to |
|             | xed32 <#sfixed32>`__ |       | load the file into   |
|             |                      |       | (when viewing        |
|             |                      |       | multiple files)      |
+-------------+----------------------+-------+----------------------+
| render_mode | `RenderMode <#       |       | The render mode to   |
|             | CARTA.RenderMode>`__ |       | use. Additional      |
|             |                      |       | modes will be added  |
|             |                      |       | in subsequent        |
|             |                      |       | versions.            |
+-------------+----------------------+-------+----------------------+

.. _CARTA.OpenFileAck:

OpenFileAck
~~~~~~~~~~~

OPEN_FILE_ACK

Response for OPEN_FILE. Also supplies file information

+-------------------+-------------------+-------+-------------------+
| Field             | Type              | Label | Description       |
+===================+===================+=======+===================+
| success           | `bool <#bool>`__  |       | Defines whether   |
|                   |                   |       | OPEN_FILE was     |
|                   |                   |       | successful        |
+-------------------+-------------------+-------+-------------------+
| file_id           | `sfixed           |       | Which file slot   |
|                   | 32 <#sfixed32>`__ |       | the file was      |
|                   |                   |       | loaded into (when |
|                   |                   |       | viewing multiple  |
|                   |                   |       | files)            |
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
| f                 | `fixe             |       | Optional bitflags |
| ile_feature_flags | d32 <#fixed32>`__ |       | specifying        |
|                   |                   |       | feature flags of  |
|                   |                   |       | the file being    |
|                   |                   |       | opened.           |
+-------------------+-------------------+-------+-------------------+

.. container:: file-heading

   .. rubric:: region.proto
      :name: region.proto

   `Top <#title>`__

.. _CARTA.RemoveRegion:

RemoveRegion
~~~~~~~~~~~~

REMOVE_REGION:

Removes a region

+-----------+-----------------------+-------+-----------------------+
| Field     | Type                  | Label | Description           |
+===========+=======================+=======+=======================+
| region_id | `sf                   |       | Unique region ID of   |
|           | ixed32 <#sfixed32>`__ |       | the region to be      |
|           |                       |       | removed               |
+-----------+-----------------------+-------+-----------------------+

.. _CARTA.SetRegion:

SetRegion
~~~~~~~~~

SET_REGION:

Creates or updates a region. Backend responds with SET_REGION_ACK

+-------------+----------------------+-------+----------------------+
| Field       | Type                 | Label | Description          |
+=============+======================+=======+======================+
| file_id     | `sfi                 |       | File slot of the     |
|             | xed32 <#sfixed32>`__ |       | reference image      |
+-------------+----------------------+-------+----------------------+
| region_id   | `sfi                 |       | Unique region ID.    |
|             | xed32 <#sfixed32>`__ |       | <=0 if a new region  |
|             |                      |       | is being created.    |
+-------------+----------------------+-------+----------------------+
| region_info | `RegionInfo <#       |       | Region parameters    |
|             | CARTA.RegionInfo>`__ |       |                      |
+-------------+----------------------+-------+----------------------+

.. _CARTA.SetRegionAck:

SetRegionAck
~~~~~~~~~~~~

SET_REGION_ACK:

Response for SET_REGION

+-----------+-----------------------+-------+-----------------------+
| Field     | Type                  | Label | Description           |
+===========+=======================+=======+=======================+
| success   | `bool <#bool>`__      |       | Defines whether       |
|           |                       |       | SET_REGION was        |
|           |                       |       | successful            |
+-----------+-----------------------+-------+-----------------------+
| message   | `string <#string>`__  |       | Error message (if     |
|           |                       |       | applicable)           |
+-----------+-----------------------+-------+-----------------------+
| region_id | `sf                   |       | The unique region ID. |
|           | ixed32 <#sfixed32>`__ |       | If the region is      |
|           |                       |       | updated, this will be |
|           |                       |       | the same as the       |
|           |                       |       | region ID specified   |
|           |                       |       | in SET_REGION. If a   |
|           |                       |       | new region is being   |
|           |                       |       | created, the ID of    |
|           |                       |       | the new region will   |
|           |                       |       | be passed back.       |
+-----------+-----------------------+-------+-----------------------+

.. container:: file-heading

   .. rubric:: region_requirements.proto
      :name: region_requirements.proto

   `Top <#title>`__

.. _CARTA.SetHistogramRequirements:

SetHistogramRequirements
~~~~~~~~~~~~~~~~~~~~~~~~

SET_HISTOGRAM_REQUIREMENTS:

Sets which histogram data needs to be streamed to the frontend when the
region is updated

+------------+---------------------+----------+---------------------+
| Field      | Type                | Label    | Description         |
+============+=====================+==========+=====================+
| file_id    | `sfix               |          | Which file slot the |
|            | ed32 <#sfixed32>`__ |          | requirements        |
|            |                     |          | describe            |
+------------+---------------------+----------+---------------------+
| region_id  | `sfix               |          | ID of the region    |
|            | ed32 <#sfixed32>`__ |          | that is having      |
|            |                     |          | requirements        |
|            |                     |          | defined. If a       |
|            |                     |          | region ID of -1 is  |
|            |                     |          | given, this         |
|            |                     |          | corresponds to the  |
|            |                     |          | entire 2D image.    |
+------------+---------------------+----------+---------------------+
| histograms | `SetHistogramRequi  | repeated | List of required    |
|            | rements.HistogramCo |          | histograms, along   |
|            | nfig <#CARTA.SetHis |          | with the number of  |
|            | togramRequirements. |          | bins. If the        |
|            | HistogramConfig>`__ |          | channel is -1, the  |
|            |                     |          | current channel is  |
|            |                     |          | used. If the        |
|            |                     |          | channel is -2, the  |
|            |                     |          | histogram is        |
|            |                     |          | constructed over    |
|            |                     |          | all channels. If    |
|            |                     |          | the number of bins  |
|            |                     |          | is less than zero,  |
|            |                     |          | an automatic bin    |
|            |                     |          | size is used, based |
|            |                     |          | on the number of    |
|            |                     |          | values.             |
+------------+---------------------+----------+---------------------+

.. _CARTA.SetHistogramRequirements.HistogramConfig:

SetHistogramRequirements.HistogramConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========
Field    Type                     Label Description
======== ======================== ===== ===========
channel  `sfixed32 <#sfixed32>`__       
num_bins `sfixed32 <#sfixed32>`__       
======== ======================== ===== ===========

.. _CARTA.SetRegionRequirements:

SetRegionRequirements
~~~~~~~~~~~~~~~~~~~~~

SET_REGION_REQUIREMENTS:

Sets which spatial profile data needs to be streamed to the frontend
when the region is updated

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| file_id          | `fixed           |          |                  |
|                  | 32 <#fixed32>`__ |          |                  |
+------------------+------------------+----------+------------------+
| region_id        | `fixed           |          | ID of the region |
|                  | 32 <#fixed32>`__ |          | that is having   |
|                  |                  |          | requirements     |
|                  |                  |          | defined. If a    |
|                  |                  |          | region ID of 0   |
|                  |                  |          | is given, this   |
|                  |                  |          | corresponds to   |
|                  |                  |          | the point region |
|                  |                  |          | defined by the   |
|                  |                  |          | cursor position. |
+------------------+------------------+----------+------------------+
| x                | `bool <#bool>`__ |          | Is the X-profile |
|                  |                  |          | (of the current  |
|                  |                  |          | Stokes           |
|                  |                  |          | parameter)       |
|                  |                  |          | required?        |
+------------------+------------------+----------+------------------+
| y                | `bool <#bool>`__ |          | Is the Y-profile |
|                  |                  |          | (of the current  |
|                  |                  |          | Stokes           |
|                  |                  |          | parameter)       |
|                  |                  |          | required?        |
+------------------+------------------+----------+------------------+
| z                | `bool <#bool>`__ |          | Is the Z-profile |
|                  |                  |          | (of the current  |
|                  |                  |          | Stokes           |
|                  |                  |          | parameter)       |
|                  |                  |          | required?        |
+------------------+------------------+----------+------------------+
| add              | `str             | repeated | List of          |
| itional_profiles | ing <#string>`__ |          | additional       |
|                  |                  |          | profiles needed  |
|                  |                  |          | (for example,    |
|                  |                  |          | [“Qz”, “Uz”])    |
|                  |                  |          | will include the |
|                  |                  |          | Z-profile of the |
|                  |                  |          | Q and U Stokes   |
|                  |                  |          | cube, regardless |
|                  |                  |          | of which Stokes  |
|                  |                  |          | parameter is     |
|                  |                  |          | currently in     |
|                  |                  |          | use.             |
+------------------+------------------+----------+------------------+

.. _CARTA.SetSpatialRequirements:

SetSpatialRequirements
~~~~~~~~~~~~~~~~~~~~~~

SET_SPATIAL_REQUIREMENTS:

Sets which information needs to be streamed to the frontend when the
region is updated

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| file_id          | `sfixed3         |          | Which file slot  |
|                  | 2 <#sfixed32>`__ |          | the requirements |
|                  |                  |          | describe         |
+------------------+------------------+----------+------------------+
| region_id        | `sfixed3         |          | ID of the region |
|                  | 2 <#sfixed32>`__ |          | that is having   |
|                  |                  |          | requirements     |
|                  |                  |          | defined. If a    |
|                  |                  |          | region ID of 0   |
|                  |                  |          | is given, this   |
|                  |                  |          | corresponds to   |
|                  |                  |          | the point region |
|                  |                  |          | defined by the   |
|                  |                  |          | cursor position. |
+------------------+------------------+----------+------------------+
| spatial_profiles | `str             | repeated | List of spatial  |
|                  | ing <#string>`__ |          | profiles needed. |
|                  |                  |          | If no Stokes     |
|                  |                  |          | parameter is     |
|                  |                  |          | specified (i.e.  |
|                  |                  |          | just “x” or      |
|                  |                  |          | “y”), the active |
|                  |                  |          | Stokes parameter |
|                  |                  |          | is used.         |
+------------------+------------------+----------+------------------+

.. _CARTA.SetSpectralRequirements:

SetSpectralRequirements
~~~~~~~~~~~~~~~~~~~~~~~

SET_SPECTRAL_REQUIREMENTS:

Sets which spectral profile data needs to be streamed to the frontend
when the region is updated

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| file_id          | `sfixed3         |          | Which file slot  |
|                  | 2 <#sfixed32>`__ |          | the requirements |
|                  |                  |          | describe         |
+------------------+------------------+----------+------------------+
| region_id        | `sfixed3         |          | ID of the region |
|                  | 2 <#sfixed32>`__ |          | that is having   |
|                  |                  |          | requirements     |
|                  |                  |          | defined. If a    |
|                  |                  |          | region ID of 0   |
|                  |                  |          | is given, this   |
|                  |                  |          | corresponds to   |
|                  |                  |          | the point region |
|                  |                  |          | defined by the   |
|                  |                  |          | cursor position. |
+------------------+------------------+----------+------------------+
| s                | `SetSpectr       | repeated | List of spectral |
| pectral_profiles | alRequirements.S |          | profiles needed, |
|                  | pectralConfig <# |          | along with which |
|                  | CARTA.SetSpectra |          | stats types are  |
|                  | lRequirements.Sp |          | needed for each  |
|                  | ectralConfig>`__ |          | profile. If no   |
|                  |                  |          | Stokes parameter |
|                  |                  |          | is specified     |
|                  |                  |          | (i.e. just “z”)  |
|                  |                  |          | or if the        |
|                  |                  |          | coordinate is    |
|                  |                  |          | empty, the       |
|                  |                  |          | active Stokes    |
|                  |                  |          | parameter is     |
|                  |                  |          | used. If the     |
|                  |                  |          | region is a      |
|                  |                  |          | point region,    |
|                  |                  |          | the statsTypes   |
|                  |                  |          | field is         |
|                  |                  |          | ignored.         |
+------------------+------------------+----------+------------------+

.. _CARTA.SetSpectralRequirements.SpectralConfig:

SetSpectralRequirements.SpectralConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ================================ ======== ===========
Field       Type                             Label    Description
=========== ================================ ======== ===========
coordinate  `string <#string>`__                      
stats_types `StatsType <#CARTA.StatsType>`__ repeated 
=========== ================================ ======== ===========

.. _CARTA.SetStatsRequirements:

SetStatsRequirements
~~~~~~~~~~~~~~~~~~~~

SET_STATS_REQUIREMENTS:

Sets which stats data needs to be streamed to the frontend when the
region is updated

+-----------+---------------------+----------+---------------------+
| Field     | Type                | Label    | Description         |
+===========+=====================+==========+=====================+
| file_id   | `sfix               |          | Which file slot the |
|           | ed32 <#sfixed32>`__ |          | requirements        |
|           |                     |          | describe            |
+-----------+---------------------+----------+---------------------+
| region_id | `sfix               |          | ID of the region    |
|           | ed32 <#sfixed32>`__ |          | that is having      |
|           |                     |          | requirements        |
|           |                     |          | defined. If a       |
|           |                     |          | region ID of -1 is  |
|           |                     |          | given, this         |
|           |                     |          | corresponds to the  |
|           |                     |          | entire 2D image.    |
+-----------+---------------------+----------+---------------------+
| stats     | `StatsType <#       | repeated | List of required    |
|           | CARTA.StatsType>`__ |          | stats               |
+-----------+---------------------+----------+---------------------+

.. container:: file-heading

   .. rubric:: register_viewer.proto
      :name: register_viewer.proto

   `Top <#title>`__

.. _CARTA.RegisterViewer:

RegisterViewer
~~~~~~~~~~~~~~

REGISTER_VIEWER:

Registers the viewer with the backend.

Responds with REGISTER_VIEWER_ACK

+-------------------+-------------------+-------+-------------------+
| Field             | Type              | Label | Description       |
+===================+===================+=======+===================+
| session_id        | `fixe             |       | Unique session ID |
|                   | d32 <#fixed32>`__ |       | parameter (can be |
|                   |                   |       | generated using   |
|                   |                   |       | UUID libraries).  |
|                   |                   |       | Passing in an     |
|                   |                   |       | existing session  |
|                   |                   |       | ID can be used    |
|                   |                   |       | for resuming      |
|                   |                   |       | sessions          |
+-------------------+-------------------+-------+-------------------+
| api_key           | `st               |       | Optional          |
|                   | ring <#string>`__ |       | user-specific API |
|                   |                   |       | key to be used    |
|                   |                   |       | for basic         |
|                   |                   |       | authentication.   |
|                   |                   |       | Could be an       |
|                   |                   |       | encrypted JWT for |
|                   |                   |       | secure            |
|                   |                   |       | authentication.   |
+-------------------+-------------------+-------+-------------------+
| cli               | `fixe             |       | Optional feature  |
| ent_feature_flags | d32 <#fixed32>`__ |       | bitflag           |
|                   |                   |       | specifying        |
|                   |                   |       | client-side       |
|                   |                   |       | feature set       |
+-------------------+-------------------+-------+-------------------+

.. _CARTA.RegisterViewerAck:

RegisterViewerAck
~~~~~~~~~~~~~~~~~

REGISTER_VIEWER_ACK

Acknowledgement response for REGISTER_VIEWER.

Informs the frontend whether the session was correctly.

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| session_id       | `fixed           |          | Unique session   |
|                  | 32 <#fixed32>`__ |          | ID               |
+------------------+------------------+----------+------------------+
| success          | `bool <#bool>`__ |          | Defines whether  |
|                  |                  |          | the              |
|                  |                  |          | REGISTER_VIEWER  |
|                  |                  |          | command was      |
|                  |                  |          | successful       |
+------------------+------------------+----------+------------------+
| message          | `str             |          | Error message    |
|                  | ing <#string>`__ |          | (if applicable)  |
+------------------+------------------+----------+------------------+
| session_type     | `Ses             |          | Defines the type |
|                  | sionType <#CARTA |          | of session       |
|                  | .SessionType>`__ |          | established      |
+------------------+------------------+----------+------------------+
| serv             | `fixed           |          | Optional feature |
| er_feature_flags | 32 <#fixed32>`__ |          | bitflag          |
|                  |                  |          | specifying       |
|                  |                  |          | server-side      |
|                  |                  |          | feature set      |
+------------------+------------------+----------+------------------+
| user_preferences | `RegisterV       | repeated | Map of user      |
|                  | iewerAck.UserPre |          | preferences      |
|                  | ferencesEntry <# |          | retrieved from   |
|                  | CARTA.RegisterVi |          | the server       |
|                  | ewerAck.UserPref |          | database. If     |
|                  | erencesEntry>`__ |          | this is empty    |
|                  |                  |          | and the server   |
|                  |                  |          | does not have    |
|                  |                  |          | the              |
|                  |                  |          | USER_PREFERENCES |
|                  |                  |          | feature flag     |
|                  |                  |          | set, then the    |
|                  |                  |          | user preferences |
|                  |                  |          | are read from    |
|                  |                  |          | localStorage     |
|                  |                  |          | instead.         |
+------------------+------------------+----------+------------------+
| user_layouts     | `R               | repeated | Map of user      |
|                  | egisterViewerAck |          | layouts          |
|                  | .UserLayoutsEntr |          | retrieved from   |
|                  | y <#CARTA.Regist |          | the server       |
|                  | erViewerAck.User |          | database         |
|                  | LayoutsEntry>`__ |          |                  |
+------------------+------------------+----------+------------------+

.. _CARTA.RegisterViewerAck.UserLayoutsEntry:

RegisterViewerAck.UserLayoutsEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ==================== ===== ===========
Field Type                 Label Description
===== ==================== ===== ===========
key   `string <#string>`__       
value `string <#string>`__       
===== ==================== ===== ===========

.. _CARTA.RegisterViewerAck.UserPreferencesEntry:

RegisterViewerAck.UserPreferencesEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ==================== ===== ===========
Field Type                 Label Description
===== ==================== ===== ===========
key   `string <#string>`__       
value `string <#string>`__       
===== ==================== ===== ===========

.. container:: file-heading

   .. rubric:: resume_session.proto
      :name: resume_session.proto

   `Top <#title>`__

.. _CARTA.ImageProperties:

ImageProperties
~~~~~~~~~~~~~~~

+------------------+--------------------+----------+-------------+
| Field            | Type               | Label    | Description |
+==================+====================+==========+=============+
| directory        | `s                 |          |             |
|                  | tring <#string>`__ |          |             |
+------------------+--------------------+----------+-------------+
| file             | `s                 |          |             |
|                  | tring <#string>`__ |          |             |
+------------------+--------------------+----------+-------------+
| hdu              | `s                 |          |             |
|                  | tring <#string>`__ |          |             |
+------------------+--------------------+----------+-------------+
| file_id          | `sfixe             |          |             |
|                  | d32 <#sfixed32>`__ |          |             |
+------------------+--------------------+----------+-------------+
| render_mode      | `RenderMode <#CA   |          |             |
|                  | RTA.RenderMode>`__ |          |             |
+------------------+--------------------+----------+-------------+
| channel          | `sfixe             |          |             |
|                  | d32 <#sfixed32>`__ |          |             |
+------------------+--------------------+----------+-------------+
| stokes           | `sfixe             |          |             |
|                  | d32 <#sfixed32>`__ |          |             |
+------------------+--------------------+----------+-------------+
| regions          | `ImageProperties   | repeated |             |
|                  | .RegionsEntry <#CA |          |             |
|                  | RTA.ImagePropertie |          |             |
|                  | s.RegionsEntry>`__ |          |             |
+------------------+--------------------+----------+-------------+
| contour_settings | `SetContourParamet |          |             |
|                  | ers <#CARTA.SetCon |          |             |
|                  | tourParameters>`__ |          |             |
+------------------+--------------------+----------+-------------+

.. _CARTA.ImageProperties.RegionsEntry:

ImageProperties.RegionsEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ================================== ===== ===========
Field Type                               Label Description
===== ================================== ===== ===========
key   `sfixed32 <#sfixed32>`__                 
value `RegionInfo <#CARTA.RegionInfo>`__       
===== ================================== ===== ===========

.. _CARTA.ResumeSession:

ResumeSession
~~~~~~~~~~~~~

+---------------+--------------------------+----------+-------------+
| Field         | Type                     | Label    | Description |
+===============+==========================+==========+=============+
| images        | `ImageProperties <#C     | repeated |             |
|               | ARTA.ImageProperties>`__ |          |             |
+---------------+--------------------------+----------+-------------+
| catalog_files | `OpenCatalogFile <#C     | repeated |             |
|               | ARTA.OpenCatalogFile>`__ |          |             |
+---------------+--------------------------+----------+-------------+

.. _CARTA.ResumeSessionAck:

ResumeSessionAck
~~~~~~~~~~~~~~~~

======= ==================== ===== ===========
Field   Type                 Label Description
======= ==================== ===== ===========
success `bool <#bool>`__           
message `string <#string>`__       
======= ==================== ===== ===========

.. container:: file-heading

   .. rubric:: set_cursor.proto
      :name: set_cursor.proto

   `Top <#title>`__

.. _CARTA.SetCursor:

SetCursor
~~~~~~~~~

SET_CURSOR:

Sets the current cursor position in image space coordinates.

The cursor defines a special case of a region, with a single control
point.

+-------------------+-------------------+-------+-------------------+
| Field             | Type              | Label | Description       |
+===================+===================+=======+===================+
| file_id           | `sfixed           |       | Which file slot   |
|                   | 32 <#sfixed32>`__ |       | the cursor is     |
|                   |                   |       | moving over       |
+-------------------+-------------------+-------+-------------------+
| point             | `Point            |       | XY-coordinates of |
|                   | <#CARTA.Point>`__ |       | cursor in image   |
|                   |                   |       | space             |
+-------------------+-------------------+-------+-------------------+
| spa               | `SetSpa           |       | Optional          |
| tial_requirements | tialRequirements  |       | accompanying      |
|                   | <#CARTA.SetSpatia |       | spatial           |
|                   | lRequirements>`__ |       | requirements      |
|                   |                   |       | message to be     |
|                   |                   |       | processed prior   |
|                   |                   |       | to cursor update  |
+-------------------+-------------------+-------+-------------------+

.. container:: file-heading

   .. rubric:: set_image_channels.proto
      :name: set_image_channels.proto

   `Top <#title>`__

.. _CARTA.SetImageChannels:

SetImageChannels
~~~~~~~~~~~~~~~~

SET_IMAGE_CHANNELS

Sets the current image channel and Stokes parameter

+----------------+-------------------+-------+-------------------+
| Field          | Type              | Label | Description       |
+================+===================+=======+===================+
| file_id        | `sfixed           |       | The file ID that  |
|                | 32 <#sfixed32>`__ |       | the view          |
|                |                   |       | corresponds to    |
+----------------+-------------------+-------+-------------------+
| channel        | `sfixed           |       | The image channel |
|                | 32 <#sfixed32>`__ |       | (Z-coordinate)    |
+----------------+-------------------+-------+-------------------+
| stokes         | `sfixed           |       | The image stokes  |
|                | 32 <#sfixed32>`__ |       | parameter         |
+----------------+-------------------+-------+-------------------+
| required_tiles | `AddRequired      |       | Required tiles    |
|                | Tiles <#CARTA.Add |       | when changing     |
|                | RequiredTiles>`__ |       | channels          |
+----------------+-------------------+-------+-------------------+

.. container:: file-heading

   .. rubric:: spectral_line_request.proto
      :name: spectral_line_request.proto

   `Top <#title>`__

.. _CARTA.SpectralLineRequest:

SpectralLineRequest
~~~~~~~~~~~~~~~~~~~

=============== ====================================== ===== ===========
Field           Type                                   Label Description
=============== ====================================== ===== ===========
frequency_range `DoubleBounds <#CARTA.DoubleBounds>`__       
=============== ====================================== ===== ===========

.. _CARTA.SpectralLineResponse:

SpectralLineResponse
~~~~~~~~~~~~~~~~~~~~

+--------------------+--------------------+----------+-------------+
| Field              | Type               | Label    | Description |
+====================+====================+==========+=============+
| success            | `bool <#bool>`__   |          |             |
+--------------------+--------------------+----------+-------------+
| message            | `s                 |          |             |
|                    | tring <#string>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| data_size          | `sfixe             |          |             |
|                    | d32 <#sfixed32>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| headers            | `Cat               | repeated |             |
|                    | alogHeader <#CARTA |          |             |
|                    | .CatalogHeader>`__ |          |             |
+--------------------+--------------------+----------+-------------+
| spectral_line_data | `Spectra           | repeated |             |
|                    | lLineResponse.Spec |          |             |
|                    | tralLineDataEntry  |          |             |
|                    | <#CARTA.SpectralLi |          |             |
|                    | neResponse.Spectra |          |             |
|                    | lLineDataEntry>`__ |          |             |
+--------------------+--------------------+----------+-------------+

.. _CARTA.SpectralLineResponse.SpectralLineDataEntry:

SpectralLineResponse.SpectralLineDataEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ================================== ===== ===========
Field Type                               Label Description
===== ================================== ===== ===========
key   `fixed32 <#fixed32>`__                   
value `ColumnData <#CARTA.ColumnData>`__       
===== ================================== ===== ===========

.. container:: file-heading

   .. rubric:: tiles.proto
      :name: tiles.proto

   `Top <#title>`__

.. _CARTA.AddRequiredTiles:

AddRequiredTiles
~~~~~~~~~~~~~~~~

ADD_REQUIRED_TILES

Provides a list of tiles that are required for the specified file

+------------------+------------------+----------+------------------+
| Field            | Type             | Label    | Description      |
+==================+==================+==========+==================+
| file_id          | `sfixed3         |          | The file ID that |
|                  | 2 <#sfixed32>`__ |          | the view         |
|                  |                  |          | corresponds to   |
+------------------+------------------+----------+------------------+
| tiles            | `sfixed3         | repeated | The list of      |
|                  | 2 <#sfixed32>`__ |          | tiles required,  |
|                  |                  |          | in encoded       |
|                  |                  |          | coordinate       |
+------------------+------------------+----------+------------------+
| compression_type | `Compression     |          | The compression  |
|                  | Type <#CARTA.Com |          | algorithm used   |
|                  | pressionType>`__ |          |                  |
+------------------+------------------+----------+------------------+
| com              | `f               |          | Compression      |
| pression_quality | loat <#float>`__ |          | quality switch   |
+------------------+------------------+----------+------------------+

.. _CARTA.RemoveRequiredTiles:

RemoveRequiredTiles
~~~~~~~~~~~~~~~~~~~

REMOVE_REQUIRED_TILES

Provides a list of tiles that are required for the specified file

+---------+----------------------+----------+----------------------+
| Field   | Type                 | Label    | Description          |
+=========+======================+==========+======================+
| file_id | `sfi                 |          | The file ID that the |
|         | xed32 <#sfixed32>`__ |          | view corresponds to  |
+---------+----------------------+----------+----------------------+
| tiles   | `sfi                 | repeated | The list of tiles    |
|         | xed32 <#sfixed32>`__ |          | required, in encoded |
|         |                      |          | coordinate           |
+---------+----------------------+----------+----------------------+

.. container:: file-heading

   .. rubric:: user_layout.proto
      :name: user_layout.proto

   `Top <#title>`__

.. _CARTA.SetUserLayout:

SetUserLayout
~~~~~~~~~~~~~

SET_USER_LAYOUT:

Sets or clears a user layout.

Backend responds with SET_USER_LAYOUT_ACK

+-------+----------------------+-------+-------------------------+
| Field | Type                 | Label | Description             |
+=======+======================+=======+=========================+
| name  | `string <#string>`__ |       | Name of the layout to   |
|       |                      |       | update. If no layout    |
|       |                      |       | with the given name is  |
|       |                      |       | present in the server   |
|       |                      |       | database, a new layout  |
|       |                      |       | is created              |
+-------+----------------------+-------+-------------------------+
| value | `string <#string>`__ |       | JSON string             |
|       |                      |       | representing the        |
|       |                      |       | layout. If the value is |
|       |                      |       | empty, the user layout  |
|       |                      |       | is cleared from the     |
|       |                      |       | server database.        |
+-------+----------------------+-------+-------------------------+

.. _CARTA.SetUserLayoutAck:

SetUserLayoutAck
~~~~~~~~~~~~~~~~

SET_USER_LAYOUT_ACK

Response for SET_USER_LAYOUT

+---------+------------------+-------+------------------------+
| Field   | Type             | Label | Description            |
+=========+==================+=======+========================+
| success | `bool <#bool>`__ |       | Defines whether        |
|         |                  |       | SET_USER_LAYOUT was    |
|         |                  |       | successful Error       |
|         |                  |       | message (if            |
|         |                  |       | applicable)            |
+---------+------------------+-------+------------------------+

.. container:: file-heading

   .. rubric:: user_preferences.proto
      :name: user_preferences.proto

   `Top <#title>`__

.. _CARTA.SetUserPreferences:

SetUserPreferences
~~~~~~~~~~~~~~~~~~

SET_USER_PREFERENCES:

Sets or clears one or more user preferences.

Backend responds with SET_USER_PREFERENCES_ACK

+----------------+--------------------+----------+-------------+
| Field          | Type               | Label    | Description |
+================+====================+==========+=============+
| preference_map | `SetUserPreferen   | repeated |             |
|                | ces.PreferenceMapE |          |             |
|                | ntry <#CARTA.SetUs |          |             |
|                | erPreferences.Pref |          |             |
|                | erenceMapEntry>`__ |          |             |
+----------------+--------------------+----------+-------------+

.. _CARTA.SetUserPreferences.PreferenceMapEntry:

SetUserPreferences.PreferenceMapEntry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== ==================== ===== ===========
Field Type                 Label Description
===== ==================== ===== ===========
key   `string <#string>`__       
value `string <#string>`__       
===== ==================== ===== ===========

.. _CARTA.SetUserPreferencesAck:

SetUserPreferencesAck
~~~~~~~~~~~~~~~~~~~~~

SET_USER_PREFERENCES_ACK

Response for SET_USER_PREFERENCES

+---------+------------------+-------+------------------------+
| Field   | Type             | Label | Description            |
+=========+==================+=======+========================+
| success | `bool <#bool>`__ |       | Defines whether        |
|         |                  |       | SET_USER_PREFERENCES   |
|         |                  |       | was successful Error   |
|         |                  |       | message (if            |
|         |                  |       | applicable)            |
+---------+------------------+-------+------------------------+

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
