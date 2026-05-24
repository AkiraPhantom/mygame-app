import streamlit as st

# Page Configuration
st.set_page_config(page_title="Akira Phantom Gaming Assistant", page_icon="🎮", layout="centered")

# App Header
st.title("🎮 Akira Phantom Gaming Assistant")
st.write("Welcome to your advanced gaming strategy dashboard!")

st.markdown("---")

# FEATURE 1: Faction & Unit Analytics (Counter Picker)
st.header("🔥 Faction & Counter Picker Analytics")

faction = st.selectbox(
    "Select Faction:",
    ["Confederation", "Resistance", "Wuthering Echoes"]
)

# Dynamic Counter Strategy Logic
if faction == "Confederation":
    st.info("💡 **Faction Selected: Confederation.** Heavy Assault units are ready!")
    st.markdown("""
    **🎯 Tactical Strategy & Counters:**
    * **Best Against:** Resistance Infantry and Light Vehicles. (Use Heavy Assault to crush their frontlines).
    * **Counter Warning:** Watch out for enemy long-range Artillery and Snipers. 
    * **Pro Tip:** Deploy Shield Generators to protect your Heavy Assault infantry while pushing.
    """)
elif faction == "Resistance":
    st.info("💡 **Faction Selected: Resistance.** Guerrilla and Speed units are ready!")
    st.markdown("""
    **🎯 Tactical Strategy & Counters:**
    * **Best Against:** Slow-moving heavy armor and bases. (Use hit-and-run tactics).
    * **Counter Warning:** Highly vulnerable to Confederation Heavy Assault in direct face-to-face combat.
    * **Pro Tip:** Use camouflage and minefields to lure enemies into traps.
    """)
else:
    st.info("💡 **Faction Selected: Wuthering Echoes.** Resonance and Combat Skills Active!")
    st.markdown("""
    **🎯 Tactical Strategy & Counters:**
    * **Best Against:** Bosses and Elite single targets. (Perfect for fast parrying and dodging).
    * **Counter Warning:** Watch out for crowd control (CC) attacks from multiple mob spawns.
    * **Pro Tip:** Switch characters at 100% Concerto Energy to trigger powerful Intro/Outro skills.
    """)

st.markdown("---")

# FEATURE 2: Combat Damage & Stat Calculator
st.header("🧮 Combat Damage & Stat Calculator")
st.write("Calculate your unit or character potential power instantly.")

col1, col2 = st.columns(2)

with col1:
    base_atk = st.number_input("Base Attack Power (ATK):", min_value=1, value=100, step=10)
    level = st.slider("Character/Unit Level:", min_value=1, max_value=90, value=20)

with col2:
    crit_rate = st.slider("Crit Rate (%):", min_value=0, max_value=100, value=50)
    crit_dmg = st.number_input("Crit Damage (%):", min_value=100, value=150, step=5)

# Calculation Logic
level_multiplier = 1 + (level * 0.05)
scaled_atk = base_atk * level_multiplier
average_damage = scaled_atk * (1 + (crit_rate / 100) * ((crit_dmg - 100) / 100))

# Display Results
st.subheader("📊 Estimated Combat Results")
st.success(f"⚔️ **Scaled Attack (at Lv.{level}):** {scaled_atk:.1f}")
st.metric(label="💥 Expected Average Damage (DPS)", value=f"{average_damage:.1f}")

st.markdown("---")

# FEATURE 3: Match Tracker
st.header("📊 Match Tracker")
current_win_rate = st.slider("Current Win Rate (%)", min_value=0, max_value=100, value=86)
st.write(f"Your target win rate is locked at **{current_win_rate}%**.")

st.markdown("---")

# System Status Footer
st.success("Manager System: Connected & Operational! 🚀")