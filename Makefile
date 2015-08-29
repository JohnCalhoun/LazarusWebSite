.PHONY:publish clean javascript

css:
	cd ./css && make all
documentation:css
	cd ./documentation && make all

main:
	cd ./main && make all

font_directory:
	mkdir -p ./staging/fonts
fonts:font_directory 
	cp ./boot*/boot*/fonts/* ./staging/fonts

clean:
	rm -rf /var/www/html/lazarus/*

javascript:
	cd ./javascript && make all

all:clean documentation main javascript

publish:all
	cp -r ./staging/* /var/www/html/lazarus
