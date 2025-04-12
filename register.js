// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCvSoS85MB3ZxTgnalaKPbBUnQs89Ds-l8",
  authDomain: "hackerstreetz.firebaseapp.com",
  projectId: "hackerstreetz",
  storageBucket: "hackerstreetz.firebasestorage.app",
  messagingSenderId: "129990423263",
  appId: "1:129990423263:web:f47f01e1d480ad159aef6a",
  measurementId: "G-V4CZTY31VW"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

document.getElementById("submit").addEventListener("click", (e) => {
    e.preventDefault(); // Prevent form refreshing

    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("confirm-password").value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    // user create
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            alert("Registration Successful!");
            console.log(userCredential.user);

            window.location.href = "frontend/index.html";  
        })
        .catch((error) => {
            alert(error.message);
            console.error(error);
        });
});