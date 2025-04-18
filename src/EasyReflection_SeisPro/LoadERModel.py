import numpy as np
import pandas as pd
from .scheme.Model import EasyReflectionModel


class EasyReflectionLoadModel:

    @staticmethod
    def LoadModelER(path_file):
        data = []
        with open(path_file, 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines):
                if idx == 0:
                    values = line.strip().split('\t')
                    columns = list(column for column in values if column)
                else:
                    line_data = line.strip().split('\t')
                    line_data = [str(value).replace(',', '.') if isinstance(value, str) else value for value in
                                 line_data]
                    data.append(line_data)
        return data, columns

    @staticmethod
    def CreatePandasTable(data, columns):
        table = pd.DataFrame(data)
        table.columns = columns
        for i in table.columns:
            series = table[i].replace([None, ''], np.nan).to_numpy().astype(float)
            idx_pass_st = np.where(~np.isnan(series))[0][0]
            idx_pass_end = np.where(~np.isnan(series))[0][-1]
            table.loc[idx_pass_end + 1:, i] = -99999
            table.loc[:idx_pass_st - 1, i] = -99999
        return table

    @staticmethod
    def ReplaceToNone(table):
        table = table.applymap(lambda x: np.nan if x == '' or x == 'NaN' else x).astype(float)
        return table

    @staticmethod
    def GetModel(table, mode = 'Z'):
        return table.loc[:, table.columns.str.startswith(mode)].to_numpy()

    def GetEasyReflection(self, path_file):
        data, column_names = self.LoadModelER(path_file)
        table = self.CreatePandasTable(data, column_names)
        table = self.ReplaceToNone(table)

        x = table.X.to_numpy().astype(float)
        relief = table.Alt.to_numpy().astype(float)
        depth_model = self.GetModel(table, 'Z').T
        velocity_model = self.GetModel(table, 'V').T

        model = EasyReflectionModel(x, relief, depth_model, velocity_model)

        return model



