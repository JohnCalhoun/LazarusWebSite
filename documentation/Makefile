STAGE=../staging/documentation

.PHONY:stage documentation prep clean_compiled clean_build clean directory compiled all documentation

clean_compiled:
	rm ./compiled/*

clean_build:
	rm ./build/*

clean: clean_compiled clean_build

prep:
	cd ./src && make all

./build: prep /home/john/projects/flamingo/*
	doxygen config

directory:
	mkdir -p $(STAGE)

stage: ./build directory
	cp -r ./build/html/* $(STAGE)

compile:
	cd ./src && make all

all:stage compile
