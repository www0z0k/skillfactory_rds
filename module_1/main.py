import pandas as pd
import numpy as np
import os
from IPython.display import display

pd.set_option('display.max_rows', 1200)
pd.set_option('display.max_columns', 20)

data = pd.read_csv('data.csv')
#1
# display(data[data.budget == data.budget.max()])
#2
# display(data[data.runtime == data.runtime.max()])
#3
# display(data[data.runtime == data.runtime.min()])
#4
# display(data.runtime.mean())
#5
# display(data.runtime.median())
data['profit'] = data['revenue'] - data['budget']
#6
# display(data[data['profit'] == data['profit'].max()])
#7
# display(data[data['profit'] == data['profit'].min()])
#8
# display(data[data['profit'] > 0].count())
# display(len(data[data['profit'] > 0]))

#9
# d2008 = data[data['release_year'] == 2008]
# display(d2008[d2008['profit'] == d2008['profit'].max()])

#10
# sliced = data.query('2011 < release_year < 2015')
# display(sliced[sliced['profit'] == sliced['profit'].min()])

#11
def get_genres(df, g):
	return df[df.genres.str.contains(g)]

all_genres = []
unique_genre_sets = data.genres.unique()
for lst in unique_genre_sets:
	genre_names = lst.split('|')
	for g in genre_names:
		if g not in all_genres:
			all_genres.append(g)

#####
# TODO - make a kind of sorted array when I got time
#####

# display(len(get_genres(data, 'Action')))
# display(len(get_genres(data, 'Adventure')))
# display(len(get_genres(data, 'Drama')))
# display(len(get_genres(data, 'Comedy')))
# display(len(get_genres(data, 'Thriller')))

#12
# display(len(get_genres(data, 'Action').query('profit > 0')))
# display(len(get_genres(data, 'Adventure').query('profit > 0')))
# display(len(get_genres(data, 'Drama').query('profit > 0')))
# display(len(get_genres(data, 'Comedy').query('profit > 0')))
# display(len(get_genres(data, 'Thriller').query('profit > 0')))

#13 - this one looks better than previous two
# display(data.query('director in ["Steven Spielberg", "Ridley Scott", "Steven Soderbergh", "Christopher Nolan", "Clint Eastwood"]').director.value_counts())

#14
# display(data.query('director in ["Steven Spielberg", "Ridley Scott", "Steven Soderbergh", "Christopher Nolan", "Clint Eastwood"] & profit > 0').director.value_counts())

#15
# pivot = data.loc[data['director'].isin(["Steven Spielberg", "James Cameron", "Christopher Nolan", "David Yates", "Peter Jackson"])].pivot_table(values=['profit'],
# index=['director'],
# aggfunc='sum',
# fill_value=0)
# display(pivot)

#16
# display(data.query('cast.str.contains("Emma Watson")').profit.sum())
# display(data.query('cast.str.contains("Johnny Depp")').profit.sum())
# display(data.query('cast.str.contains("Michelle Rodriguez")').profit.sum())
# display(data.query('cast.str.contains("Orlando Bloom")').profit.sum())
# display(data.query('cast.str.contains("Rupert Grint")').profit.sum())

#17
def get_profit_by_actor(df, actor):
	return df.query('cast.str.contains("' + actor + '")').profit.sum()

d2012 = data[data['release_year'] == 2012]
# df = pd.DataFrame({'Nicolas Cage': [get_profit_by_actor(d2012, 'Nicolas Cage')], 
# 'Danny Huston': [get_profit_by_actor(d2012, 'Danny Huston')], 
# 'Kirsten Dunst': [get_profit_by_actor(d2012, 'Kirsten Dunst')], 
# 'Jim Sturgess': [get_profit_by_actor(d2012, 'Jim Sturgess')], 
# 'Sami Gayle': [get_profit_by_actor(d2012, 'Sami Gayle')]})
# display(df)

#18
avg = data.budget.mean()
high_budget = data[data.budget > avg]
# display(len(high_budget.query('cast.str.contains("Tom Cruise")')))
# display(len(high_budget.query('cast.str.contains("Mark Wahlberg")')))
# display(len(high_budget.query('cast.str.contains("Matt Damon")')))
# display(len(high_budget.query('cast.str.contains("Angelina Jolie")')))
# display(len(high_budget.query('cast.str.contains("Adam Sandler")')))

