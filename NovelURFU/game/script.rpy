define anna = Character('Анна', color='#FF0000')
define danil = Character('Данил', color='#FF0000')
 
label  character_choce():
    menu:
        'Какого персонажа ты выберешь?'
        'Anna':
            jump anna_history
        'Danil':
            jump danil_history

label start:
    call character_choce 
    return