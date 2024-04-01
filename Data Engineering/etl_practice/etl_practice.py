import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime


'''
create a log file and output file
'''

log_file = 'log_file.txt'
target_file = 'transformed_data.csv'


# 1. Extract data from different file formats

def extract_from_csv(file_to_process):
    data = pd.read_csv(file_to_process)
    return data



def extract_from_json(file_to_process):
    data = pd.read_json(file_to_process, lines=True)
    return data


def extract_from_xml(file_to_process):
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    headers = ['car_model', 'year_of_manufacture', 'price', 'fuel']
    rows=[]
    for row in root:
        car_model=row.find('car_model').text
        year_of_manufacture=row.find('year_of_manufacture').text
        price=row.find('price').text
        fuel=row.find('fuel').text
        rows.append({'car_model':car_model, 'year_of_manufacture':year_of_manufacture, 'price':price, 'fuel':fuel})
    data=pd.DataFrame(rows, columns=headers)
    return data



def extract():
    extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
    for file in glob.glob('*.csv'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(file))], ignore_index=True)
    for file in glob.glob('*.json'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(file))], ignore_index=True)
    for file in glob.glob('*.xml'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(file))], ignore_index=True)
    return extracted_data



# 2. Transform 


def transform(data):
    data['price'] = data['price'].astype(str).radd('$')
    return data


# 3. Load and Log

def load(target_file, transformed_data):
    transformed_data.to_csv(target_file, index=False)


def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
            f.write(timestamp + ',' + message + '\n') 

log("ETL Job Started") 

log("Extract phase Started") 
extracted_data = extract() 
log("Extract phase Ended")

log("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data") 
print(transformed_data) 
log("Transform phase Ended")

log("Load phase Started")
load(target_file, transformed_data)
log("Load phase Ended")

log("ETL Job Ended")
