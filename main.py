def my_sum(*args):
  print(args)

print(my_sum(3,4,5))











# args for entering as many arguments possible
def a_sum(*args):
  for num in args:
    print(num)

print(a_sum(1))
print(a_sum(1,3))
print(a_sum(1,3,4,5,6))











