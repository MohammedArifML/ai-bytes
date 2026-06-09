# 🧠 AI Bytes

AI Bytes is a lightweight AI publication built with Streamlit that delivers concise, high-value insights from the world of Artificial Intelligence.

The goal is simple:

> Stay informed about AI in under 5 minutes a day.

---

## Features

- 📰 AI News
- 🔬 Research Breakthroughs
- 🤖 AI Agents
- 🛠️ AI Tools
- 🏢 Enterprise AI
- 🚀 Future Trends
- 🔍 Search and Filtering
- ⭐ Featured Stories
- 📊 Top 10 AI Insights
- 📱 Responsive Layout

---

## Data Sources

Content is curated from leading AI organizations, publications, research institutions and communities including:

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

and other trusted AI sources.

---

## Project Structure

```text
AI-BYTES/
│
├── assets/
│   └── logo.png
│
├── pages/
│   └── About AI Bytes.py
│
├── styles/
│   └── style.css
│
├── ai_bytes.json
├── top10_insights.json
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ai-bytes.git
cd ai-bytes
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
streamlit run app.py
```

---

## Content Workflow

### Generate AI Bytes

1. Collect sources in NotebookLM
2. Generate:
   - AI Bytes
   - Featured Stories
   - Top 10 Insights
3. Export to JSON

### Update Website

Replace:

```text
ai_bytes.json
```

and

```text
top10_insights.json
```

Commit and push changes.

Streamlit Cloud automatically redeploys.

---

## JSON Schema

### ai_bytes.json

```json
{
  "id": 1,
  "title": "Example Title",
  "category": "AI News",
  "byte": "byte text",
  "why_it_matters": "Why it matters",
  "key_takeaway": "...",
  "source": "OpenAI",
  "url": "https://...",
  "date": "2026-06-09",
  "featured": true,
  "read_time": "20 sec",
  "tags": ["LLM", "OpenAI"]
}
```

### top10_insights.json

```json
{
  "rank": 1,
  "headline": "Example Headline",
  "justification": "Explanation"
}
```

---

## Deployment

This project can be deployed for free using:

- Streamlit Community Cloud
- GitHub

Deploy:

1. Push repository to GitHub
2. Connect repository to Streamlit Cloud
3. Select `app.py`
4. Deploy

---

## Tech Stack

- Python
- Streamlit
- Pandas
- NotebookLM
- JSON

---

## Future Roadmap

- Source Links
- AI Byte Detail Pages
- Weekly Archives
- Dark Mode
- Email Newsletter
- RSS Feed
- Analytics Dashboard
- AI Podcast Integration

---

## Author

**Mohammed Arif**

Senior Data Engineer | AI Engineer

---

## License

This project is released under the MIT License.