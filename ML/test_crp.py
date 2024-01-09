import pandas as pd
import joblib as jb


def test_crop(data):
    model = jb.load('ML/crop_rf.pkl')

    y_pred = model.predict(data)
    ans = y_pred[0]

    def find_key_by_value(dictionary, target_value):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                nested_key = find_key_by_value(value, target_value)
                if nested_key is not None:
                    return key + '.' + nested_key
            elif value == target_value:
                return key
        return None

    with open("ML/map_crop.txt", "r") as file:
        maps = file.read()
        maps = eval(maps)

    result = find_key_by_value(maps, ans)
    if result is not None:
        key_name = result.split('.')[-1]
        return key_name
    else:
        return "result not found."