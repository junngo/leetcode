#1. Make var and dataframe
english <- c(90, 80, 50, 75) # englisht var
math <- c(40, 45, 100, 20)   # math var
data.frame(english, math)    # score data frame

#2. use the external data

## excel
library(readxl)                          # load package readxl
df_exam <- read_excel("excel_exam.xlsx") # load excel file (first row is name)
df_exam <- read_excel("excel_exam.xlsx", col_names = F) # load excel file (first row is data)

## csv file
df_csv_exam <- read.csv("csv_exam.csv")                # load csv file
df_midterm <- data.frame(english = c(50, 40, 66, 80),  # make data frame
                         math = c(30, 64, 20, 100),
                         class = c(1, 1, 2, 2))
write.csv(df_midterm, file = "df_midterm.csv")         # save csv file

## Rda file
load("df_midterm.rda")
save(df_midterm, file = "df_midterm.rda")
