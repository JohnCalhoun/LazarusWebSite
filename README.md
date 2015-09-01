#LAZARUS website
css files are in the /css directory
"make all" compiles all .scss files in /css/src to .css files in /css/compiled

doxygen documentation settings and files are in /documentation
"make all" generates all documenation and puts it in /documentation/build

images and photes are in /photos

/main/src stores the haml files for the non documentation pages
"make all" compiles all /main/src to their html files in /main/compiled

"make all" in / builds all components for the website and stores web site in /staging
/staging is ready to be uploaded to webserver

