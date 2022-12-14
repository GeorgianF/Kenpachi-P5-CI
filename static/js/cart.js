const updateBtns = document.getElementsByClassName('update-cart');

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product;
		var action = this.dataset.action;

		if (user == 'AnonymousUser'){
			var alerted = localStorage.getItem('alerted') || '';
        	if (alerted != 'yes') {
         		alert(
					"You must create an account to be able to submit orders. \nThe cart items won't be remembered at checkout");
         		localStorage.setItem('alerted','yes');
        	}
			updateCartAnonymusUser(productId, action);
		} else {
			updateUserOrder(productId, action);
		}
	});
}

function updateCartAnonymusUser(productId, action) {
	if (action == 'add') {
		if (cart[productId] == undefined) {
			cart[productId] = {'quantity':1};
		} else {
			cart[productId]['quantity'] += 1;
		}
	}
	if (action == 'remove') {
		cart[productId]['quantity'] -= 1;
		if (cart[productId]['quantity'] <= 0){
			delete cart[productId];
		}
	}

	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/";
	location.reload();
}

function updateUserOrder (productId, action) {
	var url = 'item_update/';

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken': csrftoken,
			}, 
			body:JSON.stringify({
				'productId': productId,
				'action': action,
			})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload();
		});
}
