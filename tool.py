import csv

# Create dictionary to store player data
players = {}

# Open CSV file and read contents
with open('PlayerRatings.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip header row
    next(reader)
    # Loop through rows and add data to dictionary
    for row in reader:
        name, team, pos, spd, strn, elu, hnd, rtr, rbk, pbk, tck, prs, rns, pcv, thp, tha, thv, pot = row
        players[name] = {
            'Team': team,
            'Pos': pos,
            'Spd': int(spd),
            'Str': int(strn),
            'Elu': int(elu),
            'Hnd': int(hnd),
            'RtR': int(rtr),
            'RBk': int(rbk),
            'PBk': int(pbk),
            'Tck': int(tck),
            'PRs': int(prs),
            'RnS': int(rns),
            'PCv': int(pcv),
            'ThP': int(thp),
            'ThA': int(tha),
            'ThV': int(thv),
            'Pot': int(pot)
        }

# Function to calculate overall rating for a player
def calculate_overall(player):
    total_weighted = 0
    attributes = ['Spd', 'Str', 'Elu', 'Hnd', 'RtR', 'RBk', 'PBk', 'Tck', 'PRs', 'RnS', 'PCv', 'ThP', 'ThA', 'ThV', 'Pot']
    weights = {'Spd': 2, 'Str': 2, 'Elu': 1, 'Hnd': 1, 'RtR': 1, 'RBk': 1, 'PBk': 1, 'Tck': 3, 'PRs': 1, 'RnS': 1, 'PCv': 1, 'ThP': 2, 'ThA': 2, 'ThV': 2, 'Pot': 4}
    
    for attribute in attributes:
        if attribute != 'Pos':
            total_weighted += int(players[player][attribute]) * weights[attribute]
    
    return total_weighted // sum(weights.values())




# Function to print player's attributes and overall rating
def print_player_stats(player):
    print(f'Player: {player}')
    for attribute in players[player]:
        if attribute != 'Team':
            print(f'{attribute}: {players[player][attribute]}')
    print(f'Overall rating: {calculate_overall(player)}')
    print()

# Test the functions with sample player data
print_player_stats('Conner Emerson')
print_player_stats('Hubie Connor')
print_player_stats('Eric Keeling')
