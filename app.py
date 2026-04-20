import streamlit as st

st.set_page_config(page_title="UK Content Team Tools", layout="wide")

# --------- BRAND ---------
st.markdown(
    """
    <style>
      .tool-card {border:1px solid #eee; padding:18px 16px; border-radius:14px; box-shadow:0 2px 6px rgba(0,0,0,.06);}
      .tool-wrap {display:flex; gap:16px; flex-wrap:wrap;}
      .tool-card h3 {margin:0 0 6px 0;}
      .muted {color:#6b7280; font-size:0.95rem;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("UK Content Team Tools")
st.caption("Quick launchpad for sports utilities.")

# --------- CONFIG (edit this list to add more tools) ---------
TOOLS = {
    "Cricket": [
        {
            "name": "Cricket Reduced Matches Settler",
            "desc": "Reduce/settle outcomes quickly from copied market text.",
            "url": "https://cricketreducedsettler-fjcp9xykrrrn9cdjeuqb86.streamlit.app/",
        },
        {
            "name": "Cricket Player Props Extractor",
            "desc": "Parse Unibet markets → Boss-ready CSV/XLSX export.",
            "url": "https://cricket-player-props-extractor-jbf4b3rpyddzxnm3dgx279.streamlit.app/",
        },
        {
            "name": "Cricket Player Props Extractor Test Matches",
            "desc": "Test cricket (1st Innings): Top Bowler & Top Batter + Player of the Match.",
            "url": "https://cricket-player-props-extractor-test-matches-nunemh477kz2apjnhl.streamlit.app/",
        },
        {
            "name": "Player 365 Pricing (Cricket- New)",
            "desc": "Generate Bet365-style player markets from free-text names.",
            "url": "https://cricket-bet365-pricing-yftepvsmpjcf5iruyp8egg.streamlit.app/",
        },
    ]
}

# --------- RENDER ---------
st.header("🚀 All Tools")

# Flatten to one list
all_tools = []
for items in TOOLS.values():
    all_tools.extend(items)

# Up to 5 columns
num_tools = len(all_tools)
num_cols = min(5, max(1, num_tools))
cols = st.columns(num_cols, gap="large")

for i, tool in enumerate(all_tools):
    with cols[i % num_cols]:
        st.markdown(
            f"""
            <div class="tool-card">
              <h3>{tool['name']}</h3>
              <div class="muted">{tool['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("Open", tool["url"], use_container_width=True)

st.divider()
st.caption("More tools could be added in the future.")
