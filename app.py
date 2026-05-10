# =========================================================
# 🌸 Bloom With Care
# Interactive Flower Growth Simulator
# Built with Python & Streamlit
# =========================================================

# ---------------- IMPORT LIBRARIES ----------------
import streamlit as st
import random

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Bloom With Care 🌸",
    page_icon="🌸",
    layout="wide"
)

# =========================================================
# CUSTOM CSS STYLING
# =========================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to bottom right, #fce7f3, #ede9fe, #dbeafe);
    color: #374151;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #bbf7d0, #bfdbfe);
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: #1f2937;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #db2777;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #6b7280;
    margin-bottom: 30px;
}

/* Card Design */
.card {
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Flower Display */
.flower {
    text-align: center;
    font-size: 120px;
    animation: float 3s ease-in-out infinite;
}

/* Floating Animation */
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #ec4899, #8b5cf6);
    color: white;
    border-radius: 12px;
    border: none;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
}

/* Footer */
.footer {
    text-align: center;
    color: #6b7280;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🌸 Bloom With Care")

    st.markdown("---")

    mode = st.radio(
        "🌿 Select Mode",
        [
            "🏠 Home",
            "💧 Water Plant",
            "📖 About"
        ]
    )

    st.markdown("---")

    dark_mode = st.toggle("🌙 Dark Mode")

    st.markdown("---")

    st.success("Nature Simulation App")

# =========================================================
# DARK MODE
# =========================================================

if dark_mode:

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #111827, #1f2937);
        color: white;
    }

    .card {
        background: rgba(255,255,255,0.08);
        color: white;
    }

    .subtitle {
        color: #d1d5db;
    }

    </style>
    """, unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "health" not in st.session_state:
    st.session_state.health = 50

if "happiness" not in st.session_state:
    st.session_state.happiness = 50

# =========================================================
# HOME PAGE
# =========================================================

if mode == "🏠 Home":

    st.markdown(
        '<div class="main-title">🌸 Bloom With Care</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">A relaxing flower care simulator built with Streamlit</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h2>🌿 Welcome Gardener!</h2>
        <p>
        Your mission is to take care of your flower by watering it properly.
        Too little water makes it dry 🥀 and too much water weakens it 🌧️.
        Give the perfect amount of water and watch your flower bloom beautifully 🌸
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Display Flower Stage
    health = st.session_state.health

    if health <= 20:
        flower = "🥀"

    elif health <= 40:
        flower = "🌱"

    elif health <= 70:
        flower = "🌿"

    elif health <= 90:
        flower = "🌷"

    else:
        flower = "🌸"

    st.markdown(
        f'<div class="flower">{flower}</div>',
        unsafe_allow_html=True
    )

    # Progress Bars
    st.markdown("### 🌱 Plant Health")
    st.progress(st.session_state.health)

    st.markdown("### 😊 Happiness Level")
    st.progress(st.session_state.happiness)

# =========================================================
# WATERING PAGE
# =========================================================

elif mode == "💧 Water Plant":

    st.markdown(
        '<div class="main-title">💧 Water Your Flower</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
    Adjust the water level carefully to help your flower grow.
    </div>
    """, unsafe_allow_html=True)

    # Water Slider
    water = st.slider(
        "🌧️ Select Water Amount",
        0,
        100,
        50
    )

    # Water Button
    if st.button("💦 Water Plant"):

        # Too Little Water
        if water <= 30:

            st.session_state.health -= 15
            st.session_state.happiness -= 10

            st.warning("🥀 Your flower is drying. It needs more water!")

            flower = "🥀"

        # Healthy Watering
        elif 31 <= water <= 70:

            st.session_state.health += 15
            st.session_state.happiness += 20

            st.success("🌸 Perfect watering! Your flower is blooming beautifully!")

            st.balloons()

            flower = "🌸"

        # Too Much Water
        else:

            st.session_state.health -= 10
            st.session_state.happiness -= 5

            st.error("🌧️ Too much water! Your flower is overwatered.")

            flower = "🌧️"

        # Limit Values
        st.session_state.health = max(0, min(100, st.session_state.health))
        st.session_state.happiness = max(0, min(100, st.session_state.happiness))

        # Flower Display
        st.markdown(
            f'<div class="flower">{flower}</div>',
            unsafe_allow_html=True
        )

    # Health Meter
    st.markdown("### 🌱 Plant Health")
    st.progress(st.session_state.health)

    # Happiness Meter
    st.markdown("### 😊 Happiness Score")
    st.progress(st.session_state.happiness)

    # Motivational Quotes
    quotes = [
        "🌼 Every flower blooms at its own pace.",
        "☀️ Small care creates beautiful growth.",
        "🌸 Happiness blooms from within.",
        "🌿 Nature always rewards patience."
    ]

    st.info(random.choice(quotes))

    # Reset Button
    if st.button("🔄 Reset Garden"):

        st.session_state.health = 50
        st.session_state.happiness = 50

        st.success("🌱 Garden has been reset!")

# =========================================================
# ABOUT PAGE
# =========================================================

elif mode == "📖 About":

    st.markdown(
        '<div class="main-title">📖 About This App</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>🌸 Bloom With Care</h3>

        <p>
        This interactive application was developed using:
        </p>

        <ul>
            <li>Python 🐍</li>
            <li>Streamlit ⚡</li>
            <li>Custom CSS 🎨</li>
        </ul>

        <p>
        The project simulates emotional plant care and demonstrates how
        proper nurturing helps flowers grow and bloom beautifully.
        </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
🌸 Made with love using Python & Streamlit
</div>
""", unsafe_allow_html=True)
