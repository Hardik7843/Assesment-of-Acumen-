import pandas as pd
from .models import person


# Read CSV file into a DataFrame
csv_file_path = 'Sample.csv'
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():

    # Create the Product instance
    p = person(
        uniqe_id = row['uniqe_id'],
        email = row['email'],
        url = row['url']
    )
    #to save the current product
    if (p.is_valid()):
        person.save()
    


print("CSV data has been loaded into the Django database.")