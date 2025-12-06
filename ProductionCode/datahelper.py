import csv
import os

def get_player_stats(player_name, data_file='Data/2023_2024.csv'):
    """
    Purpose: Gets the player stats for a specified player
    Arguments: player_name, data_file
    Returns: returns the row that the player statistics is found/none when not found
    """
    if not os.path.exists(data_file):
        return None

    try:
        with open(data_file, 'r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 8 and row[0].lower() == player_name.lower():
                    return {
                        'Player': row[0],
                        'Pos': row[1], 
                        'Tm': row[2],
                        'G': row[3],
                        'TRB': row[4],
                        'AST': row[5], 
                        'PTS': row[6],
                        'Season': row[7]
                    }
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    return None

def get_team_players(team_name, data_file='Data/2023_2024.csv'):
    """
    Purpose: Gets all players for a specified team
    Arguments: team_name, data_file
    Returns: returns all players on the team if it exists, if it does not exist returns an empty list
    """
    if not os.path.exists(data_file):
        return []

    players = []
    try:
        with open(data_file, 'r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 8 and row[2].lower() == team_name.lower():
                    players.append({
                        'Player': row[0],
                        'Pos': row[1], 
                        'Tm': row[2],
                        'G': row[3],
                        'TRB': row[4],
                        'AST': row[5], 
                        'PTS': row[6],
                        'Season': row[7]
                    })
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    return players

def get_top_players(limit=10, data_file='Data/2023_2024.csv'):
    """
    Purpose: Gets top players by points scored
    Arguments: limit, data_file  
    Returns: list of top players sorted by points
    """
    if not os.path.exists(data_file):
        return []

    players = []
    try:
        with open(data_file, 'r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 8:
                    try:
                        points = float(row[6])
                        players.append({
                            'Player': row[0],
                            'Pos': row[1], 
                            'Tm': row[2],
                            'G': row[3],
                            'TRB': row[4],
                            'AST': row[5], 
                            'PTS': row[6],
                            'Season': row[7]
                        })
                    except ValueError:
                        continue
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    # Sort by points (descending) and return top players
    players_sorted = sorted(players, key=lambda x: float(x['PTS']), reverse=True)
    return players_sorted[:limit]

def get_all_players(data_file='Data/2023_2024.csv'):
    """
    Purpose: Gets all players from the data file
    Arguments: data_file  
    Returns: list of all player names
    """
    if not os.path.exists(data_file):
        return []

    players = []
    try:
        with open(data_file, 'r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 8:
                    players.append(row[0])  # Player name is first column
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    # Remove duplicates and sort
    unique_players = sorted(list(set(players)))
    return unique_players