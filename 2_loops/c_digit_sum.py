# Create a function that takes in a positive integer and adds each digit together
# Example: 1234 --> 1+2+3+4 = 10
def digit_sum(n):
  string_num = str(n)
  acc = 0
  for i in range(len(string_num)):
    acc += int(string_num[i])
  return acc

print digit_sum(1234)
print digit_sum(123456789)
