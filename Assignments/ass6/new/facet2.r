library(ggplot2)

b1 <- read.csv("bias1.txt")
jpeg("bias1.jpg",width=1080,height=1080)
ggplot(b1,aes(x=bias))+geom_line(fill="blue")+facet_wrap(~line)
print(b1)
dev.off()

b2 <- read.csv("bias2.txt")
jpeg("bias2.jpg",width=1080,height=1080)
ggplot(b2,aes(x=bias))+geom_line(fill="red")+facet_wrap(~line)
print(b2)
dev.off()

b3 <- read.csv("bias3.txt")
jpeg("bias3.jpg",width=1080,height=1080)
ggplot(b3,aes(x=bias))+geom_line(fill="green")+facet_wrap(~line)
print(b3)
dev.off()

b4 <- read.csv("bias4.txt")
jpeg("bias4.jpg",width=1080,height=1080)
ggplot(b4,aes(x=bias))+geom_line(fill="yellow")+facet_wrap(~line)
print(b4)
dev.off()

b5 <- read.csv("bias5.txt")
jpeg("bias5.jpg",width=1080,height=1080)
ggplot(b5,aes(x=bias))+geom_line(fill="brown")+facet_wrap(~line)
print(b5)
dev.off()

q()

