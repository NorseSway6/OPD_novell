define m = Character('[name]', color='#fafafa')
# define w = Character('[name]', color='#fafafa')
define n = Character(None, kind=nvl)
define h = Character('Herceg', color='#fafafa')
define memory1 = False
define memory2 = False
$ skin_women_choice = ''
$ skin_men_choice = ''
$ gender = 0

### Запихать мужской и женский скин просто в скин, в скринах тупо в две функции объеденить в одну. Либо в выборах персонажей через иф чекая гендер. 
### Поиграться с окончаниями, что бы для женищины не делать отдельную историю.

init:
    $ main_character = Position(xalign = 0.2, yalign = 0.8)
    $ secondary_character = Position(xalign = 0.85, yalign = 0.8)

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
    with fade

    call gender_choce from _call_gender_choce

    if gender == 0:
        call screen choice_men_character
        return

    if gender == 1:
        call screen choice_woman_character
        return
    
    return