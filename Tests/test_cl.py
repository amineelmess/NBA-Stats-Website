import unittest
import subprocess
from ProductionCode.datasource import DataSource

if __name__ == '__main__':
    unittest.main()

class TestGetPlayerStats(unittest.TestCase):
    def setUp(self):
        """set up the Datasource"""
        self.db = DataSource()
    
    def test_get_player_stats(self):
        """
        Purpose: tests the get_player_stats functionality (STANDARD CASE - multiple valid players)
        Arguments: N/A
        Returns: N/A
        """
        result = self.db.get_player_stats_db("LeBron James")
        self.assertIsNotNone(result)
        result2 = self.db.get_player_stats_db("Stephen Curry")
        self.assertIsNotNone(result2)
        result3 = self.db.get_player_stats_db("Giannis Antetokounmpo")
        self.assertIsNotNone(result3)
        result4 = self.db.get_player_stats_db("Bam Adebayo")
        self.assertIsNotNone(result4)
        result5 = self.db.get_player_stats_db("Precious Achiuwa")
        self.assertIsNotNone(result5)
        result6 = self.db.get_player_stats_db("Shai Gilgeous-Alexander")
        self.assertIsNotNone(result6)
        result7 = self.db.get_player_stats_db("Giannis Antetokounmpo")
        self.assertIsNotNone(result7)
        result8 = self.db.get_player_stats_db("Jayson Tatum")
        self.assertIsNotNone(result8)
        result9 = self.db.get_player_stats_db("Anthony Edwards")
        self.assertIsNotNone(result9)
        result10 = self.db.get_player_stats_db("Donovan Mitchell")
        self.assertIsNotNone(result10)

    def test_invalid_get_player_stats(self):
        """
        Purpose: tests the get_player_stats functionality with an invalid input (EDGE CASE)
        Arguments: N/A
        Returns: N/A
        """
        results = self.db.get_player_stats_db("INVALID PLAYER")
        self.assertIsNone(results)

class TestGetTeamPlayers(unittest.TestCase):
    def setUp(self):
        """Set up Datasource"""
        self.db = DataSource()
    
    def test_get_team_players(self):
        """
        Purpose: tests the get_team_player functionality (STANDARD CASE - multiple valid teams)
        Arguments: N/A
        Returns: N/A
        """
        result = self.db.get_players_by_team("LAL")
        self.assertGreater(len(result), 0)
        result2 = self.db.get_players_by_team("GSW")
        self.assertGreater(len(result2), 0)
        result3 = self.db.get_players_by_team("DEN")
        self.assertGreater(len(result3), 0)
        result4 = self.db.get_players_by_team("DAL")
        self.assertGreater(len(result4), 0)
        result5 = self.db.get_players_by_team("PHI")
        self.assertGreater(len(result5), 0)
        result6 = self.db.get_players_by_team("OKC")
        self.assertGreater(len(result6), 0)
        result7 = self.db.get_players_by_team("MIL")
        self.assertGreater(len(result7), 0)
        result8 = self.db.get_players_by_team("BOS")
        self.assertGreater(len(result8), 0)
        result9 = self.db.get_players_by_team("MIN")
        self.assertGreater(len(result9), 0)
        result10 = self.db.get_players_by_team("CLE")
        self.assertGreater(len(result10), 0)
    
    def test_invalid_get_team_players(self):
        """
        Purpose: tests the get_team_player functionality with an invalid team (EDGE CASE)
        Arguments: N/A
        Returns: N/A
        """
        results = self.db.get_players_by_team("INVALID TEAM")
        self.assertEqual(results, [])        
class main_test(unittest.TestCase):
    def test_CL(self):
        """
        Purpose: tests a valid command_line input (STANDARD CASE)
        Returns: N/A
        """
        code = subprocess.Popen(['python3', '-u', 'command_line.py','--stat', 'LeBron James'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(),"Statistics for LeBron James:\nPosition: SF\nTeam: LAL\nGames: 56\nPoints: 30.3\nAssists: 6.2\nRebounds: 8.2")
        code.terminate()

    def test_invalid_CL(self):
        """
        Purpose: tests invalid input for the command line (EDGE CASE)
        Arguments: N/A
        Returns: N/A
        """
        code = subprocess.Popen(['python3', '-u', 'command_line.py'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        print(output.strip('\n'))
        self.assertEqual(output.strip(), 'NBA Player Statistics Lookup\nUsage: python3 command_line.py --stat PLAYER_NAME\npython3 command_line.py --player TEAM_NAME\nExample: python3 command_line.py --stat "LeBron James"\nExample: python3 command_line.py --player "LAL"')

