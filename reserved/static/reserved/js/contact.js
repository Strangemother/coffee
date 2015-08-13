
;(function(global){

	var header = $('header .bar')
		, sticky = false
		, lastpos
		, scroll
		, top
		;


	var main = function(){
		ui();
	};

	var ui = function(){
	    google.maps.event.addDomListener(window, 'load', map);

	};

    var pos;

    var map = function(){
        pos = new google.maps.LatLng(addressLatLong[0], addressLatLong[1]);
		var mapCanvas = document.getElementById('g-map');
		var options = mapOptions(mapCanvas)
    	var map = new google.maps.Map(mapCanvas, options);
    	var marker = new google.maps.Marker();

        var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
        var marker = new google.maps.Marker({
          position: pos,
          map: map,
          // icon: iconBase + 'schools_maps.png'
        });

    	var infowindow = new google.maps.InfoWindow({
    		content:"<b>Cafe Milano</b><br/>89 W west campbell street<br/> Glasgow"
    	});

    	google.maps.event.addListener(marker, "click", function(){
    		infowindow.open(map,marker);
    	});

    	infowindow.open(map, marker);

	}

	var mapOptions = function(canvas) {

		return {
			center: pos,
            zoom: 17,
            mapTypeId: google.maps.MapTypeId.ROADMAP
		}
	}

	main();
})(window)
