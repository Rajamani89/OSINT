"70.32.23.72",
import pythonfofa
import csv
import time

# Initialize the FOFA Client with your email and API key
client = pythonfofa.Client(email='enter your email', key='EnterApikey')

# Define a list of IP addresses to search for
ip_addresses = ["72.9.100.68",
"85.187.128.49",
"88.99.242.20"]
timer = 1
# Create or open a CSV file to save the results
with open('fofa_results.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['IP', 'URL', 'Port'])

    # Iterate over the list of IP addresses
    for ip in ip_addresses:
        # Define the query string for searching the current IP address
        query_str = f'ip="{ip}"'
        print ("Printing value ",timer," now")
        timer = timer + 1

        # Perform the search
        results = client.search(query_str)

        # Get the first result from the list (if available)
        first_result = results['results'][0] if 'results' in results and len(results['results']) > 0 else []

        # Extract IP, Country, and City information
        ip = first_result[0] if len(first_result) > 0 else 'N/A'
        url = first_result[1] if len(first_result) > 1 else 'N/A'
        port = first_result[2] if len(first_result) > 2 else 'N/A'

        # Write the data to the CSV file
        writer.writerow([ip, url, port])



        # Add a delay of 30 seconds between queries
        time.sleep(1)
