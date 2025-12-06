# User Analysis for NBA Player Statistics Command Line Interface

## Potential Users

- Basketball fans who want to look up specific player statistics
- Students learning about NBA players and their performance

## Potential Benefits

- Quick access to NBA player statistics without needing a web browser
- Simple command line interface that's easy to use

## CIDER Analysis

### Assumption 1: Users who knows the player names in full

**Critique**: The interface assumes users know the exact spelling and formatting of NBA player names (e.g. "LeBron James" vs "Lebron James" vs "Lebron").

**Imagine**: What if a user doesn't know the exact spelling or full name? They might get frustrated when searches fail due to minor spelling differences.

**Design**: We could implement partial name matching or suggest similar names when an exact match isn't found. For example, if someone searches for "lebron" it could suggest "LeBron James".

### Assumption 2: Users want basic statistics only

**Critique**: The interface currently only shows basic stats like points, assists, and rebounds. Some users might want more detailed statistics.

**Imagine**: Advanced basketball fans might need more advanced statistics.

**Design**: We could add an optional flag like `--detailed` to show more comprehensive statistics, or allow users to specify which stats they want to see.

### Assumption 3: Users know exact team names

**Critique**: The new `--player` feature assumes users know the exact team names as they appear in the database.

**Imagine**: Users might search for "LA Lakers" when the database uses "LAL", or "GWS" instead of "Warriors" or "Golden State Warriors".

**Design**: We could implement full or partial team name matching or provide a list of available team names when an invalid team is searched.

## Potential Harms/Exclusion

- Users unfamiliar with basketball terminology might not understand the statistics
- The command line interface might exclude users who prefer graphical interfaces
- Only includes current NBA players, excluding historical players or other leagues
- Requires users to have Python and command line knowledge

---

# Flask App User Analysis

## CIDER Analysis for Flask App

### Assumption 1: Users prefer clicking links over typing URLs

**Critique**: The web interface assumes users want to click provided example links rather than manually typing player/team names in URLs.

**Imagine**: Some users might want to directly type URLs or bookmark specific players/teams without navigating through the homepage.

**Design**: We could add a search form on the homepage or auto complete functionality for direct URL entry.

### Assumption 2: Users understand team abbreviations

**Critique**: The interface uses NBA team abbreviations like "LAL" and "GSW" which some users might not recognize.

**Imagine**: Casual fans might not know that "LAL" means Lakers or "GSW" means Warriors.

**Design**: We could display full team names alongside abbreviations or provide a team directory page.

### Assumption 3: Users want to see all players on a team at once

**Critique**: The team route displays all players for a team in one long list, assuming users want to browse the entire roster.

**Imagine**: Users might only want specific players or prefer filtering options (by position, stats, etc.).

**Design**: We could add filtering options or pagination for large team rosters.

### Assumption 4: Users have stable internet connections

**Critique**: The database backed web interface assumes users have reliable internet connections to access the stearns server.

**Imagine**: Users with poor internet connections might experience timeouts, failed queries, or inability to access the application entirely.

**Design**: We could provide downloadable datasets for local use, or create web app functionality that works offline.

## Potential Harms/Exclusion

- Non-english speakers might not understand the interface text
- Users on slow internet connections might find the web interface slower than command line
- The interface still requires knowledge of exact player names and team abbreviations

---

# Database User Analysis

## CIDER Analysis for Database Implementation

### Assumption 1: Data completeness represents reality

**Critique**: The database assumes that the NBA statistics dataset is complete and accurately represents all relevant player performance data.

**Imagine**: Missing games, incorrect statistics, or selective reporting could lead to biased analysis and unfair player comparisons.

**Design**: We could add data validation, data source verification, or clearly indicate data limitations and collection dates to users.

### Assumption 2: Player names are unique identifiers

**Critique**: The database structure assumes player names alone are sufficient to uniquely identify players across seasons and teams.

**Imagine**: Players with the same name (e.g multiple players named "Johnson") could cause data conflicts or incorrect results or players with special characters.

**Design**: We could implement unique player IDs, combine names with additional identifiers (birth year, team history), or add disambiguation when multiple matches exist.

### Assumption 3: Team abbreviations are universally understood

**Critique**: The database uses NBA team abbreviations that may not be familiar to all users, especially international users or casual fans.

**Imagine**: Users might not know that "LAL" means Lakers or "GSW" means Warriors, leading to failed searches or confusion.

**Design**: We could provide team name lookups, auto-suggest functionality, or display full team names alongside abbreviations.

---

# Front-End GUI User Analysis

## CIDER Analysis for Front-End GUI

### Assumption 1: Users can see and distinguish colors clearly

**Critique**: The interface uses green and orange color scheme that assumes users have normal color vision and can distinguish between these colors.

**Imagine**: Users with color blindness (especially red-green color blindness) might have difficulty distinguishing interface elements or reading text against colored backgrounds.

**Design**: We could implement high contrast modes, use patterns/textures in addition to colors, and ensure sufficient color contrast ratios for text readability.

### Assumption 2: Users navigate with mouse/trackpad clicking

**Critique**: The GUI assumes users will primarily interact through mouse clicks on links and buttons.

**Imagine**: Users with motor disabilities, those using assistive technologies, or keyboard-only navigation users might struggle with mouse-dependent interactions.

**Design**: We could ensure all interactive elements are keyboard accessible, add proper tab ordering, and include ARIA labels for screen readers.

### Assumption 3: Users know exact player names for searching

**Critique**: The search functionality assumes users know the exact spelling and capitalization of NBA player names to find them effectively.

**Imagine**: Users might only remember partial names, nicknames, or different spellings (e.g searching "Lebron" instead of "LeBron James").

**Design**: We implemented an autocomplete search feature that suggests player names as users type, helping them find the correct spelling and complete names even with partial input.
