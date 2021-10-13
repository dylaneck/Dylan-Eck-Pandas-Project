###########################
#Dylan Eck
#CPSC 222, Fall 2021
#Data Assignment #3
#I did not attempt the bonus
#This program reads in 2 different csv files, then prompts a user for a section of the data and a column, then calculates summary stats for this column and section
#This then merges the 2 files and sorts them by day of week, then takes the mean of the user selected column and prints both of these to csv files
#############################

import utils

youtube_df, days_df = utils.open_csv()
#Opens csv files

new_df, col = utils.slice_data(youtube_df)
#Slices data and returns new data frame and column

utils.calculate_sum_stats(new_df)
# Calculates summary stats

merged_df = utils.merge_tables(youtube_df, days_df)
# Merges tables

utils.means_by_day(merged_df, col)
#Gives averages of the selected column by day of the week