# carta-protobuf

Protocol buffer message definitions for CARTA frontend/backend interface
`dev` branch should be used for `dev` branches of `carta-frontend` and `carta-backend` repos

## Updating the documentation

The CARTA Backend/Frontend ICD is automatically generated from this repository using [Sphinx](https://www.sphinx-doc.org), and published on [ReadTheDocs](https://readthedocs.org/) at <https://carta-protobuf.readthedocs.io>. To update this document, edit the [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) documents in `docs`.

After a change to the protocol buffer files you must also regenerate the `*.rst.txt` files by running `make` in the `protoc` subdirectory. These files are generated with [protoc-gen-doc](https://github.com/pseudomuto/protoc-gen-doc). Make sure that both the `protoc` and `protoc-gen-doc` executables are in your path. `protoc` is provided by [`protobuf`](https://github.com/protocolbuffers/protobuf).

To make it possible for the automatically generated message documentation to categorise messages correctly, please put all submessages in `shared/defs.proto`, even if they are only used in one file.

[Plantuml](https://plantuml.com/) diagrams are rendered by the [Plantweb](https://plantweb.readthedocs.io/) extension and should be added to the text as UML, not as images. 

To preview the built documentation locally, install the `sphinx`, `plantuml` and `sphinxcontrib-svg2pdfconverter` Python packages (install the latest versions with `pip3` or a similar tool -- the Ubuntu Sphinx package is very far behind, and Plantweb is not packaged). Then run `make html` in the `docs` directory.

*`sphinxcontrib-svg2pdfconverter` is required for PDF generation, and depends on the `rsvg-convert` executable (provided by the `librsvg2-bin` package in Ubuntu) -- but you do not have to install this dependency to build the HTML pages.*