#19
cage = data.query('cast.str.contains("Nicolas Cage")')
# display(len(get_genres(cage, 'Drama')))
# display(len(get_genres(cage, 'Action')))
# display(len(get_genres(cage, 'Thriller')))
# display(len(get_genres(cage, 'Adventure')))
# display(len(get_genres(cage, 'Crime')))

#20
# display(len(data.query('production_companies.str.contains("Universal")')))
# display(len(data.query('production_companies.str.contains("Paramount Pictures")')))
# display(len(data.query('production_companies.str.contains("Columbia Pictures")')))
# display(len(data.query('production_companies.str.contains("Warner Bros")')))
# display(len(data.query('production_companies.str.contains("Twentieth Century Fox Film Corporation")')))

#21
d2015 = data[data['release_year'] == 2015]
# display(len(d2015.query('production_companies.str.contains("Universal Pictures")')))
# display(len(d2015.query('production_companies.str.contains("Paramount Pictures")')))
# display(len(d2015.query('production_companies.str.contains("Columbia Pictures")')))
# display(len(d2015.query('production_companies.str.contains("Warner Bros")')))
# display(len(d2015.query('production_companies.str.contains("Twentieth Century Fox Film Corporation")')))

#22
def named_field_entries_count(df, field, s):
	return s + ' ' + str(len(df.query(field + '.str.contains("' + s + '")')))

def named_field_entries_sum(df, field, s, inner):
	return s + ' ' + str((df.query(field + '.str.contains("' + s + '")')[inner].sum()))


comedies = get_genres(data, 'Comedy')
# print(named_field_entries_sum(comedies, 'production_companies', 'Warner Bros', 'profit'))
# print(named_field_entries_sum(comedies, 'production_companies', 'Universal', 'profit'))
# print(named_field_entries_sum(comedies, 'production_companies', 'Columbia Pictures', 'profit'))
# print(named_field_entries_sum(comedies, 'production_companies', 'Paramount Pictures', 'profit'))
# print(named_field_entries_sum(comedies, 'production_companies', 'Walt Disney', 'profit'))

#23
def field_entries_count(df, field, s):
	return len(df.query(field + '.str.contains("' + s + '")'))

def field_entries_sum(df, field, s, inner):
	return df.query(field + '.str.contains("' + s + '")')[inner].sum()


# df = pd.DataFrame({'Universal': [field_entries_sum(d2012, 'production_companies', 'Universal', 'profit')],
# 'Warner Bros': [field_entries_sum(d2012, 'production_companies', 'Warner Bros', 'profit')],
# 'Columbia Pictures': [field_entries_sum(d2012, 'production_companies', 'Columbia Pictures', 'profit')],
# 'Paramount Pictures': [field_entries_sum(d2012, 'production_companies', 'Paramount Pictures', 'profit')],
# 'Lucasfilm': [field_entries_sum(d2012, 'production_companies', 'Lucasfilm', 'profit')]
# })
# display(df)

#24
paramounts = data.query('production_companies.str.contains("Paramount Pictures")')
# display(paramounts[paramounts.profit == paramounts.profit.min()])

#25
# pivot = data.loc[data['release_year'].isin([2002, 2008, 2012, 2014, 2015])].pivot_table(values=['profit'],
# index=['release_year'],
# aggfunc='sum',
# fill_value=0)
# display(pivot)

#26
# warners = data.query('production_companies.str.contains("Warner Bros")')
# pivot = warners.loc[warners['release_year'].isin([2002, 2008, 2012, 2014, 2015])].pivot_table(values=['profit'],
# index=['release_year'],
# aggfunc='sum',
# fill_value=0)
# display(pivot)

#27
def by_month(df, index):
	return df[df.release_date.str.find(index, 0, len(index)) == 0]

jan = by_month(data, '1/')
jun = by_month(data, '6/')
dec = by_month(data, '12/')
sep = by_month(data, '9/')
may = by_month(data, '5/')
# display(len(jan), len(jun), len(dec), len(sep), len(may))

#28
jul = by_month(data, '7/')
aug = by_month(data, '8/')
# display(len(jun) + len(jul) + len(aug))
def field_entries_sum(df, field, s, inner):
	return df.query(field + '.str.contains("' + s + '")')[inner].sum()


