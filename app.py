import streamlit as st
import pandas as pd
import altair as alt

# பக்கத்தின் அமைப்பு (Wide Layout)
st.set_page_config(page_title="Cricket Analytics Dashboard", layout="wide", page_icon="🏏")

# கஸ்டம் CSS மூலம் பேக்ரவுண்டை பிளாக் கலராகவும், டெக்ஸ்ட் கலரை வெள்ளையாகவும் வைத்தல்
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6, span, p, label {
        color: #ffffff !important;
    }
    .stMetric {
        background-color: #1e2530;
        padding: 10px;
        border-radius: 10px;
        border-left: 5px solid #ffcc00;
    }
    </style>
""", unsafe_allow_html=True)

st.title(" Comprehensive IPL & Cricket Analytics Dashboard")
st.markdown("---")

# CSV ஃபைல்களை லோட் செய்தல் (Caching உடன்)
@st.cache_data
def load_all_data():
    try:
        matches = pd.read_csv("matches.csv")
        deliveries = pd.read_csv("deliveries.csv")
        batting = pd.read_csv("batting_stats.csv")
        bowling = pd.read_csv("bowling_stats.csv")
        fielding = pd.read_csv("fielding_stats.csv")
        points = pd.read_csv("points_table.csv")
        squads = pd.read_csv("squads.csv")
        venues = pd.read_csv("venues.csv")
        return matches, deliveries, batting, bowling, fielding, points, squads, venues
    except Exception as e:
        return None, None, None, None, None, None, None, None

matches_df, deliveries_df, batting_df, bowling_df, fielding_df, points_df, squads_df, venues_df = load_all_data()

# மஞ்சள் நிற பார் சார்ட் உருவாக்குவதற்கான ஃபங்ஷன் (Yellow Bar Chart)
def yellow_bar_chart(data, x_col, y_col):
    chart = alt.Chart(data).mark_bar(color='#ffcc00').encode(
        x=alt.X(x_col, sort='-y', title=x_col),
        y=alt.Y(y_col, title=y_col)
    ).properties(
        background='#0e1117',
        config={
            'view': {'stroke': 'transparent'},
            'axis': {'domainColor': 'white', 'tickColor': 'white', 'labelColor': 'white', 'titleColor': 'white'}
        }
    )
    st.altair_chart(chart, use_container_width=True)

# சைட்பாரில் நேவிகேஷன்
st.sidebar.title("📊 Select Section")
page = st.sidebar.radio("Go to", [
    "IPL Teams & Trophies", 
    "Matches", 
    "Deliveries", 
    "Batting Stats", 
    "Bowling Stats", 
    "Fielding Stats", 
    "Points Table", 
    "Squads", 
    "Venues"
])

# 0. IPL Teams & Trophies Section (Ordered as requested)
if page == "IPL Teams & Trophies":
    st.header("🏆 IPL Teams, Trophies & Championship Moments")
    st.markdown("இங்கு நீங்கள் குறிப்பிட்ட வரிசைப்படி ஐபிஎல் அணிகள் மற்றும் கோப்பை விவரங்கள் கொடுக்கப்பட்டுள்ளன:")
    
    teams_trophies_data = [
        {
            "name": "Chennai Super Kings (CSK)",
            "titles": "5 Times Champions (2010, 2011, 2018, 2021, 2023)",
            "city": "Chennai",
            "home": "MA Chidambaram Stadium",
            "logo": "https://wallpaperaccess.com/thumb/4679541.jpg"
        },
        {
            "name": "Mumbai Indians (MI)",
            "titles": "5 Times Champions (2013, 2015, 2017, 2019, 2020)",
            "city": "Mumbai",
            "home": "Wankhede Stadium",
            "logo": "https://wallpaperaccess.com/thumb/2302511.jpg"
        },
        {
            "name": "Rajasthan Royals (RR)",
            "titles": "1 Time Champion (2008)",
            "city": "Jaipur",
            "home": "Sawai Mansingh Stadium",
            "logo": "https://wallpaperaccess.com/full/3961272.jpg"
        },
        {
            "name": "Sunrisers Hyderabad (SRH)",
            "titles": "2 Times Champions (2009, 2016)",
            "city": "Hyderabad",
            "home": "Rajiv Gandhi Stadium",
            "logo": "https://wallpaperaccess.com/full/4105816.jpg"
        },
        {
            "name": "Punjab Kings (PBKS)",
            "titles": "Runners-up",
            "city": "Mohali",
            "home": "PCA Stadium",
            "logo": "https://wallpaperaccess.com/full/8008926.png"
        },
        {
            "name": "Kolkata Knight Riders (KKR)",
            "titles": "3 Times Champions (2012, 2014, 2024)",
            "city": "Kolkata",
            "home": "Eden Gardens",
            "logo": "https://wallpaperaccess.com/full/3746298.jpg"
        },
        {
            "name": "Delhi Capitals (DC)",
            "titles": "Playoffs Contenders",
            "city": "Delhi",
            "home": "Arun Jaitley Stadium",
            "logo": "https://wallpaperaccess.com/full/4033881.png"
        },
        {
            "name": "Gujarat Titans (GT)",
            "titles": "1 Time Champion (2022)",
            "city": "Ahmedabad",
            "home": "Narendra Modi Stadium",
            "logo": "https://wallpaperaccess.com/full/9253197.jpg"
        },
        {
            "name": "Royal Challengers Bengaluru (RCB)",
            "titles": "🔥 Champions (2025, 2026)",
            "city": "Bengaluru",
            "home": "M. Chinnaswamy Stadium",
            "logo": "https://wallpaperaccess.com/full/14748374.jpg"
        }
    ]

    # Grid வடிவத்தில் அணிகளின் விவரங்கள் மற்றும் புகைப்படங்களைக் காட்டுதல்
    for i in range(0, len(teams_trophies_data), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(teams_trophies_data):
                team = teams_trophies_data[i + j]
                with cols[j]:
                    with st.container(border=True):
                        st.image(team['logo'], width=130)
                        st.markdown(f"<h4 style='color: #ffcc00; margin: 8px 0 4px 0;'>{team['name']}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<p style='color: #00ffcc; font-size: 14px; margin: 0;'><b>🏆 {team['titles']}</b></p>", unsafe_allow_html=True)
                        st.markdown(f"<p style='color: #ffffff; margin: 5px 0 0 0; font-size: 13px;'><b>City:</b> {team['city']}</p>", unsafe_allow_html=True)
                        st.markdown(f"<p style='color: #cccccc; font-size: 12px; margin: 2px 0 0 0;'><b>Home:</b> {team['home']}</p>", unsafe_allow_html=True)

# 1. Matches Section
elif page == "Matches":
    st.header("🏟️ Matches Statistics & Visuals")
    if matches_df is not None:
        col1, col2 = st.columns(2)
        col1.metric("Total Matches Played", len(matches_df))
        if 'match_winner' in matches_df.columns:
            col2.metric("Total Teams Won", matches_df['match_winner'].nunique())
        
        st.markdown("---")
        st.subheader("🏆 Match Winners Breakdown")
        if 'match_winner' in matches_df.columns:
            winner_df = matches_df['match_winner'].value_counts().reset_index()
            winner_df.columns = ['Team', 'Count']
            yellow_bar_chart(winner_df, 'Team', 'Count')
            
        st.subheader("🪙 Toss Decisions Visual")
        if 'toss_decision' in matches_df.columns:
            toss_df = matches_df['toss_decision'].value_counts().reset_index()
            toss_df.columns = ['Decision', 'Count']
            yellow_bar_chart(toss_df, 'Decision', 'Count')
            
        st.subheader("📋 Detailed Matches Data")
        st.dataframe(matches_df)
    else:
        st.error("matches.csv file not found!")

# 2. Deliveries Section
elif page == "Deliveries":
    st.header("⚾ Deliveries (Ball-by-Ball) Visuals")
    if deliveries_df is not None:
        st.metric("Total Deliveries Recorded", len(deliveries_df))
        st.markdown("---")
        if 'total_runs' in deliveries_df.columns:
            st.subheader("📊 Runs Distribution in Deliveries")
            runs_df = deliveries_df['total_runs'].value_counts().sort_index().reset_index()
            runs_df.columns = ['Runs', 'Count']
            runs_df['Runs'] = runs_df['Runs'].astype(str)
            yellow_bar_chart(runs_df, 'Runs', 'Count')
        st.subheader("📋 Deliveries Data Preview")
        st.dataframe(deliveries_df.head(1000))
    else:
        st.error("deliveries.csv file not found!")

# 3. Batting Stats Section
elif page == "Batting Stats":
    st.header("🏏 Batting Statistics & Visuals")
    if batting_df is not None:
        st.metric("Total Batting Records", len(batting_df))
        st.markdown("---")
        st.subheader("📋 Batting Stats Data")
        st.dataframe(batting_df)
    else:
        st.error("batting_stats.csv file not found!")

# 4. Bowling Stats Section
elif page == "Bowling Stats":
    st.header("🎯 Bowling Statistics & Visuals")
    if bowling_df is not None:
        st.metric("Total Bowling Records", len(bowling_df))
        st.markdown("---")
        st.subheader("📋 Bowling Stats Data")
        st.dataframe(bowling_df)
    else:
        st.error("bowling_stats.csv file not found!")

# 5. Fielding Stats Section
elif page == "Fielding Stats":
    st.header("🧤 Fielding Statistics & Visuals")
    if fielding_df is not None:
        st.metric("Total Fielding Records", len(fielding_df))
        st.markdown("---")
        if 'catches' in fielding_df.columns and 'player' in fielding_df.columns:
            st.subheader("📊 Catches Visual Breakdown")
            catches_df = fielding_df.sort_values(by='catches', ascending=False).head(10)
            yellow_bar_chart(catches_df, 'player', 'catches')
        st.subheader("📋 Fielding Stats Data")
        st.dataframe(fielding_df)
    else:
        st.error("fielding_stats.csv file not found!")

# 6. Points Table Section
elif page == "Points Table":
    st.header("🏆 Points Table & Visuals")
    points_df = points_df if points_df is not None else None
    if points_df is not None:
        st.metric("Teams in Points Table", len(points_df))
        st.markdown("---")
        if 'points' in points_df.columns and 'team' in points_df.columns:
            st.subheader("📊 Team Points Comparison")
            yellow_bar_chart(points_df, 'team', 'points')
        st.subheader("📋 Points Table Data")
        st.dataframe(points_df)
    else:
        st.error("points_table.csv file not found!")

# 7. Squads Section
elif page == "Squads":
    st.header("👥 Squads Information")
    if squads_df is not None:
        st.metric("Total Squad Entries", len(squads_df))
        st.markdown("---")
        st.subheader("📋 Squads Data")
        st.dataframe(squads_df)
    else:
        st.error("squads.csv file not found!")

# 8. Venues Section
elif page == "Venues":
    st.header("📍 Venues Information & Visuals")
    if venues_df is not None:
        st.metric("Total Venues", len(venues_df))
        st.markdown("---")
        st.subheader("📋 Venues Data")
        st.dataframe(venues_df)
    else:
        st.error("venues.csv file not found!")