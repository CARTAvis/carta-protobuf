.. _introduction:

Introduction
============

The CARTA application is designed in a server-client model, with the backend (written in C++) communicating with the frontend (Web-based, using HTML and JavaScript web frameworks) through an interface defined in this document. While CARTA is required to support a number of file formats (FITS, CASA, HDF5 and Miriad), throughout the document, nomenclature will be defaulted to FITS files, such as when referring to multiple HDUs in a file, and header entries.

:comment:`Throughout this document, things that require some clarity, or are not finalised are commented on in this font style.`

