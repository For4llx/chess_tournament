def player_form():
    players_full_name = []
    print('Tournoi à 8 joueurs')
    print('Entrer le nom complet des joueur. exemple: Dupont Jean')

    for i in range(8):
        print('Entrer le nom complet du joueur:')
        players_full_name.append(str(input()))

    return players_full_name
