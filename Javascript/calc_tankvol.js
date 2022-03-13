function tankvol(h, d, vt) {
    // checks if any value is null ==> returns 0
    if (h == null || d == null || vt == null) return 0;

    // base area
    let barea = Math.PI * (d/2)**2;
    // cylinder length (height)
    let l = vt / barea;
    // angle of the vertical section
    let alpha = Math.acos((d/2 - h) * 2 / d) * 2;
    let section = (alpha / (2*Math.PI)) * barea;
    // triangle_area
    let tarea = Math.sin(alpha/2) * (d/2) * Math.cos(alpha/2)*(d/2);
    // fuel_area
    let farea = section - tarea;
    return parseInt(farea * l);
}


console.log("solution: " + tankvol(40, 120, 3600))