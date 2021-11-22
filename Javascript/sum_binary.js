var countBits = function(n) {
   let sum = 0;
   let binary = int((n >>> 0).toString(2));
    
   // console.log(binary.toString());
   for (var i=0; i < binary.length; i++)
   {
      if (binary[i] == 1)
      {
         sum += 1;
      }
   }
    
   // console.log(sum.toString());
   return sum;
};

console.log(countBits(123432).toString());