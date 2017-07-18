// For 30 days the amount doubls
//amount starts at .01 



    var p = .01;

    for(var d = 1; d <31; d++) {
        console.log(d);
        if( d < 31 ){
            p *= 2;
    }
    console.log(d + p);
    }