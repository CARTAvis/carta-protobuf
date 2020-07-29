

.. CARTA.AnimationFrame:

AnimationFrame
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| channel | sfixed32 |  |  |
+-------+------+-------+-------------+
| stokes | sfixed32 |  |  |
+-------+------+-------+-------------+



.. CARTA.CatalogFileInfo:

CatalogFileInfo
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| name | string |  |  |
+-------+------+-------+-------------+
| type `CatalogFileType <CARTA.CatalogFileType>`__  |  |
+-------+------+-------+-------------+
| file_size | sfixed64 |  |  |
+-------+------+-------+-------------+
| description | string |  |  |
+-------+------+-------+-------------+
| coosys `Coosys <CARTA.Coosys>`__ repeated |  |
+-------+------+-------+-------------+
| date | sfixed64 |  |  |
+-------+------+-------+-------------+



.. CARTA.CatalogHeader:

CatalogHeader
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| name | string |  |  |
+-------+------+-------+-------------+
| data_type `ColumnType <CARTA.ColumnType>`__  |  |
+-------+------+-------+-------------+
| column_index | sfixed32 |  |  |
+-------+------+-------+-------------+
| description | string |  |  |
+-------+------+-------+-------------+
| units | string |  |  |
+-------+------+-------+-------------+



.. CARTA.CatalogImageBounds:

CatalogImageBounds
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| x_column_name | string |  |  |
+-------+------+-------+-------------+
| y_column_name | string |  |  |
+-------+------+-------+-------------+
| image_bounds `ImageBounds <CARTA.ImageBounds>`__  |  |
+-------+------+-------+-------------+



.. CARTA.ColumnData:

ColumnData
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| data_type `ColumnType <CARTA.ColumnType>`__  |  |
+-------+------+-------+-------------+
| string_data | string | repeated | All data types other than string sent as binary |
+-------+------+-------+-------------+
| binary_data | bytes |  | binary data will get converted to a TypedArray |
+-------+------+-------+-------------+



.. CARTA.Coosys:

Coosys
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| equinox | string |  |  |
+-------+------+-------+-------------+
| epoch | string |  |  |
+-------+------+-------+-------------+
| system | string |  |  |
+-------+------+-------+-------------+



.. CARTA.DoubleBounds:

DoubleBounds
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| min | double |  |  |
+-------+------+-------+-------------+
| max | double |  |  |
+-------+------+-------+-------------+



.. CARTA.FileInfo:

FileInfo
^^^^^^^^^^^^^

File info message structure (internal use only)


+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| name | string |  |  |
+-------+------+-------+-------------+
| type `FileType <CARTA.FileType>`__  |  |
+-------+------+-------+-------------+
| size | sfixed64 |  |  |
+-------+------+-------+-------------+
| HDU_list | string | repeated |  |
+-------+------+-------+-------------+
| date | sfixed64 |  |  |
+-------+------+-------+-------------+



.. CARTA.FileInfoExtended:

FileInfoExtended
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| dimensions | sfixed32 |  | Number of dimensions of the image file |
+-------+------+-------+-------------+
| width | sfixed32 |  | Width of the XY plane |
+-------+------+-------+-------------+
| height | sfixed32 |  | Height of the XY plane |
+-------+------+-------+-------------+
| depth | sfixed32 |  | Number of channels |
+-------+------+-------+-------------+
| stokes | sfixed32 |  | Number of Stokes parameters |
+-------+------+-------+-------------+
| stokes_vals | string | repeated | List of Stokes parameters contained in the file (if applicable). For files that do not explicitly specify Stokes files, this will be blank. |
+-------+------+-------+-------------+
| header_entries `HeaderEntry <CARTA.HeaderEntry>`__ repeated | Header entries from header string or attributes |
+-------+------+-------+-------------+
| computed_entries `HeaderEntry <CARTA.HeaderEntry>`__ repeated |  |
+-------+------+-------+-------------+



.. CARTA.FilterConfig:

