build:
	python3 generate.py ~/文档/cutekibry.github.io-source ~/文档/cutekibry.github.io
server, serve:
	python3 generate.py ~/文档/cutekibry.github.io-source ~/文档/cutekibry.github.io
	cd ~/文档/cutekibry.github.io && python3 -m http.server