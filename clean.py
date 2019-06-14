# @author: Robert Freeman

import numpy as np
import pandas as pd

# Sources it looks like we will use for UDFAs
# nfl.com (2009-2014)
# https://www.silverandblackpride.com/2008/4/27/462138/2008-nfl-draft-undrafted-f 2008 , updated like may
# http://www.footballsfuture.com/phpBB2/viewtopic.php?t=135197 2007. kinda sketchy, not verified. not updated. best we got
# https://www.espn.com/nfl/draft06/news/story?id=2431991 2006, updated late may

# read in the names of the players who have been drafted in the 2006-2014 drafts
# or were shortly after signed as UDFAs into a list

# create a list of tuples where each player name is matched with the corresponding
# ID in the collegefootball database, if enough statistics are there for that players

# TODO Figure out the threshold

# create a dataframe that reads in all the wide receiver data that we want, and
# remove the rows of the players that are irrelevant here.

# manipulate the dataframe to have all the stats we are looking for, as well as
# an indicator variable showing whether or not a player was drafted
