df <- read.csv("./avengers.csv",header = F)
library("ggplot2")
ggplot(df,aes(x=V1,y=V2,color=V3)) + geom_point(position="jitter")
