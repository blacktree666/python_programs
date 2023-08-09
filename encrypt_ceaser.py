def encrypt(alp,key,name):
    n=[]
    enc=[]
    for char in name:
        if char!=" ":
            ind=alp.index(char)
        else:
            ind=-1
        n.append(ind)
    for i in range(len(name)):
        a=(key+n[i])%26 
        enc.append(a) 
    for i in enc:
        if alp[i]=="c":
            alp[i]=" "
        print(alp[i],end="")
alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key=3 
data=str(input("Enter text to encrypt:"))
print("Encrypted data is:")
encrypt(alp,key,data)


