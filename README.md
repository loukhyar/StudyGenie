
# 📚 StudyGenie

**StudyGenie** is an AI-powered educational tool designed to generate personalized study plans and context-aware prompts using advanced prompt engineering techniques. Built with Python and Flask, it enables users to create optimized learning experiences tailored to their goals.


---

## 🚀 Features

* ✨ **Dynamic Prompt Generation**: Leverages GPT-like models to generate study prompts and guides.
* 🧠 **Context-Aware Prompting**: Utilizes context from user inputs or subjects to enhance response relevance.
* 🗂️ **Personalized Study Plans**: Creates customized study plans based on topics and user preferences.
* 📊 **Model Training Notebook**: Includes a Jupyter Notebook for experimenting with or fine-tuning prompt models.
* 🌐 **Web Interface**: Simple front-end built with HTML to interact with the AI backend.

---

## 🖼️ Screenshots

![Screenshot 2025-05-16 161851](https://github.com/user-attachments/assets/ba1410bc-c702-4dee-82a0-4e4570fa3d11)
![Screenshot 2025-05-16 162059](https://github.com/user-attachments/assets/20052099-85cb-45dc-a136-0ec2a066ef5e)
![Screenshot 2025-05-16 161902](https://github.com/user-attachments/assets/a5dccb15-0be7-4e8e-a863-780424b8b787)

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **AI & NLP**: OpenAI/GPT-like prompts (manual logic)
* **Frontend**: HTML (Jinja templates)
* **Notebook**: Jupyter, for model training and testing

---

## 📁 Project Structure

```

StudyGenie/
├── advanced\_prompting.py      # Handles advanced prompt engineering
├── app.py                     # Flask app routing and server logic
├── context\_prompt.py          # Contextual enhancement for prompts
├── prompt\_generator.py        # Core prompt generation logic
├── study\_plan.py              # Logic to build study plans
├── ModelTraining.ipynb        # Jupyter Notebook for prompt/model testing
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # Basic HTML interface
└── README.md                  # Project documentation

````

---

## 🔧 Installation & Setup

1. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
``

2. **Install Ollama (for running LLMs locally)**:
   Follow instructions from: [https://ollama.com/download](https://ollama.com/download)

3. **Pull and run a model (e.g., LLaMA 2)**:

   ```bash
   ollama run llama2
   ```

   > ℹ️ This step may take a few minutes as the model is downloaded and initialized.

4. **Start the Flask server**:

   ```bash
   python app.py
   ```

5. **Access the application** in your browser at:

   ```
   http://localhost:5000
   ```



## 🧪 Usage

* Navigate to the homepage.
* Enter your study goals or topics.
* Generate study plans and prompts.
* Optionally explore or modify the `ModelTraining.ipynb` for AI model exploration.

---

## 📈 Future Improvements

* User authentication and profiles
* Integration with real AI APIs (e.g., OpenAI)
* Interactive study dashboard
* Mobile-responsive UI

---

## 📄 License

This project is licensed under the MIT License.

```
