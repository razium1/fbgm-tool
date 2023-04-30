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
# Function to calculate overall rating for a player based on position
def calculate_overall(player):
    total_weighted = 0
    pos_weights = {
        'QB': {'ThP': 3, 'ThA': 3, 'ThV': 3, 'PCv': 2, 'Pot': 4},
        'RB': {'Spd': 3, 'Str': 3, 'Elu': 3, 'Hnd': 2, 'Pot': 4},
        'WR': {'Spd': 3, 'RtR': 3, 'Hnd': 3, 'Elu': 2, 'Pot': 4},
        'TE': {'Spd': 2, 'Str': 3, 'Hnd': 3, 'RtR': 2, 'PBk': 1, 'RBk': 1, 'Pot': 4},
        'OL': {'Str': 3, 'RBk': 3, 'PBk': 3, 'Pot': 4},
        'DL': {'Str': 3, 'Tck': 3, 'Elu': 2, 'Pot': 4},
        'LB': {'Tck': 3, 'Spd': 2, 'Str': 2, 'Elu': 2, 'Pot': 4},
        'CB': {'Spd': 3, 'RtR': 3, 'Tck': 2, 'Pot': 4},
        'S': {'Spd': 3, 'Tck': 3, 'PRs': 2, 'Pot': 4},
        'K': {'ThP': 2, 'KAc': 3, 'KAa': 3, 'Pot': 4},
        'P': {'KAc': 2, 'KAa': 2, 'KAb': 2, 'Pot': 4}
    }
    
    for attribute, weight in pos_weights[players[player]['Pos']].items():
        total_weighted += int(players[player][attribute]) * weight
    
    return total_weighted // sum(pos_weights[players[player]['Pos']].values())





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
