define w = Character('[name]', color='#FF0000')
define m = Character('[name]', color='#FF0000')

label  gender_choce():
    menu:
        'Какого персонажа ты выберешь?'
        'Женщина':
            jump creat_woman
        'Мужчина':
            jump creat_man

label start:

    call gender_choce
    if w:
        call woman_history()
    if m:
        call man_history()
    return