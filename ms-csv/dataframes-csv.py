from pandas import *
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'users.csv')
customer_df = read_csv(csv_path
                    #    , names=['fname', 'lname', 'email', 'contact_number']  #it assumes the csv has no header and takes the passed values as header.
            )
print(customer_df)
customer_df.first_name[1] = 'Mayank'

print(customer_df)

customer_df.to_csv(os.path.join(current_dir, 'customers.csv'), index=False)