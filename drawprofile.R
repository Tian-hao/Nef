#Rcode
library(RColorBrewer)
mycol <- brewer.pal(8,'Accent')
b1 <- read.table('../analysis2/fitness_residue.txt',header=1)

drawpic <- function(name,colu){
png(paste('../figures/Fitness_profile_',name,'.png',sep=''),res=600,height=2500,width=4500)
plot(b1$Pos,b1[,colu],type='h',lwd=4,col=mycol[1],ylab='log10 fitness',ylim=c(-0.7,0.5),xaxt='n',yaxt='n')
box(lwd=4)
axis(1,at=c(0,20,40,60,80),lwd=4)
axis(2,at=c(-0.5,0,0.5),lwd=4)
dev.off()
}

drawpic('SL9',2)
drawpic('SL9No',3)
drawpic('KF11',4)
drawpic('KF11No',5)
