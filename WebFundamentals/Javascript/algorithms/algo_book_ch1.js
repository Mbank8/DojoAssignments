/*“Setting and Swapping
Set myNumber to 42. Set myName to your name. Now swap myNumber into myName & vice versa.
”

Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. */

// var myNumber = 42;
// var myName = "Matt";
// temp = myNumber;

// if(myNumber == 42){
//     myNumber = myName;
// }
// console.log(myNumber);
// // console.log(myName);
// if(myName == "Matt"){
//     myName = temp;
// }
// console.log(myName);


/*“Print -52 to 1066
Print integers from -52 to 1066 using a FOR loop.”

Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. */

// for(var i = -52; i < 1067; i++){
//     console.log(i);
// }

/*“Don’t Worry, Be Happy
Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.”*/

// function beCheerful(){
//     var greeting = "good morning!";
//     for(var i =1; i < 100; i++){
//         if( i >= 1 && i < 100){
//             console.log(greeting);
//         }
//     }
// } 
// beCheerful()

/*“ Multiples of Three – but Not All
Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6” */

// for(var i = -300; i < 1; i++){
//     if(i == -3 || i == -6){
//         continue;
//     }
//     else if(i % 3 === 0){
//         console.log(i);
//     }
// }

/*“ Printing Integers with While
Print integers from 2000 to 5280, using a WHILE.”*/
// var i = 2000
// while(i < 5281){ 
//     console.log(i);
//     i++;
// }

//“If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....”
// function happyBirthday(x,y){
// var bday = 41
// if(x + y == bday){
//     console.log("How did you know?");
// }
// else{
//     console.log("Just another day");
// }

// }
// happyBirthday(12,29)

/*“Leap Year
Write a function that determines whether a given year is a leap year. If a year is divisible by four, 
it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.” */

// function leapYear(x) {
// var year = x;
// if(year % 100 != 0 && (year % 4 === 0 || year % 400 === 0)){
//     console.log("Its a leap year");
// }
// else{
//     console.log("Nope, not a leap year");
// }

// }
// leapYear(2022)

/*“ Print and Count
Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.”
*/

// var count = 0;
// for(var i = 512; i< 4096; i++) {
//     if(i % 5 == 0){
//         console.log(i);
//     }
//     if(i % 5 == 0){
//         console.log(count++);
//     }
// }

/*“ Multiples of Six
Print multiples of 6 up to 60,000, using a WHILE.”
NOT SOLVED */

// var num = 1;

// while( num < 60001 ){
//     if(num % 6 == 0){
//         console.log(num);
//         num++;
//     }
// }

/*“ Counting, the Dojo Way
Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".”
*/

// for(var num = 1; num < 101; num++){
//     if(num % 10 == 0 && num % 5 == 0){
//         console.log('Coding Dojo');
//     }
//     else if(num % 5 == 0 && num % 10 != 0){
//         console.log('Coding');
//     }
//     else{
//         console.log(num);
//     }
// }
/*“Whoa, That Sucker’s Huge…
Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?”
// */
// var sum = 0;
// for (var i = -300000; i < 300001; i++){
//     if( i % 2 != 0){
//         sum = i + i;
        
//     }
//     console.log(sum);
// }

/*“ Countdown by Fours
Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.”
*/
// var i = 2016;

// while(i > 0){
//     if(i % 4 == 0){
//         console.log(i);
        
//     }
//     i--;
// }
/*“Create a function that accepts a number as an input. Return a new array that counts down by one, from the number
 (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array?”
*/
// function countDown(num){
//     var arr =[];
//     while (num >= 0){
//         arr.push(num);
//         num--;
//     }
    
//     return arr;
    
// }
// console.log(countDown(8));



//Your function will receive an array with two numbers. Print the first value, and return the second.
// function printReturn(x,y){

//     console.log(x);
//     return y;
// }

// printReturn(2,5);

/*“First Plus Length
Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the 
array’s first value is not a number, but a string (like "what?") or a boolean (like false).”
*/
// function firstLength(arr){
// if(typeof arr[0] != 'number'){
//     arr[0] = 0+ arr.length;
// }
// else{
//     arr[0]= arr[0] + arr.length;
// }
// console.log(arr[0]);
// return arr;
// }
// firstLength(["ribbit",2,3,4,5]);

//“For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.”
function greaterSecond([arr]){
    var num = 0;
    for(var i = 0; i >arr[1];){
        console.log(arr[i]);
        num++;
    }
    
        
  
    console.log(num);
   return num;

}
greaterSecond([1,3,5,7,9,13]);