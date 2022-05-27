import argparse
import os
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db") # required to enable model registry in local development
mlflow.set_experiment("hw2-random-forest-experiment")
mlflow.sklearn.autolog(disable=False)

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


def train(data_path:str):

    with mlflow.start_run():

        X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
        X_valid, y_valid = load_pickle(os.path.join(data_path, "valid.pkl"))

        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_valid)

        rmse = mean_squared_error(y_valid, y_pred, squared=False)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        default="./artifacts/data/processed",
        help="the location where the processed NYC taxi trip data was saved."
    )
    args = parser.parse_args()

    train(args.data_path)
