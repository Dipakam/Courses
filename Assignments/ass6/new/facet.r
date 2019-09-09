df <- read.csv("bias.csv",header=F)
library("ggplot2")
jpeg("bias.jpg",width=1080,height=1080)
ggplot(df,aes(x=V2,y=V3,group=V1))+geom_line(aes(colour=V1))+facet_grid(vars(V1))+geom_bar(aes(fill=V1),stat="identity",colour="white",position=position_dodge2("single"))+geom_point()
dev.off()

