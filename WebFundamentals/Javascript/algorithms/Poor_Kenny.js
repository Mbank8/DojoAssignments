// var array = [3,1,6,4,2];
// console.log(array.reverse());


function reverseArr(input) {
    var ret = new Array;
    for (var i = 0; i < input.length; i--) {
        ret.push(input[i]);
    }
    console.log(ret);
}

var a = [3,5,4,2];
var b = reverseArr(a);