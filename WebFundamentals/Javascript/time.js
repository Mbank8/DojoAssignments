var HOUR = 10;
var MINUTE = 30;
var PERIOD = "PM";

if (MINUTE < 30 && PERIOD == "AM") {
    console.log("It is just after", HOUR, "in the morning.")
}
else if (MINUTE >= 30 && PERIOD == "AM") {
    console.log("It is almost", HOUR+1, "in the morning")
}
else if (MINUTE < 30 && PERIOD == "PM") {
    console.log("It is just after", HOUR, "in the evening")
}
else{
    console.log("It is almost", HOUR + 1, "in the evening")
}