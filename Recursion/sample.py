


def func(i):
  
  print(i)
  if( i > 3):
    return "Done"

  j = i+1
  return func(j)


print(func(0))
