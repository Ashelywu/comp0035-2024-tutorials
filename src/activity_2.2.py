from pathlib import Path
import pandas as pd

def dataframe_data(dataframe):

    print(dataframe.shape)
    

if __name__ == '__main__':
    datafile_csv = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data', 'paralympics_events_raw.csv')
    datafile_xslx = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data', 'paralympics_all_raw.xlsx')

    df_csv = pd.read_csv(datafile_csv)
    df_xsl = pd.read_excel(datafile_xslx)

    dataframe_data(df_csv)
    dataframe_data(df_xsl)
    print("Done")