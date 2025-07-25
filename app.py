
import streamlit as st
from core.poisson_model import estimate_goal_probabilities

st.set_page_config(page_title="MLB - Over 1.5 / 2.5 Probabilités", layout="wide")

st.title("📊 Prédiction de Buts - Modèle Poisson")

col1, col2 = st.columns(2)
with col1:
    home_avg_goals = st.number_input("Moyenne de buts de l'équipe à domicile", min_value=0.0, value=1.8)
with col2:
    away_avg_goals = st.number_input("Moyenne de buts de l'équipe à l'extérieur", min_value=0.0, value=1.2)

if st.button("Calculer les probabilités"):
    result = estimate_goal_probabilities(home_avg_goals, away_avg_goals)
    st.success("Probabilités estimées :")
    st.write(f"✅ Over 1.5 : {result['over_1_5']} %")
    st.write(f"✅ Over 2.5 : {result['over_2_5']} %")
    st.write(f"🤝 BTTS (Both Teams To Score) : {result['btts']} %")
