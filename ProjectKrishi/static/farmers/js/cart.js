var updateBtns = document.getElementsByClassName('update-cart')
console.log(updateBtns)
console.log("Hiiiiiiiiiiiiiiiiiiiii")
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
        console.log('User logged in')
    }
}


