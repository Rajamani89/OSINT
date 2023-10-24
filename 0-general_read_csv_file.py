import csv

# Define a list to store the IP addresses
ip_addresses = []

# Specify the path to your CSV file
# Replace with the path to your CSV file
file_path = "ip_addresses.csv"  

# Open and read the CSV file
with open(file_path, mode='r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Assuming the IP address is in the first column (index 0)
        ip_address = row[0]
        ip_addresses.append(ip_address)

# Now, the 'ip_addresses' list contains all the IP addresses from the CSV file
print("IP Addresses:", ip_addresses)
