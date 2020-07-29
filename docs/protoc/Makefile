# TODO add the splitting here; output to parent directory

protoc.rst: protoc.html
	pandoc -o $@ $<

# TODO: this should depend on the protocol buffer files
protoc.html:
	protoc --doc_out=. --doc_opt=html,$@ -I../../control -I../../request -I../../shared -I../../stream --plugin=protoc-gen-doc=/home/adrianna/go/bin/protoc-gen-doc ../../*/*.proto
