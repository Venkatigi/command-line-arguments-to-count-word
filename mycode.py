## Name          : Venkatesh E
## Reference No  : 21003352
import sys
f1=open(sys.argv[1])
data=f1.read()
word=data.split()
print("The word count is",len(word))
f1.close()