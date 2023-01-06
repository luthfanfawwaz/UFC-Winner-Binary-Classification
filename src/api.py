from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import numpy as np
import util as utils
from data_preprocessing import scale_transform

config = utils.load_config()
model_data = utils.pickle_load(config["production_model_path"])
scaler = utils.pickle_load(config["scaler_path"])

# test using several feature
class api_data(BaseModel):
    lose_streak_dif:int
    win_streak_dif:int
    longest_win_streak_dif:int
    win_dif:int
    loss_dif:int
    total_round_dif:int
    total_title_bout_dif:int
    ko_dif:int
    sub_dif:int
    height_dif:float
    reach_dif:float
    age_dif:int

app = FastAPI()

@app.get("/")
def home():
    return "Hello, FastAPI up!"

@app.post("/predict/")
def predict(data: api_data):

    # Convert data api to dataframe
    preds = config["predictors"]
    data = pd.DataFrame(data).set_index(0).T.reset_index(drop = True)
    data.columns = preds

    # Convert dtype
    data = pd.concat(
        [
            data[config["float_columns"]].astype(np.float64),  # type: ignore
            data[config["int_columns"]].astype(np.int64)  # type: ignore
        ],
        axis = 1
    )

    # Scale the data
    data = scale_transform(df=data,
                           scaler=scaler,
                           preds=preds)

    # Predict data
    y_pred = model_data.predict(data)

    print(type(y_pred))
    print(y_pred)
    if y_pred[0] == 0:
        y_pred = "Biru Menang."
    else:
        y_pred = "Merah Menang."
    return {"res" : y_pred, "error_msg": ""}

if __name__ == "__main__":
    uvicorn.run("api:app", host = "0.0.0.0", port = 8080, reload=True)

