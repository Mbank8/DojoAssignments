//function needs a start
//function needs a end (end is not included in the print
//function needs a skip amount (count by ...)

// var start = 1 ;
// var end = 3 ;
// var skip = 1;

// function printRange(){
//     for(var i = start; i < end; i = i+skip){
//         console.log(i);
//     }

// }
// return printRange();



function printRange(start, end, skip){
    while(start < end){
        console.log(start);
        start += skip;
    }
}
return printRange(2,10,2);
