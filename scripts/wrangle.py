import pandas as pd
def wrangle(file_path):
    df = pd.read_csv(file_path)
    print('Hello World')
    return df