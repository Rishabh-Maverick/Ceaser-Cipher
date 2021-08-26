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
    for i in lst:
        ciphertext += str(i)
    print(ciphertext)
def d(cipher, key):
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
            

                
        
        
