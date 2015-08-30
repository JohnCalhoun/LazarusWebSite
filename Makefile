.PHONY:publish clean javascript css documentation main images font_directory fonts all publish

css:
	cd ./css && make all
documentation:css
	cd ./documentation && make all

main:
	cd ./main && make all
images:
	cd ./photos && make all


font_directory:
	mkdir -p ./staging/fonts
fonts:font_directory 
	cp ./boot*/boot*/fonts/* ./staging/fonts

clean:
	rm -rf /var/www/html/lazarus/*

javascript:
	cd ./javascript && make all

all:clean documentation main javascript images

publish:all
	cp -r ./staging/* /var/www/html/lazarus
