#Rcode
library(RColorBrewer)
mycol <- brewer.pal(4,'Accent')
a1 <- read.table('../analysis2/cor_ent_res.txt',header=1)
a1[,3] <- log10(a1[,3]+0.001)
png('../figures/cor_ent_res.png',res=600,height=3000,width=3000)
plot(a1[,3],a1[,4],pch=16,col=mycol[1],ylim=c(-1,0.5),ylab='relative resistance',xlab='log10 Shannon entropy',xaxt='n',yaxt='n')
axis(side=1,at=c(-3,-2,-1,0,1),lwd=2)
axis(side=2,at=c(-1.0,-0.5,0,0.5),lwd=2)
box(lwd=2)
x <- a1[,3]
y <- a1[,4]
#fit <- lm(y ~ log(x))
fit <- lm(y ~ x)
lines(seq(from=-3,to=1,length.out=1000),predict(fit,newdata=list(x=seq(from=-3,to=1,length.out=1000))),lwd=4,lty=2)
#lines(seq(from=0,to=3,length.out=1000),predict(fit,newdata=list(x=seq(from=0,to=3,length.out=1000))),lwd=4,lty=2)
dev.off()
