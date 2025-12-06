# CS257. JAN - NBA Players' StatCompare

A command line and web interface for looking up NBA player statistics from a PostgreSQL database.

## Database Setup

This application uses a PostgreSQL database on the stearns server. The database contains NBA player statistics with the following structure:

- Player name, position, team abbreviation, games played, points, assists, rebounds, season information

## Usage

### Command Line Interface

To run the command line interface:

```bash
python3 command_line.py --stat "PLAYER_NAME"
python3 command_line.py --player "TEAM_NAME"
```

### Web Interface

To run the Flask web on stearns:

```bash
python3 flask_app.py
```

Then navigate to `steans.mathcs.carleton.edu:5120` in your browser.

## Examples

### Command Line Examples

Look up LeBron James' statistics:

```bash
python3 command_line.py --stat "LeBron James"
```

Look up Stephen Curry's statistics:

```bash
python3 command_line.py --stat "Stephen Curry"
```

Look up all players who played on the Lakers:

```bash
python3 command_line.py --player "LAL"
```

Look up all players who played on the Warriors:

```bash
python3 command_line.py --player "GSW"
```

### Web Interface Examples

- `/stat/LeBron-James` - Get statistics for LeBron James
- `/player/LAL` - Get all players on the Lakers
- `/player/GSW` - Get all players on the Warriors

## Testing

To run the test suite:

```bash
python3 -m unittest discover Tests/
```

## Web Design Principles

Our website implements the following usability principles:

### Scanability

- **Clear headings and structure**: The website uses headings (h1, h2) to organize content hierarchically
- **Visual navigation**: Navigation menu is displayed in the header with clear, descriptive link text
- **Consistent layout**: Similar content (player stats, team rosters) follows the same visual patterns
- **White space**: Adequate spacing between elements prevents visual clutter and improves readability
- **Featured player section**: Main content is prominently displayed with clear visual hierarchy

### Satisficing

- **Autocomplete search**: Smart search bar provides real-time suggestions as users type, reducing effort to find players
- **Season switching**: Quick dropdown allows users to change data timeframes without complex navigation
- **Error guidance**: Clear feedback when players aren't found, with fallback to featured content
- **Minimal interaction**: Users can find any player information with just typing and clicking
- **Dynamic updates**: Search results replace featured player content immediately, no page reloads needed

### Muddling Through

- **Forgiving search**: Autocomplete helps users find correct player names even with partial/misspelled input
- **Multiple data access**: Users can browse by season for specific players, or view top players
- **Immediate feedback**: Interface provides instant visual confirmation of user actions
- **Flexible exploration**: Users can easily switch between different seasons and players to explore data

## Option B: Front-End Design Improvements

### 1. Hover Tooltips for Abbreviations

**Usability Issue**: Team abbreviations (LAL, PHI) and position abbreviations (C, PG) were unclear to users who don't know NBA terminology.

**Pages**: Home page, Top Players page, Team Roster page

**Solution**: Added hover tooltips that display full names when users hover over abbreviations (e.g., "LAL" to "Los Angeles Lakers", "C" to "Center"). Visual dotted underline indicates the abbreviations are interactive.

### 2. Player and Team Photos

**Usability Issue**: Players without individual photos displayed an empty placeholder, and team pages had no visual identity.

**Pages**: Home page, Top Players page, Team Roster page, Teams page

**Solution**: Added fallback images - when players don't have individual photos, their team logos display instead. Teams page now shows team logos in team boxes for better visual recognition and engagement.

### 3. Color Theme and Accessibility

**Usability Issue**: Original green/orange color scheme and later blue-on-blue text made the site difficult for users with vision impairments and color blindness.

**Pages**: All pages

**Solution**: Changed to blue and white color scheme with proper contrast:
- White text on dark blue backgrounds for headers and navigation
- Dark text on light blue backgrounds for content sections
- Black text on white backgrounds for input fields and dropdowns
- All changes follow WCAG AA contrast standards for accessibility

## Team Members
- Amine El Messaoudi
- Jeremy Gautama
- Ngelek Thayai
