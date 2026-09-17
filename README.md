# AI Smart Classroom Assistant

## BSc AI 3rd Year Project

This project combines four subjects:

1. Computer Vision (CV)
2. Natural Language Processing (NLP)
3. Computer Networks (CN)
4. Cloud Computing (CC)

## What the project does

- Uses OpenCV to detect faces from a webcam frame.
- Uses NLP with TF-IDF and cosine similarity to answer classroom/AI questions.
- Uses TCP client-server communication to send activity logs.
- Includes Docker and Render configuration so the Flask application can be deployed to a cloud server.

## Requirements

Install Python 3.11 or newer.

Open Command Prompt inside this project folder.

### Windows setup

```text
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Start CN server

Open Command Prompt 1:

```text
python network_server.py
```

Keep it running.

### Start web application

Open Command Prompt 2:

```text
venv\Scripts\activate
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Example NLP questions

- What is AI?
- What is computer vision?
- What is NLP?
- What is computer networking?
- What is cloud computing?
- How does face detection work?
- What is this project?
- What technologies are used?

## Cloud Computing

The project contains a Dockerfile and render.yaml. A Docker-compatible cloud platform can build the application from these files.

Important: the webcam feature normally requires a browser with camera permission. For a college demonstration, run the web app locally and explain that the Flask application is cloud-ready.

## Architecture

User Browser
    |
    v
Flask Web Application
    |
    +---- CV Module -> OpenCV Face Detection
    |
    +---- NLP Module -> TF-IDF Question Answering
    |
    +---- CN Module -> TCP Client -> TCP Server
    |
    +---- CC -> Docker Container -> Cloud Deployment

## Suggested project title

"AI Smart Classroom Assistant Using Computer Vision, Natural Language Processing, Computer Networks and Cloud Computing"
