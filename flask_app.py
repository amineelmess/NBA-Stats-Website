from flask import Flask, Response, render_template, request, redirect, jsonify, url_for
from ProductionCode.datasource import DataSource

app = Flask(__name__)

# Initialize database connection
try:
    db = DataSource()
except SystemExit:
    # If database connection fails, the error message will be printed by DataSource
    db = None

@app.route('/')
def homepage():
    """
    Purpose:Display the main homepage (index.html) with player statistics from the database.
    Renders the homepage with featured player data and popular players filtered by
    the selected season. Retrieves data from the PostgreSQL database.
    Args: None
    Returns:Rendered HTML template with player data
    """
    if not db:
        return "Database connection failed. Please check your configuration.", 500

    player_name = request.args.get('name')
    season = request.args.get('season', '2023-2024')
    featured_player = None
    popular_players = []

    try:
        all_players = db.get_top_PPG_by_season(season, limit=5)
        popular_players = []
        if all_players:
            # Convert tuples to dicts for template
            popular_players = [
                {
                    'Player': p[0],
                    'Pos': p[1],
                    'Tm': p[2],
                    'G': p[3],
                    'PTS': p[4],
                    'AST': p[5],
                    'TRB': p[6],
                    'Season': p[7] if len(p) > 7 else 'N/A'
                }
                for p in all_players
            ]
    except Exception as e:
        print(f"Error retrieving popular players: {e}")
        popular_players = []

    player_found = True
    if player_name:
        # Look up specific player
        searched_player_data = db.get_player_stats_db(player_name)

        if searched_player_data and len(searched_player_data) > 0:
            # Filter by season - find matching season or use first result
            player = None
            for p in searched_player_data:
                if len(p) > 7 and p[7] == season:
                    player = p
                    break
            # If no match for season, use first result
            if player is None:
                player = searched_player_data[0]

            featured_player = {
                'Player': player[0],
                'Pos': player[1],
                'Tm': player[2],
                'G': player[3],
                'PTS': player[4],
                'AST': player[5],
                'TRB': player[6],
                'Season': player[7] if len(player) > 7 else 'N/A'
            }
            player_found = True
        else:
            player_found = False
            # Show top scorer as fallback
            try:
                top_scorers = db.get_top_PPG_by_season(season, limit=1)
                if top_scorers:
                    p = top_scorers[0]
                    featured_player = {
                        'Player': p[0],
                        'Pos': p[1],
                        'Tm': p[2],
                        'G': p[3],
                        'PTS': p[4],
                        'AST': p[5],
                        'TRB': p[6],
                        'Season': p[7] if len(p) > 7 else 'N/A'
                    }
            except Exception as e:
                print(f"Error retrieving fallback player: {e}")
    else:
        # Show top scorer
        try:
            top_scorers = db.get_top_PPG_by_season(season, limit=1)
            if top_scorers:
                p = top_scorers[0]
                featured_player = {
                    'Player': p[0],
                    'Pos': p[1],
                    'Tm': p[2],
                    'G': p[3],
                    'PTS': p[4],
                    'AST': p[5],
                    'TRB': p[6],
                    'Season': p[7] if len(p) > 7 else 'N/A'
                }
        except Exception as e:
            print(f"Error retrieving featured player: {e}")

    return render_template('index.html',
                         featured_player=featured_player,
                         popular_players=popular_players,
                         searched_player=player_name,
                         current_season=season,
                         player_found=player_found)

@app.route('/api/players')
def api_players():
    """
    Provide autocomplete suggestions for the player search bar.

    Queries the database for all players and filters by the search query.
    Returns up to 10 matching player names as JSON for autocomplete functionality.

    Args:
        q (str): Search query parameter for filtering players
        season (str): Season filter parameter

    Returns:
        JSON: List of matching player names (up to 10 results)
    """
    if not db:
        return jsonify([])

    query = request.args.get('q', '').lower()

    try:
        all_players = db.get_all_player_names()

        if query:
            # Filter players by query
            filtered_players = [player for player in all_players if query in player.lower()]
            return jsonify(filtered_players[:10])
        else:
            return jsonify(all_players[:10])
    except Exception as e:
        print(f"Error retrieving players for autocomplete: {e}")
        return jsonify([])  

