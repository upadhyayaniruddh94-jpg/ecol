# EcoLogix ESG Dashboard (Streamlit Web Application)

An ESG and Carbon Footprint Compliance Dashboard built with Python and Streamlit for easy deployment on Streamlit Community Cloud and GitHub.

## 📁 Repository Structure
- `app.py` - Main Streamlit web application.
- `requirements.txt` - Python dependencies needed for deployment.
- `README.md` - Instructions for local running and Streamlit Cloud deployment.

---

## 🚀 Quick Setup & Deployment

### 1. Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

### 2. Push to GitHub
1. Create a new repository on GitHub named `ecologix-esg-streamlit`.
2. Open terminal inside the project directory and run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Streamlit app"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ecologix-esg-streamlit.git
   git push -u origin main
   ```

---

### 3. Deploy to Streamlit Cloud (streamlit.app)
1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
2. Click **"New app"**.
3. Select your repository: `ecologix-esg-streamlit`.
4. Set Main file path to: `app.py`.
5. Click **"Deploy!"**.
