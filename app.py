import pandas as pd 
import numpy as np
import streamlit as st

def load_data():
    return pd.read_csv(r"C:\Users\55149\OneDrive - Fatec Centro Paula Souza\Documents\repos\curso_git\projeto\data\raw\bike.csv")

def main():
    df=load_data()

    st.dataframe(df)

if __name__=='__main__':
        main()

