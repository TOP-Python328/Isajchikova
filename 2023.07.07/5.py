mille = float(input('Введите колличество миль :'))
tenths = float(input('Введите колличество десятых : '))
mille_tenths = mille + tenths / 10

km = round(mille_tenths * 1.61)
print(f"{str(mille_tenths)} миль = {str(km)} км ( округление до круглого функцией round )"  )

km_0 = f'{(mille_tenths * 1.61):.2f}'
print(f"{str(mille_tenths)} миль = {str(km_0)} км ( округление до сотых)"  )

km_0 = f'{(mille_tenths * 1.61):.1f}'
print(f"{str(mille_tenths)} миль = {str(km_0)} км ( округление до десятых)"  )

km_0 = f'{(mille_tenths * 1.61):.0f}'
print(f"{str(mille_tenths)} миль = {str(km_0)} км ( округление до круглого f строкой )"  )

