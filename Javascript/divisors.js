function divisors(input) {
    let results = [];
    for(i=2; i<=input/2; i++){
        if (input % i == 0) {
            results.push(i);
        }
    }
    if (results.length == 0) return String(input) + " is prime";
    return results;
};