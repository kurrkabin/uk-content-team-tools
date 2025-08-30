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
            "name": "Cricket Reduced Settler - Rules NOT updated, do not use for now",
            "desc": "Reduce/settle outcomes quickly from copied market text.",
            "url": "https://cricketreducedsettler-fjcp9xykrrrn9cdjeuqb86.streamlit.app/"
        },
        {
            "name": "End Game Stats Extractor",
            "desc": "Scrape/format end-game stats for sheets.",
            "url": "https://cric-stats-extractor-bzapwd4g5z2vha7wldojku.streamlit.app/"
        },
    ],
    "Rugby/Aussie": [   # 👈 change header here
        {
            "name": "Rugby/Aussie Rules Scorers Creator",   # 👈 updated tool name
            "desc": "Paste Bet365 players page → clean columns.",
            "url": "https://rugbyleague.streamlit.app/"
        },
    ],
}


# --------- RENDER ---------
for sport, items in TOOLS.items():
    st.header(f"{'🏏' if sport=='Cricket' else '🏉'} {sport}")
    cols = st.columns(3, gap="large")
    for i, tool in enumerate(items):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="tool-card">
                  <h3>{tool['name']}</h3>
                  <div class="muted">{tool['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.link_button("Open", tool["url"], use_container_width=True)

st.divider()
st.caption("More Tools Could Be Added In The Future")
