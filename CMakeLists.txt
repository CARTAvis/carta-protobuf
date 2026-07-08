SET(Protobuf_IMPORT_DIRS shared stream control request .)

if (TARGET protobuf::libprotobuf)
        # The vendored protobuf/absl headers must be found before any system
        # copies pulled in by the top-level include directories.
        include(FetchContent)
        FetchContent_GetProperties(protobuf)
        FetchContent_GetProperties(absl)
        INCLUDE_DIRECTORIES(BEFORE
                ${protobuf_SOURCE_DIR}/src
                ${protobuf_SOURCE_DIR}/third_party/utf8_range
                ${protobuf_BINARY_DIR}/src
                ${absl_SOURCE_DIR})
else()
        FIND_PACKAGE(Protobuf REQUIRED)
        INCLUDE_DIRECTORIES(${PROTOBUF_INCLUDE_DIR})
endif()
# Included directly because find_package(Protobuf) may be redirected by
# FetchContent and never load this module; PROTOBUF_GENERATE_CPP needs it.
include(FindProtobuf)

file(GLOB PROTO_FILES
        "shared/*.proto"
        "control/*.proto"
        "request/*.proto"
        "stream/*.proto"
        )
PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER ${PROTO_FILES})
ADD_LIBRARY(carta-protobuf ${PROTO_HEADER} ${PROTO_SRC})
target_include_directories(carta-protobuf PUBLIC ${CMAKE_CURRENT_BINARY_DIR})
target_link_libraries(carta-protobuf PUBLIC protobuf::libprotobuf)
