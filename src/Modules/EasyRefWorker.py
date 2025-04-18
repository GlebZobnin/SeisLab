import numpy as np

from src.EasyReflection_SeisPro.LoadERModel import EasyReflectionLoadModel
from src.Interpolations.LinearInterpolation import Interp1D
from plot.EasyReflection.ERModel import ERPlot

class EasyReflectionWorker:

    def __init__(self):
        self.er_model_init = EasyReflectionLoadModel()
        self.interp1d = Interp1D

    def Interpolation1D(self, x, map):
        for i in range(len(map)):
            map[i] = self.interp1d(x, map[i])
        idx_replace = np.where(map == -99999)
        map[idx_replace] = np.nan
        return map

    def calculate(self, path_file, mode_plot = 'True'):

        model = self.er_model_init.GetEasyReflection(path_file)
        model.depth_model = self.Interpolation1D(model.x, model.depth_model)
        model.velocity_model = self.Interpolation1D(model.x, model.velocity_model)


        if mode_plot:
            ERPlot(model)

        return model


