import os

# Save the Data as a .csv file into given file path
def save_data_as_csv(Data, filepath):
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise
        with open(filepath, 'w') as datafile:
            Data.to_csv(filepath, sep=',', encoding='utf-8')
