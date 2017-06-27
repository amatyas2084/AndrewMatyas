#Andrew Matyas
#25 October 2015


sex_lies<- read.table("sex_lies.txt", header=TRUE, sep="")
View(sex_lies)

Males <- subset(sex_lies, gender==2)
  
Females <- subset(sex_lies, gender==1)


#-------Q1-------


# Independant variables:  Gender, scale, sex, lies, religion

# Dependant: count

# The count variable is dependant on the gender, scale, sex, lies, and religion
# to be explained.


#-------Q2-------

mean(Males$count)
mean(Females$count)

sd(Males$count)
sd(Females$count)

# The males mean and stadard deviation (M=29.19, SD=15.95) are both lower 
# than the mean and standard deviation of the females (M=42, SD=23.04).

#-------Q3-------

aov.lies.males <- aov(count~lies,data=Males)
summary(aov.lies.males)

print(model.tables(aov.lies.males,"means"),digits=3)

aov.lies.females <- aov(count~lies,data=Females)
summary(aov.lies.females)

print(model.tables(aov.lies.females,"means"),digits=3)

boxplot(
  count~lies, 
  data=Males,
  main="males propensity to lie",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)

boxplot(
  count~lies, 
  data=Females,
  main="females propensity to lie",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)


# I conducted a one way ANOVA on the males and female groups seperately, with 
# count being the dependant and propensity to lie being the independant. 
# The propensity to lie for males(F(1, 30) = 0.78, p=0.38) and 
# females(F(1,30) = 0.12, p = 0.71) showed no significant difference. 
# Females show that they have a higher mean of high propensity liers(M=40.5) along with
# a higher mean of low propensity liers (M=43.5) compared to mens high propensity 
# liers (M=31.7) and low propensity liers(M=26.7).


#-------Q4-------

Ritualistic <- subset(sex_lies, scale==1)
Experimental<- subset(sex_lies, scale==2)
Ideological<- subset(sex_lies, scale==3)
Composite <- subset(sex_lies, scale==4)
#Ritualistic
aov.lies.Ritualistic <- aov(count~lies,data=Ritualistic)
summary(aov.lies.Ritualistic)

print(model.tables(aov.lies.Ritualistic,"means"),digits=3)

boxplot(
  count~lies, 
  data=Ritualistic,
  main="propensity to lie amongst Ritualistic",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)
#Experimental
aov.lies.Experimental <- aov(count~lies,data=Experimental)
summary(aov.lies.Experimental)

print(model.tables(aov.lies.Experimental,"means"),digits=3)

boxplot(
  count~lies, 
  data=Experimental,
  main="propensity to lie amongst Experimental",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)


#Ideological
aov.lies.Ideological <- aov(count~lies,data=Ideological)
summary(aov.lies.Ideological)

print(model.tables(aov.lies.Ideological,"means"),digits=3)

boxplot(
  count~lies, 
  data=Ideological,
  main="propensity to lie amongst Ideological",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)


#Composite
aov.lies.Composite <- aov(count~lies,data=Composite)
summary(aov.lies.Composite)

print(model.tables(aov.lies.Composite,"means"),digits=3)

boxplot(
  count~lies, 
  data=Composite,
  main="propensity to lie amongst Composite",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)


# I conducted a one way ANOVA on the Ritualistic, Experimental, Ideological,
# and Composite scales seperately, with count being the dependant variable and propensity
# to lie being the independant variable. The propensity to lie for Ritualistic(F(1, 14) = 0.01, p=0.93),
# Experimental(F(1,14) = 0.01, p = 0.91), Ideological(F(1,14) = .00, p = .95),
# Composite(F(1,14) = 0.01, p = .92) showed no significant difference. 
# All of the different scales had very similar means when it came to the high and low
# propensity for lying. Ritualistic mean for high (M= 36) and low (M=35) 
# compared to Experimentals high (M=36) and low(M=34.9), Ideological high (M=36.4)
# low (M=35.5), along with Composite high (M=36) and low (M=35). The means were all 
# very close together and showed no significant difference. 

#-------Q5--------

#Ritualistic
aov.sex.Ritualistic <- aov(count~sex,data=Ritualistic)
summary(aov.sex.Ritualistic)

print(model.tables(aov.sex.Ritualistic,"means"),digits=3)

