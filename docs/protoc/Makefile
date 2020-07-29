PROTODIRS=control request stream shared
PROTOSECTIONS=control request stream defs enums
PROTOFILES=$(shell find ../.. -type f -name '*.proto')
INCLUDES=$(patsubst %,-I../../%,$(PROTODIRS))
PROTODOCS=$(patsubst %,../%.rst,$(PROTOSECTIONS))

$(PROTODOCS) &: $(PROTOFILES) rest.tmpl
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../defs.rst $(INCLUDES) ../../shared/defs.proto
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../enums.rst $(INCLUDES) ../../shared/enums.proto
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../control.rst $(INCLUDES) ../../control/*.proto
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../request.rst $(INCLUDES) ../../request/*.proto
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../stream.rst $(INCLUDES) ../../stream/*.proto
	@sed -ri 's/\| (CARTA\.([^ ]+)) \|/`\2 <\1>`__/g' $(PROTODOCS)
