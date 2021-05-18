#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
require(numbers)
sum_powers <- function(x=2, p=2){
  d = as.bigz(x^p)
  sum(as.numeric(unlist(strsplit(as.character(d), split = ''))))
}

sum_powers(x=2,p=1000)
