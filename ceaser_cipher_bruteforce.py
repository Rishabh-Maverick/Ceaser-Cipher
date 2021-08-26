from ceaser_cipher import d

def b():
    dict1 = {}
    cipher = input("Enter the text to brute force: ")
    for i in range(0,50):
        dict1 = {}
        if len(cipher) > 20:
            value = d(cipher[:20], i)
            dict1[value] = i
            print(dict1,"\n")
        else:
            a = cipher[:int(((len(cipher))/2))]
            value = d(a, i)
            dict1[value] = i
            print(dict1,"\n")
    key = int(input("ENTER THE NUMBER NEXT TO TEXT PRINTED ABOVE WHICH IS READABLE: "))
    print("THE CRACKED CODE IS: ", d(cipher,key))
    
    
        
        
