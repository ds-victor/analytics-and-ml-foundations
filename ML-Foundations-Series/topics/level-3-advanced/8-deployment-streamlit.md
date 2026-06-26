# Deployment & Streamlit

## 1. Why This Matters
A model is only useful if someone can use it. Deployment puts your model in the hands of users.

## 2. Core Concept
**Streamlit** is a Python library to turn scripts into interactive web apps. You can deploy for free on Streamlit Cloud, Hugging Face Spaces, or on your own server.

```mermaid
graph LR
    Model[Trained Model] --> Script[app.py]
    Script --> Streamlit[Streamlit App]
    Streamlit --> Web[Web Browser/Stakeholders]
```

## 3. Real-World Examples
• Data scientists build internal tools for stakeholders.
• Showcase your house price predictor on a public URL for your portfolio.

## 4. Comparison
| Tool | Ease of use | Customisation | Hosting options |
|------|-------------|---------------|-----------------|
| Streamlit | Very easy | Medium | Cloud, own server |
| Flask/FastAPI | Medium | High | Anywhere |
| Gradio | Very easy | Low | Hugging Face |

## 5. Decision Tree
1. Need a quick interactive demo? → Streamlit or Gradio
2. Need a production API? → FastAPI
3. Need full frontend control? → Flask + React

## 6. Common Misconceptions
• Deployment is not just 'putting a notebook online' – you need to manage dependencies and security.
• Streamlit apps can be stateful with `st.session_state`.

## 7. FAQ
**Q: Is Streamlit free?** Streamlit Cloud offers free tier with limits.
**Q: Do I need to know web development?** No, Streamlit handles that.

## 8. Next Steps
Review all topics and start building your own projects.

## 9. Running Example
We'll create a `app.py` that loads our trained model and lets users input house features (area, bedrooms, location score) to get a predicted price. Deploy it on Streamlit Cloud and share the link.

## 10. Interview Prep
1. What are the challenges of deploying ML models?
2. How would you monitor a deployed model for degradation?

