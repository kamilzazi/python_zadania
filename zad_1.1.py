# ziemniaki_kg = float(input('Ile kosztuje kilogram ziemniaków? '))
# waga = 5
# print(f'Za {waga} kg ziemniaków trzeba zapłacić {ziemniaki_kg * waga} zł.')
#
# ziemniaki_kg = float(input('Ile kosztuje kilogram ziemniaków? '))
# ile_kg = float(input('Ile kilogramów ziemniaków chcesz kupić? '))
# print(f'Za {ile_kg} kg ziemniaków będziesz musiał zapłacić {ziemniaki_kg * ile_kg} zł')

ziemniaki_cena = float(input('Ile kosztuje kg ziemniaków? '))
ziemniaki_waga = float(input('Ile kg ziemniaków chcesz kupić? '))
banany_cena = float(input('Ile kosztuje kg bananów? '))
banany_waga = float(input('Ile kg bananów chcesz kupić? '))

print(f'Za ziemniaki i banany trzeba zapłacić {ziemniaki_cena * ziemniaki_waga + banany_cena * banany_waga} zł')
if ziemniaki_cena * ziemniaki_waga > banany_cena * banany_waga:
    print('Za ziemniaki trzeba zapłacić wiecej.')
elif ziemniaki_cena * ziemniaki_waga == banany_cena * banany_waga:
    print('Za ziemniaki i banany trzeba zapłacić taką samą kwotę.')
else:
    print('Za banany trzeba zapłacić więcej. ')