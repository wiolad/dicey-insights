import streamlit as st
import pandas as pd
from src.utils.bgg_api import use_bgg_api


def main():
    st.title(' :game_die:  Checkout single game')
    st.text('This page uses bgg-api by SukiCZ')
    bg_ranks = pd.read_csv("datasets/boardgames_ranks.csv")
    selected_name = st.selectbox('Select a game', bg_ranks['name'])
    use_bgg_api(selected_name)


if __name__ == '__main__':
    main()
