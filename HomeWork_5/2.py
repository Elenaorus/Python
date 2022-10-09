import string

with open('file_encode.txt', 'r') as data:
    for st in data:
        st=st.translate({ord(c): None for c in string.whitespace})
        
        count=1
        res=''
        for i in range(len(st)-1):
            if   i<(len(st)-1) and st[i] ==st[i+1]:
                count+=1        
                
            else:
                
                res+=str(count)+st[i]
                
                count=1
            if i==(len(st)-1):
                res+=str(count)+st[i] 
            if i==(len(st)-2):
                res+=str(count)+st[i+1] 
                 
        print(res)
        
        


    


