############### Utility Functions For World-Food-Facts Dataset #############
import pandas as pd

def getByCountry(dataset, country_name):
	country_regex = r'%s' % country_name
	isInCountry = dataset.countries_en.str.contains(country_regex)
	isInCountry = isInCountry.fillna(False)
	return dataset.loc[isInCountry]

def getUniqueCountries(dataset):
	return_list = []
	unique_countries_raw = dataset.countries_en.unique()
	for country in unique_countries_raw:
		x = str(country).split(',')
		if (len(x) == 1 and x[0] != 'nan'):
			return_list.append(x[0])
	return return_list

def getAvg(dataset, nutriment):
	return dataset[nutriment][dataset[nutriment].notnull()].mean()

def compareCountriesByNutrimentAverage(data, countries, nutriment):
	df = pd.DataFrame(index=['average'], columns=countries)
	for i in range(len(countries)):
		country = countries[i]
		country_data = getByCountry(data, country)
		if (country_data[nutriment].notnull().sum() > 30):
			avg = getAvg(country_data, nutriment)
			df[country] = avg
	return df.T.sort_values(by='average', axis=0).dropna()
