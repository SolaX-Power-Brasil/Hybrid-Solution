
from api_common import *

if __name__ == "__main__":
    root_folder = "../"
    for file_name in threePhase_220V_files:
        data = get_data(file_path = root_folder + file_name)
        if data != None:
            insert_all_records(data=data, url_api=api_production_post_3p_220_hv_bat)
            
    #for file_name in threePhase_380V_files:
    #    data = get_data(file_path = root_folder + file_name)
    #    if data != None:
    #        insert_all_records(data=data)
    print("Finished")
                
