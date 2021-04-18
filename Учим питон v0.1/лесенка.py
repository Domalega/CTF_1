def ladder():
    a = int(input())
    choose = input("влево или вправо: \n")
    if choose == "влево":
        for i in range(0, a + 1):
            print(" " * (a - i) + "*" * i)

    elif choose == "вправо":    
        for i in range(0, a + 1):
            print("*" * i + " " * (a - i)) 

ladder()