
import pandas as pd
import os


'''
# Change History #
Version : Initial
Programmed by : Aadesh
Date : 20-JUNE-2021

'''

# Following class encapsulates function for loading and preparing data for further process
class loadData:

    def __init__(self, data_dir, file_name) -> None:
        self.data_dir = data_dir
        self.file_name = file_name

    '''
    # purpose of the function is to check the input dataset file is present in the mentioned directory
    # If yes then return cleansed data as dataframe
    # returns : Dataframe - object containing clean data 
    '''
    def load_data(self) -> object:
        working_dir = os.getcwd()
        dataset = os.path.join(working_dir,self.data_dir,self.file_name)
        if os.path.exists(dataset):
            print('file {} found in given directory'.format(self.file_name))
            raw_data = pd.read_csv(dataset)
            cleaned_data = raw_data.drop(['url_legal', 'license'], axis=1)
            cleaned_data = cleaned_data.replace({'excerpt' : '\W+'}, {'excerpt' : ' '}, regex=True)
            return cleaned_data
        else:
            print ('directory {} doesnot exist'.format(self.data_dir))