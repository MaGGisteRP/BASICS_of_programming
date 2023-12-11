import pymorphy3

morph = pymorphy3.MorphAnalyzer()
name = input('ваше имя : ')
nname = morph.parse(name)[0].inflect({'datv'}).word.title()
drink = input(f'{nname} нужен здоровый сон. В каких местах ты бывал во сне? ')
ndrink = morph.parse(drink)[0].inflect({'nomn'}).word.title()
ope = input(f'{ndrink} обычно мне только сниться. Как вы опишите это место? ')
nope = morph.parse(ope)[0].inflect({'plur'}).word.title()
print(f'ИИ такие же {nope}')