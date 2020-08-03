PROTODIRS=control request stream shared
PROTOSECTIONS=control request stream defs enums
PROTOFILES=$(shell find ../.. -type f -name '*.proto')
INCLUDES=$(patsubst %,-I../../%,$(PROTODIRS))
PROTODOCS=$(patsubst %,../%.rst.txt,$(PROTOSECTIONS))

$(PROTODOCS) &: $(PROTOFILES) rest.tmpl
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../defs.rst.txt $(INCLUDES) ../../shared/defs.proto
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../enums.rst.txt $(INCLUDES) ../../shared/enums.proto
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../control.rst.txt $(INCLUDES) ../../control/*.proto
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../request.rst.txt $(INCLUDES) ../../request/*.proto
	@protoc --doc_out=.. --doc_opt=rest.tmpl,../stream.rst.txt $(INCLUDES) ../../stream/*.proto

# TODO add contents back to the template
# TODO add a script for post-processing the generated files, to add colours and hyperlinks 
# TODO add CAPITAL_SNAKE anchors to files to simplify references
