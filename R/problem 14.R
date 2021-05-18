#The following iterative sequence is defined for the set of positive integers:
#n ??? n/2 (n is even)
#n ??? 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 ??? 40 ??? 20 ??? 10 ??? 5 ??? 16 ??? 8 ??? 4 ??? 2 ??? 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million

collatz <- function(r){
  count = 0
    repeat{
    if(r==1){
      count=count+1
      break
      return(count)
    } else if(r%%2==0){
      r = r/2
      count = count +1
      next
    }else r = 3*r+1
    count = count+1
    next
   }
  return(count)
}


#Generating collatz squence for any given number
collatzseq <- function(s){
  k = s
  l = collatz(s)
  seq_collatz = numeric(collatz(s)-1)
  repeat{
    if(s==1){
      break
      seq_collatz[l-collatz(s)] <- s
      return(seq_collatz)
    } else if(s%%2==0){
      s = s/2
      seq_collatz[l-collatz(s)] <- s
      next
    }else s = 3*s+1
    seq_collatz[l-collatz(s)] <- s
    next
  }
  return(c(k, seq_collatz))
}

maxcollatz <- function(n){
  x = 1:n
  return(which.max(vapply(x, collatz, 0)))
}
t = Sys.time()
(maxcollatz(1e6))
Sys.time()-t
#ANSWER=837799











