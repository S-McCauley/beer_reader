import numpy as np
import pandas as pd

df = pd.read_csv('Total Beer Sales March_2.0.csv') #defines csv file
df = df.dropna() #drops all NaN entries
del df['1 - Frothy Beard Brewing 1401 Sam Rittenburg Blvd.  '] #delets the first colulmn
df.drop('Unnamed: 1', inplace=True, axis =1) #deletes unnamed column 1
df.drop('Unnamed: 4', inplace=True, axis =1) #deletes unnamed column 4
df.drop('Unnamed: 5', inplace=True, axis =1) #deletes unnamed column 5
df.drop('Unnamed: 6', inplace=True, axis =1) #deletes unnamed column 6
df.drop('Unnamed: 7', inplace=True, axis =1) #deletes unnamed column 7
df.drop('Unnamed: 8', inplace=True, axis =1) #deletes unnamed column 8
df.drop('Unnamed: 9', inplace=True, axis =1) #deletes unnamed column 9

half = df[df['Unnamed: 2'].str.contains('1/2')] #makes a DataFrame with all the words containing '1/2'
half = half.astype({'Unnamed: 3':'int'}) #converts the 'Unnamed: 3' column into ints
half["BBLS"] = half["Unnamed: 3"]*0.00201613 #multiplies and creates the column 'bbls'

pint = df[df['Unnamed: 2'].str.contains('Pint')] #creates DataFrame of just Pints
pint2 = pint[pint["Unnamed: 2"].str.contains('1/2')==False] #removes all 1/2's from Pint list
pint2 = pint2.astype({'Unnamed: 3':'int'}) #converts column values from object to int
pint2["BBLS"] = pint2["Unnamed: 3"]*0.00403226

mug = df[df['Unnamed: 2'].str.contains('Mug')]
mug = mug.astype({'Unnamed: 3':'int'})
mug["BBLS"] = mug['Unnamed: 3']*0.00554435

ptr = df[df['Unnamed: 2'].str.contains('PTR')]
ptr = ptr.astype({'Unnamed: 3':'int'})
ptr["BBLS"] = ptr['Unnamed: 3']*0.01612903

thirtytwo = df[df['Unnamed: 2'].str.contains('32oz')]
thirtytwo = thirtytwo.astype({'Unnamed: 3':'int'})
thirtytwo["BBLS"] = thirtytwo['Unnamed: 3']*0.00806452

sixtyfour = df[df['Unnamed: 2'].str.contains('64oz')]
sixtyfour = sixtyfour.astype({'Unnamed: 3':'int'})
sixtyfour["BBLS"] = sixtyfour['Unnamed: 3']*0.01612903

total = df[df['Unnamed: 2'].str.contains('Tot')]

#print(df.columns) #prints the names of the columns in the DataFrame
#print(half)
#print(pint2)
#print(mug)
#print(ptr)
#print(thirtytwo)
#print(sixtyfour)
print(total)
#print(mug.dtypes)
#print(half['Unnamed: 3']*2)

#print(pint2.sum(axis = 0, skipna = True))
