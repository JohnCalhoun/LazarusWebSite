STAGE=../staging/documentation

.PHONY:stage documentation prep clean_compiled clean_compiled clean_build documentation

clean_compiled:
	rm ./compiled/*

clean_build:
	rm ./build/*

clean: clean_compiled clean_build

prep:
	cd ./src && make all

documentation: prep
	doxygen config

directory:
	mkdir -p $(STAGE)

stage: documentation directory
	cp -r ./build/html/* $(STAGE)

compile:
	cd ./src && make all

all:stage compile
