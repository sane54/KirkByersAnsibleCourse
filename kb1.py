import yaml
import json
mylist = range(8)
mylist.append("notwithstanding")
mylist[8] = "hello"
mylist[0] = "hot"
mylist.append({})
mylist[-1] ['ip_address'] = "10.4.4.5"
mylist[-1] ["attributes"] = {}
mylist[-1] ["attributes"] ["name"] = "John"
file = open("kb1_yaml_dump", "w")
file.write(yaml.dump(mylist, default_flow_style = False) )
file.close()
file2 = open("kb1_json_dump", "w")
file2.write(json.dumps(mylist))
file2.close()
