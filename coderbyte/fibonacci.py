def Fibonacci(num):
  if num == 1 or num == 2:
    return 1
  
  return Fibonacci(num - 2) + Fibonacci(num - 1)

# keep this function call here 
print(Fibonacci(int(input())))