.PHONY: all
../compiled/global.css:global.scss ./stylesheets/bootstrap/*.scss
	sass global.scss ../compiled/global.css

../compiled/parallax.css:parallax.scss
	sass parallax.scss	../compiled/parallax.css

../compiled/mainpage.css:mainpage.scss
	sass mainpage.scss ../compiled/mainpage.css

all:../compiled/global.css  ../compiled/parallax.css ../compiled/mainpage.css
	
