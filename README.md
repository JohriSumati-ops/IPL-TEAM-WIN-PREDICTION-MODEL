# 🏏 IPL Win Probability Predictor 📊

A machine learning–based **web application** that predicts the **win probability of an IPL match** based on real-time match conditions such as runs, wickets, overs, and team information.  
The project integrates an ML model with an interactive **Gradio web interface** for instant predictions.

---

## 🌐 Web Application
This project features a **Gradio-powered website** where users can input current match details and receive the predicted win probability for each team in real time.
(https://a9698610a4c6b6d69d.gradio.live/)
---

## 📊 Dataset
The model is trained on historical **IPL match data**, which includes:
- Batting and Bowling Teams  
- Current Score  
- Overs Completed  
- Wickets Fallen  
- Target Score  

The target output is the **probability of winning** for the batting team.

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- Gradio  
- Dill (for model serialization)  
- Matplotlib / Seaborn  
- Jupyter Notebook  

---

## 🧠 Model Overview
This project applies **supervised machine learning (classification)** to analyze match situations and estimate win probabilities.  
The data is preprocessed and engineered to capture match dynamics such as run rate and required run rate.

---

## 🤖 Algorithms Used
- Logistic Regression  
- Random Forest Classifier  

The final model was selected based on its probability calibration and consistency, then serialized using **`dill`** for deployment.

---

## 💾 Model Persistence
The trained model is saved and loaded using the **`dill` library**, enabling seamless integration of the ML model with the Gradio web application.

---

## 📈 Model Evaluation
The model was evaluated using:
- Accuracy  
- Log Loss  
- ROC-AUC Score  

The final model provides stable and realistic probability estimates.

---

## ▶️ How to Run the Project Locally

1. Clone the repository  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

<img width="1918" height="913" alt="image" src="https://github.com/user-attachments/assets/b85b6d17-97ac-43f3-8b56-279b853d4cb7" />
<img width="1917" height="912" alt="image" src="https://github.com/user-attachments/assets/19fb2400-e5e2-4f8a-9081-8ceb724fdacc" />
