
;(function(global){

	var header = $('header .bar')
		, sticky = false
		, lastpos
		, scroll
		, top
		;


	var main = function(){
		ui();
		humanizeCost();
		createCache(menuData)
	};

	var ui = function(){
		dataOn('add', addItem);
	}

	var addItem = function(e){
		var id = $(this).data('id');
		addToCart(id);
	}

	var _cache = {};

	var createCache = function(data){
		var ids = _cache['id'] = {};

		for (var i = data.products.length - 1; i >= 0; i--) {
			var product = data.products[i];
			ids[product.id] = product;
		};
	}

	var getProduct = function(id) {
		return _cache.id[id]
	}

	var dataOn = function(name, cb){
		return $('*[data-action="' + name + '"]').on('click', cb)
	};

	var dataGet = global.dataGet = function(s){
		return $('*[data-item="' + s + '"]')
	};

	var humanizeCost = function(){
		/* Run through all the price items. If the element
		has not been templated the view item is altered and a
		data flag is stored.
		If the item has been templated it is omited.*/

		var each = function(i,e){
			// Each element found
			var $this = $(e);
			// original pence.
			var d = $this.data('units');
			var op = $this.data('price');

			if(d == undefined) {
				$this.data('units', op);
			};

			$this.find('.cost').text( convertPrice(op) );
			n = 'prefix';
			if(op < 100){
				n = 'postfix'
			};

			$this.find('.cost-fix');
			$this.find('.cost-' + n).removeClass('hidden')
		};

		dataGet('cost').each(each);
	};

	var convertPrice = function(pennies, prefix) {
		prefix = prefix == undefined? false: prefix
		/* convert the pennies to pounds pence string.*/
		var p = parseInt(pennies) / 100;
		var fn = prefix ? 'formatMoney': 'formatNumber'
		if(prefix) {
			f = accounting.formatMoney(p, '£')
		}  else {
			f = accounting.formatNumber(p, 2)

		}
		return f
	};

	var cart = []
	var addToCart = function(id) {
		/*
		add item to the cart.
		*/
		var product = getProduct(id)
		cart.push(product)
		renderCart(cart)
	}

	var renderCart = function(cart) {
		var totalCost = 0;
		for (var i = cart.length - 1; i >= 0; i--) {
			var item = cart[i];
			totalCost += item.price
			dataGet('product-' + item.id).addClass('in-cart')
		};

		dataGet('cart-count').text(cart.length)
		dataGet('cart-total').text(convertPrice(totalCost, true))
	}


	main();
})(window)
