function init(){
    chrome.runtime.sendMessage({message: 'isSignedIn'}, function (response){
        if (response.message === 'success' && response.payload){
            window.location.replace("./main.html");
        }
    })
}

init();