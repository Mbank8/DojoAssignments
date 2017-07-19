//function that takes number of quarters (1 quarter = 1 game)
//1 in 100 chance to win the slot machine
//a win gives you a random number between 50 and 100 quarters(use Math.random and Math.floor)
//if they win return the random number of quarters added to their remaining quarters
//return 0 if no more quarters

function playSlots(numOfQuarters) {
    var win = Math.random;
    console.log(win);

    if(numOfQuarters >=1 && win < .01){
        var winnings = (Math.floor(Math.random()*50)+50);
        console.log(winnings);
    }
    if(winnings > 0){
        console.log(numOfQuarters += winnings);
    }
    if(numOfQuarters === 0){
        return 0;
    }
}
playSlots();
