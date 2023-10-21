#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

summultiples <-function(x){
      i <- 2:(x-1)
      m <- i[i%%2==0|i%%5==0]
        return(sum(m))
}
summultiples(1000)


# i <- 2:1000
# m <- i[i%%3==0|i%%5==0]
# sum(m)
