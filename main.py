def linear_probing(no,pos):
    while(hashtable[pos]!=0):
        pos+=1
    return pos
no_of_ele=0GG
size=int(input("Enter size of table"))
hashtable=list(0 for i in range(size))
while 1:
    print("Enter NO:")
    no=int(input())
    pos=no%size
    if(hashtable[pos])==0:
        hashtable[pos]=no
        no_of_ele+=1
    else:
        pos=linear_probing(no,pos)
        hashtable[pos]=no
    print("More no,s???")
    chr=int(input("1 for continue 0 for exit"))
    if(chr==0):
        break
    print(hashtable)
    
    