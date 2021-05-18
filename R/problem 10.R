#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.



require(primes)

primebelowmillion <- generate_primes(min=0, max=2e6)
sum(as.numeric(primebelowmillion))