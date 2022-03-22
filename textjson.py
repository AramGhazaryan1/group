#import json
#import yaml

#with open('task_urls.json') as f:
#    file_1 = f.read()
#    json_data = json.loads(file_1)
#   print(type(json_data))


#with open('new.yaml','w') as file:
#    yaml.dump(json_data, file)


import json
import yaml
def read_json():
    try:
        with open('task_urls.json') as f:
            file_1 = f.read()
            json_data = json.loads(file_1)
        with open('new.yaml','w') as file:
        	yaml.dump(json_data, file)


    except FileNotFoundError:
        print("File does not exist.")
    except json.decoder.JSONDecodeError:
   		print("this file a problem accessing the equipment data. ")


read_json()
