label creat_man:
    $ alf = 'йцукенгшщзхъфывапролджэюбьтимсчяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЮБЬТИМСЧЯqwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM'
    $ name = renpy.input('Введите имя пресонажа', length=15, allow=alf).strip()
    
    if name == '':
        $ name = 'Данил'

    # вариации персонажей
    show man1:
        xpos 0.05
        ypos 0.3
    show man2:
        xpos 0.25
        ypos 0.3
    show man3:
        xpos 0.45
        ypos 0.3
    show man4:
        xpos 0.65
        ypos 0.3
    show man5:
        xpos 0.85
        ypos 0.3
    
    menu:
        'Вариант 1':
            $ skin_men_choice = 'images/sprites/man1.png'
        'Вариант 2':
            $ skin_men_choice = 'images/sprites/man2.png'
        'Вариант 3':
            $ skin_men_choice = 'images/sprites/man3.png'
        'Вариант 4':
            $ skin_men_choice = 'images/sprites/man4.png'
        'Вариант 5':
            $ skin_men_choice = 'images/sprites/man5.png'
    
    scene bg

    return

label man_history:

    image skin_man = '[skin_men_choice]'
    show skin_man:
        xpos 0.2
        ypos 0.3

    m "Привет"
    return