# MockPLC.py
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import os

class MockPLC:
    dataset_path = 'nphantawee/pump-sensor-data/'
    file_name = 'sensor.csv'
    destination_path = './datasets/'

    def sensor_output(self):
        """
        Uses the download_csv_from_kaggle function to download a dataset and
        outputs a pandas DataFrame with the content of the dataset.
    """

        # Download the CSV file from Kaggle
        self.download_csv_from_kaggle(self.dataset_path, self.file_name, self.destination_path)

        # Construct the full path to the CSV file
        csv_file_path = os.path.join(self.destination_path, self.file_name)

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Return the DataFrame
        return df

    def download_csv_from_kaggle(self, dataset_path, file_name, destination_path):
        """
        Downloads a specific CSV file from a Kaggle dataset.

        Parameters:
        - dataset_path: Path to the dataset on Kaggle (e.g., 'ownerSlug/some-dataset')
        - file_name: Name of the CSV file to download (e.g., 'data.csv')
        - destination_path: Local path where the CSV should be saved
        """
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_file(dataset_path, file_name, path=destination_path)
        print(f"Downloaded {file_name} to {destination_path}")

        # Check if the file has been downloaded as a zip file, then extract it
        zip_file_path = os.path.join(destination_path, file_name + '.zip')
        if os.path.exists(zip_file_path):
            import zipfile
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(destination_path)
            print(f"Extracted {file_name}.zip to {destination_path}")

if __name__ == '__main__':
    print(MockPLC().sensor_output().describe())