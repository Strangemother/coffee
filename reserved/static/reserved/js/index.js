
;(function(global){

	var header = $('header .bar')
		, sticky = false
		, lastpos
		, scroll
		, top
		;


	var main = function(){
		ui();
		// humanizeCost()
	};

	var dataGet = global.dataGet = function(s){
		return $('*[data-action="' + s + '"]')
	};

	var ui = function(){

		header.addClass('static').removeClass('fixed')

		$(global).scroll(function (event) {
		    scroll = $(global).scrollTop();
		    // Do something
		    // console.log(scroll);
		    top = header.position().top;

		    if( !sticky && scroll > top) {
		    	lastpos = (!sticky) ? top: lastpos;
		    	if(!sticky) header.removeClass('static').addClass('fixed');
		    	sticky = true;
		    } else if( scroll < lastpos && sticky) {
		    	if(sticky) header.addClass('static').removeClass('fixed');
		    	sticky = false;
		    }
		});
	};

	main();
})(window)
