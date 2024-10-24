label creat_woman:
    $ alf = 'йцукенгшщзхъфывапролджэюбьтимсчяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЮБЬТИМСЧЯqwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM'
    $ name = renpy.input('Введите имя пресонажа', length=15, allow=alf).strip()
    
    if name == '':
        $ name = 'Анна'

    # вариации персонажей
    show woman1:
        xpos 0.05
        ypos 0.3
    show woman2:
        xpos 0.25
        ypos 0.3
    show woman3:
        xpos 0.45
        ypos 0.3
    show woman4:
        xpos 0.65
        ypos 0.3
    show woman5:
        xpos 0.85
        ypos 0.3
    
    menu:
        'Вариант 1':
            $ skin_women_choice = 'images/sprites/woman1.png'
        'Вариант 2':
            $ skin_women_choice = 'images/sprites/woman2.png'
        'Вариант 3':
            $ skin_women_choice = 'images/sprites/woman3.png'
        'Вариант 4':
            $ skin_women_choice = 'images/sprites/woman4.png'
        'Вариант 5':
            $ skin_women_choice = 'images/sprites/woman5.png'
    
    scene bg

    return

label woman_history:

    image skin_woman = '[skin_women_choice]'
    show skin_woman:
        xpos 0.2
        ypos 0.3

    w "Привет"
    return