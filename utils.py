import csv
from identifier import Identifier

def get_identifiers_from_csv(file):
    identifiers = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None) #Skip header
        for row in csv_reader:
            identifier = Identifier(row[0])
            identifiers.append(identifier)
        return identifiers
    
 
def write_data_to_csv(filename, identifier_array):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        header = ["identifier"]
        writer.writerow(header)
        for identifier in identifier_array:
            writer.writerow([identifier.identifier])
