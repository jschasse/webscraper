import streamlit as st
import pandas as pd
from constants import *

def start_window():
    rc = pd.read_csv(f"{FILEPATH}/table_1.csv")
    rows = rc.iterrows()
    df = pd.DataFrame({'first column': [1, 2, 3, 4] })
    
    df