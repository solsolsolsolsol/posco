#import pandas
#import pandas as pd
from pandas import read_excel
df=read_excel('')

from pandas import *

from pandas import Series
s=Series(["hi", "hello", "bye"], ["a","b","c"])
print(s)
print(s[0], s[2])
print(s['a'], s['c'])
indice=[0,2]
print(s.iloc[ indice ])

print(s.iloc[0:2])
print(s.loc["hi":"bye"])

s=Series(data=[100,200,300], index=["a","b","c"])
print(s+10)

print(3==4)


def say(one, two):
    print(one)
    print(two)
    
say("kim", "lee")

def say(one, two="park"):
    print(one)
    print(two)
    
say("kim")

def say(one="kim", two="park"):
    print(one)
    print(two)
    
say("cho")

a=Series(data=[100,200,300], index=["a","b","c"])
cond=a>100
for i in a:
    if i>100:
        print(i)
print(a [ cond ])

from pandas import Series, DataFrame

data=[ 
      [100,200,300]        ,
      [400,500,600]        ,
      [700,800,900]        ,
     ]

df=DataFrame(data, index=["a","b","c"], columns=['d', 'e', 'f'])
print(df)

print(df.loc['a'])
indice=[0,2]
print(df.iloc[indice])

print(df['d'])


row=df.iloc[1]
print(row.iloc[1])
print(row.loc['e'])
print(df.iloc[1].iloc[1])