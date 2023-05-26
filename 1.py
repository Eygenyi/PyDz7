l=('АОУЫЭЕЁИЮЯ')
f=input().upper().split()
def countInList(l,f):
    lst=[]
    for i in f:
        count=0   
        for j in i:
            if j in l:
                count+=1
        lst.append(count)
    print(lst)
    return(lst)
if len(set(countInList(l,f)))==1:
    print('парам-парам-пампам')
else: print('пара-рам')