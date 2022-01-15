document.querySelector('#signOutB').addEventListener('click', ()=>{
    chrome.runtime.sendMessage({ message: 'signOut' }, function(response){
        if (response.message === 'success'){
            window.location.replace("./popup.html")
        }
    })
});