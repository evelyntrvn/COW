let signedIn = false;

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse){
    if (request.message === 'isSignedIn'){
        sendResponse({
            message: 'success',
            payload: signedIn
        });
    }else if (request.message === 'signOut'){
        signedIn = false;
        sendResponse({ message: 'success' });
    } else if (request.message === 'signIn'){
        signedIn = true;
        sendResponse({ message: 'success' });
    }
    return true;
});