def round_form(round):
    results = []
    for match in round['matches']:
        full_name_player_1 = match[0][0]['last_name'] + ' ' + match[0][0]['first_name']
        full_name_player_2 = match[1][0]['last_name'] + ' ' + match[1][0]['first_name']

        print('Sélectionner le résultat du match:')
        print(f'1) {full_name_player_1}')
        print(f'2) {full_name_player_2}')
        print('3) Égalité')

        results.append(str(input()))
        
    return results

