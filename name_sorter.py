#reader method to read the csv file to be sorted
import csv

#acquiring the file to read and sort.
file = open('random_name.csv', 'r')

#convert the csv file to a csv object, with ',' to separate the columns. 
csv_object = csv.reader(file, delimiter=',')

#convert the object to a list allowing the data to be sorted. 
nested_list = list(csv_object)

#alphabetically sorted data.
   #key -> specifies a function of one argument that is used to extract a comparison from each element of the list
   #lambda -> a function that acted as a value of a key to treat string elements as an integer to assess each element properly. 
   #x: x[1] -> used to describe which column will be used to sort the elements.  
sorted_list = sorted(nested_list, key=lambda x: x[1])

#close the sorter file. 
file.close()

#open a new file where the sorted data will be written and stored.
	#w+ -> to overwrite the file everytime it is executed. 
	#newline -> to prevent extra white spaces in between in row.
new_csv = open('sorted_names.csv', 'w+', newline='') 

#to create a writer object to convert the input/data into strings.
csv_writer = csv.writer(new_csv, delimiter=',')

#to identify the data that will be placed in each column.
csv_writer.writerow(['Given Name', 'Last Name'])

#display the sorted data into the new csv file. 
csv_writer.writerows(sorted_list)












