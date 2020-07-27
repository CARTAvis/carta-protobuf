.PHONY: all

# TODO: this is temporary; once the conversion is done all the conversion steps will be removed
all: ICD_clean.rst protoc.rst

ICD_clean.rst: ICD_clean.html
	pandoc ICD_clean.html -o ICD_clean.rst

ICD_clean.html: CARTABackendFrontendInterfaceControlDocument.html clean_html.py
	./clean_html.py CARTABackendFrontendInterfaceControlDocument.html > ICD_clean.html

CARTABackendFrontendInterfaceControlDocument.html: downloaded_ICD.zip
	unzip -o downloaded_ICD.zip
	touch CARTABackendFrontendInterfaceControlDocument.html

downloaded_ICD.zip:
	wget -O downloaded_ICD.zip 'https://docs.google.com/document/d/1V4KzJaV3zQYJoA_ims28iBTit_aixo_xYcAfPiq8hic/export?format=zip'

protoc.rst: protoc.html
	pandoc -o protoc.rst protoc.html

# TODO: this should depend on the protocol buffer files
protoc.html:
	protoc --doc_out=. --doc_opt=html,protoc.html -I../control -I../request -I../shared -I../stream --plugin=protoc-gen-doc=/home/adrianna/go/bin/protoc-gen-doc ../*/*.proto
