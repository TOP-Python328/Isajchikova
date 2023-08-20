number = int(input('Введите трехзначное число : '))
number_1 = number//100
number_2 = (number - number_1*100)//10
number_3 = number%10
summa = number_1 + number_2 + number_3
product = number_1 * number_2 * number_3
# вывод переменных  использовала  для самоконтроля  
# print(number_1)
# print(number_2)
# print(number_3)

print(f"Сумма цифр = {str(summa)}")
print(f"Произведение цифр = {str(product)}")
