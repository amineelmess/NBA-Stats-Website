import argparse
from ProductionCode.datasource import DataSource

def print_usage():
    """
    Prints out usage statement for the command line interface.
    Shows available commands and examples for looking up player statistics
    and team rosters.
    """
    print("NBA Player Statistics Lookup")
    print("Usage: python3 command_line.py --stat PLAYER_NAME")
    print("python3 command_line.py --player TEAM_NAME")
    print("Example: python3 command_line.py --stat \"LeBron James\"")
    print("Example: python3 command_line.py --player \"LAL\"")

def main():
    """
    Purpose: Main entry point for the command line interface for looking up NBA player statistics.
    Args: None (uses command line arguments via argparse)
    Returns: None
    """
    db = DataSource()

    parser = argparse.ArgumentParser(description="Look up NBA player statistics")
    parser.add_argument('--stat', metavar='PLAYER', help='Player name to look up statistics for')
    parser.add_argument('--player', metavar='TEAM', help='Team name to look up players for')

    args = parser.parse_args()

    if not args.stat and not args.player:
        print_usage()
        return

    if args.stat:
        player_data = db.get_player_stats_db(args.stat)

        if player_data and len(player_data) > 0:
            player = player_data[0]
            print(f"Statistics for {player[0]}:")
            print(f"Position: {player[1]}")
            print(f"Team: {player[2]}")
            print(f"Games: {player[3]}")
            print(f"Points: {player[4]}")
            print(f"Assists: {player[5]}")
            print(f"Rebounds: {player[6]}")
        else:
            print(f"Player '{args.stat}' not found in the database.")

    if args.player:
        team_players = db.get_players_by_team(args.player)

        if team_players and len(team_players) > 0:
            print(f"Players on {args.player}:")
            for player in team_players:
                print(f"- {player[0]} ({player[1]})")
        else:
            print(f"No players found for team '{args.player}'.")

if __name__ == "__main__":
    main()