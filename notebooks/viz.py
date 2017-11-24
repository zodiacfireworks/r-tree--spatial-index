# Ajustes generales para los gráficos
from distutils.spawn import find_executable

from matplotlib.font_manager import *
from matplotlib.collections import *
from matplotlib.patches import *
from matplotlib.pylab import *
from matplotlib import colors

import osmnx as ox
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from descartes import PolygonPatch
from shapely.geometry import Point, Polygon, MultiPolygon

import seaborn
import gc

ioff()

rc('lines', linewidth=1)
rc('font', family='serif')

if find_executable('latex'):
    rc('text', usetex=True)

font_title = FontProperties(size=(1.728 * 12))
font_label = FontProperties(size=(1.2 * 12))
font_legend = FontProperties(size=(1.0 * 12))
font_ticks = FontProperties(size=(0.833 * 12))

seaborn.set(context='notebook', style='darkgrid')

ox.config(
    log_console=True,
    use_cache=True
)

# Programa
district_name = input("Ingrese el nombre del distrito: ")

while True:
    LIMA31 = ox.gdf_from_place(
        '{0}, Lima, Perú'.format(district_name)
    )

