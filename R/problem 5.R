#2520 is the smallest number that can be divided by 
#each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
t <- Sys.time()
#x <- 2520
#while(all(x%%2:20==0)==FALSE){
#  x <- x+1
#  next
#}
#x
#Sys.time()-t
v_prime_factors <- Vectorize(prime_factors)
m <- unique(unlist(v_prime_factors(2:10)))
                          