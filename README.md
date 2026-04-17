# 🚀 Job Recommendation System using NLP

## 📌 Overview

The **Job Recommendation System** is a web-based application that analyzes a user's resume and suggests the most relevant job roles based on their skills. It uses **Natural Language Processing (NLP)** techniques to match resume content with job descriptions and provides accurate recommendations.

---

## 🎯 Features

* 📄 Upload Resume (PDF format)
* 🤖 Intelligent Job Matching using NLP
* 📊 Top 3 Job Recommendations with scores
* 🧠 Skill-based analysis using TF-IDF
* ⚡ Fast and lightweight backend

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)
* **Data Handling:** Pandas
* **PDF Processing:** PyPDF2

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. Text is extracted from the resume
3. Job dataset is vectorized using TF-IDF
4. Resume is converted into a vector
5. Cosine similarity is calculated
6. Top matching jobs are returned

---

## 📂 Project Structure


job-recommendation-system/
│
├── app.py
├── jobs.csv
├── requirements.txt
└── README.md
```

⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/job-recommendation-system.git
cd job-recommendation-system
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```
python app.py
```

### 4️⃣ Access the API

```
http://127.0.0.1:5000/recommend

 🧪 API Testing (Postman)
*Method:** POST
* **Endpoint:** `/recommend`
* **Body:** form-data

  * Key: `resume` (Upload PDF file)

---

## 📊 Sample Output

`json
[
  {
    "title": "Python Developer",
    "score": 0.87
  },
  {
    "title": "Data Scientist",
    "score": 0.75
  }
]
 🚀 Future Enhancements

* 🔍 Skill Gap Analysis (missing skills detection)
* 🌐 Frontend using React
* ☁️ Deployment (Render / Netlify)
* 📊 Real-time job data integration (LinkedIn API)



---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
