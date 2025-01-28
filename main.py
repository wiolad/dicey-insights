import streamlit as st
import pandas as pd
from src.utils.bgg_api import use_bgg_api


def main():
    st.title(' :game_die:  Dicey Insights')
    bg_data = pd.read_csv("datasets/board_games.csv")

    vars_dict = {
        'Users rated [N]': 'users_rated',
        'Mechanics [N]': 'n_mechanics',
        'Categories [N]': 'n_categories'
     }

    selection = st.selectbox("Select variable to plot",
                             vars_dict.keys())

    def count_sep_by_commas(row):
        if not pd.isna(row):  # Check if row text is not empty
            return len(row.split(","))
        return 0

    bg_data['n_mechanics'] = bg_data["mechanic"].apply(count_sep_by_commas)
    bg_data['n_categories'] = bg_data["category"].apply(count_sep_by_commas)

    st.scatter_chart(bg_data,
                     x=vars_dict[selection], x_label=selection,
                     y='average_rating', y_label='Average rating')


if __name__ == '__main__':
    main()

