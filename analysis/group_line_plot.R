cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()
library(ggplot2)


#### IF YOU WANT TO KEEP THE LINE PLOTS::: REMEMBER TO REMOVE 0000

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3_cdat/CASKDATA.csv"
# THE_LIMIT   <- 65
# THE_DS_NAME <- "CASKDATA"

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3_expr/EXPRESS42.csv"
# THE_LIMIT   <- 75
# THE_DS_NAME <- "EXPRESS42"

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3_berg/BLOOMBERG.csv"
# THE_LIMIT   <- 30
# THE_DS_NAME <- "BLOOMBERG"

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3_moz/MOZILLA.csv"
# THE_LIMIT   <- 110
# THE_DS_NAME <- "MOZILLA"

# THE_FILE   <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3_ost/OPENSTACK.csv"
# THE_LIMIT  <- 100
# THE_DS_NAME <- "OPENSTACK"

# THE_FILE   <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3_wik/WIKIMEDIA.csv"
# THE_LIMIT  <- 300
# THE_DS_NAME <- "WIKIMEDIA"


# Y_LABEL     <- "Count of Smells per File"
Y_LABEL     <- "Smell Density (KLOC)"
#SMELL_DENSITY  ,  CNT_PER_FIL

LINE_DATA <- read.csv(THE_FILE)
the_plot  <- ggplot(data=LINE_DATA, aes(x=MONTH, y=SMELL_DENSITY, group=1)) + 
  geom_point(size=0.1) + scale_x_discrete(breaks = LINE_DATA$MONTH[seq(1, length(LINE_DATA$MONTH), by = THE_LIMIT)]) + 
  geom_smooth(size=0.95, aes(color=TYPE), method='loess') +   
  facet_grid( . ~ TYPE) +
  labs(x='Month', y=Y_LABEL) +
  theme(legend.position="none") +
  ggtitle(THE_DS_NAME) + theme(plot.title = element_text(hjust = 0.5)) +
  theme(text = element_text(size=12.5), axis.text.x = element_text(angle=45, hjust=1, size=12.5), axis.text.y = element_text(size=15), axis.title=element_text(size=12.5, face="bold"))  



the_plot
t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))