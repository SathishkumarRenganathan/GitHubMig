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

print(samsung)
#print(samsung["Year"])
#samsung["Year"]=2020
print(samsung["model1"]["Year"])

for x in samsung:
    no=samsung[x]["Year"]
    if(no == 2021):
        print("duplicate")
        raise Exception("Duplicate year found!!!")
    else:
        print("Unique")
