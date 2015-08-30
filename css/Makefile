.PHONY:clean
clean:
	rm ./compiled/*
compile:
	cd ./src && make all
directory:
	mkdir -p ../staging/css

all:compile directory
	cp ./compiled/*.css ../staging/css
