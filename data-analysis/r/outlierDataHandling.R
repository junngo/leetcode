# 1. missing data handling
table(is.na(df$score))

df_nomiss <- df %>% filter(!is.na(score))

df_nomiss <- df %>% filter(!is.na(score) & is.na(gender))

mean(df$score, na.rm = T)
exam %>% summarise(mean_math = mean(math, na.rm = T))

# 2. over data handling
table(outlier$gender)
outlier$gender <- ifelse(outlier$gender == 3, NA, outlier$gender)
boxplot(mpg$hwy)$stats
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)
