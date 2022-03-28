#First task:Write an R program to create three vectors a, b, c with 5 integers. Combine the three vectors to become a 3×5 matrix where each column represents a vector. Print the content of the matrix. Plot a graph and label correctly.
a=c(21,12,19,15,11)
b=c(3,7,5,9,2)
c=c(55,33,66,44,22)
d=c(a,b,c)
print(d)
M=matrix(d,nrow=3)
print(M)
M1=matrix(d,ncol=5)
print(M1)
plot(a,b,type ="o")


#second task:Write a R program to create a Data frames which contain details of 5 employees and display the details. (Name, Age, Role and Length of service).
Name <- c("Peter", "Marry", "Anna", "Sam", "Neil")
Age <- c(18,20,22,39,19)
Role <- c("Trainee1", "Jr Data Scientist", "Tester", "Manager", "Trainee2")
LOS <- c(1,3,2,17,2)

df <- data.frame(Name, Age, Role, LOS)

print (df)

#fourth task:Create a simple bar plot of five subjects

marks<-c(89,78,80,94,99)
students<-c("Millie","Dan","Aamina","Kavya","Neha")
barplot(marks)
barplot(marks,xlab="Student names",ylab="Marks obtained",main="Exam Results",names.arg=students,col="yellow")
