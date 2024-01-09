import pandas as pd
import joblib as jb

def test_fertilizer(df):
    model=jb.load('ML/ftlzr_rf.pkl')

    with open("ML/map_ftlzr.txt", "r") as file:
        maps = file.read()
        maps = eval(maps)

        for i in ["Crop Type"]:
            df[i].replace(maps[i],inplace=True)
    
    ypred=model.predict(df)
    ans=ypred[0]

    fertilizer_dict = {key: value for key, value in maps['fertilizer'].items()}

    def get_fertilizer_name(value):
        for key, val in fertilizer_dict.items():
            if val == value:
                return key
        return None

    fertilizer_value = ans
    fertilizer_name = get_fertilizer_name(fertilizer_value)
    return fertilizer_name

    