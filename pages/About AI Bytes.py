import streamlit as st
from datetime import datetime

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
LOGO_FILE = BASE_DIR / "assets" / "logo.png"

st.set_page_config(
    page_title="About | AI Bytes",
    page_icon="🧠",
    layout="wide"
)

nav1, nav2, nav3 = st.columns([1,2,1])

with nav3:
    st.page_link(
        "app.py",
        label="🏠 Home"
    )

# --------------------------------------------------
# LOGO HEADER
# --------------------------------------------------

if LOGO_FILE.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image(
            str(LOGO_FILE),
            width=280
        )

st.markdown(
    """
    <div style='text-align:left;'>

    <h3>
    About This Publication
    </h3>

    <p style='color:gray;'>
    Curated AI insights, research breakthroughs, tools, agents and trends for busy professionals.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown("""
## What is AI Bytes?

AI Bytes is a curated collection of concise, high-impact insights from the world of Artificial Intelligence.

The goal is simple:

> Help busy professionals stay informed about the latest developments in AI without spending hours reading articles, research papers, blogs, or watching videos.

Each AI Byte is designed to be consumed in under 30 seconds while still delivering meaningful value.

---

## What You'll Find

AI Bytes covers:

- 📰 AI News
- 🔬 Research Breakthroughs
- 🤖 AI Agents
- 🛠️ AI Tools
- 🏢 Enterprise AI
- 📊 Machine Learning
- 🛡️ AI Safety
- 🚀 Future Trends

---

## Sources

Content is curated and summarized from leading AI organizations, research institutions, technical blogs, podcasts, and publications, including:

- OpenAI
- Anthropic
- Google DeepMind
- Microsoft AI
- NVIDIA
- Hugging Face
- LangChain
- arXiv
- MIT Technology Review
- DeepLearning.AI

and other trusted sources.

---

## Why AI Bytes?

The AI ecosystem moves faster than most professionals can realistically keep up with.

AI Bytes focuses on:

- High signal, low noise
- Practical insights
- Research distilled into plain English
- Enterprise and real-world AI adoption
- The developments that matter most

---

## How the Content Is Created

AI Bytes leverages a curated knowledge base of AI research, technical content, industry news, podcasts, videos, and expert commentary.

Content is analyzed, synthesized, and transformed into concise insights designed for rapid consumption.

---

## Disclaimer

AI Bytes is intended for educational and informational purposes.

While every effort is made to ensure accuracy, readers should always refer to the original source material for complete context and verification.

""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()
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