import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Bytes",
    page_icon="📰",
    layout="wide"
)

nav1, nav2, nav3 = st.columns([1,2,1])
with nav3:
    st.page_link(
        "pages/About AI Bytes.py",
        label="ℹ️ About"
    )

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).parent

CSS_FILE = BASE_DIR / "styles" / "style.css"
LOGO_FILE = BASE_DIR / "assets" / "logo.png"
JSON_FILE = BASE_DIR / "ai_bytes.json"
TOP10_FILE = BASE_DIR / "top10_insights.json"

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

def load_css():
    try:
        with open(CSS_FILE, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("styles/style.css not found")

# load_css()

# --------------------------------------------------
# LOAD JSON DATA
# --------------------------------------------------

# --------------------------------------------------
# LOAD TOP 10 INSIGHTS
# --------------------------------------------------

def load_top10():

    try:
        with open(TOP10_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

top10_data = load_top10()

def load_data():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        st.error("ai_bytes.json not found")
        return []

    except json.JSONDecodeError:
        st.error("Invalid JSON format")
        return []

data = load_data()

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

if LOGO_FILE.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image(str(LOGO_FILE), width=280)

st.markdown(
    """
        <h3>
            AI News, Tools & Research — Simplified!
        </h3>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric(
        "AI Bytes",
        len(data)
    )

with metric2:
    st.metric(
        "Daily Read",
        "5 Min"
    )

with metric3:
    st.metric(
        "Updated",
        datetime.now().strftime("%b %d")
    )

# --------------------------------------------------
# BANNER
# --------------------------------------------------

st.info(
    "🔥 Trending Today: AI Agents • Open Source Models • Enterprise AI • Research Breakthroughs"
)

# --------------------------------------------------
# SEARCH + FILTERS
# --------------------------------------------------

st.divider()

col1, col2 = st.columns([3, 1])

with col1:
    search_term = st.text_input(
        "🔍 Search AI Bytes",
        placeholder="Search by title, summary, source..."
    )

with col2:

    categories = sorted(
        list(
            set(
                item.get("category", "Other")
                for item in data
            )
        )
    )

    category_options = ["All"] + categories

    selected_category = st.selectbox(
        "Category",
        category_options
    )

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------

filtered_data = []

for item in data:

    title = item.get("title", "")
    summary = item.get("summary", "")
    category = item.get("category", "")

    search_match = (
        search_term.lower() in title.lower()
        or search_term.lower() in summary.lower()
        or search_term.lower() in category.lower()
    )

    category_match = (
        selected_category == "All"
        or category == selected_category
    )

    if search_match and category_match:
        filtered_data.append(item)

# --------------------------------------------------
# ICONS
# --------------------------------------------------

icons = {
    "AI News": "📰",
    "Research": "🔬",
    "AI Tool": "🛠️",
    "AI Agent": "🤖",
    "Enterprise AI": "🏢",
    "Future Trend": "🚀",
    "Machine Learning": "📊",
    "AI Safety": "🛡️",
    "AI Productivity": "⚙️",
    "Myth vs Reality": "⚡"
}

category_colors = {
    "AI News": "#2563EB",          # Blue
    "Research": "#7C3AED",         # Purple
    "AI Tool": "#059669",          # Green
    "AI Agent": "#DC2626",         # Red
    "Enterprise AI": "#EA580C",    # Orange
    "Future Trend": "#DB2777",     # Pink
    "Machine Learning": "#0891B2", # Cyan
    "AI Safety": "#B45309",        # Amber
    "AI Productivity": "#16A34A",  # Emerald
    "Myth vs Reality": "#9333EA"   # Violet
}

# --------------------------------------------------
# SECTION HEADER
# --------------------------------------------------

st.divider()

featured_items = [
    item for item in filtered_data
    if item.get("featured", False)
]

if featured_items:

    st.subheader("🔥 Featured Stories")

    cols = st.columns(len(featured_items))

    for col, item in zip(cols, featured_items):

        category = item.get("category", "Other")
        color = category_colors.get(category, "#6B7280")

        with col:

            with st.container(border=True):

                st.markdown(
                    f"""
                    <span style="
                        background-color:{color};
                        color:white;
                        padding:6px 12px;
                        border-radius:15px;
                        font-size:12px;
                        font-weight:bold;
                    ">
                    {category}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <h4 style='color:{color};'>
                    {item['title']}
                    </h4>
                    """,
                    unsafe_allow_html=True
                )

                st.write(item["summary"])

                st.caption(
                    f"📖 {item.get('read_time','20 sec')} • {item['source']}"
                )

    st.divider()

regular_items = [
    item for item in filtered_data
    if not item.get("featured", False)
]    

st.subheader("📰 Today's AI Bytes")

# st.caption(
#     f"Showing {len(regular_items)} of {len(data)} AI Bytes"
# )

# --------------------------------------------------
# DISPLAY CARDS
# --------------------------------------------------

if not filtered_data:

    st.warning("No AI Bytes found.")

else:

    cols = st.columns(2)

    for idx, item in enumerate(regular_items):

        col = cols[idx % 2]

        with col:

            with st.container(border=True):

                category = item.get("category", "Other")
                icon = icons.get(category, "📌")

                color = category_colors.get(category, "#6B7280")

                st.markdown(
                    f"""
                    <span style="
                        background-color:{color};
                        color:white;
                        padding:6px 12px;
                        border-radius:15px;
                        font-size:14px;
                        font-weight:bold;
                    ">
                    {icon} {category}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <h3 style='color:{color}; margin-top:15px;'>
                    {item.get("title", "")}
                    </h3>
                    """,
                    unsafe_allow_html=True
                )

                summary = item.get("summary", "")

                if len(summary) > 250:
                    summary = summary[:250] + "..."

                st.write(summary)

                tags = item.get("tags", [])

                if tags:

                    st.caption(" • ".join(tags))

                with st.expander("Why It Matters"):
                    st.write(
                        item.get("why_it_matters", "")
                    )

                st.caption(
                    f"📖 {item.get('read_time', '20 sec')} • {item.get('source', 'Unknown')}"
                )

st.divider()

# # --------------------------------------------------
# # TOP 10 INSIGHTS
# # --------------------------------------------------

# st.divider()

# st.markdown("### Top 10 Most Important AI Insights")

# st.caption(
#     "The most impactful developments, trends, and breakthroughs identified from today's AI sources."
# )

# if top10_data:

#     df = pd.DataFrame(top10_data)

#     df = df.rename(
#         columns={
#             "rank": "Rank",
#             "headline": "Headline",
#             "justification": "Justification"
#         }
#     )

#     st.dataframe(
#         df,
#         use_container_width=True,
#         hide_index=True
#     )

# else:

#     st.info(
#         "No Top 10 insights available."
#     )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    f"""
    <div style='text-align:center; color:gray; margin-top:20px;'>

    AI News  |  Research  |  AI Tools  |  AI Agents  |  Enterprise AI  |  Updated: {datetime.now().strftime('%d %b %Y')}  |  Powered by NotebookLM + Streamlit

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='text-align:center; color:gray; margin-top:20px;'>

    © 2026 AI Bytes • All Rights Reserved • Mohammed Arif

    </div>
    """,
    unsafe_allow_html=True
)