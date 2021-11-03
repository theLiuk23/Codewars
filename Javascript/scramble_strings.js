function scramble(s1, s2) {
    for (const char of s2) {
        if (s1.match(char).length < s2.match(char).length) {
            return false;
        }
    }
    return true
}

console.log(scramble("lucailking", "klucingali").toString())