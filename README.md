# MLB Standings
 
## Purpose
In 2020, Jon Bois and Alex Rubenstien released their series "The History of the Seattle Mariners," a 6 part series detailing the history of baseball in Seattle, Washington from 1932 to the present. As part of that series, they visualized the game-by-game progress of the Mariners through charts. Enjoying that series broadly and that portion in particular, I wanted to build something that would create similar charts for the current season. Using fellow GitHub user jldbc's [pybaseball](https://github.com/jldbc/pybaseball "pybaseball") package, these scripts access [Baseball-Reference.com](Baseball-Reference.com) to produce graphs for each division.

## Scripts
### Standings_Funcs.py
This script defines four functions that can be imported and used in additional scripts to create graphs and databases:
1. to_500 (y,t)
to_500 takes in a year and a team abbreviation[^1], and outputs a dataframe with the game number, and then the number of games back of .500 that the team was following that game.

2. w_pct (y,t)
w_pct works in the same way as to_500, but outputs the winning percentage after each game rather than the games back of .500.

3. grph (y,t)
grph again works the same way as to_500, but additionally outputs a column containing the team's abbreviation in each row. This can be useful for making graphs.

4. div_graph (y,d)
div_graph takes in a year and a list containing the abbrevation of several teams. It then loops through that list using the grph(y,t) function, and creates a dataframe containing the records of the teams in that list, then generates a graph using seaborn from that dataframe, and saving the graph.

### Graph_Generator.py
This scripts outlines a list of the team abbreviations for each division, league, and MLB at large, then takes in a division/league/MLB and a year, then uses the div_graphs(y,d) function from Standings_Funcs.py to generate a graph for that division and year.

### Record_Save.py
This script uses the pybaseball snr function to save all the outputs for a specific team to a .csv file



[^1]: Each team has either a two [2] or three [3] letter abbreviation (i.e. "SEA" for the Seattle Mariners or "SF" for the San Fransisco Giants)