label creat_woman:
    $ alf = 'йцукенгшщзхъфывапролджэюбьтимсчяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЮБЬТИМСЧЯqwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM'
    $ name = renpy.input('Введите имя пресонажа', length=15, allow=alf).strip()
    
    if name == '':
        $ name = 'Анна'

    # вариации персонажей
    show w1:
        xpos 0.2

    menu:
        'Вариант 1':
            $ skin_women_choice = 'images/sprites/w1.png'
    
    scene bg
    return

label woman_history:

    image skin_woman = '[skin_women_choice]'
    show skin_woman 

    w 'Привет'
    return