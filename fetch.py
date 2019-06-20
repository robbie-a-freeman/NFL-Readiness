# @author: Robert Freeman, robbie.a.freeman@gmail.com

# Sources of UDFAs if we want to use them (not localized)
# nfl.com (2009-2014)
# https://www.silverandblackpride.com/2008/4/27/462138/2008-nfl-draft-undrafted-f 2008 , updated like may
# http://www.footballsfuture.com/phpBB2/viewtopic.php?t=135197 2007. kinda sketchy, not verified. not updated. best we got
# https://www.espn.com/nfl/draft06/news/story?id=2431991 2006, updated late may

import numpy as np
import pandas as pd

# create a table of all players and their stats
df = pd.DataFrame(columns=['playerID', 'position', 'college_years', 'thrown_yds_pg', 'thrown_yds_ps', 'thrown_yds_sd', 'thrown_ints_pg', 'thrown_ints_ps', 'thrown_ints_sd', 'thrown_tds_pg', 'thrown_tds_ps', 'thrown_tds_sd', 'rushing_atts_pg', 'rushing_atts_ps', 'rushing_atts_sd', 'rushing_yds_pg', 'rushing_yds_ps', 'rushing_yds_sd', 'rushing_tds_pg', 'rushing_tds_ps', 'rushing_tds_sd', 'receiving_yds_pg', 'receiving_yds_ps', 'receiving_yds_sd', 'receiving_catches_pg', 'receiving_catches_ps', 'receiving_catches_sd', 'receiving_tds_pg', 'receiving_tds_ps', 'receiving_tds_sd', 'tackles_pg', 'tackles_ps', 'tackles_sd', 'hurries_pg', 'hurries_ps', 'hurries_sd', 'sacks_pg', 'sacks_ps', 'sacks_sd', 'ints_pg', 'ints_ps', 'ints_sd', 'tfls_pg', 'tfls_ps', 'tfls_sd', 'pass_defs_pg', 'pass_defs_ps', 'pass_defs_sd', 'fumbles_lost_pg', 'fumbles_lost_ps', 'fumbles_lost_sd', 'fumbles_forced_pg', 'fumbles_forced_ps', 'fumbles_forced_sd', 'kickoff_ret_yds_pg', 'kickoff_ret_yds_ps', 'kickoff_ret_yds_sd', 'kickoff_ret_tds_pg', 'kickoff_ret_tds_ps', 'kickoff_ret_tds_sd', 'punt_ret_yds_pg', 'punt_ret_yds_ps', 'punt_ret_yds_sd', 'punt_ret_tds_pg', 'punt_ret_tds_ps', 'punt_ret_tds_sd', 'combine_height', 'combine_weight', 'combine_40yd', 'combine_cone', 'combine_vertical', 'combine_broad'])
# pull primarily from player-game-statistics.xlsv


# read in the names of the players who have been drafted in the 2006-2014 drafts

# create a list of tuples where each player name is matched with the corresponding
# ID in the collegefootball database, if enough statistics are there for that player.
# TODO set a threshold for minimum data requirements


# create a dataframe that reads in all the wide receiver data that we want, and
# remove the rows of the players that are irrelevant here.

# manipulate the dataframe to have all the stats we are looking for, as well as
# an indicator variable showing whether or not a player was drafted
