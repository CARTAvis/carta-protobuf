ICD_clean.md: ICD_clean.html
	pandoc ICD_clean.html -o ICD_clean.md

ICD_clean.html: CARTABackendFrontendInterfaceControlDocument.html
	./clean_html.py CARTABackendFrontendInterfaceControlDocument.html > ICD_clean.html

CARTABackendFrontendInterfaceControlDocument.html: downloaded_ICD.zip
	unzip -o downloaded_ICD.zip

downloaded_ICD.zip:
	wget -O downloaded_ICD.zip 'https://docs.google.com/document/d/1V4KzJaV3zQYJoA_ims28iBTit_aixo_xYcAfPiq8hic/export?format=zip'
