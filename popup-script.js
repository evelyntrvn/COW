// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.3/firebase-app.js";
import { getAuth, OAuthProvider, signInWithPopup } from 'https://www.gstatic.com/firebasejs/9.6.3/firebase-auth.js';

const firebaseConfig = {
    apiKey: "AIzaSyBIg3HskDKONl6FEqTWyDbyLPvU1Rgv_Io",
    authDomain: "cowextension.firebaseapp.com",
    projectId: "cowextension",
    storageBucket: "cowextension.appspot.com",
    messagingSenderId: "82391294195",
    appId: "1:82391294195:web:520cabb5c66fcac81d1786",
    measurementId: "G-NSR9TGFGJK"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig),
    auth = getAuth(),
    provider = new OAuthProvider('microsoft.com');

provider.addScope('calendars.read');

// Initialize the FirebaseUI Widget using Firebase.
// const ui = new firebaseui.auth.AuthUI(auth);

// const uiConfig = {
//     callbacks: {
//         signInSuccessWithAuthResult: function (authResult, redirectUrl) {
//             return false;
//         },
//         uiShown: function () {
//             document.getElementById('signInB').style.display = 'none';
//         }
//     },
//     // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
//     signInFlow: 'popup',
//     // signInSuccessUrl: '<url-to-redirect-to-on-success>',
//     signInOptions: [
//         // Leave the lines as is for the providers you want to offer your users.
//         auth.GoogleAuthProvider.PROVIDER_ID,
//         auth.FacebookAuthProvider.PROVIDER_ID,
//         auth.TwitterAuthProvider.PROVIDER_ID,
//     ]
// };

document.getElementById('signIn').addEventListener('click', () => {
    console.log("button clicked")
    signInWithPopup(auth, provider)
        .then((result) => {
            console.log("signed in")
            chrome.runtime.sendMessage({ message: 'signIn' }, function(response){
                if (response.message === 'success'){
                    window.location.replace('./main.html');
                }
            })

            const credential = OAuthProvider.credentialFromResult(result);
            const accessToken = credential.accessToken;
            const idToken = credential.idToken;
        })
        .catch((error) => {
            // Handle error.
            console.log(error.code + '/n' + error)
        });
});