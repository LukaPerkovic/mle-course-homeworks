import urllib.request as urllib
import zipfile
import pandas as pd
from io import StringIO


class BikeRentalDataLoader:
    def __init__(self):

        self.url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip"

    def fetch_file(self):

        filehandle, _ = urllib.urlretrieve(self.url)
        zip_file_object = zipfile.ZipFile(filehandle, "r")
        first_file = zip_file_object.namelist()[2]
        file = zip_file_object.open(first_file)

        return file.read()

    def csv_to_pandas_dataframe(self, file):
        s = str(file, "utf-8")
        df = pd.read_csv(StringIO(s))

        return df

    def get_data(self):
        csv = self.fetch_file()

        return self.csv_to_pandas_dataframe(file=csv)
