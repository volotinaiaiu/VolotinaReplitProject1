def break_point(number):
  num_str = str(number)
  for i in range(1, len(num_str)):
      left_sum = sum(map(int, num_str[:i]))
      right_sum = sum(map(int, num_str[i:]))
      if left_sum == right_sum:
          return True
  return False

print(break_point(159780))
print(break_point(112))
print(break_point(10))
print(break_point(1034))
print(break_point(343))