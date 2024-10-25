from pathlib import Path
import pandas as pd

pd.set_option("display.max_columns", None)

def dataframe_data(dataframe):
    """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
    """
    #print(dataframe.shape)
    #print(dataframe.head())
    #print(dataframe.tail())
    #print(dataframe.columns)
    print(dataframe.dtypes)
    #print(dataframe.info)
    #print(dataframe.describe)

def prepare_data(df,npc):
    # Change columns' type
    float_columns = df.select_dtypes(include=['float64']).columns
    for col in float_columns:
        try:
            df[col] = df[col].astype('int')
        except ValueError as e:
            print(f"Error, can't convert column {df[col].name} to int: {e}")
    
    print("The change column type is:")
    print(df.loc[:, float_columns].dtypes)

    # Change display info
    df['start'] = pd.to_datetime(df['start'], format = '%d/%m/%Y')
    df['end'] = pd.to_datetime(df['end'], format = '%d/%m/%Y')

    # Merge two file with similar info in one column of each file 
    df_merge = df.merge(npc, how='left', left_on='country', right_on='Name')

    # Remove unwanted columns
    df_prepared = df.drop(columns=['URL', 'disabilities_included', 'highlights'], axis=1)

if __name__ == '__main__':
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data', 'paralympics_events_raw.csv')
    paralympics_datafile_xslx = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data', 'paralympics_all_raw.xlsx')
    npc_code = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data', 'npc_codes.csv')

    df_csv = pd.read_csv(paralympics_datafile_csv)
    df_xsl = pd.read_excel(paralympics_datafile_xslx)
    # Read only the column we need from a new file
    npc_df = pd.read_csv(npc_code, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])

    prepare_data(df_csv,npc_df)
    #change_type(df_xsl)

    dataframe_data(df_xsl)
    #print("Done")
    #dataframe_data(df_xsl)
    #print("Done")