#29
# display(len(data[(data['director'] == "Steven Soderbergh") & ((data.release_date.str.find('1/', 0, len('1/')) == 0) | (data.release_date.str.find('2/', 0, len('2/')) == 0) | (data.release_date.str.find('12/', 0, len('12/')) == 0))]))
# display(len(data[(data['director'] == "Christopher Nolan") & ((data.release_date.str.find('1/', 0, len('1/')) == 0) | (data.release_date.str.find('2/', 0, len('2/')) == 0) | (data.release_date.str.find('12/', 0, len('12/')) == 0))]))
# display(len(data[(data['director'] == "Clint Eastwood") & ((data.release_date.str.find('1/', 0, len('1/')) == 0) | (data.release_date.str.find('2/', 0, len('2/')) == 0) | (data.release_date.str.find('12/', 0, len('12/')) == 0))]))
# display(len(data[(data['director'] == "Ridley Scott") & ((data.release_date.str.find('1/', 0, len('1/')) == 0) | (data.release_date.str.find('2/', 0, len('2/')) == 0) | (data.release_date.str.find('12/', 0, len('12/')) == 0))]))
# display(len(data[(data['director'] == "Peter Jackson") & ((data.release_date.str.find('1/', 0, len('1/')) == 0) | (data.release_date.str.find('2/', 0, len('2/')) == 0) | (data.release_date.str.find('12/', 0, len('12/')) == 0))]))

#30 Think more!!!
# years = data.release_year.unique()
# lst = []
# for y in years:
# 	lst.append([y, jan.query('release_year == ' + str(y)).profit.sum(), jun.query('release_year == ' + str(y)).profit.sum(), dec.query('release_year == ' + str(y)).profit.sum(), sep.query('release_year == ' + str(y)).profit.sum(), may.query('release_year == ' + str(y)).profit.sum()])

# df = pd.DataFrame(np.array(lst), columns = ['y', 'jan', 'jun', 'dec', 'sep', 'may'])
# df['mv'] = df.max(axis = 1)

#31
# display(data.query('production_companies.str.contains("Universal")').original_title.str.len().mean())
# display(data.query('production_companies.str.contains("Warner Bros")').original_title.str.len().mean())
# display(data.query('production_companies.str.contains("Jim Henson Company, The")').original_title.str.len().mean())
# display(data.query('production_companies.str.contains("Paramount Pictures")').original_title.str.len().mean())
# display(data.query('production_companies.str.contains("Four By Two Productions")').original_title.str.len().mean())

#32
# display(data.query('production_companies.str.contains("Universal")').original_title.str.split().map(lambda a: len(a)).mean())
# display(data.query('production_companies.str.contains("Warner Bros")').original_title.str.split().map(lambda a: len(a)).mean())
# display(data.query('production_companies.str.contains("Jim Henson Company, The")').original_title.str.split().map(lambda a: len(a)).mean())
# display(data.query('production_companies.str.contains("Paramount Pictures")').original_title.str.split().map(lambda a: len(a)).mean())
# display(data.query('production_companies.str.contains("Four By Two Productions")').original_title.str.split().map(lambda a: len(a)).mean())

#33
# names = data.original_title.values.tolist();

# words = []
# for w in names:
# 	arr = w.split(' ')
# 	for s in arr:
# 		if s.lower() not in words:
# 			words.append(s.lower())
# print(len(words))

#34
# topsorted = data.sort_values('vote_average', ascending = False)
# display(topsorted.head(int(0.01 * len(topsorted))))

#35
# display(len(data.query('cast.str.contains("Johnny Depp") & cast.str.contains("Helena Bonham Carter")')))
# display(len(data.query('cast.str.contains("Hugh Jackman") & cast.str.contains("Ian McKellen")')))
# display(len(data.query('cast.str.contains("Vin Diesel") & cast.str.contains("Paul Walker")')))
# display(len(data.query('cast.str.contains("Adam Sandler") & cast.str.contains("Kevin James")')))
# display(len(data.query('cast.str.contains("Daniel Radcliffe") & cast.str.contains("Rupert Grint")')))

#36
# display(len(data.query('director == "Quentin Tarantino" & profit > 0')) / len(data.query('director == "Quentin Tarantino"')))
# display(len(data.query('director == "Steven Soderbergh" & profit > 0')) / len(data.query('director == "Steven Soderbergh"')))
# display(len(data.query('director == "Robert Rodriguez" & profit > 0')) / len(data.query('director == "Robert Rodriguez"')))
# display(len(data.query('director == "Christopher Nolan" & profit > 0')) / len(data.query('director == "Christopher Nolan"')))
# display(len(data.query('director == "Clint Eastwood" & profit > 0')) / len(data.query('director == "Clint Eastwood"')))




