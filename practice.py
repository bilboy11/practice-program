##name=input('Enter your name')
##print("My name is",name.lower())
##print("My name is",name.title())
##print("My name is",name.upper())


##fn=input('Enter your first name')
##ln=input('Enter your last name')
##print(fn,ln)

###Addition
##sum=int(input('Enter the number'))
##sum2=int(input('Enter the number'))
##sum3=int(input('Enter the number'))
##ans=sum + sum2 + sum3
##print("The result of the calculation is",ans)

###Subtraction
##sum=int(input('Enter the number'))
##sum2int(input('Enter the number'))
##ans=sum - sum2
##print("The result of the calculaton is",ans)
##
###Multiplication
##sum=int(input('Enter the number'))
##sum2=int(input('Enter the number'))
##ans=sum*sum2
##print("The result of the calculation is",ans)
##
###Division
##sum=int(input('Enter the number'))
##sum2=int(input('Enter the number'))
##ans=sum/sum2
##print("The result of the calculation is",ans)
##
###Exponent
##
##sum=int(input('Enter the number'))
##sum2=int(input('Enter the number'))
##ans=sum**sum2
##print("The result of the calculation is",ans)
##
##
##length=float(input("Enter the length"))
##breadth=float(input("Enter the breath"))
##area=length*breadth
##print("The area of the reactangle is",int(area))

##num=int(input("Enter the number"))
##ans=num**2 
##print("The square is",ans)


##fn=input('My name is')
##ln=input('thank you')
##print(fn,ln)
##

##fn=input('Enter first name')
##ln=input('Enter last name')
##mn=input('Enter middle name')
##print(mn,fn,ln)

##n=int(input('Enter the integer'))
##ans=n+(n**2)+(n**3)
##print(ans)

##
##num1=input('Enter the first number')
##num2=input('Enter the second number')
##num3=input('Enter the third number')
##sum=num1+num2+num3
##if(num1==num2==num3):
##    result=3*sum
##else:
##    result=sum
##print("The result is",result)

##num=int(input('Enter number'))
##if(num%2==0):
##    print(num,"is even")
##else:
##    print(num,"is odd")

##print('find the distance between two numbers on the number line')
##n1=int(input('Enter the first number'))
##n2=int(input('Enter the second number'))
##distance=n1-n2
##print('The distance betwwen',n1, 'and',n2,'is',distance,'unit')

      
##name=input('Enter your name')
##age=input('Enter your age')
##print(name + 'is' + age)


##any=input('Enter the first string')
##any2=input('Enter the second string')
##print(any,any2)

##i=1
##while i<=10:
##    print(i)
##    i=i+1

##sum=0
##x=10
##while x>0:
##    sum=sum+x
##    x=x-1
##print(sum)


##birth_year=input("What is your birth year")
##age=2023-int(birth_year)
##print("your age is",age)

##i=0
##while i<5:
##  i += 1
##  if i==3:
##    print("Skipping 3")
##    continue
##  print(i)

##while True:
##    x=input()
##    if x==0:
##        Break

##BMI Calculator
##Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²
##
##The resulting number indicates one of the following categories:
##
##Underweight = less than 18.5
##
##Normal = more or equal to 18.5 and less than 25
##
##Overweight = more or equal to 25 and less than 30
##
##Obesity = 30 or more
##
##Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.
##
##Sample Input
##
##85
##
##1.9
##
##Sample Output
##
##Normal
##
##level
##Weight is in kg, height is in meters. 
##
##Note, that height is a float.
##weight=int(input("Enter your weight"))
##height=float(input("Enter your height"))
##BMI=weight/height**2
##if(BMI<18.5):
##    print("Underweight")
##elif(BMI>=18.5 and BMI<25):
##    print("Normal")
##elif(BMI>=25 and BMI<30):
##    print("Overweight")
##else:
##    print("obesity")


##text=["Love","You","I"]
##print(text[2])
##print(text[0])
##print(text[1])

##m = [
##    [1, 2, 3],
##    [4, 5, 6]
##    ]

##x = [2, 4]
##x += [6, 8]
##print(x[2]//x[0])


##words = ["spam", "egg", "spam", "sausage"]
##print("spam" in words)
##print("egg" in words)
##print("tomato" in words)


##a=int(input('Enter the first number'))
##b=int(input('Enter the second number'))
##c=int(input('Enter the third number'))
##if(a>b and a>c):
##    print(a,'is the largest')
##elif(b>a and b>c):
##    print(b,'is the largest')
##else:
##    print(c,'is the largest')

