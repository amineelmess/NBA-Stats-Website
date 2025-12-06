import sys
import psycopg2
import ProductionCode.psql_config as config

class DataSource:

    def __init__(self):
        """
        Purpose: Initializes the DataSource by establishing a database connection.
        Args: None
        Returns: None
        """
        self.connection = self.connect()

    def connect(self):
        """
        Purpose: Establishes a connection to the PostgreSQL database using credentials from config.
        Args: None
        Returns: psycopg2 connection object, or exits program if connection fails
        """
        try:
            connection = psycopg2.connect(
                database=config.DATABASE,
                user=config.USER,
                password=config.PASSWORD,
                host="localhost"
            )
            return connection
        except psycopg2.OperationalError as e:
            print(f"Database connection failed. Unable to connect to '{config.DATABASE}'.")
            print(f"Please verify database credentials in psql_config.py: {e}")
            sys.exit(1)
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            sys.exit(1)
    
    def get_player_stats_db(self, player_name):
        """
        Purpose: Gets the statistics for a specified player from the database.
        Args: player_name
        Returns: List of tuples containing player statistics (name, position, team, games, points, assists, rebounds, season), or None if player not found or error occurs
        """
        if not player_name or not isinstance(player_name, str):
            return None

        try:
            cursor = self.connection.cursor()
            query = "SELECT name, position, team, games, points, assists, rebounds, season FROM nba_stats WHERE name = %s;"
            cursor.execute(query, (player_name,))
            results = cursor.fetchall()

            if not results:
                return None

            return results

        except Exception as e:
            print(f"Error retrieving player stats for '{player_name}': {e}")
            return None

    def get_players_by_team(self, team_name):
        """
        Purpose: Gets all players from a specified team.
        Arguments: team_name
        Returns:list: List of tuples containing (name, position) for each player on the team, or empty list if no players found or error occurs
        """
        if not team_name or not isinstance(team_name, str):
            return []

        try:
            cursor = self.connection.cursor()
            query = "SELECT name, position FROM nba_stats WHERE team = %s;"
            cursor.execute(query, (team_name,))
            results = cursor.fetchall()

            if not results:
                return []

            return results

        except Exception as e:
            print(f"Error retrieving players for team '{team_name}': {e}")
            return []

    def get_stats_by_player_name(self, name):
        """
        Purpose: Gets statistics for a player by name.
        Args: name - name of player
        Returns: List of tuples containing player statistics (name, position, team, games, points, assists, rebounds, season), or None if player not found or error occurs
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT name, position, team, games, points, assists, rebounds, season FROM nba_stats WHERE name = %s;"
            cursor.execute(query, (name,))
            return cursor.fetchall()

        except Exception as e:
            print(f"Error retrieving stats for player '{name}': {e}")
            return None

    def get_all_player_names(self):
        """
        Gets all unique player names from the database.
        Arguments: N/A
        Returns:list: List of unique player names sorted alphabetically, or empty list if error occurs
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT DISTINCT name FROM nba_stats ORDER BY name;"
            cursor.execute(query)
            results = cursor.fetchall()
            # Extract just the name from each tuple
            return [r[0] for r in results] if results else []

        except Exception as e:
            print(f"Error retrieving all player names: {e}")
            return []

    def get_top_PPG_by_season(self, season, limit=10):
        """
        Purpose: Gets the highest scoring players for a specific season in descending order.
        Arguments: season, limit
        Returns: list: List of tuples containing (name, position, team, games, rebounds, assists, points, season) sorted by points descending  for that season, or empty list if error occurs
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT name, position, team, games, points, assists, rebounds, season FROM nba_stats WHERE season = %s ORDER BY points DESC LIMIT %s;"
            cursor.execute(query, (season, limit))
            return cursor.fetchall()

        except Exception as e:
            print(f"Error retrieving top scorers for season '{season}': {e}")
            return []