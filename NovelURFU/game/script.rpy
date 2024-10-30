define w = Character('[name]', color='#fafafa')
define m = Character('[name]', color='#fafafa')
$ skin_women_choice = ''
$ skin_men_choice = ''
$ gender = 0

label gender_choce:
    
    menu:
        'Какого персонажа ты выберешь?'

        'Женщина':
            $ gender = 1
            jump creat_woman
        'Мужчина':
            $ gender = 0
            jump creat_man

label start:

    scene choice character

    call gender_choce

    scene choice character

    if gender == 0:
        call screen choice_men_character
        return

    if gender == 1:
        call screen choice_woman_character
        return
    
    return