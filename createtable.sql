/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS nba_stats;

/* Create the table in the database & give it a name */
CREATE TABLE nba_stats (

/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
	name TEXT,
    position TEXT,
    team TEXT,
    games INTEGER,
    rebounds NUMERIC,
    assists NUMERIC,
    points NUMERIC,
    season TEXT
);