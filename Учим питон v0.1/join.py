def foo(l, s):
  for i in range(0, len(l) - 1):
    if i < len(l) - 2:
      print(l[i], end = s)
  else:
    print(l[i])

l = [str(i) for i in input().split()]
s = input()
foo(l,s)
