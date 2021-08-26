import random
def e():
    str1 = input("Enter text to encrypt using ceaser: ")
    key = int(input("Enter the key to encrypt the data with: "))
    str1 = str1.lower()
    lst = list(str1)
    dict1 = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(lst)):
        f = lst[i]
        if lst[i] not in dict1:
            continue
        else:
            if dict1.index(f)<= int(25 - key):
                lst[i] = dict1[dict1.index(f)+ key]
            else:
                lst[i] = dict1[25-int(dict1.index(f))]
                
    ciphertext = ""
    key = str(key)
    for i in lst:
        ciphertext += str(i)
    print(ciphertext)
    key_limit = [1,2,3,4,5,6,7,8,9]
    mult_enc = int(input("Encrypt multiple times to increase protection. Enter the number of times to encrypt: "))
    for i in range(mult_enc):
        a = random.choice(key_limit)
        ciphertext = me(ciphertext, a)
        key += str(a)
    print(ciphertext, key)
        
        

def me(str1,key):
    str1 = str1.lower()
    lst = list(str1)
    dict1 = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(lst)):
        f = lst[i]
        if lst[i] not in dict1:
            continue
        else:
            if dict1.index(f)<= int(25 - key):
                lst[i] = dict1[dict1.index(f)+ key]
            else:
                lst[i] = dict1[25-int(dict1.index(f))]
                
    ciphertext = ""
    for i in lst:
        ciphertext += str(i)
    return ciphertext

def md(cipher, key):
    key = int(key)
    cipher = cipher.lower()
    lst = list(cipher)
    dict1 = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(lst)):
        f = lst[i]
        if lst[i] not in dict1:
            continue
        else:
            if dict1.index(f) >= key:
                lst[i] = dict1[dict1.index(f)-key]
            else:
                lst[i] = dict1[25 - int(dict1.index(f))]
    plain = ""
    for i in lst:
        plain += str(i)
    return plain
    
    
    
def d(cipher, key):
    plain_text = ""
    mult = input("Is it multiple encryption? (Y/N): ")
    if mult.lower() == "y":
        for i in key[::-1]:
            cipher = md(cipher, i)
        print(cipher,i)
    else:
        
        
                    
        cipher = cipher.lower()
        lst = list(cipher)
        dict1 = list("abcdefghijklmnopqrstuvwxyz")
        for i in range(len(lst)):
            f = lst[i]
            if lst[i] not in dict1:
                continue
            else:
                if dict1.index(f) >= key:
                    lst[i] = dict1[dict1.index(f)-key]
                else:
                    lst[i] = dict1[25 - int(dict1.index(f))]
        plain = ""
        for i in lst:
            plain += str(i)
        return plain
            

                
        
        
