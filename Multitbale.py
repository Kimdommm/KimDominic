rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
table = [[(a + 1) * (b + 1) for b in range(cols)] for a in range(rows)]
print("\nMultiplication Table:")
for row in table:
    print('\t'.join(str(val) for val in row))
search_num = int(input("\nEnter a number to search: "))
found = False
for a, row in enumerate(table):
    for b, val in enumerate(row):
        if val == search_num:
            print(f"Number {search_num} found at Row {a+1}, Column {b+1}")
            found = True
if not found:
    print(f"Number {search_num} not found in the table.")