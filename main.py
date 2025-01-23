# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
from src.utils.bgg_api import use_bgg_api_directly, use_bgg_api


def main():
    st.title(' :game_die:  Dicey Insights')
    st.text('This page uses bgg-api by SukiCZ')
    #use_bgg_api()
    bg_data = pd.read_csv("datasets/board_games.csv")
    st.scatter_chart(bg_data, y='average_rating', x='users_rated',
                     y_label='Average rating',
                     x_label='Users rated [N]')

    def count_sep_by_commas(row):
        if not pd.isna(row):  # Check if row text is not empty
            return len(row.split(","))
        return 0

    bg_data['n_mechanics'] = bg_data["mechanic"].apply(count_sep_by_commas)
    #st.dataframe(bg_data)

    st.scatter_chart(bg_data, y='average_rating', x='n_mechanics',
                     y_label='Average rating',
                     x_label='Mechanics [N]')

    bg_data['n_categories'] = bg_data["category"].apply(count_sep_by_commas)
    st.scatter_chart(bg_data, y='average_rating', x='n_categories',
                     y_label='Average rating',
                     x_label='Categories [N]')



if __name__ == '__main__':
    main()

