print('Hello. This is a calculator for averaging.')
total = 0
count = 0
user_input = input('Please enter a number here :(When all numeric inputs are complete, enter q to terminate the program.).')
while user_input != 'q' :
   num = float(user_input)
   total += num
   count += 1
   user_input = input('Please enter a number here :(When all numeric inputs are complete, enter q to terminate the program.).')
if count == 0:
    result = 0
else:
    result = total / count
result = total / count
print('The average of the numbers you enter is ' + str(result))
# 写出数字求平均值
