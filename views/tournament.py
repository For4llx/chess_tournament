def tournament_form():
    print('Nom:')
    name = str(input())

    print('Lieu:')
    place = str(input())

    print('Nombre de tours:')
    rounds_number = int(input())

    while True:
        print('Temps:\n')
        print('1) Bullet')
        print('2) Blitz')
        print('3) Coup rapide')
        time_control = str(input())
        if time_control == '1':
            time_control = 'Bullet'
            break
        elif time_control == '2':
            time_control = 'Blitz'
            break
        elif time_control == '3':
            time_control = 'Coup rapide'
            break
        else:
            print('entrer une option valide (1, 2 ou 3)')

    print('description')
    description = str(input())

    return {
        'name': name,
        'place': place,
        'rounds_number': rounds_number,
        'time_control': time_control,
        'description': description
    }

def menu_tournament(tournaments):
    print('Tournoi:')
    print('Sélectionner un tournoi')
    for tournament in tournaments:
        print(str(tournament.doc_id) + ')' + ' ' + tournament['name'])

    return str(input())
