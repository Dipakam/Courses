library("ggplot2")
df <- read.csv("bias.txt")
jpeg("facet.jpg",width=1080,height=1080)
ggplot(df,aes(x=bias))+geom_density()+facet_wrap(~line)
dev.off()
q()

