// 1.
// Poor Kenny
// Kenny tries to stay safe, but somehow everyday something happens. Out of the last 100
// days, there were 10 days with volcanos, 15 others with tsunamis, 20 earthquakes, 25
// blizzards and 30 meteors (for 100 days total). If these probabilities continue, write
// whatHappensToday() to print a day’s outcome.


// var random = Math.random();
// console.log(random)
// function whatHappensToday(){
//     if (random > 0 && random < .1){
//         console.log("Volcano Erupted!");
//     } else if( random >= .1 && random < .25){
//         console.log("Tsunami!");
//     } else if (random >= .25 && random < .45){
//         console.log("Earthquakessssss");
//     }else if(random >= .45 && random < .70){
//         console.log("BLIZZARD BRRRR");
//     }else {
//         console.log("METEORS");
//     }
// }

// whatHappensToday()

// 2.
// Reverse An Array
// Given array, write a function to reverse values, in-place. Example: reverse([3,1,6,4,2]) returns same
// array, containing [2,4,6,1,3].

//input [3,1,6,4,2]
//output[2,4,6,1,3]
// var my_array = [3,1,6,4,2]
// function reverseArray(arr){
//     var new_array = []
//     //reverse the array
//     for (var i = arr.length - 1; i>=0; i--){
//         console.log(arr[i], i)
//         new_array.push(arr[i])
//     }

// console.log(new_array) //[2,4,6,1,3]
// return new_array;
// }
// reverseArray(my_array)
// function reverseArrayInPlace(arr){
//     for(var i = 0; i < arr.length/2; i++){
//         var temp = arr[i];
//         arr[i] = arr[arr.length-1 - i];
//         arr[arr.length-1 - i] = temp;
//     }
//     return arr;
// }
// var my_array = reverseArrayInPlace(my_array);
// console.log(my_array);

// 3.
// Clock Hand Angles
// Regardless of how hard a Dojo student works (and they should work hard), they need time
// now and then to unwind – like hands on a clock. Traditional clocks are increasingly
// uncommon, but most can still read an analog clock’s hands of hours, minutes and seconds.
// Create clockHandAngles(seconds) that, given a number of seconds since 12:00:00, prints
// angles (in degrees) of the hour, minute and second hands. As review, 360 degrees form a
// full rotation. For input of 3600 secs (equivalent to 1:00:00), print "Hour hand: 30 degs.
// Minute hand: 0 degs. Second hand: 0 degs." For an input parameter seconds of 119730 (which
// is equivalent to 9:15:30 plus 24 hours!), you should log "Hour hand: 277.745 degs. Minute
// hand: 93 degs. Second hand: 180 degs." Note: in the second example, the angle for the minute
// hand is not simply 90 degrees; it has advanced a bit further, because of the additional 30
// seconds in that minute so far.
// Second: also calculate and print degrees for an additional “week hand” that rotates once
// each week.

//angle of hour hand based on seconds -> calculate the nuymber of degrees per second
//angle of minute based on seconds -> calculat the number or degrees per second for minute
//angle of seconds based on seconds

// every hour is 30 degrees
// every minute is 30/60
// every second is 30/60/60 = > .5/60 -> .00833

// number of seconds / .008333

//every 5 minutes is 30 degrees 
// every 600 seconds is 30 degrees
//every second is 30/600
//resets ever 3600 seconds

//every 5 seconds = 30 degrees
//every 60 seconds = 360 degrees
//
// function clockHandAngles(seconds){
//     var angleOfHour = seconds % 86400 * .5/60
//     console.log("angle of hour:" + angleOfHour)
//     var angleOfMinutes = seconds % 3600 * 1/10
//     console.log("angle of minutes:" + angleOfMinutes);
//     var angleOfSeconds = (seconds % 60) * 6;
//     console.log("angle of second hand:" + angleOfSeconds); 
// }
// clockHandAngles(119730)



// 4.
// Credit Card Validation
// The Luhn formula is sometimes used to validate credit card numbers. Create the function
// isCreditCardValid(digitArr) that accepts an array of digits on the card (13-19 depending on
// the card), and returns a boolean whether the card digits satisfy the Luhn formula, as
// follows:
// 1) Set aside the last digit; do not include it in these calculations (until step 5);
// 2) Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by
// 2;
// 3) If any results are larger than 9, subtract 9 from them;
// 4) Add all numbers (not just our odds) together;
// 5) Now add the last digit back in – the sum should be a multiple of 10.
// For example, when given digit array [5,2,2,8,2], after step 1) it becomes [5,2,2,8], then after
// step 2) it is [5,4,2,16]. Post-3) we have [5,4,2,7], then following 4) it becomes 18. After step
// 5) our value is 20, so ultimately we return true. If the final digit were any non-multiple-of-10,
// we would instead return false.

//input = [1,2,3,4,5,6,7,8,9,10,11,12,13]
//output = false
var input = [1,2,3,4,5,6,7,8,9,10,11,12,13]
function isCreditCardValid(digitArr){
    var last = digitArr.pop();
    for(var i = digitArr.length - 1; i <= 0; i-=2) {
        digitArr[i] = digitArr[i] * 2;
        if(digitArr[i] > 9) {
            digitArr[i] -= 9;
        }
    }
    var sum = 0
}