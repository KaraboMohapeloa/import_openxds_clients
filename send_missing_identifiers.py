from openxds_session import Openxds_session
from utils import get_identifiers_from_csv
from utils import write_data_to_csv
import time

def main():
    filename = input("Enter CSV file name: ")
    openxds_session = Openxds_session()
    identifiers = get_identifiers_from_csv(filename)
    sent_identifiers = []
    failed_identifiers = []
    batch = 0
    for identifier in identifiers:
        batch+=1
        if(batch == 500):
            time.sleep(15)
            batch = 0
        if(identifier.send_to_openxds(openxds_session)):
            sent_identifiers.append(identifier)
        else:
            failed_identifiers.append(identifier)
        
    print("=================Found identifiers=================\n")
    for identifier in sent_identifiers:
        print(identifier.identifier+"\n")

    print("=================Missing identifiers=================\n")
    for identifier in failed_identifiers:
        print(identifier.identifier+"\n")

    write_data_to_csv("sent_identifiers.csv", sent_identifiers)
    write_data_to_csv("failed_identifiers.csv", failed_identifiers)



main()