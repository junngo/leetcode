# 1. missing data handling
## check na data
df <- data.frame(gender = c("M", "F", NA, "M", "F"), # make data
                 score = c(5, 4, 3, 4, NA))

is.na(df) # check na data
table(is.na(df$score))
table(is.na(df$gender))

## delete na data
library(dplyr)
df %>% filter(is.na(score))
df_nomiss <- df %>% filter(!is.na(score) & !is.na(gender))
### or
df_nomiss2 <- na.omit(df)

## mean, sum
mean(df$score)
sum(df$score)
### remove na
mean(df$score, na.rm = T)
sum(df$score, na.rm = T)

## simple example
exam <- read.csv("csv_exam.csv") # make data
exam[c(3, 8, 15), "math"] <- NA

exam %>% summarise(mean_math = mean(math))
exam %>% summarise(mean_math = mean(math, na.rm = T))

exam %>% summarise(mean_math = mean(math, na.rm = T),
                   sum_math = sum(math, na.rm = T),
                   median_math = median(math, na.rm = T))

## replace from na data to mean data
mean(exam$math, na.rm=T)
exam$math <- ifelse(is.na(exam$math), 55, exam$math)
table(is.na(exam$math))
mean(exam$math)

# 2. over data handling
outlier <- data.frame(gender = c(1, 2, 1, 3, 2, 1), # 3 data is outlier
                      score = c(5, 4, 3, 4, 2, 6))  # 6 data is outlier
table(outlier$gender)
table(outlier$score)

outlier$gender <- ifelse(outlier$gender == 3, NA, outlier$gender) # replace outlier data
outlier$score <- ifelse(outlier$score > 5, NA, outlier$score)     # replace outlier data

outlier %>% filter(!is.na(gender) & !is.na(score)) %>% 
            group_by(gender) %>%
            summarise(mean_score = mean(score))

boxplot(mpg$hwy)$stats                                            # check data

mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)       # replace outlier data
