############### Utility Functions For World-Food-Facts Dataset #############

def getByCountry(dataset, country_name):
	country_regex = r'%s' % country_name
	isInCountry = dataset.countries_en.str.contains(country_regex)
	isInCountry = isInCountry.fillna(False)
	return dataset.loc[isInCountry]
