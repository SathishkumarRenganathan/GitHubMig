samsung = {
    "model1" : {
        "Model": "J6",
        "Year": 2019,
        "Features": {"Camera","Screen Size","Memory"}
    },
    "model2" : {
        "Model": "J3",
        "Year": 2021,
        "Features": {"Camera","Screen Size","Memory", "Video Call"}
    }
}
samsung["model2"]["Year"] = 2028
print(samsung["model2"]["Year"])
#print(samsung)
#print(samsung["Year"])
#samsung["Year"]=2020
print(samsung["model1"]["Year"])
print(len(samsung["model2"]))

x = samsung["model2"].keys()
print(x)

samsung["model1"].update({"Model": "M10"})
print("By Using Update method: ", samsung["model1"])
samsung["model1"]["price"] = 10000
print("After add the keys: ", samsung["model1"])
samsung["model1"].pop("price")
print("After pop: ", samsung["model1"])

for x in samsung:
    no=samsung[x]["Year"]
    if(no == 2028):
        print("duplicate")
        #raise Exception("Duplicate year found!!!")
    else:
        print("Unique")
        samsung[x]["Release Date"] = '12-Jul-2025'


dictName = {
    "key1":"Value1",
    "key2":"Value2",
    "key3": ''
}

print(dictName)
print(samsung)
#delete the keys
del dictName["key2"]
print(dictName)

#items method
print('Using items metho: ',dictName.items())

#Check keys are exist
for key in samsung["model1"].keys():
    if key in samsung["model2"].keys():
        print("Keys are available")
    else:
        print("Keys are not available")