@app.route('/top-players')
def top_players_page():
    """
    Render the top players page showing the highest scoring players.

    Retrieves the top 10 scorers from the database and displays them on
    a dedicated page. Supports filtering by season.

    Args:
        season (str): Query parameter for season filter

    Returns:
        Rendered HTML template with top players data
    """
    if not db:
        return "Database connection failed. Please check your configuration.", 500

    season = request.args.get('season', '2023-2024')
    available_seasons = ['2023-2024', '2022-2023', '2021-2022']

    try:
        # Get top scorers for the specific season
        top_scorers = db.get_top_PPG_by_season(season, limit=10)
        top_players = []
        if top_scorers:
            top_players = [
                {
                    'Player': p[0],
                    'Pos': p[1],
                    'Tm': p[2],
                    'G': p[3],
                    'PTS': p[4],
                    'AST': p[5],
                    'TRB': p[6],
                }
                for p in top_scorers
            ]
        return render_template('top_players.html',
                             players=top_players,
                             current_season=season,
                             seasons=available_seasons)
    except Exception as e:
        print(f"Error retrieving top players: {e}")
        return render_template('top_players.html',
                             players=[],
                             current_season=season,
                             seasons=available_seasons)


@app.route('/stat/<player_name>', strict_slashes = False)
def stat_redirect(player_name):
    """
        Purpose: redirects 
        Arguments: player_name
        Returns: redirect to page that was made to display player stats
    """
    player = player_name.replace('-', ' ')
    return redirect(url_for('homepage', name=player))

@app.route('/player/<team_name>', strict_slashes=False)
def team_players(team_name):
    """
    Get all players for a specified team.

    Retrieves all players from the database who play for the given team and
    displays them in an HTML list.

    Args:
        team_name (str): Team abbreviation to look up (e.g., 'LAL', 'GSW')

    Returns:
        HTML page with list of players on the team, or 404 page if team not found
    """
    if not db:
        return "Database connection failed. Please check your configuration.", 500

    try:
        team_players_list = db.get_players_by_team(team_name)

        if team_players_list:
            # Convert tuples to html list items
            players_html = "".join([
                f"<li>{player[0]} ({player[1]})</li>"
                for player in team_players_list
            ])
            return f"""
            <h2>Players on {team_name}</h2>
            <ul>
            {players_html}
            </ul>
            <a href="/">Back to Home</a>
            """
        else:
            return f"<h2>No players found for team '{team_name}'.</h2><a href='/'>Back to Home</a>", 404
    except Exception as e:
        print(f"Error retrieving players for team '{team_name}': {e}")
        return f"<h2>Error retrieving players for team '{team_name}'.</h2><a href='/'>Back to Home</a>", 500
    

@app.route('/about')
def about_page():
    """
    Purpose: Display the about page with information about the website.

    Shows details about what the website is, its features, how to use it,
    data information, technologies used, and accessibility features.

    Args: None

    Returns: Rendered about.html template
    """
    return render_template('about.html')


@app.route('/teams')
def teams_page():
    """
    Purpose: Display the teams page with all NBA teams as clickable boxes.

    Retrieves all unique teams from the database and displays them in a grid format.
    Users can click on a team box to view all players on that team.

    Args: None

    Returns: Rendered teams.html template with list of teams
    """
    if not db:
        return "Database connection failed. Please check your configuration.", 500

    # List of all NBA teams with their abbreviations and full names
    teams = [
        {'abbr': 'ATL', 'name': 'Atlanta Hawks'},
        {'abbr': 'BOS', 'name': 'Boston Celtics'},
        {'abbr': 'BRK', 'name': 'Brooklyn Nets'},
        {'abbr': 'CHO', 'name': 'Charlotte Hornets'},
        {'abbr': 'CHI', 'name': 'Chicago Bulls'},
        {'abbr': 'CLE', 'name': 'Cleveland Cavaliers'},
        {'abbr': 'DAL', 'name': 'Dallas Mavericks'},
        {'abbr': 'DEN', 'name': 'Denver Nuggets'},
        {'abbr': 'DET', 'name': 'Detroit Pistons'},
        {'abbr': 'GSW', 'name': 'Golden State Warriors'},
        {'abbr': 'HOU', 'name': 'Houston Rockets'},
        {'abbr': 'IND', 'name': 'Indiana Pacers'},
        {'abbr': 'LAC', 'name': 'Los Angeles Clippers'},
        {'abbr': 'LAL', 'name': 'Los Angeles Lakers'},
        {'abbr': 'MEM', 'name': 'Memphis Grizzlies'},
        {'abbr': 'MIA', 'name': 'Miami Heat'},
        {'abbr': 'MIL', 'name': 'Milwaukee Bucks'},
        {'abbr': 'MIN', 'name': 'Minnesota Timberwolves'},
        {'abbr': 'NOP', 'name': 'New Orleans Pelicans'},
        {'abbr': 'NYK', 'name': 'New York Knicks'},
        {'abbr': 'OKC', 'name': 'Oklahoma City Thunder'},
        {'abbr': 'ORL', 'name': 'Orlando Magic'},
        {'abbr': 'PHI', 'name': 'Philadelphia 76ers'},
        {'abbr': 'PHO', 'name': 'Phoenix Suns'},
        {'abbr': 'POR', 'name': 'Portland Trail Blazers'},
        {'abbr': 'SAC', 'name': 'Sacramento Kings'},
        {'abbr': 'SAS', 'name': 'San Antonio Spurs'},
        {'abbr': 'TOR', 'name': 'Toronto Raptors'},
        {'abbr': 'UTA', 'name': 'Utah Jazz'},
        {'abbr': 'WAS', 'name': 'Washington Wizards'},
    ]

    return render_template('teams.html', teams=teams)


