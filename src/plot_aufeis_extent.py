# -*- coding: utf-8 -*-
"""
created on: 2025-12-01
@author:    Jasper Heuer
use:        plot aufeis extent
"""

# import packages =============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

# set working directory =======================================================

base_path = "C:/Jasper/PhD/Classes/CEE_506_Environmental_Spatial_Data_Analysis/Project"
os.chdir(base_path)

# import data =================================================================

df = pd.read_csv("./data/aufeis_extent.csv", parse_dates=["date"])
df = df.drop(columns="Unnamed: 0")

plt.plot(df["date"][df["polygon"] == 1], df["area"][df["polygon"] == 1], label="Polygon 1")
plt.plot(df["date"][df["polygon"] == 2], df["area"][df["polygon"] == 2], label="Polygon 2")
plt.plot(df["date"][df["polygon"] == 3], df["area"][df["polygon"] == 3], label="Polygon 3")
plt.plot(df["date"][df["polygon"] == 4], df["area"][df["polygon"] == 4], label="Polygon 4")
plt.plot(df["date"][df["polygon"] == 5], df["area"][df["polygon"] == 5], label="Polygon 5")
plt.title("Aufeis extent over time")
plt.ylabel("Aufeis area in m²")
plt.xticks(rotation=45)
plt.legend()
plt.savefig("./data/aufeis_extent.png", dpi=300, bbox_inches="tight")
