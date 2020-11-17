PROTODIRS=control request stream shared
PROTOSECTIONS=messages defs enums
PROTOFILES=$(shell find ../.. -type f -name '*.proto')
INCLUDES=$(patsubst %,-I../../%,$(PROTODIRS))
PROTODOCS=$(patsubst %,../src/%.rst.txt,$(PROTOSECTIONS))

$(PROTODOCS) &: protoc.json clean_protoc.py
	@./clean_protoc.py protoc.json ../src

protoc.json: $(PROTOFILES)
	@protoc --doc_out=. --doc_opt=json,protoc.json $(INCLUDES) ../../*/*.proto
