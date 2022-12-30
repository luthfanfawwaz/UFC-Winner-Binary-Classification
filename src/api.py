from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import numpy as np
import util as utils

config = utils.load_config()
model_data = utils.pickle_load(config["production_model_path"])

# test using several feature
class api_data(BaseModel):
    Red_odds: float
    Blue_odds: float
    Gender: str

app = FastAPI()

@app.get("/")
def home():
    return "Hello, FastAPI up!"

# @app.post("/predict/")
# def predict(data: api_data):    
#     # Convert data api to dataframe
#     preds = config["predictors"]
#     data = pd.DataFrame(data).set_index(0).T.reset_index(drop = True)  # type: ignore
#     data.columns = preds

#     # Convert dtype
#     data = pd.concat(
#         [
#             data[config["predictors"][:4]].astype(np.float64),  # type: ignore
#             data[config["predictors"][4:]].astype(np.int64)  # type: ignore
#         ],
#         axis = 1
#     )

#     # Check range data
#     try:
#         data_pipeline.check_data(data, config, True)  # type: ignore
#     except AssertionError as ae:
#         return {"res": [], "error_msg": str(ae)}

#     # Predict data
#     y_pred = model_data.predict(data)

#     if y_pred[0] == 0:
#         y_pred = "Tidak ada api."
#     else:
#         y_pred = "Ada api."
#     return {"res" : y_pred, "error_msg": ""}

if __name__ == "__main__":
    uvicorn.run("api:app", host = "127.0.0.1", port = 8080)
