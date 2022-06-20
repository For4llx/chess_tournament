def player_form():
    print('Tournoi à 8 joueurs')
    print('Entrer le nom complet des joueur. exemple: Dupont Jean')

    print('Nom:')
    last_name = str(input())
    print('Prénom:')
    first_name = str(input())
    print('Date de naissance:')
    birth_date = str(input())
    print('Sex:')
    sex = str(input())
    print('classement:')
    rank = str(input())

    return {
      'last_name': last_name,
      'first_name': first_name,
      'birth_date': birth_date,
      'sex': sex,
      'rank': rank
    }
