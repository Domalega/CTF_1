def foo():
  a = int(input())
  b = int(input())
  for i in range(1, a + 1):
    for j in range(1, b + 1):
      if i == 1 or i == a:
        print("@", end = " ")
      else:
        print("@" + " " * (a + 1) + "@", end = " ")
        break
    print("\n")

foo()
