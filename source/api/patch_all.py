
from api_common import *

if __name__ == "__main__":
    for file_name in files:
        root_folder = "../"
        data = get_data(file_path = root_folder + file_name)
        if data != None:
            insert_all_records(data=data)

    print("Finished")
                
