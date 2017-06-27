# Andrew Matyas
# ISTA 370
# Group 11
# Experiment Results - Data Analysis
# Date

high_post_anx<

experiment_results <- read.table("group11-experiment-results.csv", header=TRUE, sep=",")
View(experiment_results)

median_pre_exam_anx <- median(experiment_results$pre.exam.anx)
median_post_exam_anx <- median(experiment_results$post.exam.anx)

#Independent Variables
cor(experiment_results$achieved.score, experiment_results$instructions)
cor(experiment_results$achieved.score, experiment_results$pre.exam.anx)
cor(experiment_results$achieved.score, experiment_results$post.exam.anx)

cor(experiment_results$expected.score, experiment_results$instructions)
cor(experiment_results$expected.score, experiment_results$pre.exam.anx)
cor(experiment_results$expected.score, experiment_results$post.exam.anx)

cor(experiment_results$As.Es, experiment_results$instructions)
cor(experiment_results$As.Es, experiment_results$pre.exam.anx)
cor(experiment_results$As.Es, experiment_results$post.exam.anx)

summary(aov(achieved.score~instructions*pre.exam.anx*post.exam.anx, data=experiment_results)) #All 3 independent variables

summary(aov(achieved.score~pre.exam.anx*post.exam.anx, data=experiment_results)) #Pre & Post against As
summary(aov(achieved.score~instructions*pre.exam.anx, data=experiment_results)) #Instructions & Pre against As
summary(aov(achieved.score~instructions*post.exam.anx, data=experiment_results)) #Instructions & Post against As

summary(aov(expected.score~instructions*pre.exam.anx*post.exam.anx, data=experiment_results)) #All 3 independent variables

summary(aov(expected.score~pre.exam.anx*post.exam.anx, data=experiment_results)) #Pre & Post against Es
summary(aov(expected.score~instructions*pre.exam.anx, data=experiment_results)) #Instructions & Pre against Es
summary(aov(expected.score~instructions*post.exam.anx, data=experiment_results)) #Instructions & Post against Es

summary(aov(As.Es~instructions*pre.exam.anx*post.exam.anx, data=experiment_results)) #All 3 independent variables

summary(aov(As.Es~pre.exam.anx*post.exam.anx, data=experiment_results)) #Pre & Post against As-Es
summary(aov(As.Es~instructions*pre.exam.anx, data=experiment_results)) #Instructions & Pre against As-Es
summary(aov(As.Es~instructions*post.exam.anx, data=experiment_results)) #Instructions & Post against As-Es

low_pre_anx <- subset(experiment_results, pre.exam.anx <= median_pre_exam_anx) 
high_pre_anx <- subset(experiment_results, pre.exam.anx > median_pre_exam_anx) 

low_post_anx <- subset(experiment_results, post.exam.anx <= median_post_exam_anx) 
high_post_anx <- subset(experiment_results, post.exam.anx > median_post_exam_anx) 

t.test(low_pre_anx$achieved.score,high_pre_anx$achieved.score)
t.test(low_pre_anx$expected.score,high_pre_anx$expected.score)
t.test(low_pre_anx$As.Es,high_pre_anx$As.Es)

t.test(low_post_anx$achieved.score,high_post_anx$achieved.score)
t.test(low_post_anx$expected.score,high_post_anx$expected.score)
t.test(low_post_anx$As.Es,high_post_anx$As.Es)

#Measured Extraneous Variables
cor(experiment_results$achieved.score, experiment_results$age)
cor(experiment_results$achieved.score, experiment_results$gender)
cor(experiment_results$achieved.score, experiment_results$class.rank)

cor(experiment_results$expected.score, experiment_results$age)
cor(experiment_results$expected.score, experiment_results$gender)
cor(experiment_results$expected.score, experiment_results$class.rank)

cor(experiment_results$As.Es, experiment_results$age)
cor(experiment_results$As.Es, experiment_results$gender)
cor(experiment_results$As.Es, experiment_results$class.rank)

summary(aov(achieved.score~age*gender*class.rank, data=experiment_results)) #All 3 independent variables

summary(aov(achieved.score~age*gender, data=experiment_results)) #Age & Gender against As
summary(aov(achieved.score~age*class.rank, data=experiment_results)) #Age & Class Rank against As
summary(aov(achieved.score~gender*class.rank, data=experiment_results)) #Gender & Class Rank against As

summary(aov(expected.score~age*gender*class.rank, data=experiment_results)) #All 3 independent variables

summary(aov(expected.score~age*gender, data=experiment_results)) #Age & Gender against As
summary(aov(expected.score~age*class.rank, data=experiment_results)) #Age & Class Rank against As
summary(aov(expected.score~gender*class.rank, data=experiment_results)) #Gender & Class Rank against As

summary(aov(As.Es~age*gender*class.rank, data=experiment_results)) #All 3 independent variables

summary(aov(As.Es~age*gender, data=experiment_results)) #Age & Gender against As-Es
summary(aov(As.Es~age*class.rank, data=experiment_results)) #Age & Class Rank against As-Es
summary(aov(As.Es~gender*class.rank, data=experiment_results)) #Gender & Class Rank against As-Es

summary(aov(As.Es~class.rank, data=experiment_results)) #Class Rank against As-Es

low_pre_anx <- subset(experiment_results, pre.exam.anx <= median_pre_exam_anx) 
high_pre_anx <- subset(experiment_results, pre.exam.anx > median_pre_exam_anx) 

low_post_anx <- subset(experiment_results, post.exam.anx <= median_post_exam_anx) 
high_post_anx <- subset(experiment_results, post.exam.anx > median_post_exam_anx) 

males <- subset(experiment_results,gender==1) # Males = 1
females <- subset(experiment_results, gender==2) # Females = 2

frosh_soph <- subset(experiment_results,class.rank<=2)
jun_sen <- subset(experiment_results,class.rank>2)

t.test(males$achieved.score,females$achieved.score)
t.test(males$expected.score,females$expected.score)
t.test(males$As.Es,females$As.Es)

t.test(frosh_soph$achieved.score,jun_sen$achieved.score)
t.test(frosh_soph$expected.score,jun_sen$expected.score)
t.test(frosh_soph$As.Es,jun_sen$As.Es)


# Mary's Tests:
cor(experiment_results$achieved.score, experiment_results$test.anx)
cor(experiment_results$achieved.score, experiment_results$expected.score)
cor(experiment_results$expected.score, experiment_results$test.anx)
cor(experiment_results$As.Es, experiment_results$test.anx)

summary(aov(achieved.score~test.anx*expected.score, data=experiment_results)) #Test Anxiety & Es against As
summary(aov(expected.score~test.anx*achieved.score, data=experiment_results)) #Test Anxiety & As against Es
summary(aov(As.Es~test.anx, data=experiment_results)) #Test Anxiety against
summary(aov(As.Es~class.rank, data=experiment_results)) #Class Rank against As-Es
summary(aov(achieved.score~test.anx, data=experiment_results))
summary(aov(achieved.score~expected.score, data=experiment_results))
summary(aov(expected.score~achieved.score, data=experiment_results))


median_test_anx <- median(experiment_results$test.anx)
low_test_anx <- subset(experiment_results, test.anx <= median_test_anx) 
high_test_anx <- subset(experiment_results, test.anx > median_test_anx) 

t.test(low_test_anx$achieved.score,high_test_anx$achieved.score)
t.test(low_test_anx$expected.score,high_test_anx$expected.score)
t.test(low_test_anx$As.Es,high_test_anx$As.Es)


max(experiment_results$age)
min(experiment_results$age)
