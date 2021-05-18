
for (i in 2:10) {
  a = (2:(i-1))
  b = as.matrix(i%%a)
  c = colSums(b != 0)
  if (c == i-2)
  {
    print(i)
  }
}

allPrime <- function(n) {
  primes <- rep(TRUE, n)
  primes[1] <- FALSE
  for (i in 1:sqrt(n)) {
    if (primes[i]) primes[seq(i^2, n, i)] <- FALSE
  }
  which(primes)
}


#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
for(i in allPrime(floor(sqrt(600851475143)))){
  factor <- rep(NA, i)
  if(600851475143%%i==0){
    factor[i] <- i
  }
}

allnumbers <- c(1:600851475143/2)

factors <- function(m){
factor <- c()
for(i in in c(2:m)){
  if(m%%i!=0){
    next
  }else 
    factor[i]<-i
}  
}

factors <- allnumbers[c()]
sieve <- function(x, y=c()){
  y <-y[c(y%%x!=0&y>x)]
  return(y)
}


sieve(2, c(5:500))
replicate(sieve(x=2, y=(2:130)), 5)
primes <- function(n=c()){
  p <- c(2:n)
  m <-p*n 
  for(i in 2:m[m<n]){
   prime <- sieve(i, y=c(1:n))
  }
  return(prime)
}

primes(20)

sieve(x=c(2,3),y=c(1:100))
rem.multiples(20)
allPrime(1e7)
