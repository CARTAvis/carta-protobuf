../index.rst: ICD.rst.ignore clean_rst.py
	./clean_rst.py $< ..

ICD.rst.ignore: ICD.html
	pandoc $< --wrap=none --to=rst -o $@

ICD.html: CARTABackendFrontendInterfaceControlDocument.html clean_html.py
	./clean_html.py $< $@

CARTABackendFrontendInterfaceControlDocument.html: downloaded_ICD.zip
	unzip -o $<
	touch $@

downloaded_ICD.zip:
	wget -O $@ 'https://docs.google.com/document/d/1V4KzJaV3zQYJoA_ims28iBTit_aixo_xYcAfPiq8hic/export?format=zip'
