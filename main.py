def fac(no):
  if no == 0:
    return 1
  else:
    return no * fac(no - 1)


print(fac(8))
