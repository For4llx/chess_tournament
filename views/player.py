def player_form():
    print('Ajouter un joueur:\n')

    print('Nom:')
    last_name = str(input())
    print('Prénom:')
    first_name = str(input())
    print('Date de naissance:')
    birth_date = str(input())
    print('Sex:')
    sex = str(input())
    print('Classement:')
    ranking = str(input())

    return {
      'last_name': last_name,
      'first_name': first_name,
      'birth_date': birth_date,
      'sex': sex,
      'ranking': ranking
    }
