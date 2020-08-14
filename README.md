# carta-protobuf

Protocol buffer message definitions for CARTA frontend/backend interface
`dev` branch should be used for `dev` branches of `carta-frontend` and `carta-backend` repos

## Updating the documentation

The CARTA Backend/Frontend ICD is automatically generated from this repository using [Sphinx](https://www.sphinx-doc.org), and published on [ReadTheDocs](https://readthedocs.org/). *Link will be added here when setup is complete.* To update this document, edit the reStructuredText documents in `docs`. 

After a change to the protocol buffer files you must also regenerate the `*.rst.txt` files by running `make` in the `protoc` subdirectory. These files are generated with [protoc-gen-doc](https://github.com/pseudomuto/protoc-gen-doc). Make sure that both the `protoc` and `protoc-gen-doc` executables are in your path.

[Plantuml](https://plantuml.com/) diagrams are rendered by the [Plantweb](https://plantweb.readthedocs.io/) extension and should be added to the text as UML, not as images. 

To preview the built documentation locally, install the `sphinx` and `plantuml` packages, preferably with `pip3`. Then run `make html` in the `docs` directory.
