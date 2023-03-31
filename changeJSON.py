import json

for i in range(1,1001):
    with open(str(i) + ".json", "r") as json_file:
        json_data = json.load(json_file)
        json_data.pop('edition')
        json_data.pop('compiler')
        with open(str(i) + ".json", 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

#reference
#https://abluesnake.tistory.com/107
