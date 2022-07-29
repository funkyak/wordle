function answer (){

// Banner
function func1() {
    var ddfs = ("░╚██╗████╗██╔╝██║░░██║██");
    var gfdrs= ("████╔╝██║░░██║██║░░░░░█████╗░░");
    var gdfwe = ("░██║░░██╗░░██║██╔══██╗██╔══");
    var lwpfd =("██╗██╔══██╗██║░░░░░██╔════╝");
    var erfq = ("░░░╚═╝░░░╚═╝░░░╚════╝░");
    var eigres = ("╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝");
    var qwksa = ("░░╚██╔╝░╚██╔╝░╚█████╔╝██");
    var mafef= ("║░░██║██████╔╝███████╗███████╗");
    var dsdf = ("░██╗░░░░░░░██╗░█████╗░████");
    var ksq = ("██╗░██████╗░██╗░░░░░███████╗");
    var fdvk = ("░░████╔═████║░██║░░██║██╔══█");
    var fdfgv = ("█╗██║░░██║██║░░░░░██╔══╝░░");
    console.log(dsdf+ksq);
    console.log(gdfwe+lwpfd);
    console.log(ddfs+gfdrs);
    console.log(fdvk+fdfgv);
    console.log(qwksa+mafef);
    console.log(erfq+eigres);  
}

var a = window.localStorage.getItem("nyt-wordle-state"); // Getting into the local storage 

if (a.match(/WIN.*/)) { // WIN function
// Simple math to generate the word from Local storage from the application tab
var word = a.slice(157,162);
alert("You have completed todays wordle : " + '"'+word+'"' );
} 

if (a.match(/IN_PROGRESS.*/)){ // Going for the win ;)  Could use this idea for the python version 
console.log("You have completed todays wordle : " + '"'+correct+'"' );

// DO NOT CHANGE BELLOW THIS 

// Simple math to generate the word from Local storage from the application tab
var Char1  = a.slice(105,106); // Char 1 
var Char2 = a.slice(106,107); // Char 2
var Char3 = a.slice(107,108); // Char 3
var Char4 = a.slice(108,109); // Char 4
var Char5 = a.slice(109,110); // Char 5
var correct = a.slice(105,110) // For the alert at the end
//Entering phase

window.dispatchEvent(new KeyboardEvent('keydown' , {'key' : Char1 })); // Entering the  First Character onto the website
window.dispatchEvent(new KeyboardEvent('keydown' , {'key' : Char2})); // Entering the Secound Character onto the website
window.dispatchEvent(new KeyboardEvent('keydown' , {'key' : Char3})); // Entering the Third Character onto the website
window.dispatchEvent(new KeyboardEvent('keydown' , {'key' : Char4})); // Entering the Fourth Character onto the website
window.dispatchEvent(new KeyboardEvent('keydown' , {'key' : Char5})); // Entering the Fith Character onto the website
// Submition phase
// Pressing the enter key

window.dispatchEvent(new KeyboardEvent('keydown', {
    key: "Enter",
    keyCode: 13,
    which: 13,
    code: "Enter", 
    location: 0,
    altKey: false,
    ctrlKey: false,
    metaKey: false}));
}
console.clear()
func1()}

answer()
