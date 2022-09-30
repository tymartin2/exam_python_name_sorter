import sys 
#reader method to read the csv file to be sorted
import csv

args = 2
cli_args = len(sys.argv)

if cli_args < args : 
	print('Argument Missing: 2nd parameter is required')
else: 
	#get second argument from cli
	random_csv = sys.argv[1].lower()

	if random_csv.endswith('.csv') :
		
		#acquiring the file to read and sort.
		file = open(random_csv, 'r')

		#convert the csv file to a csv object, with ',' to separate the columns. 
		csv_object = csv.reader(file, delimiter=',')

		#convert the object to a list allowing the data to be sorted. 
		nested_list = list(csv_object)

		#alphabetically sorted data.  
		sorted_list = sorted(nested_list, key=lambda x: x[1])

		#close the sorter file. 
		file.close()

		#open a new file where the sorted data will be written and stored.
		new_csv = open('sorted_names.csv', 'w+', newline='') 
		#to create a writer object to convert the input/data into strings.
		csv_writer = csv.writer(new_csv, delimiter=',')

		#to identify the data that will be placed in each column.
		csv_writer.writerow(['Given Name', 'Last Name'])

		#display the sorted data into the new csv file. 
		csv_writer.writerows(sorted_list)
	else :
		print('Incorrect File: csv file required')