boxplot(
  count~sex, 
  data=Ritualistic,
  main="premarital permissiveness amongst Ritualistic",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)
#Experimental
aov.sex.Experimental <- aov(count~sex,data=Experimental)
summary(aov.sex.Experimental)

print(model.tables(aov.sex.Experimental,"means"),digits=3)

boxplot(
  count~sex, 
  data=Experimental,
  main="premarital permissiveness amongst Experimental",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)


#Ideological
aov.sex.Ideological <- aov(count~sex,data=Ideological)
summary(aov.sex.Ideological)

print(model.tables(aov.sex.Ideological,"means"),digits=3)

boxplot(
  count~sex, 
  data=Ideological,
  main="premarital permissiveness amongst Ideological",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)


#Composite
aov.sex.Composite <- aov(count~sex,data=Composite)
summary(aov.sex.Composite)

print(model.tables(aov.sex.Composite,"means"),digits=3)

boxplot(
  count~sex, 
  data=Composite,
  main="premarital permissiveness amongst Composite",
  xlab= "propensity to lie 2=high 1=low",
  ylab= "count"
)


# I conducted a one way ANOVA on the Ritualistic, Experimental, Ideological,
# and Composite scales seperately, with count being the dependant variable and propensity
# to sex being the independant variable. The propensity to lie for Ritualistic(F(1, 14) = 1.15, p=0.30),
# Experimental(F(1,14) = 1.3, p = 0.27), Ideological(F(1,14) = .76, p = .40),
# Composite(F(1,14) = 1.25, p = .28) showed no significant difference. 
# All of the different scales had very similar means when it came to the high and low
# propensity for lying. Ritualistic mean for high (M=30.1) and low (M=40.9) 
# compared to Experimentals high (M=30.1) and low(M=40.8), Ideological high (M=30.4)
# low (M=41.5), along with Composite high (M=30) and low (M=41). The means were all 
# very close together and showed no significant difference.

#-------Q6-------
Ritualistic_males <- subset(Males, scale==1)
Experimental_males <- subset(Males, scale==2)
Ideological_males <- subset(Males, scale==3)
Composite_males <- subset(Males, scale==4)

Ritualistic_females <- subset(Females, scale==1)
Experimental_females <- subset(Females, scale==2)
Ideological_females <- subset(Females, scale==3)
Composite_females <- subset(Females, scale==4)

boxplot(
  count~scale, 
  data= Males,
  main="premarital permissiveness amongst Males",
  xlab= "premarital sexual permissiveness",
  ylab= "count",
  names= c("Ritualistic", "Experimental", "Ideological", "Composite")
)

boxplot(
  count~scale, 
  data= Females,
  main="premarital permissiveness amongst Females",
  xlab= "premarital sexual permissiveness",
  ylab= "count",
  names= c("Ritualistic", "Experimental", "Ideological", "Composite")
)


mean(Ritualistic_males$count)
mean(Experimental_males$count)
mean(Ideological_males$count)
mean(Composite_males$count)

sd(Ritualistic_males$count)
sd(Experimental_males$count)
sd(Ideological_males$count)
sd(Composite_males$count)

mean(Ritualistic_females$count)
mean(Experimental_females$count)
mean(Ideological_females$count)
mean(Composite_females$count)

sd(Ritualistic_females$count)
sd(Experimental_females$count)
sd(Ideological_females$count)
sd(Composite_females$count)

# In comparing the female box plot graph the medians seem to be very similir 
# and close together except for the Ideological box plot wich seems to have a 
# median that looks a bit lower than the other box plots. As for the males 
# box plot all of the medians are pretty close together. The distribution of
# Ritualistoic box on the males graph is the largest stretching from approximatly
# 4 to around 58. The means of the scale for males were all very similar. The
# Ritualistic Males (M=29.13, SD=19.97), Experimental Males(M=29, SD=16.43), 
# and Composite Males(M=29, SD=17.5) had slightly higher standard deviations than
# Ideological Males(M=29.63, SD=12.27). 
# The means of the scale for females were all very similar. The
# Ritualistic Females (M=41.88, SD=19.49), Experimental Females(M=41.88, SD=19.93), 
# and Composite Females(M=42, SD=21) had much lower standard deviations than
# Ideological Females(M=42.25, SD=33.66).


