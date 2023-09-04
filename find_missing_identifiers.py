from openxds_session import Openxds_session
from utils import get_identifiers_from_csv
from utils import write_data_to_csv

def main():
    filename = input("Enter CSV file name: ")
    openxds_session = Openxds_session()
    identifiers = get_identifiers_from_csv(filename)
    found_identifiers = []
    missing_identifiers = []
    for identifier in identifiers:
        if(identifier.is_identifier_in_openxds(openxds_session)):
            found_identifiers.append(identifier)
        else:
            missing_identifiers.append(identifier)
        
    print("=================Found identifiers=================\n")
    for identifier in found_identifiers:
        print(identifier.identifier+"\n")
        print("\n")

    print("=================Missing identifiers=================\n")
    for identifier in missing_identifiers:
        print(identifier.identifier+"\n")

    write_data_to_csv("found_identifiers.csv", found_identifiers)
    write_data_to_csv("missing_identifiers.csv", missing_identifiers)



main()