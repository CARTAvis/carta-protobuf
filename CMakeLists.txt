SET(Protobuf_IMPORT_DIRS shared stream control request .)
FIND_PACKAGE(Protobuf MODULE REQUIRED)
include(FindProtobuf)
INCLUDE_DIRECTORIES(${PROTOBUF_INCLUDE_DIR})
if (TARGET protobuf::libprotobuf)
        # TensorStore may provide a vendored protobuf target with extra include dirs.
        get_target_property(PROTOBUF_TARGET_INCLUDE_DIRS protobuf::libprotobuf INTERFACE_INCLUDE_DIRECTORIES)
endif()

foreach(PROTOBUF_TARGET_INCLUDE_DIR ${PROTOBUF_TARGET_INCLUDE_DIRS})
        get_filename_component(PROTOBUF_SOURCE_DIR "${PROTOBUF_TARGET_INCLUDE_DIR}/.." ABSOLUTE)
        if (EXISTS "${PROTOBUF_SOURCE_DIR}/third_party/utf8_range/utf8_validity.h")
                # Vendored protobuf includes utf8_range headers outside protobuf/src.
                list(APPEND PROTOBUF_TARGET_INCLUDE_DIRS "${PROTOBUF_SOURCE_DIR}/third_party/utf8_range")
        endif()
endforeach()

if (protobuf_SOURCE_DIR AND EXISTS "${protobuf_SOURCE_DIR}/third_party/utf8_range/utf8_validity.h")
        list(APPEND PROTOBUF_TARGET_INCLUDE_DIRS "${protobuf_SOURCE_DIR}/third_party/utf8_range")
endif()

if (absl_SOURCE_DIR AND EXISTS "${absl_SOURCE_DIR}/absl/base/options.h")
        # Prefer TensorStore's vendored Abseil headers over system headers.
        INCLUDE_DIRECTORIES(BEFORE ${absl_SOURCE_DIR})
endif()

INCLUDE_DIRECTORIES(${PROTOBUF_TARGET_INCLUDE_DIRS})
file(GLOB PROTO_FILES
        "shared/*.proto"
        "control/*.proto"
        "request/*.proto"
        "stream/*.proto"
        )
PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER ${PROTO_FILES})
ADD_LIBRARY(carta-protobuf ${PROTO_HEADER} ${PROTO_SRC})
target_include_directories(carta-protobuf PUBLIC ${PROTOBUF_INCLUDE_DIR} ${PROTOBUF_TARGET_INCLUDE_DIRS})
if (TARGET protobuf::libprotobuf)
        # Propagate the same protobuf library used to compile generated sources.
        target_link_libraries(carta-protobuf PUBLIC protobuf::libprotobuf)
else()
        target_link_libraries(carta-protobuf PUBLIC ${PROTOBUF_LIBRARY})
endif()
