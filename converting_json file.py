#converting json file
from pathlib import Path
import json
import sentence_parser
def filterJson(json_file):
    list = []
    for a in json_file:
        each = a
        each["new_output"] = sentence_parser.main(a["input"])
        list.append(each)
    return list


path = "C:\\Users\\juna2\\testset\\"

temp = []
for json_file_name in Path(path).glob("*.json"):
    temp.append(json_file_name)
new_file_name = "C:\\Users\\juna2\\testset_filtered\\"
Path(new_file_name).mkdir(exist_ok=True)


a=1
for each_json_file in (temp):
    #print(order_data)
    with open(path+each_json_file.name,'r', encoding="UTF-8-sig") as json_file:
        json_to_python = json.load(json_file)
    filtered_json = filterJson(json_to_python)
    out_file3 = open(new_file_name+each_json_file.name, 'w', encoding = 'utf-8')
    json.dump(filtered_json, out_file3, indent = 4, sort_keys=False, ensure_ascii=False)
    out_file3.close()
    a+=1
    print("done and python is working on json file "+str(a))
