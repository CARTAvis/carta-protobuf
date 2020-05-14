ICD_clean.html: CARTABackendFrontendInterfaceControlDocument.html
	./clean_html.py CARTABackendFrontendInterfaceControlDocument.html > ICD_clean.html

CARTABackendFrontendInterfaceControlDocument.html: CARTA\\ Backend_Frontend\\ Interface\\ Control\\ Document.zip
	unzip -o 'CARTA Backend_Frontend Interface Control Document.zip'

# Spaces are inconvenient, but I want to keep the default filename
CARTA\\ Backend_Frontend\\ Interface\\ Control\\ Document.zip:
	wget -O 'CARTA Backend_Frontend Interface Control Document.zip' 'https://docs.google.com/document/d/1V4KzJaV3zQYJoA_ims28iBTit_aixo_xYcAfPiq8hic/export?format=zip'
