CARTA Interface Control Document
================================

:Date: 12 Oct 2021
:Authors: Angus Comrie, Rob Simmonds and the CARTA development team
:Version: 24.1.0
:ICD Version Integer: 24
:CARTA Target: Version 3.0

.. include:: changelog.rst.txt

Versioning
----------

* Major version change (``1.2.3`` -> ``2.0.0``): this is a breaking change.
* Minor version change (``1.2.3`` -> ``1.3.0``): this is added functionality which is optional and non-breaking.
* Patch (``1.2.3`` -> ``1.2.4``): this is a change which does not affect functionality (e.g. a typo fix in a comment, or a changed field name).

Some legacy changelog entries may not follow this approach. Only changes to the protocol buffer source files should be recorded here; changes only to this documentation do not require a version bump.

.. toctree::
   :numbered: 3
   :caption: Contents:

   introduction
   context
   behaviour
   layer_descriptions
   protocol_buffer_reference
