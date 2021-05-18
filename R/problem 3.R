#A palindromic number reads the same both ways. The largest palindrome made from the product of two 
#2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

t=Sys.time()
palindrome <- function(x){
    p <- unlist(strsplit(as.character(x), split=''))
    z = paste(rev(p), collapse="")
  ifelse(z==x ,return(TRUE), return( FALSE ) )
}

v_palindrome <- Vectorize(palindrome)
multiply.each <- function(l){
  x <- apply( combn(l, 2), 2, prod)
  return(x)
}
maxpalprod <- function(x){
  m = multiply.each(x)
  #maxpalprod=rep(FALSE, length(m))
  prods <- which(v_palindrome(m)) + x[1] - 1
  r_prods <- sort(prods, TRUE)
  for(i in r_prods){
    if( palindrome(i) ) break
  }
      cat('The maximum palindromic product of two', nchar(i), 'digits numbers is', i)
  
}

