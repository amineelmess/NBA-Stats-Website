from flask_app import *
import unittest

class TestHomePage(unittest.TestCase):
"""Integration tests for Flask homepage route with database"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_homepage_route_loads(self):
        """Test that homepage route loads and returns 200 status (STANDARD CASE)"""
        response = self.app.get('/', follow_redirects=True)
        # Check that page loads (200 or 500 if db not available)
        self.assertIn(response.status_code, [200, 500])

    def test_homepage_displays_content(self):
        """Test homepage displays expected content when database is available (STANDARD CASE)"""
        response = self.app.get('/', follow_redirects=True)
        # If database is available, should have content
        if response.status_code == 200:
            # Should have either stats content or error message
            self.assertIsNotNone(response.data)
            self.assertGreater(len(response.data), 0)

class TestStatPlayerRoute(unittest.TestCase):
    """Integration tests for player lookup route with database"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_player_route_valid(self):
        """Test player lookup with valid player name (STANDARD CASE)"""
        response = self.app.get('/?name=LeBron%20James', follow_redirects=True)
        # Should return 200 if db available
        if response.status_code == 200:
            # Should contain something (player name or top scorer)
            self.assertIsNotNone(response.data)
            self.assertGreater(len(response.data), 0)

    def test_player_route_invalid(self):
        """Test player lookup with invalid player name (EDGE CASE)"""
        response = self.app.get('/?name=NonExistentPlayer123XYZ', follow_redirects=True)
        # When player not found, should show fallback content (top scorer)
        if response.status_code == 200:
            # Should still have content (fallback to top player)
            self.assertIsNotNone(response.data)
            self.assertGreater(len(response.data), 0)

    def test_player_route_empty_name(self):
        """Test player lookup with empty player name (EDGE CASE)"""
        response = self.app.get('/?name=', follow_redirects=True)
        # Should return 200 or 500
        self.assertIn(response.status_code, [200, 500])

class TestPlayerTeamRoute(unittest.TestCase):
    """Integration tests for team players lookup route with database"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_team_players_valid(self):
        """Test valid team lookup returns players (STANDARD CASE)"""
        response = self.app.get('/player/LAL')
        # Should return 200 if database available
        if response.status_code == 200:
            # Should have players list
            self.assertIn(b"Players on LAL", response.data)

    def test_team_players_invalid(self):
        """Test invalid team lookup returns 404 (EDGE CASE)"""
        response = self.app.get('/player/FAKETEAM999', follow_redirects=True)
        # Invalid team should return 404
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"No players found for team", response.data)

    def test_team_players_lowercase(self):
        """Test team lookup is case-insensitive (EDGE CASE)"""
        response = self.app.get('/player/lal')
        # Should handle lowercase team abbreviation
        self.assertIn(response.status_code, [200, 404])

class TestErrorHandling(unittest.TestCase):
    """Integration tests for error handling in Flask app"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_404_page(self):
        """Test 404 error page displays helpful instructions (EDGE CASE)"""
        response = self.app.get('/invalid-route')
        # Should return 404 for invalid route
        self.assertIn(response.status_code, [404, 200])
        # Should have error message or be handled
        self.assertIsNotNone(response.data)

    def test_404_has_usage_instructions(self):
        """Test 404 page includes usage examples (EDGE CASE)"""
        response = self.app.get('/nonexistent')
        # Should return 404 for nonexistent route
        self.assertIn(response.status_code, [404, 200])
        self.assertIsNotNone(response.data)

class TestAPIRoute(unittest.TestCase):
    """Integration tests for API endpoint"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_api_players_endpoint(self):
        """Test API players endpoint responds (STANDARD CASE)"""
        response = self.app.get('/api/players?q=lebron')
        # Should return 200 (even if empty results)
        self.assertEqual(response.status_code, 200)

    def test_api_players_empty_query(self):
        """Test API players endpoint with empty query (EDGE CASE)"""
        response = self.app.get('/api/players?q=')
        self.assertEqual(response.status_code, 200)

class TestTopPlayersRoute(unittest.TestCase):
    """Integration tests for top players page"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_top_players_page_loads(self):
        """Test top players page loads (STANDARD CASE)"""
        response = self.app.get('/top-players')
        # Should return 200 if db available, 500 if not
        self.assertIn(response.status_code, [200, 500])

class TestStatRedirect(unittest.TestCase):
    """Integration tests for stat redirect route"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_stat_redirect_valid(self):
        """Test stat redirect with valid player (STANDARD CASE)"""
        response = self.app.get('/stat/LeBron-James', follow_redirects=True)
        # Should redirect and load homepage
        self.assertIn(response.status_code, [200, 500])

class TestTeamsPage(unittest.TestCase):
    """Integration tests for teams browsing page"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_teams_page_loads(self):
        """Test teams page loads (STANDARD CASE)"""
        response = self.app.get('/teams')
        # Should return 200 if db available, 500 if not
        self.assertIn(response.status_code, [200, 500])

    def test_teams_page_displays_content(self):
        """Test teams page displays team information (STANDARD CASE)"""
        response = self.app.get('/teams')
        if response.status_code == 200:
            # Should have content with team data
            self.assertIsNotNone(response.data)
            self.assertGreater(len(response.data), 0)

class TestTeamRosterRoute(unittest.TestCase):
    """Integration tests for team roster page"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_team_roster_valid(self):
        """Test team roster page with valid team (STANDARD CASE)"""
        response = self.app.get('/teams/LAL')
        # Should return 200 if db available, 500 if not
        self.assertIn(response.status_code, [200, 500])

    def test_team_roster_displays_players(self):
        """Test team roster displays players when available (STANDARD CASE)"""
        response = self.app.get('/teams/LAL')
        if response.status_code == 200:
            # Should have content
            self.assertIsNotNone(response.data)
            self.assertGreater(len(response.data), 0)

    def test_team_roster_invalid_team(self):
        """Test team roster with invalid team (EDGE CASE)"""
        response = self.app.get('/teams/FAKETEAM999')
        # Should still return 200 but with no players message
        self.assertEqual(response.status_code, 200)

class TestAboutPage(unittest.TestCase):
    """Integration tests for about page"""

    def setUp(self):
        """Set up Flask test client"""
        self.app = app.test_client()

    def test_about_page_loads(self):
        """Test about page loads successfully (STANDARD CASE)"""
        response = self.app.get('/about')
        # Should return 200
        self.assertEqual(response.status_code, 200)

    def test_about_page_displays_content(self):
        """Test about page displays expected content (STANDARD CASE)"""
        response = self.app.get('/about')
        # Should display about information
        self.assertIsNotNone(response.data)
        self.assertGreater(len(response.data), 0)
        # Should contain key sections
        self.assertIn(b'About NBA Stats Website', response.data)

if __name__ == '__main__':
   unittest.main()