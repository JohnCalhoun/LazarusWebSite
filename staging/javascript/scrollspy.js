$('#mainnav').affix({
	offset:{
		top: 100
	}
});

$('#mainnav').affix({
	offset:{
		bottom:function(){
			return (this.botom=$('.footer').outerHeight(true))
			}
	}
});

