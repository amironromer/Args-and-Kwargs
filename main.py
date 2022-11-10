# def my_sum(*args):
#   print(args)

# print(my_sum(3,4,5))











# # args for entering as many arguments possible
# def a_sum(*args):
#   for num in args:
#     print(num)

# print(a_sum(1))
# print(a_sum(1,3))
# print(a_sum(1,3,4,5,6))

# list=[3,4,5,6,7,8,9,45,67]
# def sum_num(num1,num2,num3):
#   sum=0
#   for num in list:
#     sum=sum+num
#   return sum
# print(sum(list))

def a_sum(*args):
  # total=0
  # for num in args:
  #   total += num
  # return total
  return sum(args)
print(a_sum(4,56,77,88,9,45,76))
























