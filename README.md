# 💕 MumMind

MumMind helps new mothers feel supported by decoding their baby’s cries and monitoring their own mental well-being through daily check-ins and AI.

[👉 Try the App](https://mummind.streamlit.app/)  
[📂 View the Repository](https://github.com/A-n-i-e/MumMind)

---

## 🧠 What It Does

- 🎧 **Baby Cry Analysis**: Upload a recording of your baby's cry and get insights on what it might mean — e.g., hunger, discomfort, or sleepiness — using a deep learning model trained on baby cry audio.
- 💬 **Daily Mental Health Check-ins**: Mothers can express how they're feeling, and receive AI-powered tips and encouragement based on their mood.

This app combines emotional support with machine learning to help improve the postpartum experience.

---
Contributors
- Stephanie Emenike
- Ijeoma Ukonu
- Abiodun Feyisayomi
---

## 🛠️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/A-n-i-e/MumMind.git
cd MumMind
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and add your API key like this:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the app

```bash
streamlit run moodanalyser.py
```

---

## 🧪 Tech Stack

- **Streamlit** – for the web interface  
- **PyTorch / Librosa** – for cry classification  
- **Google Generative AI (Gemini)** – for intelligent mood advice  
- **dotenv** – for secure API key handling  
- **Kaggle** – for training the classification model

---

## 📦 Requirements

See [`requirements.txt`](./requirements.txt)

```txt
streamlit
python-dotenv
google-genai
google-generativeai
librosa
torch
torchaudio
numpy
```

---

## 🚀 Live Demo

The app is deployed on Streamlit Cloud.  
👉 [Click here to try it](https://mummind.streamlit.app/)

---

## 📝 Future Plans

- 🔔 Real-time audio recording  
- 📈 Mood tracking over time  
- 🍼 Better cry analysis  
- 📱 Mobile optimization  

---


## ❤️ Acknowledgements

- The team at **HelpMum Hackathon**  
- **Donate-a-Cry Dataset** and researchers  
- **Streamlit** and **Google's Gemini API**
