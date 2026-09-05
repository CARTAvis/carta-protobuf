SET(Protobuf_IMPORT_DIRS shared stream control request .)
FIND_PACKAGE(Protobuf REQUIRED)
INCLUDE_DIRECTORIES(${PROTOBUF_INCLUDE_DIR})
file(GLOB PROTO_FILES
        "shared/*.proto"
        "control/*.proto"
        "request/*.proto"
        "stream/*.proto"
        )
PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER ${PROTO_FILES})
ADD_LIBRARY(carta-protobuf ${PROTO_HEADER} ${PROTO_SRC})