#A palindromic number reads the same both ways. The largest palindrome made from
#the product of two 2-digit numbers is 9009 = 91 � 99.
#ind the largest palindrome made from the product of two 3-digit numbers.

palindrome <- function(x){
  p <- as.numeric(unlist(strsplit(as.character(x), split='')))
  z = as.numeric(paste(rev(p), collapse=""))
  if(z==x){
    TRUE
  }else FALSE
}

multiply.each <- function(l){
  as.vector(as.matrix(as.data.frame(combn(l,2,FUN=function(y) y[1]*y[2]))))
}

maxpalprod <- function(x){
  m = multiply.each(x)
  maxpalprod=rep(FALSE, length(m))
  for(i in m){
    if(palindrome(i)){
      maxpalprod[which(m==i)]=i
    } else next
  }
  cat('The maximum palindromic product of two', nchar(x[1]), 'digits numbers is', max(maxpalprod))

}

maxpalprod(x=100:999)
#Finding the two unique numbers
for(p in 100:999){
  for(t in p:999){
    if(t*p==906609)
      cat('The maximum palindromic product of two three digits numbers is',906609, 'and the two three digt numbers are,', t, 'and', p, '\n')
  }
}
