""" numbers = [1, 2, 3, 4, 5]

# Use map() to double the numbers
doubled_numbers = map(lambda x: x * 2, numbers)

print(list(doubled_numbers)) """

""" data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row (skip this)
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

for row in data[1:]:  # Skip the first row
    print(row) """

""" def calcRow(data):
    row_totals = {}

    for row in data[1:]:  # Skipping the first row
        store_name = row[0]  # First column is the store name
        sales = map(int, row[1:])  # Convert sales to numbers
        row_totals[store_name] = sum(sales)  # Sum up sales for the store

    return row_totals

# Example Data
sales_data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

totals = calcRow(sales_data)
print(totals) """

temperatures = ["Label", 32, 50, 77, 104]

# Use map() to convert Fahrenheit to Celsius, skipping the first item

def calc():
    cel = 0

    for temp in temperatures[1:]:
      cel = (temp - 32)*(5/9)
      print(cel)
calc()

map(calc, temperatures)