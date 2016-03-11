import csv
import operator

def dict_of_med_prices():
	csv_file = ('lmpriser.csv')
	with open(csv_file, 'rb') as f:
	    next(f)
	    reader = csv.reader(f)
	    for row in reader:
			price_list = list()
			if len(row[142]) > 0: #select only current medicin  - still makes an empty list - fix it!	
				counter = 1 
				for cell in row:
					if counter > 8 and len(cell) > 0: #skip the first 8 rows and the empty cells
						float_cell = float(cell.replace(',', ''))
						price_list.append(float_cell)
					else:
						price_list.append(None)
					counter += 1
			else:
				price_list.append(0)
			d = dict()
			for value in price_list:
				d.setdefault(row[1] + ' ' + row[2] + ' ' + row[6] + ' ' + row[7], []).append(value) #making dict of key = varenummer+variabel, value = list of prices
			yield d
	f.close()

def dict_of_pct_increase(dic):
	for value in dic:
		for key in value.keys():
			prices = value[key]
			last_price = float(prices[-1])
			min_price = float(min(value for value in prices if value is not None))
			try:
				pct_increase = (last_price-min_price) / min_price * 100
				price_dict = {key: pct_increase}
			except:
				price_dict = {key: 0}
			yield price_dict

def write_highest_increase_csv():
	new_d = dict() # joining dicts in one dict
	for d in dict_of_pct_increase(dict_of_med_prices()):
		for key in d.keys():
			if 'aup' in key: # aup is the code for sell prices
				new_d[key] = d[key] 
	with open('outfile.csv', 'wb') as csvfile:
		sorted_increase = sorted(new_d.items(), key=operator.itemgetter(1))
		for item in sorted_increase:
			dicwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			dicwriter.writerow(item)
	csvfile.close()


write_highest_increase_csv()