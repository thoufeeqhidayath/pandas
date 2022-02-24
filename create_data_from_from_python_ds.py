import pandas


import pandas as pd

# dictionary with list object in values
details = {
    'Name': ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    'Age': [23, 21, 22, 21],
    'University': ['BHU', 'JNU', 'DU', 'BHU'],
}

# creating a Dataframe object from dictionary
# with custom indexing
df = pd.DataFrame(details, index=['a', 'b', 'c', 'd'])
print(df.head())
print(df.columns)
print(df.index)



# import pandas library
import pandas as pd

# dictionary with dictionary object
# in values i.e. nested dictionary
details = {
	0 : {
		'Name' : 'Ankit',
		'Age' : 22,
		'University' : 'BHU'
		},
	1 : {
		'Name' : 'Aishwarya',
		'Age' : 21,
		'University' : 'JNU'
		},
	2 : {
		'Name' : 'Shaurya',
		'Age' : 23,
		'University' : 'DU'
		}
}

# creating a Dataframe object
# from nested dictionary
# in which inside dictionary
# key is act as index value
# and column value is 0, 1, 2...
df = pd.DataFrame(details)

# swap the columns with indexes
df = df.transpose()
print(df)
from diskcache import Cache