import constants

PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS


def clean_data(data):
    cleaned = []
    for user in data:
        fixed = {}
        fixed["name"] = user["name"]
        fixed["guardians"] = user["guardians"]
        if user["experience"] == 'YES':
            fixed["experience"] = True
        elif user["experience"] == 'NO':
            fixed["experience"] = False
        fixed["height"] = int(user["height"].split(" ")[0])
        cleaned.append(fixed)
    return cleaned


def divide_players(players, teams):
    players_per_team = int(round(len(players) / len(teams)))
    list_teams = {team: [] for team in teams}
    remain_players = players[:]
    
    for team in teams:
        players_needed = min(players_per_team, len(remain_players))
        players_to_join = remain_players[:players_needed]
        list_teams[team].extend(players_to_join)
        remain_players = remain_players[players_needed:]
        
    return list_teams


def main_app():
    PLAYERS_CLEAN = clean_data(PLAYERS)
    list_teams = divide_players(PLAYERS_CLEAN,TEAMS)
    teams_name = {key.lower(): value for key, value in list_teams.items()}
    print("*---------------*Welcome*---------------*")
    
    while True:
        for team, player in list_teams.items():
            print("Team: ", team)
        user_choose = input("\nWhich team do you want to see: ")
        if user_choose.lower() in teams_name:
            print("\nTeam: ",user_choose.capitalize())
            print("Team members: ")
            for player in teams_name[user_choose.lower()]:
                print("\t",player['name'])
            print("\nIf you want to exit, press X")
            print("\n------------------------")
        elif user_choose.lower() == "x":
            break
        else:
            print("Invalid team name. Please choose again!")
main_app()
