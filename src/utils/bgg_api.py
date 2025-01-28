import streamlit as st
from boardgamegeek import BGGClient
import sys
import requests
import time
import xml.etree.ElementTree as ET


def use_bgg_api(game_name):
    bgg = BGGClient()
    game = bgg.games(game_name)
    st.write("Rating average", game[0].rating_average)
    st.write("Year", game[0].year)


def use_bgg_api_directly(mindate = '2024-01-01', maxdate = '2024-02-01'):
    # Retrieve command line arguments
    # if len(sys.argv) < 3:
    #     print("Please provide mindate and maxdate parameters.")
    #     sys.exit(1)
    # mindate = sys.argv[1]
    # maxdate = sys.argv[2]

    # API request URL
    # url = f'https://boardgamegeek.com/xmlapi2/plays?username=pkufahl&min...={mindate}&maxdate={maxdate}&type=thing&subtype=boardgame&brief=1'
    url = f'https://boardgamegeek.com/xmlapi2/thing?type=boardgame&id=1000'

    # Make the API request
    response = requests.get(url)

    while response.status_code == 202:
        print("Waiting for response...")
        time.sleep(0.33)
        response = requests.get(url)

    if response.status_code != 200:
        print(f'url request failed with code {response.status_code}')
        exit(1)

    xml_str = response.text
    st.write(xml_str)

    # Parse the XML string
    root = ET.fromstring(xml_str)

    # Extract game IDs and number of plays
    # games = root.findall('.//play/item')
    # plays_per_game = {}
    # for game in games:
    #     game_id = game.attrib['objectid']
    #     st.write(game.attrib)
    #     st.write(game_id)

