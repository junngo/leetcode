# 0. import lib and data
library(dplyr)
exam <- read.csv("csv_exam.csv")

# 1. conditioned data extraction
exam %>% filter(english >= 80)
exam %>% filter(class == 1 & math >= 50)
exam %>% filter(math >= 90 | english >= 90)
exam %>% filter(class %in% c(1, 3, 5))

# 2. needed var data extraction
exam %>% select(math)
exam %>% select(-math)
exam %>% select(class, math, english)
exam %>% select(id, math) %>% head(10)

# 3. arrange data
exam %>% arrange(math)
exam %>% arrange(desc(math))
exam %>% arrange(class, math)

# 4. add temp var
exam %>% mutate(total = math + english + science)
exam %>% mutate(total = math + english + science,
                mean = (math + english + science)/3)
exam %>% mutate(test = ifelse(science >= 60, "pass", "fail"))
exam %>% mutate(total = math + english + science) %>% arrange(total)

# 5. summary group by
exam %>% group_by(class) %>% summarise(mean_math = mean(math))
mpg %>% group_by(manufacturer, drv) %>% summarise(mean_cty = mean(cty))

# 6. data connect
## create data
test1 <- data.frame(id = c(1, 2, 3, 4, 5),
                    midterm = c(60, 80, 70, 90, 85))
test2 <- data.frame(id = c(1, 2, 3, 4, 5),
                    final = c(70, 83, 65, 95, 89))

group_a <- data.frame(id = c(1, 2, 3, 4, 5),
                      test = c(60, 80, 70, 90, 85))
group_b <- data.frame(id = c(6, 7, 8, 9, 10),
                      test = c(55, 89, 45, 36, 66))

## join data
total <- left_join(test1, test2, by="id")
group_all <- bind_rows(group_a, group_b)
