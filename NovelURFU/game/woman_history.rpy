label creat_woman:
    $ alf = 'йцукенгшщзхъфывапролджэюбьтимсчяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЮБЬТИМСЧЯqwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM'
    $ name = renpy.input('Введите имя пресонажа', length=15, allow=alf).strip()
    
    if name == '':
        $ name = 'Анна'
    
    return

label woman_history:

    image skin_woman = '[skin_women_choice]'
    show skin_woman:
        xpos 0.2
        ypos 0.3

    w "Привет"

    return