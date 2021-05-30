
var updateBtns = document.getElementsByClassName('update-cart')
console.log(updateBtns)
console.log("Hiiiiiiiiiiiiiiiiiii")
for (i = 0; i < updateBtns.length; i++)
{
    // On each click this function will run
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product // this is same as self in python
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
    })

    console.log('User:', user)
    if(user == 'AnonymousUser'){
        console.log('Not logged in')
    }
    else{
        updateUserOrder(productId, action)
    }
}

function updateUserOrder(productId, action){
    console.log('User logged in')

    var url = '/update_item/' // This is where we want to send our data

    fetch(url, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        // Data to send to the backend 
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
    })
}


