
# Define a function factorial that takes an integer x as input,
# And calculates the factorial of that number
def factorial(x):
  f = 1
  for i in range(x, 0, -1):
    f = f * i
  return f



print factorial(4) #Should return 24
print factorial(1) #Should return 1
print factorial(3) #Should return 6