FilterConfig
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| column_name | string |  |  |
+-------+------+-------+-------------+
| comparison_operator `ComparisonOperator <CARTA.ComparisonOperator>`__  |  |
+-------+------+-------+-------------+
| value | double |  |  |
+-------+------+-------+-------------+
| secondary_value | double |  |  |
+-------+------+-------+-------------+
| sub_string | string |  |  |
+-------+------+-------+-------------+



.. CARTA.HeaderEntry:

HeaderEntry
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| name | string |  |  |
+-------+------+-------+-------------+
| value | string |  |  |
+-------+------+-------+-------------+
| entry_type `EntryType <CARTA.EntryType>`__  |  |
+-------+------+-------+-------------+
| numeric_value | double |  |  |
+-------+------+-------+-------------+
| comment | string |  |  |
+-------+------+-------+-------------+



.. CARTA.Histogram:

Histogram
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| channel | sfixed32 |  |  |
+-------+------+-------+-------------+
| num_bins | sfixed32 |  |  |
+-------+------+-------+-------------+
| bin_width | double |  |  |
+-------+------+-------+-------------+
| first_bin_center | double |  |  |
+-------+------+-------+-------------+
| bins | sfixed32 | repeated |  |
+-------+------+-------+-------------+
| mean | double |  |  |
+-------+------+-------+-------------+
| std_dev | double |  |  |
+-------+------+-------+-------------+



.. CARTA.ImageBounds:

ImageBounds
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| x_min | sfixed32 |  |  |
+-------+------+-------+-------------+
| x_max | sfixed32 |  |  |
+-------+------+-------+-------------+
| y_min | sfixed32 |  |  |
+-------+------+-------+-------------+
| y_max | sfixed32 |  |  |
+-------+------+-------+-------------+



.. CARTA.Point:

Point
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| x | float |  |  |
+-------+------+-------+-------------+
| y | float |  |  |
+-------+------+-------+-------------+



.. CARTA.RegionInfo:

RegionInfo
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| region_type `RegionType <CARTA.RegionType>`__  | The type of region described by the control points. The meaning of the control points will differ, depending on the type of region being defined. |
+-------+------+-------+-------------+
| control_points `Point <CARTA.Point>`__ repeated | Control points for the region |
+-------+------+-------+-------------+
| rotation | float |  | (Only applicable for ellipse and rectangle) Rotation of the region in the xy plane (radians). |
+-------+------+-------+-------------+



.. CARTA.RegionStyle:

RegionStyle
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| name | string |  | The name of the region, displayed as an annotation label. |
+-------+------+-------+-------------+
| color | string |  | Color as a name ("blue"), RGB string, or hex string |
+-------+------+-------+-------------+
| line_width | sfixed32 |  | Width in pixels |
+-------+------+-------+-------------+
| dash_list | sfixed32 | repeated | Dash length: on, off |
+-------+------+-------+-------------+



.. CARTA.SpatialProfile:

SpatialProfile
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| start | sfixed32 |  |  |
+-------+------+-------+-------------+
| end | sfixed32 |  |  |
+-------+------+-------+-------------+
| raw_values_fp32 | bytes |  |  |
+-------+------+-------+-------------+
| coordinate | string |  |  |
+-------+------+-------+-------------+



.. CARTA.SpectralProfile:

SpectralProfile
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| coordinate | string |  |  |
+-------+------+-------+-------------+
| stats_type `StatsType <CARTA.StatsType>`__  |  |
+-------+------+-------+-------------+
| raw_values_fp32 | bytes |  |  |
+-------+------+-------+-------------+
| raw_values_fp64 | bytes |  |  |
+-------+------+-------+-------------+



.. CARTA.StatisticsValue:

StatisticsValue
^^^^^^^^^^^^^




+-------+------+-------+-------------+
| Field | Type | Label | Description |
+=======+======+=======+=============+
| stats_type `StatsType <CARTA.StatsType>`__  |  |
+-------+------+-------+-------------+
| value | double |  |  |
+-------+------+-------+-------------+





