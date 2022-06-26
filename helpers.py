def get_rank(player):
  return player.get('ranking')

def get_score(player):
  return player.get('score')

def generate_paire():
    matches = []

    players_number = len(players)
    middle_index = players_number // 2
    upper_class_players = players[:middle_index]
    lower_class_players = players[middle_index:]

    for i in range(middle_index):
        match = [[upper_class_players[i], {'score': 0}] ,[lower_class_players[i], {'score': 0}]]
        matches.append(match)
