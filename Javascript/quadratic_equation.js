function quad_eq(a=0, b=0, c=0, round=2) {
    delta = b**2 - 4*a*c
    if (delta < 0) {
        throw "Delta is less than 0. There are no solutions to the equation."
    }
    if (delta == 0) {
        let x = (-b / (2 * a)).toPrecision(round)
        console.log("The solutions are equivalent and they are: " + x.toString())
    }
    if (delta > 0) {
        let x1 = ((-b - Math.sqrt(delta)) / (2*a)).toPrecision(round)
        let x2 = ((-b + Math.sqrt(delta)) / (2*a)).toPrecision(round)
        console.log(`The solutions are: x=${x1} or  x=${x2}`)
    }
}

quad_eq(1, 3, 1, 3)