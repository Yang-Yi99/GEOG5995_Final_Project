import os
import pandas as pd

# open the directory and view its contents
data_dir = os.listdir(os.getcwd() + '/data')

# create a list to store pandas data frames for csv data files
df_list = []

# loop the contents of the directory
for data_file in data_dir:
    
    print(data_file)
    
    # skip lines that fail to parse, and put the dataframe into df_list
    df_list.append(pd.read_csv('data/' + data_file, error_bad_lines=False))

# concatenate data frames vertically
concatenated_df = pd.concat(df_list)

# save data frame to CSV file
concatenated_df.to_csv('west-yorkshire-street-merged.csv', index=False)
