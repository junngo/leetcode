# 1.ready data and package
mpg <- as.data.frame(ggplot2::mpg)
library(dplyr)
library(ggplot2)

# 2. check data
head(mpg)    # check head data
tail(mpg)    # check tail data
View(mpg)    # view data
dim(mpg)     # check dimension
str(mpg)
summary(mpg) # data summary

# 3. rename name of col
mpg <- rename(mpg, company=manufacturer)  # change col name manufacturer -> company

# 4. make new col
mpg$total <- (mpg$cty + mpg$hwy) / 2                # make new col
mpg$test <- ifelse(mpg$total >= 20, "pass", "fail") # make new col that get condition

# 5. check frequency
table(mpg$test) # print mpg$test
qplot(mpg$test) # make graph
