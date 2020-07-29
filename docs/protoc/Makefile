PROTODIRS=control request stream shared
INCLUDES=$(patsubst %,-I../../%,$(PROTODIRS))
PROTODOCS=$(patsubst %,../%.rst,$(PROTODIRS))

.PHONY: all
all: $(PROTODOCS)

../%.rst: %.html
	pandoc -o $@ $<

%.html: $(shell find ../../% -type f -name '*.proto')
	protoc --doc_out=. --doc_opt=html,$@ $(INCLUDES) ../../$(basename $@)/*.proto
