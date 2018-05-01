# 0. instal package
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
economics <- as.data.frame(ggplot2::economics)

# 1. scatter plot
ggplot(data = mpg, aes(x = displ, y = hwy))
ggplot(data = mpg, aes(x = displ, y = hwy)) + geom_point()
ggplot(data = mpg, aes(x = displ, y = hwy)) + geom_point() + xlim(3, 6)
ggplot(data = mpg, aes(x = displ, y = hwy)) + geom_point() + xlim(3, 6) + ylim(10, 30)


# 2. average bar graph
## 1) average table
df_mpg <- mpg %>%
          group_by(drv) %>%
          summarise(mean_hwy = mean(hwy))

## 2) draw grapth - geom_col
ggplot(data = df_mpg, aes(x = drv, y = mean_hwy)) + geom_col()
ggplot(data = df_mpg, aes(x = reorder(drv, -mean_hwy), y = mean_hwy)) + geom_col()

## 3) draw grapth - geom_bar
ggplot(data = mpg, aes(x = drv)) + geom_bar()

## 4) draw grapth - geom_line
ggplot(data = economics, aes(x = date, y = unemploy)) + geom_line()

## 5) draw grapth - geom_boxplot
ggplot(data = mpg, aes(x = drv, y = hwy)) + geom_boxplot()
