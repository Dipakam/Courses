df <- read.csv("gprof.csv")
library("ggplot2")
jpeg("gprof.jpg",width=1080,height=1080)
ggplot(df,aes(x=func,y=time))+geom_bar(stat="identity",fill=c("red","greeen","blue")) #need to change this for unknown number of colours
#scale_fill_grey()+theme_clasic() is not giving proper shades
dev.off()
q()
