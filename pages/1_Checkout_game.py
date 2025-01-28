import streamlit as st
import pandas as pd
from src.utils.bgg_api import use_bgg_api


def main():
    st.title(' :game_die:  Checkout a single game')
    st.text('This page uses bgg-api by SukiCZ')
    bg_ranks = pd.read_csv("datasets/boardgames_ranks.csv")

    # Get only games with over 100 user ratings
    bg_ranks_filt = bg_ranks[bg_ranks['usersrated'] > 100]
    del bg_ranks

    # Select a game and get info
    selected_name = st.selectbox('Select a game', bg_ranks_filt['name'])
    use_bgg_api(selected_name)


if __name__ == '__main__':
    main()
