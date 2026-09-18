🤖 AI Smart Classroom Assistant

AI Smart Classroom Assistant is an integrated AI-based web application that combines four major areas of Artificial Intelligence and Computer Science:

* 👁️ Computer Vision (CV)
* 💬 Natural Language Processing (NLP)
* 🌐 Computer Networks (CN)
* ☁️ Cloud Computing (CC)

The application provides an interactive classroom assistant through a web interface, with webcam-based face detection and an AI chatbot.

⸻

🚀 Features

👁️ Computer Vision

* Captures images using the user’s webcam.
* Uses OpenCV for image processing.
* Uses a Haar Cascade Classifier for face detection.
* Displays the number of detected faces.

💬 Natural Language Processing

* Uses TF-IDF Vectorization and Cosine Similarity.
* Answers predefined questions about AI and the project.
* Uses Gemini AI as a fallback for questions that are not covered by the local knowledge base.

The basic flow is:

User Question
      ↓
Local NLP Module
      ↓
Relevant Answer Found?
    ↙       ↘
  YES        NO
   ↓          ↓
Local Answer  Gemini AI

🌐 Computer Networks

* Demonstrates client-server communication.
* Uses TCP sockets.
* The web application can send activity information to a TCP server.

☁️ Cloud Computing

* Includes a Dockerfile for containerization.
* Includes render.yaml for cloud deployment configuration.
* The Flask application is designed to be cloud-ready.

⸻

🛠️ Technologies Used

Area	Technology
Programming Language	Python
Web Framework	Flask
Computer Vision	OpenCV
NLP	Scikit-learn
NLP Technique	TF-IDF + Cosine Similarity
Generative AI	Google Gemini API
Networking	Python TCP Sockets
Frontend	HTML, CSS, JavaScript
Containerization	Docker
Cloud Configuration	Render
Version Control	Git & GitHub

⸻

📁 Project Structure

AI-Smart-Classroom-Assistant/
│
├── app.py
├── nlp_engine.py
├── cv_module.py
├── network_server.py
├── network_client.py
│
├── requirements.txt
├── Dockerfile
├── render.yaml
├── .gitignore
│
├── templates/
│   └── index.html
│
├── README.md
└── PROJECT_REPORT.md

⸻

⚙️ Requirements

* Python 3.11 or newer
* Git
* A modern web browser
* Webcam for the Computer Vision module
* Gemini API key for Gemini fallback responses

⸻

💻 Installation — Windows

1. Clone the repository

git clone https://github.com/garrison-manoah/AI-Smart-Classroom-Assistant.git

Open the project folder:

cd AI-Smart-Classroom-Assistant

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

⸻

🔑 Gemini API Configuration

The Gemini API key should not be stored directly inside the source code.

Set the API key as an environment variable.

Windows PowerShell

[Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "YOUR_API_KEY", "User")

Restart VS Code after setting the variable.

Verify that the variable exists:

if ($env:GEMINI_API_KEY) { "GEMINI_API_KEY is set" } else { "GEMINI_API_KEY is NOT set" }

Security: Never upload your Gemini API key to GitHub or share it publicly.

⸻

🌐 Running the Computer Network Server

Open a terminal and run:

python network_server.py

Keep the server running.

The TCP server listens for communication from the application.

⸻

▶️ Running the Web Application

Open another terminal:

venv\Scripts\activate
python app.py

The application will run at:

http://127.0.0.1:5000/

Open the address in a web browser.

⸻

🧪 Example Questions

The local NLP module can answer questions such as:

* What is AI?
* What is Artificial Intelligence?
* What is Computer Vision?
* How does face detection work?
* What is NLP?
* Where can NLP be used?
* What is Computer Networking?
* How does client-server communication work?
* What is Cloud Computing?
* What is this project?
* What technologies are used?
* What are the four project modules?

Questions outside the local knowledge base can be handled by Gemini AI.

⸻

🏗️ System Architecture

                         USER
                          │
                          ▼
                 ┌─────────────────┐
                 │  Web Interface  │
                 │ HTML/CSS/JS     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Flask Web App   │
                 └────────┬────────┘
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
   ┌────────────┐  ┌────────────┐  ┌────────────┐
   │ Computer   │  │    NLP     │  │ Networking │
   │ Vision     │  │   Module   │  │   Module   │
   │ OpenCV     │  │ TF-IDF     │  │ TCP Socket │
   └────────────┘  └─────┬──────┘  └─────┬──────┘
                         │                │
                         ▼                ▼
                   Gemini AI        TCP Server
                         │
                         ▼
                  Generated Answer
                         │
                         ▼
                  Docker / Cloud
                    Deployment

⸻

🎓 Academic Modules

Module 1 — Computer Vision

OpenCV processes webcam images and detects faces using a Haar Cascade classifier.

Module 2 — Natural Language Processing

The system converts questions into TF-IDF vectors and uses cosine similarity to identify the most relevant predefined answer.

If a suitable local answer is not found, the system can send the question to Gemini AI.

Module 3 — Computer Networks

The project demonstrates TCP-based client-server communication between the application and a network server.

Module 4 — Cloud Computing

Docker and Render configuration are included so that the Flask application can be packaged and deployed to a cloud environment.

⸻

☁️ Cloud Deployment

The project contains:

Dockerfile
render.yaml

These files provide the configuration required for container-based/cloud deployment.

The webcam feature normally requires browser camera permission and is therefore easiest to demonstrate locally.

⸻

🔒 Security

* Gemini API keys are stored using environment variables.
* API keys should never be committed to GitHub.
* The .gitignore file is used to prevent sensitive/local files from being uploaded.

⸻

📌 Project Title

AI Smart Classroom Assistant Using Computer Vision, Natural Language Processing, Computer Networks and Cloud Computing

⸻

👨‍💻 Project Type

Built using Python, Flask, OpenCV, Scikit-learn, TCP sockets, Docker and Gemini AI.