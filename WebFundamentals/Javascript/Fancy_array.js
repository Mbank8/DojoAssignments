//write a function that returns arr # -> Name
//arr = ["James", "Jill", "Jane", "Jack"]

function fancyArray(arr){
var arr = ["James", "Jill", "Jane", "Jack"];
temp = arr[0];
arr[0] = arr[3];
arr[3] = temp;
    console.log[arr]
    for(var i = 0; i < arr.length; i++) {
        console.log(i + " -> " + arr[i]);
        
    }
}
return fancyArray()
