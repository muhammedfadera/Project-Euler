#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2= 385
T#he square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten
#natural numbers and the square of the sum is 3025 ??? 385 = 2640.
#Find the difference between the sum of the squares of the first one
#hundred natural numbers and the square of the sum.

sum_difference <- function(x){
  integers <- seq(1, x)
  integersquared <- integers^2
  return(abs(sum(integers))^2-sum(integersquared))
}

sum_difference(100)