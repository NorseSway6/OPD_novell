label creat_man:
    $ alf = 'йцукенгшщзхъфывапролджэюбьтимсчяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЮБЬТИМСЧЯqwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM'
    $ name = renpy.input('Введите имя пресонажа', length=15, allow=alf).strip()
    
    if name == '':
        $ name = 'Данил'

    return

label man_history:
    
    image skin_man = '[skin_men_choice]'
    show skin_man:
        xpos 0.2
        ypos 0.3

    m "Привет"
    
    return