//create a function that returns an array with only the numbers 
//var newArray = numbersOnly
//array = [1, "apple", -3, "orange", 0.5]


function numbersOnly(){
    var arr = [1, "apple", -3, "orange", 0.5]
    var newArray = [];
    
    for (var i = 0; i < arr.length; i++){
        if(typeof arr[i] === "number"){
            newArray.push(arr[i]);
        }
        console.log(newArray);
    }
}
numbersOnly()

