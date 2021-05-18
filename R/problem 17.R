#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
#3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were
#written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
#23 letters and 115 (one hundred and fifteen)
#contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


number_word <- function(x)
  {
  unit <- c("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
  teens <- c("eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
  tens <- c("ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
  hundreds_up <- c("hundred", "thousand", "million", "billion", "trillion")
  split_up <- as.numeric(unlist(strsplit(as.character(x), "")))
  if(length(split_up) == 1){
    return(unit[split_up])
  } else if( length(split_up) == 2 && x <= 19 ){
    return(teens[split_up[2]])
  } else if (x > 19 && length(split_up)==2 ){
    return(paste0(c(tens[split_up[1]], unit[split_up[2]]), collapse = " "))
  } else if(length(split_up)==3){
       h <- paste(c(unit[1], hundreds_up[1]), sep = "")
       if(split_up[3] == 0){
         
         return(paste(c(h, "and", tens[split_up[2]] ))
                
         
         
         
         
       }
