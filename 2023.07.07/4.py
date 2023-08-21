# ИСПОЛЬЗОВАТЬ везде: оформление кода согласно PEP 8 — в качестве образца можно использовать код из репозитория _scripts

number = int(input('Введите трехзначное число : '))
# ПЕРЕИМЕНОВАТЬ: цифра числа — digit
number_1 = number // 100
# number_2 = (number - number_1 * 100) // 10
# ИСПОЛЬЗОВАТЬ: можно проще
number_2 = number // 10 % 10
number_3 = number % 10

# УДАЛИТЬ: эти переменные используются каждая только единожды: с учётом простоты вычисляемых выражений, объявление данных переменных избыточно
summa = number_1 + number_2 + number_3
product = number_1 * number_2 * number_3

# УДАЛИТЬ: я ни в коем случае не против, но в дальнейшем проверочный код лучше удалять из финального варианта, иначе в не столь отдалённой перспективе количество закомментированного кода рискует превысить количество основного рабочего =)
# вывод переменных  использовала  для самоконтроля
# print(number_1)
# print(number_2)
# print(number_3)
# КОММЕНТАРИЙ: если хотите показать мне какой-либо свой промежуточный код, то оформите его отдельным коммитом, поверх которого отправьте финальный, и напишите комментарий, чтобы я посмотрел не только финальную версию, но и промежуточные

# ИСПРАВИТЬ: явное использование функции str() в f-строках избыточно
print(f"Сумма цифр = {str(summa)}")
# ИСПРАВИТЬ: лучше бы справиться за один вызов функции print()
print(f"Произведение цифр = {str(product)}")


# ДОБАВИТЬ: результат выполнения программы с собственными данными


# ИТОГ: хорошо, но можно лучше — 2/4
