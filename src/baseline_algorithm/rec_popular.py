from pathlib import Path

import click
import pandas as pd

from src.baseline_algorithm.functions import *

current_directory = Path(__file__).absolute().parent
default_data_directory = current_directory.joinpath('..', '..', 'data')


# @click.command()
# @click.option('--data-path', default="/Users/jarana/local/workspace/ucl/recsys2019/datasets/", help='Directory for the CSV files')
def main(data_path):

    # calculate path to files
    data_directory = Path(data_path) if data_path else default_data_directory
    train_csv = data_directory.joinpath('train.csv')
    test_csv = data_directory.joinpath('test.csv')
    subm_csv = data_directory.joinpath('submission_popular.csv')

    print("Reading {train_csv} ...")
    df_train = pd.read_csv(train_csv)
    print("Reading {test_csv} ...")
    df_test = pd.read_csv(test_csv)

    print("Get popular items...")
    df_popular = get_popularity(df_train)

    print("Identify target rows...")
    df_target = get_submission_target(df_test)

    print("Get recommendations...")
    df_expl = explode(df_target, "impressions")
    df_out = calc_recommendation(df_expl, df_popular)

    print("Writing {subm_csv}...")
    df_out.to_csv(subm_csv, index=False)

    print("Finished calculating recommendations.")


if __name__ == '__main__':
    main("/Users/jarana/local/workspace/ucl/recsys2019/datasets/")