##a=int(input('Enter the first number'))
##b=int(input('Enter the second number'))
##c=int(input('Enter the third number'))
##if(a<b and a<c):
##    print(a,'is the smallest')
##elif(b<a and b<c):
##    print(b,'is the smallest')
##else:
##    print(c,'is the smallest')    

##year=int(input('Enter your year of birth'))
##if year%4==0:
##         print('Your year of birth is a leap year')
##else:
##    print('Your year of birth is not a leap year')
##
##try:
##    H=input('Enter the hours')
##    R=input('Enter the rate')
##    result=H/R
##except NumericError:
##   print("Error:Please enter numeric input")
##except:
##    print("Error:Please enter numeric error")

##try:
##    hours=int(input('Enter hours'))
##    print(hours)
##    rate=int(input('Enter rate'))
##    print(rate)
##except:
##    print('error,please enter an integer value')


##score=float(input("Enter your score"))
##if score<=1 and score>=0.9:
##    print("Your score is",A)
##elif score<0.9 and score>=0.8:
##    print("Your score is",B)

##num1=int(input('Enter the first number:'))
##num2=int(input('Enter the second number:'))
##if num1<num2:
##    smallest=num1
##    largest=num2
##else:
##    smallest=num2
##    largest=num1
##print('Smallest number:',int(smallest))
##print('largest number:',int(largest))

##len=int(input('Enter first length'))
##wid=int(input('Enter first width'))
##area=len*wid
##len2=int(input('Enter second length'))
##wid2=int(input('Enter second width'))
##area2=len2*wid2
##if area>area2:
##    print('The first rectangle has a greater area')
##elif area2>area:
##    print('The second rectangle has greater area')
##else:
##    print('the two rectangles are eaqual')


##mass=float(input('Enter the mass of the object'))
##weight=mass*9.8
##if weight>1000:
##    print('The weight is too heavy')
##elif weight<10:
##    print('object is too light')
##else:
##    print('object weight is',weight)

##name=input('Enter your name')
##for letter in name:
##    print(letter)

##i=10
##for i in range(10):
##    print(i,"\t",i**2,"\t",i**3)
##
##i=10
##while i<10:
##    print(i,"\t",i**2,"\t",i**3)
##i=i+1

##for i in range(1,13):
##    for j in range(1,13):
##        print(i,"x",j,"=",i*j)
##    print("-------")
##
##scores=(70,56,77,45,65,82,50,61,59,90)
##total=0
##    total=total+score
##average=total/10
##print=("The sum of the scores is",total)
##print=("The average of the scores is",average)
##
##sum=0
##scores=(70,56,77,45,65,82,50,61,59,90)
##for i in range(scores):
##    sum=sum+scores
##average=sum/10


##total=0
##com=5
##i=1
##while i<=5:
##    cost=float(input('enter cost'))
##    total+=cost
##    i+=1
##discount=0.05
##sales=total*(1-discount)
##print('The total sales after a 5% discount is',sales)
##


##def convert(x):
##    return abs(x)
##n=int(input('Enter a negative number'))
##print('The absolute value of',n,'=',convert(n))

##def convert(x):
##    if x<0:
##        return -x
##    else:
##        return x
##x=int(input("Enter a number"))
##print('the absolute value is',convert(x))

  
##def factorial(n):
##    result=1
##    for i in range(1,n+1):
##        result*=i
##    return result
##n=int(input("Enter a number"))
##print('factorial of',n,'is',factorial(n))

##def factorial(n):
##    if(n<=1):
##        return 1 
##    else:
##        return n*factorial(n-1)
##n=int(input('enter a number'))
##print('the factorial is',factorial(n))

##FIBONACCI SERIES
    
##n_terms=int(input('how many terms'))
##n1=0
##n2=1
##count=0
##if n_terms<=0:
##    print('invalid,please enter a positive integer')
##elif n_terms==1:
##    print('fibonacci sequence upto',n_terms,':')
##else:
##    print('fibonacci series upto',n_terms,':')
##    while count<n_terms:
##        print(n1)
##        nth=n1 + n2
##        n1=n2
##        n2=nth
##        count+=1

##def fibonacci(n):
##     if n<=1:
##         return n
##     else:
##         return fibonacci(n-1)+ fibonacci(n-2)
##n=int(input('how many terms'))
##print('fobonacci series is',fibonacci(n))

  
##num=int(input('enter a number'))
##total=sum(num)
##average=total/len(num)
##
##print('the sum is',total)
##print('the average is',average)



