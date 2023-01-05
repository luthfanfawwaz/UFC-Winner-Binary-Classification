import pandas as pd

def scale_transform(df: pd.DataFrame, scaler, preds: list ) -> pd.DataFrame:
    df_scaled = pd.DataFrame(scaler.transform(df[preds]),
        index = df.index,
        columns = df[preds].columns
    )

    return df_scaled