#Andrew Matyas
#25 October 2015



sex_lies<- read.table("sex_lies.txt", header=TRUE, sep="")
View(sex_lies)



-------Q1-------
aov.scale.lies <- aov(count~scale*lies,data=sex_lies)
summary(aov.scale.lies)

print(model.tables(aov.scale.lies,"means"),digits=3)

# After running a two way Anova on the propensity to lie among different scales
# of permissiveness irrespective of gender I found that there is no effect of 
# scale (F(1,60)=0,p=.98) or lies(F(1,60)=0.04,p=.85) on the count. There is
# also no interaction effect (p-values>.05)

--------Q2-------
aov.scale.sex <- aov(count~scale*sex,data=sex_lies)
summary(aov.scale.sex)

print(model.tables(aov.scale.sex,"means"),digits=3)


# After running a two way Anova on the scale and sex's effect on count   
# irrespective of gender I found that there is a significant effect based on
# sex (F(1,60)=4.52,p=.04) showing that the counts of high permissiveness(M=30.2) 
# and low permissiveness(M=41.0) are significantly different.There was no effect of
# scale(F(1,60)=0.2,p=.98) on the count and there is no interaction effect 
# (p-values>.05).

------Q3-------
aov_gender_scale_religion <- aov(count~gender*scale*religion,data=sex_lies)
summary(aov_gender_scale_religion)

print(model.tables(aov_gender_scale_religion,"means"),digits=3)

# After running a three way Anova I noticed that there are two significant effects
# and that is the effect of gender along with the interaction between gender and
# religion. According to these results there was a significant effect of 
# gender (F(1,56)=7.16, p=.01) showing the count of males(M=29.2) 
# and females(M=42) are significantly different. There was no effect of
# scale or religion on the counts. There was an interaction effect between
# gender:religion (F(1,56)=6.88,p=.01) this means that less religious males(M=37.8),
# higher religious males(M=20.6),lower religious females(M=38.1), and higher 
# religious females(M=45.9) have significantly different counts, but no 
# interaction effects between gender:scale, scale:religion, and Gender,scale,
# religion (p-values> .05)

  
  
  