##sum=0
##for i in range(10):
##    num=int(input('Enter a number'))
##    sum=sum+num
##average=sum/10
##print('the sum is',sum,'and the average is',average)

##sum=0
##for i in range(10): 
##    num=int(input("number %d= "%i))
##    sum=sum+num
##avg=sum/10
##print('the sum is',sum,'and the average is',avg)
    


##def printinfor(name,age):
##    print('Your name is',name,'and you are',age,'years old')
##    return;
##printinfor(name=input('enter your name'),age=input('enter your age'))


##letters=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
##print("letter are",letters.lower())

##def addtwo(x,y):
##    return x+y
##x=int(input('Enter a number'))
##y=int(input('Enter a number'))
##print('The sum=',addtwo(x,y))

##
##def square(n):
##    return pow(n,2)
##def cube(n):
##    return pow(n,3)
##n=int(input('enter the range of numbers'))
##for i in range(1,n+1):
##    print(1,"\t",square(1),"\t",cube(1))



##i=0
##for i in range(1000):
##    print('I LOVE YOU')
   

##f="Apple"
##for i in range(len(f)):
##    print(i,f[i])
##
##i=0
##f="Apple"
##while i<len(f):
##    print(i,f[i])
##    i=i+1


##name='Aisha Abbas'
##print(name[0:5])
##print(name[6:11])
##print(name[6:])
##print(name[:])
##print(name[-1])
##dir(name)

##name.replace("Aisha","Fatima")
##name
##name.lower()
##name.upper()
##name.find('ba)


##loc=" Abuja "
##print(loc.lstrip())
##print(loc.rstrip())
##print(loc.strip())

##info=('Nigeria is a great nation')
##print(info.startswith("Nigeria"))
##print(info.startswith("N"))
##print(info.startswith("n"))
##print(info.endswith("nation"))



##def read_password(password):
##    if password=="zainab":
##        return 'password Successful'
##    else:
##        return 'password not Successful'
##password=input('Enter the correct password')
##print(read_password(password))


##a=True 
##b=False
##c=False
##if not a or b:
##    print(1)
##elif not a or b and c:
##    print(2)
##elif not a or b or not b and a:
##    print(3)
##else:
##    print(4)
 

##list1=["physics","chemistry","1997","2000"]
##list2=[1,2,3,4,5,6,7]
##print('list1[0]:', list1[0])
##print('list1[0]:', list1[-2])
##print('list1[-2]:', list1[1:])
##print('list2[1:5]:', list2[1:5])




##myfile=open('country.txt','r')
##c=0
##for line in myfile:
##    print(line)
##    c=c+1
##print('The number of line is',c)


##myfile=open('country.txt','r')
##c=0
##for line in myfile:
##    if (line.startswith('Nigeria')):
##        print(line)
##    c=c+1
##print('The number of line is',c)

##myfile=open('country.txt','r')
##c=0
##words=[]
##for line in myfile:
##    for word in line.split():
##        words.append(words)
##    if (line.startswith('Nigeria')):
##        print(line)
##    c=c+1
##print('The number of line is',c)
##print('The total number of words is',len(words))


##myfile=open('country.txt','r')
##for line in myfile:
##    if(line.endswith('Africa.')):
##       print(line)


##READ FILE
##myfile=open('StudentsScores.txt','r')
##for line in myfile:
##    print(line)



#SUM AND AVERAGE
##myfile=open('StudentsScores.txt','r')
##s=0
##c=0
##for score in myfile:
##    s=s+int(score)
##    c=c+1
##average=s/c
##myfile.close()
##myscore=open('Student_result.txt','w')
##myscore.write('The sum of the score=')
##myscore.write(str(s))
##myscore.write('\n')
##myscore.write('The class average=')
##myscore.write(str(average))
##myscore.close()



#APPEND

myfile=open('StudentsScores.txt','r')
s=0
c=0
for score in myfile:
    s=s+int(score)
    c=c+1
average=s/c
myfile.close()
myscore=open('Student_result.txt','w')
myscore.write('The sum of the score=')
myscore.write(str(s))
myscore.write('\n')
myscore.write('The class average=')
myscore.write(str(average))
myscore.close()
myinfo=open('StudentsScores.txt','a')
myinfo.write('\n')
myinfo.write('Above is the list of student score')
myinfo.close()
'''















    


