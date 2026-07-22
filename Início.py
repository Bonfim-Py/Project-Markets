print("BOTAFOGO")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as sts

data_frame = "Data_frame_Market.csv"
df = pd.read_csv(data_frame)
df.head()
df.info()
df.columns


