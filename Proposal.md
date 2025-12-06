# Project Proposal: JAN - NBA Players' StatCompare

## Summary
We are building an interactive web app that allows users to view, search, and compare NBA player statistics from the 2023–2024 and 2024–2025 seasons. Users can:
- View individual player stats
- Compare a player’s stats across seasons
- Compare two players side-by-side

Our goal is to make an intuitive tool for casual fans and data driven NBA enthusiasts alike.

## Dataset Summary

We are using two datasets that contain player statistics for the 2023–2024 and 2024–2025 NBA seasons:

1. **2023–2024 NBA Player Stats**  
   - **URL**: https://www.kaggle.com/datasets/vivovinco/2023-2024-nba-player-stats  
   - **Date Downloaded**: September 21, 2025  
   - **Author**: vivovinco  
   - **Filename**: `2023-2024 NBA Player Stats - Regular.csv`  
   - **Terms of Use**: For academic/personal use under Kaggle's dataset sharing guidelines  
   - **Suggested Citation**: vivovinco (2024). 2023–2024 NBA Player Stats. Kaggle.  

2. **2024–2025 NBA Player Stats**  
   - **URL**: https://www.kaggle.com/datasets/eduardopalmieri/nba-player-stats-season-2425  
   - **Date Downloaded**: September 21, 2025  
   - **Author**: eduardopalmieri  
   - **Filename**: `NBA Player Stats 24-25.csv`  
   - **Terms of Use**: For academic/personal use under Kaggle's dataset sharing guidelines  
   - **Suggested Citation**: Palmieri, Eduardo (2025). NBA Player Stats Season 24/25. Kaggle.  

Both datasets are under 20MB combined and have consistent structure and naming conventions.

## User Interactions

### 1. View an Individual Player’s Season Stats

- **Potential Users**: Casual fans, fantasy basketball players, sports bloggers
- **Interaction Mechanism**: Search bar with auto-complete to select a player and view detailed season stats
- **Potential Benefits**: Quick access to full stats without needing to browse multiple pages
- **Potential Harms**: 
  - Could be frustrating if user searches for a name spelled incorrectly
  - May reinforce gender exclusivity (NBA only data); we will add a disclaimer about scope

### 2. Compare a Player’s Stats Across Seasons

- **Potential Users**: Fans, journalists, data nerds
- **Interaction Mechanism**: Player dropdown + toggle to view season by season stats side-by-side
- **Potential Benefits**: Helps identify performance trends over time
- **Potential Harms**: Might lead users to overinterpret changes (e.g., injury affected seasons)
- **Advantage**: Clean data and uniform structure make this technically straightforward to implement

### 3. Compare Two Players Side-by-Side

- **Potential Users**: Debaters, fans, “who’s better?” arguments
- **Interaction Mechanism**: Select two players and display key stat comparisons in a table or chart
- **Potential Benefits**: Promotes data driven sports discussion
- **Potential Harms**: Could encourage reductive takes (ignoring context like teammates or position)