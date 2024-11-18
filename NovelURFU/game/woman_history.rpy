label creat_woman:
    $ alf = 'йцукенгшщзхъфывапролджэюбьтимсчяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЮБЬТИМСЧЯqwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM'
    $ name = renpy.input('Введите имя пресонажа', length=15, allow=alf).strip()
    
    if name == '':
        $ name = 'Анна'
    
    return

label woman_history:

    image skin_woman = '[skin_women_choice]'
    show skin_woman at main_character
    with dissolve

    m "Привет, реализация данного выбора в процессе. Выберете игру за мужского персонажа"

    return