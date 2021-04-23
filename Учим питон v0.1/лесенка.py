def ladder():
  a = int(input())
  choose = input("1, 2, 3, 4: \n")
  if choose == "1":
    for i in range(0, a + 1):
      print(" " * (a - i) + "*" * i)

  elif choose == "2":    
    for i in range(0, a + 1):
        print("*" * i + " " * (a - i))
        
  elif choose == "3":    
    for i in range(0, a + 1):
      print("*" * (a - i) + " " * (a - i)) 
            
  elif choose == "4":    
    for i in range(0, a + 1):
      print(" " * a + "*" * (a - i)) 

ladder()
