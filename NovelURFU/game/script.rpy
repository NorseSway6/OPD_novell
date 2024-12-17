define m = Character('[name]', color='#fafafa')
define n = Character(None, kind=nvl)
define h = Character('Herceg', color='#fafafa')
define d = Character('Дмитрий', color='#fafafa')
define k = Character('King', color='#fafafa')
define di = Character('Диана', color='#fafafa')
define ki = Character('Кирилл', color='#fafafa')
define e = Character('Екатерина', color='#fafafa')
define a = Character('Алина', color='#fafafa')
define o = Character('Олег', color='#fafafa')
define t = Character('Команда', color='#fafafa')
define memory1 = False
define memory2 = False
$ skin = ''
$ gender = 0

init python:
    ### Эта функция изменяет слово/окончание слова в зависимости от выбранного игроком пола
    def Morpher(word): 
        pronouns = {'он':'она','его':'ее', 'ним':'ней', 'ему':'ей', 'нему':'ней', 'него':'нее'}
        if gender==0:
            return word

        if word in pronouns.keys():
            return pronouns.get(word)
        if word[-2:]=='ся':
            return word[:-2] + 'ась'
        if 'шел' in word:
            return word[:-2] + 'ла'
        if 'мог' in word:
            return word + 'ла'
        return word + 'а'

init:
    $ main_character = Position(xalign = 0.2)
    $ secondary_character = Position(xalign = 0.85)
    $ center = Position(xalign = 0.5)

transform come_skin:
    xpos 200 ypos 180
    linear 0.4 xpos 200 ypos 160
    linear 0.4 xpos 220 ypos 180
    linear 0.4 xpos 240 ypos 160
    linear 0.4 xpos 260 ypos 180
    linear 0.4 xpos 280 ypos 160
    linear 0.4 xpos 300 ypos 180

transform come_team:
    xpos 840 ypos 180
    linear 0.4 xpos 840 ypos 160
    linear 0.4 xpos 820 ypos 180
    linear 0.4 xpos 800 ypos 160
    linear 0.4 xpos 780 ypos 180
    linear 0.4 xpos 760 ypos 160
    linear 0.4 xpos 740 ypos 180


label start:

    $ variants = [1, 2, 3, 4, 5, 6, 7]
    scene choice character
    with fade

    menu:
        'Какого персонажа ты выберешь?'

        'Женщина':
            $ gender = 1
            call creat_character
        'Мужчина':
            $ gender = 0
            call creat_character
    
    call screen choice_character
    
    image skin = '[skin]'

    return