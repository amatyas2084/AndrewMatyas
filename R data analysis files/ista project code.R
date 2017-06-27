#Andrew Matyas
#ISTA 370
#12/6/15
#Final Project

final_results <- read.table("group11-experiment-results.csv", header=TRUE, sep=",")
View(final_results)

median(final_results$sleep)
mean(final_results$sleep)

low_sleep<- subset(final_results,sleep < 5)
med_sleep<- subset(final_results,sleep  >= 5 & sleep<=7)
high_sleep<- subset(final_results,sleep >7)

mean(final_results$expected.score)
#77.63
sd(final_results$expected.score)
#16.33
mean(final_results$achieved.score)
#69.27
sd(final_results$achieved.score)
#17.87
length(which(final_results$instructions==1))
length(which(final_results$instructions==2))





low_pre_anx<- subset(final_results,pre.exam.anx <= 19) 
high_pre_anx<- subset(final_results,pre.exam.anx > 19) 

low_post_anx<- subset(final_results,post.exam.anx <= 14) 
high_post_anx<- subset(final_results,post.exam.anx > 14) 



#corralation between achieved score  


cor(final_results$achieved.score, final_results$post.exam.anx)

cor(final_results$achieved.score, final_results$pre.exam.anx)

cor(final_results$achieved.score, final_results$instructions)

# corralation between expected 
cor(final_results$expected.score, final_results$post.exam.anx)

cor(final_results$expected.score, final_results$pre.exam.anx)

cor(final_results$expected.score, final_results$instructions)

#corralation of difference of scores 

cor(final_results$As.Es, final_results$post.exam.anx)

cor(final_results$As.Es, final_results$pre.exam.anx)

cor(final_results$As.Es, final_results$instructions)


# 1 way Anova of achieved

summary(aov(achieved.score~pre.exam.anx,data=final_results))

summary(aov(achieved.score~post.exam.anx,data=final_results)) #significance

summary(aov(achieved.score~instructions,data=final_results))

# 1 way Anova of expected

summary(aov(expected.score~pre.exam.anx,data=final_results))

summary(aov(expected.score~post.exam.anx,data=final_results))

summary(aov(expected.score~instructions,data=final_results))

# 1 way Anova of difference of scores

summary(aov(As.Es~pre.exam.anx,data=final_results))

summary(aov(As.Es~post.exam.anx,data=final_results)) #significance

summary(aov(As.Es~instructions,data=final_results))



#T test

t.test(low_pre_anx$achieved.score,high_pre_anx$achieved.score) #significance
t.test(low_post_anx$achieved.score,high_post_anx$achieved.score) #significance

t.test(low_pre_anx$expected.score,high_pre_anx$expected.score) #significance
t.test(low_post_anx$expected.score,high_post_anx$expected.score)

t.test(low_pre_anx$As.Es,high_pre_anx$As.Es)
t.test(low_post_anx$As.Es,high_post_anx$As.Es)


# corrolations of measured extranious 

#achieved

cor(final_results$achieved.score, final_results$sleep)
cor(final_results$achieved.score, final_results$sleep.avg)
cor(final_results$achieved.score, final_results$S.Sa)
cor(final_results$achieved.score, final_results$exercise)

#expected

cor(final_results$expected.score, final_results$sleep)
cor(final_results$expected.score, final_results$sleep.avg)
cor(final_results$expected.score, final_results$S.Sa)
cor(final_results$expected.score, final_results$exercise)

#As-Es
cor(final_results$As.Es, final_results$sleep)
cor(final_results$As.Es, final_results$sleep.avg)
cor(final_results$As.Es, final_results$S.Sa)
cor(final_results$As.Es, final_results$exercise)


# anova measured extraneous 

summary(aov(achieved.score~sleep*sleep.avg*S.Sa*exercise,data=final_results)) #significant
summary(aov(expected.score~sleep*sleep.avg*S.Sa*exercise,data=final_results)) #significant
summary(aov(As.Es~sleep*sleep.avg*S.Sa*exercise,data=final_results))  #significant


summary(aov(achieved.score~sleep,data=final_results)) #significant
summary(aov(achieved.score~sleep.avg,data=final_results)) #significant
summary(aov(achieved.score~sleep.avg*exercise,data=final_results)) #significant:sleep

summary(aov(expected.score~sleep,data=final_results))
summary(aov(expected.score~sleep.avg,data=final_results)) #significant
summary(aov(expected.score~sleep*sleep.avg,data=final_results)) #significant:sleep.avg
summary(aov(expected.score~sleep*exercise,data=final_results))
summary(aov(expected.score~sleep.avg*exercise,data=final_results))
summary(aov(expected.score~sleep*sleep.avg*S.Sa,data=final_results)) #significant:sleep.avg

summary(aov(As.Es~sleep,data=final_results))  #significant
summary(aov(As.Es~sleep*exercise,data=final_results)) #significant: sleep,sleep&exercise

#T test for sleep

t.test(low_sleep$achieved.score,med_sleep$achieved.score)
t.test(low_sleep$achieved.score,high_sleep$achieved.score)
t.test(med_sleep$achieved.score,high_sleep$achieved.score)

t.test(low_sleep$expected.score,med_sleep$expected.score)
t.test(low_sleep$expected.score,high_sleep$expected.score)
t.test(med_sleep$expected.score,high_sleep$expected.score)

t.test(low_sleep$As.Es,med_sleep$As.Es)
t.test(low_sleep$As.Es,high_sleep$As.Es) #significant difference
t.test(med_sleep$As.Es,high_sleep$As.Es)


boxplot(
  achieved.score~Post.high.low,
  data=final_results,
  main="achieved on math exam based on post exam anxiety",
  xlab="anxiety level",
  ylab="achived score",
  names=c("low","high")
)
