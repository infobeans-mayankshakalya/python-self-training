from pandas import *

cric_scores = {
    'Kohli': [72, 45, 89],
    'Rohit': [56, 102, 34],
    'KLRahul': [23, 67, 54],
    'Bumrah': [2, 10, 5]
}

df = DataFrame(cric_scores, index=[1,2,3])
print(df)
print(df.index)
print(df.idxmin)
print(df.idxmax)


print('Kohli\'s Scores:')
print(df.Kohli)

print(df.Kohli[3])

print(df.loc[1]) # this will get by matching the exact key number.
print(df.iloc[1]) # this would result the 2nd column values based on the array index patterns which starts from 0, hence 1 is the 2nd index.


print(df.iloc[1:2])
print(df.iloc[[1,2]])
print(df.loc[1:2,['Kohli', 'Bumrah']])

print(df[df>100])
print(df[(df<100) & (df>50)])

print(df.at[2, 'Kohli'])
print(df.iat[2, 0])

# Sorting
print(df.sort_index(ascending=False))
print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(axis=1))

print(df.sort_values(by=1, axis=1, ascending=True))