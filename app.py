import streamlit as st
from core.poisson_model import estimate_goal_probabilities

st.set_page_config(page_title="Prédiction de Buts - Modèle Poisson", layout="centered")

st.title("📊 Prédiction de Buts - Modèle Poisson")

# Champs pour noms d'équipes
home_team = st.text_input("🏠 Nom de l'équipe à domicile", "Équipe A")
away_team = st.text_input("🚗 Nom de l'équipe à l’extérieur", "Équipe B")

# Moyennes de buts
home_avg_goals = st.number_input(f"Moyenne de buts pour {home_team} (domicile)", min_value=0.0, max_value=5.0, step=0.1, value=1.8)
away_avg_goals = st.number_input(f"Moyenne de buts pour {away_team} (extérieur)", min_value=0.0, max_value=5.0, step=0.1, value=1.2)

if st.button("📊 Calculer les probabilités"):
    result = estimate_goal_probabilities(home_avg_goals, away_avg_goals)

    st.subheader(f"🔮 Probabilités estimées : {home_team} vs {away_team}")
    st.success(f"✅ Over 1.5 : {result['over_1_5']} %")
    st.success(f"✅ Over 2.5 : {result['over_2_5']} %")
    st.info(f"🟠 BTTS (Both Teams To Score) : {result['btts']} %")
