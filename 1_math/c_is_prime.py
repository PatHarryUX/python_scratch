# Create a function that takes in an integer x,
# And determines if it is a prime number
# Prime number --> True  ;  Non-prime number --> False
def is_prime(x):
  for i in range(x-1, 1, -1):
    if x % i == 0:
      return False
  else:
    return True

print is_prime(1) # Should return --> True
print is_prime(4) # Should return --> False
print is_prime(5) # Should return --> True
print is_prime(23) # Should return --> True
print is_prime(40) # Should return --> False
print is_prime(41) # Should return --> True
