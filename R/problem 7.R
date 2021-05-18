#By listing the first six prime numbers:
#2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?



is_prime <- function(x){
  
  if( any(x == c(2, 3, 5, 7, 11, 13))) return(TRUE)
  if(x <= 1 || x%%2 == 0 || x%%3 == 0 || any(x%%10==c(5, 10)) || any(x%%c(7, 11, 13)==0
                                                                     ) ) return(FALSE)
  
  l <- floor(sqrt(x))
  k <- seq(3, l, 2)
  for(i in k){
    if(x%%i == 0) return(FALSE)
    
  }
  return(TRUE)
  
}

nth_prime <- function(n){
  if(n==1) return(2)
  m <- (n + 1)%/%2
  k <- 2*(1:m) - 1
  p <- which(unlist(purrr::map(k, is_prime)))
  d <- p[length(p)]
  while (length(p) < n ) {
    d <- d + 2
    if(is_prime(d)){
      p <- append(p, d)
    }
  }
  return(d)
}

