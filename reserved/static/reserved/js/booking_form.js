
;(function(window){

	$(document).ready(function(){
		easyDateInput('#id_arrival, #id_depature');

		$('form.booking-form').on('submit', function(){
			$('#id_arrival, #id_depature').each(function(i, e){
				var d = $(e).data('date');
				var fd = moment( d ).format('YYYY-MM-DD HH:MM:SS');

				$(e).val( fd );
			})
		})
	})

})(window)
