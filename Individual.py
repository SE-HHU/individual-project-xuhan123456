import os
import random
import os
n=int(input('请输入需要的题目个数：'))
fh=['+','-']
i=0
lst1=[]
os.remove('Exercises.txt')
os.remove('Answer.txt')
while i<n:
    fhnumber = random.randint(1, 2)
    if(fhnumber==1):
        chosen1 = random.choice(fh)
        number1 = random.randint(0,100)
        number2 = random.randint(0,100)
        suanshu1=f"{number1}{chosen1}{number2}"
        if suanshu1 not in lst1:
            if(chosen1=='+'):
                result=number1+number2
            if (chosen1 == '-'):
                result = number1 - number2
            if(result<0 or result>=100):
                continue
            else:
                lst1.append(suanshu1)
                fp1=open('Exercises.txt','a+')
                fp2 = open('Answer.txt', 'a+')
                fp1.write(f"{suanshu1}\n")
                fp2.write(f"{str(result)}\n")
                i+=1
        else:
            continue
    else:
        chosen1 = random.choice(fh)
        chosen2 = random.choice(fh)
        number1 = random.randint(0,100)
        number2 = random.randint(0,100)
        number3 = random.randint(0,100)
        suanshu1 = f"{number1}{chosen1}{number2}{chosen2}{number3}"
        if suanshu1 not in lst1:
            if (chosen1 == '+' and chosen2=='+'):
                result = number1 + number2 + number3
            if (chosen1 == '+' and chosen2 == '-'):
                result = number1 + number2 - number3
            if (chosen1 == '-' and chosen2 == '+'):
                result = number1 - number2 + number3
            if (chosen1 == '-' and chosen2=='-'):
                result = number1 - number2 - number3
            if (result<0 or result>=100):
                continue
            else:
                lst1.append(suanshu1)
                fp1 = open('Exercises.txt', 'a+')
                fp2 = open('Answer.txt', 'a+')
                fp1.write(f"{suanshu1}\n")
                fp2.write(f"{str(result)}\n")
                i+=1
        else:
            continue
