
st=input('Enter the line')
def dictionary(st):
    ls=st.split()

    di={}
    for i in range(len(ls)):
        slo=ls[i]
        key1=slo[0].capitalize()
        
        if key1 not in di:
            di[key1]=[]
        di[key1].append(slo)

    di=dict(sorted(di.items(), key=lambda x: x[0]))
    return di

print (dictionary(st))