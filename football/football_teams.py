import random

class Team_Selector:
    def __init__(self):
        pass

    def create_teams(self):
        return {1 : ["Blue", []], 2 : ["Yellow", []]}

    def coin_toss(self):
        first_pick = random.randint(1,2)
        second_pick = 1 if first_pick == 2 else 2
        return (first_pick, second_pick)

    def pick_teams(self, masterlist):
        player_list = masterlist
        teams = self.create_teams()
        order = self.coin_toss()
        while len(player_list) != 0:
            players_left = len(player_list) - 1
            teams[order[0]][1].append(player_list.pop(random.randint(0, players_left)))
            if players_left == 0:
                break
            else:
                players_left -= 1
            teams[order[1]][1].append(player_list.pop(random.randint(0, players_left)))
        team_one = teams[order[0]][0]
        return (teams, team_one)
