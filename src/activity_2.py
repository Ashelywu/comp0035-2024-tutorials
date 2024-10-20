from pathlib import Path
import pandas as pd

def dataframe_data(dataframe):
    """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
    """
    print(dataframe.shape)
    pd.set_option("display.max_columns", None)
    #print(dataframe.head)
    #print(dataframe.tail)
    #print(dataframe.columns)
    print(dataframe.dtypes)
    #print(dataframe.info)
    #print(dataframe.describe)

def change_type(Dataframe):
    i = 0
    columns_to_change= ['countries', 'events', 'participants_m', 'participants_f', 'participants']
    for i in range(0, 5):
        column_name = columns_to_change[i]
        Dataframe[column_name] = Dataframe[column_name].astype('int')
        i+=1

def change_date_time(dataframe):
    dataframe['start'] = pd.to_datetime(dataframe['start'], format = '%d/%m/%Y')

if __name__ == '__main__':
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data', 'paralympics_events_raw.csv')
    paralympics_datafile_xslx = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data', 'paralympics_all_raw.xlsx')

    df_csv = pd.read_csv(paralympics_datafile_csv)
    df_xsl = pd.read_excel(paralympics_datafile_xslx)

    #change_type(df_csv)
    #change_type(df_xsl)

    dataframe_data(df_csv)
    print("Done")
    dataframe_data(df_xsl)
    print("Done")

    change_date_time(df_csv)