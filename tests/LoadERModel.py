import numpy
import os

import numpy as np
import pandas as pd

from src.Modules.EasyRefWorker import EasyReflectionWorker

path_file = r'data/EasyReflectionData/DepthsER_Gleb.txt'
model_init = EasyReflectionWorker()
model = model_init.calculate(path_file)

df_velocity = pd.DataFrame(model.velocity_model).T
df_velocity.columns = [f"vel_{i}" for i in range(df_velocity.shape[1])]
df_velocity.insert(0, "x_lines", model.x)
file_path = "velocity_model_t0.xlsx"
with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
    df_velocity.to_excel(writer, sheet_name='Velocity Model', index=False)

df_depth = pd.DataFrame(model.depth_model).T
df_depth.columns = [f"depth_{i + 1}" for i in range(df_depth.shape[1])]
df_depth.insert(0, "x_lines", model.x)
file_path = "df_depth_t0.xlsx"
with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
    df_depth.to_excel(writer, sheet_name='Depth Model', index=False)

print(111)

