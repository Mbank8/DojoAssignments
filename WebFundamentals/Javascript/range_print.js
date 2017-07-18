//function needs a start
//function needs a end (end is not included in the print
//function needs a skip amount (count by ...)

var start = 2 ;
var end = 10 ;
var skip = 2;

function printRange(){
    for(var i = start; i < end; i = i+skip){
        console.log(i);
    }

}
return printRange();