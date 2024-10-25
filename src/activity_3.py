from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def distribution_of_data(df):
    df.plot.hist(by=None, bins=10)

if __name__ == '__main__':
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data', 'paralympics_events_raw.csv')

    df_csv = pd.read_csv(paralympics_datafile_csv)

    df_csv['participants_m'].hist()
    plt.show()