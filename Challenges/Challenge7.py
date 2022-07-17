# python 3.7
"""
Challenge 7: Write a table-lookup function: Given a CSV file with headings, write a program where you give it a
column  heading and a value and it prints out the entire row where that column has that value
"""

# import numpy as np
import pandas as pd


def search_table(path, heading, target):
    data = pd.read_csv(path)
    print(data[data[heading] == target])

"""
fpath = 'Challenge7.csv'
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])
df.to_csv(fpath)
search_table(fpath, 'b', 5)
"""

