#print("Hello World!")
#print(2**10)
def nl(a):
    i=0
    for i in range(a):
        print('\n')

class fruit:
    color='red'
    def taste(self):
        return 'delicious'

apple=fruit()
print(apple.color)
print(apple.taste())

'''
print('나이: ')

while(1):
    try:
        age=int(input())
    except:
        continue

    break
'''

'''
test='grape'
test2=type(test)

if(str(test2)=="<class 'str'>"):
    print('string')
elif(str(test2)=="<class 'int'>"):
    print('integer')
'''

'''
cnt=0

while(1):
    print('Hello ...')
    #cnt=cnt+1
    cnt+=1
    if(cnt==10):
        break
'''

'''
test='hello python'
hello='hello world'
#check=input()
'''

'''
print('age: ')
age=int(input())

if(age<20):
    print('미성년자')
else:
    print('성년')
'''

'''
print('Agroup: ')
Agroup=['kim','lee']
print(Agroup)
nl(1)

Agroup.append('park')
print('APPEND OUTCOME: ')
print(Agroup)
nl(3)

Agroup.remove('lee')
print('REMOVE OUTCOME: ')
print(Agroup)
nl(1)
'''

#print(hello)
#print(char)
#if(check==10):
#    print('correct')
#else:
#    print('false ...')
#test=test.upper()
#print(test)
