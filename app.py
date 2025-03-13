## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
  # Output the list

#1

def calc(data):
    avg = []

    for row in data[1:]:      #Skips the first row
        store = row[0]        # First column is the store name
        nm = map(int, row[1:]) #Converted the sales into numbers
        sales = list(nm)
        total = sum(sales) / len(sales) #Found the average by dividing the sum of sales with how sales there were
        avg.append((store, total))
    
    print(avg)
    return avg
calc(data)

#2





    

    







    

