#Rcode
library(RColorBrewer)
mycol <- brewer.pal(4,'Accent')
a1 <- read.table('../analysis2/cor_ddg_res.txt',header=1)
png('../figures/cor_ddg_res.png',res=600,height=3600,width=3600)
plot(a1$ddg,a1$resistance,pch=16,col=mycol[1],xlab='ddg',ylab='resistance',xlim=c(-10,10))
dev.off()
