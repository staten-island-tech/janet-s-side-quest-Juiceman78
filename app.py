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

def calc():
    total = {}

    for row in data[1:]:
        store = row[0]
        sales = map(int, row[1:])
        ind =+ 1
        total[store] = sum(sales)
        avg = total / ind
    calc()





    

    







    

