#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.




for(a in 100:500){
  for(b in 100:500){
    for(c in 100:500){
      if(a<b&&b<c){
      if((a^2+b^2)==c^2&&(a+b+c)==1000){
      cat('The pythagoras triples are', a,',', b,', and', c, 'and their product is', a*b*c)
      }
    }
   }
  }
 }