# 🤖 AI chatbot for Toutche electric bicycles

An intelligent **AI-powered chatbot** built for **Touctche Bicycle Company**, designed to enhance customer interaction, answer product-related queries, and provide smart recommendations for bicycles and accessories 🚴‍♂️💬.

This chatbot acts as a **virtual assistant**, offering instant support, product guidance, and service information — making the customer experience smoother, faster, and smarter.

---

## 🎯 Project Overview

Modern customers expect quick and personalized assistance — the **Touctche AI Chatbot** delivers exactly that.
It uses **Natural Language Processing (NLP)** and **Machine Learning** to understand customer queries and respond like a human sales representative.

The chatbot can:

* Guide users to choose the best bicycle based on needs and budget
* Provide product specifications and comparisons
* Answer FAQs related to warranty, maintenance, and accessories
* Connect users with human agents for advanced support

---

## 💡 Key Features

✅ **Product Recommendation System** — Suggests bikes or accessories based on user preferences.
✅ **Smart FAQ Engine** — Answers company-specific queries instantly.
✅ **24×7 Availability** — Always ready to assist customers.
✅ **Multilingual Support** — Communicates in multiple languages.
✅ **Integration Ready** — Can be embedded into websites, apps, or kiosks.
✅ **Voice + Text Mode** — Supports both chat and voice-based interaction.

---

## 🧠 Tech Stack

| Layer                | Technologies Used                                                                       |
| -------------------- | --------------------------------------------------------------------------------------- |
| **Frontend (UI)**    | HTML, CSS, JavaScript                                                                   |
| **Backend (Server)** | Python (Flask Framework)                                                                |
| **NLP Engine**       | Google Gemini API / Cohere API                                                          |
| **Database**         | MongoDB (for chat logs and FAQs)                                                        |
| **APIs**             | Bicycle Catalog API, Google Text-to-Speech, Azure OCR (optional for image-based inputs) |

---

## ⚙️ System Workflow

1️⃣ **User Interaction:** User chats with the AI assistant on the website.
2️⃣ **Intent Detection:** NLP model identifies the query type (product info, pricing, warranty, etc.).
3️⃣ **Response Generation:** Chatbot retrieves or generates an intelligent answer.
4️⃣ **Recommendation:** If it’s a product-related query, the system suggests the best-matched bicycles or accessories.
5️⃣ **Feedback Logging:** Stores conversation logs to improve future performance.

---

## 💻 Installation & Setup

### 🔹 Clone the Repository

```bash
git clone https://github.com/ritirai06/Touctche-AI-Chatbot.git
cd Touctche-AI-Chatbot
```

### 🔹 Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Set Environment Variables

Create a `.env` file with your API keys:

```
GEMINI_API_KEY=your_gemini_key
COHERE_API_KEY=your_cohere_key
MONGO_URI=your_mongodb_uri
```

### 🔹 Run the Application

```bash
python app.py
```

Then open in browser:
👉 `http://127.0.0.1:5000`

---

## 🗨️ Example Interactions

**User:** “Which bicycle is best for city commuting?”
**Bot:** “For daily urban rides, our *Touctche Urban Glide 3.0* offers comfort and durability at ₹24,999. Would you like to see similar models?”

**User:** “Do you have electric bicycles?”
**Bot:** “Yes! Our *Touctche Heileo M200* and *Heileo H100* are top-rated electric models with a 75 km range.”

---

## 📈 Benefits for Touctche

* 🌍 Improves online customer engagement
* ⏱️ Reduces response time to zero
* 🧠 Learns from past queries for smarter future interactions
* 💬 Enhances brand image as a tech-driven bicycle company

---

## 🌟 Future Enhancements

* Add **payment & order tracking integration**
* Introduce **AI voice assistant on website**
* Implement **AI emotion detection** to personalize responses
* Deploy on **WhatsApp, Instagram, and Telegram**

---

## 👩‍💻 Author

**Riti Rai**
💡 Data Science & AI Developer | Passionate about AI Assistants & Automation
📧 [Connect on GitHub](https://github.com/ritirai06)

---

## 🏷️ Keywords

`AI Chatbot` • `Touctche` • `Flask` • `Natural Language Processing` • `Cohere API` • `Google Gemini` • `Customer Support Bot`

