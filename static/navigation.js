// Team abbreviation to full name mapping
const teamNames = {
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
  'WAS': 'Washington Wizards',
  'TOT': 'Played for Multiple Teams'
};

// Position abbreviation to full name mapping
const positionNames = {
  'C': 'Center',
  'PF': 'Power Forward',
  'SF': 'Small Forward',
  'SG': 'Shooting Guard',
  'PG': 'Point Guard',
  'G': 'Guard',
  'F': 'Forward',
  'C-PF': 'Center-Power Forward',
  'PF-C': 'Power Forward-Center',
  'SF-SG': 'Small Forward-Shooting Guard',
  'SG-SF': 'Shooting Guard-Small Forward',
  'PG-SG': 'Point Guard-Shooting Guard',
  'SG-PG': 'Shooting Guard-Point Guard'
};

/**
 * Sets the active navigation link based on the current page
 */
function setActiveNavLink() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('nav a');

  navLinks.forEach(link => {
    // Remove active class from all links
    link.classList.remove('active');

    // Get the href and compare with current path
    const href = link.getAttribute('href');
    if (!href) return;

    // Check if current path matches the link
    if (currentPath === '/' && href === '/') {
      link.classList.add('active');
    } else if (currentPath.startsWith('/top-players') && href === '/top-players') {
      link.classList.add('active');
    } else if (currentPath.startsWith('/teams') && href === '/teams') {
      link.classList.add('active');
    } else if (currentPath.startsWith('/about') && href === '/about') {
      link.classList.add('active');
    } else if (currentPath === '/' && href === '/') {
      link.classList.add('active');
    }
  });
}

/**
 * Adds tooltips to team abbreviations in tables
 */
function addTeamTooltips() {
  const teamElements = document.querySelectorAll('.team-abbr');

  teamElements.forEach(element => {
    const teamCode = element.textContent.trim().toUpperCase();
    if (teamNames[teamCode]) {
      element.setAttribute('title', teamNames[teamCode]);
    }
  });
}

/**
 * Adds tooltips to position abbreviations in tables
 */
function addPositionTooltips() {
  const posElements = document.querySelectorAll('.position-abbr');

  posElements.forEach(element => {
    const posCode = element.textContent.trim();
    if (positionNames[posCode]) {
      element.setAttribute('title', positionNames[posCode]);
    }
  });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  setActiveNavLink();
  addTeamTooltips();
  addPositionTooltips();
});

// Also run immediately in case DOM is already loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', function() {
    setActiveNavLink();
    addTeamTooltips();
    addPositionTooltips();
  });
} else {
  setActiveNavLink();
  addTeamTooltips();
  addPositionTooltips();
}