@app.route('/teams/<team_name>')
def team_roster(team_name):
    """
    Purpose: Display the roster for a specific NBA team with players and their seasons.

    Retrieves all players for the specified team from the database and displays them
    in a table format showing player name, position, and seasons they played.

    Args: team_name (str) - Team abbreviation (e.g., 'LAL', 'GSW')

    Returns: Rendered team_roster.html template with player data
    """
    if not db:
        return "Database connection failed. Please check your configuration.", 500

    # Map team abbreviations to full names
    team_names_map = {
        'ATL': 'Atlanta Hawks',
        'BOS': 'Boston Celtics',
        'BRK': 'Brooklyn Nets',
        'CHO': 'Charlotte Hornets',
        'CHI': 'Chicago Bulls',
        'CLE': 'Cleveland Cavaliers',
        'DAL': 'Dallas Mavericks',
        'DEN': 'Denver Nuggets',
        'DET': 'Detroit Pistons',
        'GSW': 'Golden State Warriors',
        'HOU': 'Houston Rockets',
        'IND': 'Indiana Pacers',
        'LAC': 'Los Angeles Clippers',
        'LAL': 'Los Angeles Lakers',
        'MEM': 'Memphis Grizzlies',
        'MIA': 'Miami Heat',
        'MIL': 'Milwaukee Bucks',
        'MIN': 'Minnesota Timberwolves',
        'NOP': 'New Orleans Pelicans',
        'NYK': 'New York Knicks',
        'OKC': 'Oklahoma City Thunder',
        'ORL': 'Orlando Magic',
        'PHI': 'Philadelphia 76ers',
        'PHO': 'Phoenix Suns',
        'POR': 'Portland Trail Blazers',
        'SAC': 'Sacramento Kings',
        'SAS': 'San Antonio Spurs',
        'TOR': 'Toronto Raptors',
        'UTA': 'Utah Jazz',
        'WAS': 'Washington Wizards'
    }

    # Get full team name
    full_team_name = team_names_map.get(team_name.upper(), team_name)

    try:
        team_players_list = db.get_players_by_team(team_name)

        if team_players_list:
            # Get unique seasons for each player
            players_with_seasons = []
            for player_name, position in team_players_list:
                # Get all stats for this player to find seasons
                player_stats = db.get_stats_by_player_name(player_name)
                seasons = set()
                if player_stats:
                    for stat in player_stats:
                        if len(stat) > 7:
                            seasons.add(stat[7])

                seasons_str = ', '.join(sorted(seasons)) if seasons else 'N/A'

                players_with_seasons.append({
                    'name': player_name,
                    'position': position,
                    'seasons': seasons_str
                })

            return render_template('team_roster.html',
                                   team_name=full_team_name,
                                   players=players_with_seasons)
        else:
            return render_template('team_roster.html',
                                   team_name=full_team_name,
                                   players=[])

    except Exception as e:
        print(f"Error retrieving roster for team '{team_name}': {e}")
        return render_template('team_roster.html',
                               team_name=full_team_name,
                               players=[])


@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 (page not found) errors.

    Displays a helpful error page template with instructions on how to use the website
    and provides examples of valid routes.

    Args:
        e: The exception object (unused but required by Flask error handler)

    Returns:
        Rendered 404.html template with 404 status code
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """
    Handle 500 (internal server error) errors.

    Displays a helpful error page when an unexpected server error occurs
    and provides examples of valid routes for the user to try.

    Args:
        e: The exception object (unused but required by Flask error handler)

    Returns:
        HTML error page with 500 status code
    """
    return """
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong. Please try again or use one of these formats:</p>
    <ul>
        <li>/stat/player_name (Example: /stat/LeBron James)</li>
        <li>/player/team_abbreviation (Example: /player/LAL)</li>
    </ul>
    <a href="/">Back to Home</a>
    """, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5220)
    


