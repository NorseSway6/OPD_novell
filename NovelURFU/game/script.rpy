﻿define w = Character('[name]', color='#fafafa')
define m = Character('[name]', color='#fafafa')
$ skin_women_choice = ''

init:
    $ a = Position(xpos=0.1)

label gender_choce:
    
    menu:
        'Какого персонажа ты выберешь?'

        'Женщина':
            jump creat_woman
        'Мужчина':
            jump creat_man

label start:

    call gender_choce

    if w:
        call woman_history
        return

    if m:
        call man_history
        return
    
    return