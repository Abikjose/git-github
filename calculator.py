firstnumber = int(input("Enter the first number: "))
secondnumber = int(input("Enter the second number: "))

add = (firstnumber + secondnumber)
substract = (firstnumber - secondnumber)
multiply = (firstnumber * secondnumber)
divide = (firstnumber / secondnumber)

print ("1. Add")
print ("2. Substract")
print ("3. Multiply")
print ("4. Divide")

Answer = int(input("Choose the action you would like to perform and enter the number: "))

if Answer == 1: print('Answer is: ', add)
if Answer == 2: print('Answer is: ', substract)
if Answer == 3: print('Answer is: ', multiply)
if Answer == 4: print('Answer is: ', divide)
