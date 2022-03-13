function arrayDiff(a, b) {
    b.forEach(element => {
        if (a.indexOf(element) > -1) {
            a = a.filter(function(value, index, arr) {
                return value != element;
            });
        }
    });
    return a;
}

//                     a             b
console.log(arrayDiff([1, 2, 3, 4], [2, 4]))