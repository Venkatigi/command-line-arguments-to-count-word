# command-line-arguments-to-count-word
## AIM:
To write a python program for getting the word count from the contents of a file using command line arguments.
## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7
## ALGORITHM: 
### Step 1:

### Step 2: 
 
### Step 3: 

### Step 4:  

### Step 5: 

### Step 6: 

## PROGRAM:
~~~
## Name          : Venkatesh E
## Reference No  : 21003352
import sys
f1=open(sys.argv[1])
data=f1.read()
word=data.split()
print("The word count is",len(word))
f1.close()
~~~

### OUTPUT:
Code:
![code](1.jpg)
Text file:
![text](3.jpg)
Output:
![output](2.jpg)
## RESULT:
Thus the program is written to find the word count from the contents of a file using command line arguments.
