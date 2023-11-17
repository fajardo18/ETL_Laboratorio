import pandas as pd
from typing import Set
import requests
import sqlite3


def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    data = pd.read_csv('us-cities-demographics.csv', sep=';')
    data = pd.DataFrame(data)
    data = data.drop(['Race', 'Count', 'Number of Veterans'], axis=1)
    data.drop_duplicates(inplace=True)
    data.to_csv("demographics-limpio.csv")
    return data


def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    pass
