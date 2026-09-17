# AI SMART CLASSROOM ASSISTANT

## 1. Abstract

The AI Smart Classroom Assistant is a web-based artificial intelligence project that combines Computer Vision, Natural Language Processing, Computer Networks and Cloud Computing. The system provides an interactive classroom assistant through a browser. The Computer Vision module uses OpenCV to detect faces from a webcam frame. The Natural Language Processing module uses TF-IDF vectorization and cosine similarity to identify the most relevant answer for a user's question. The Computer Networks module demonstrates TCP client-server communication by sending activity logs to a network server. The Cloud Computing component makes the application container-ready using Docker so that it can be deployed on a cloud platform.

## 2. Objectives

- Build a simple AI-based classroom assistant.
- Demonstrate Computer Vision using face detection.
- Demonstrate NLP using question matching.
- Demonstrate Computer Networking using TCP sockets.
- Demonstrate Cloud Computing using containerized deployment.
- Provide a single web interface for demonstration.

## 3. Technologies Used

- Python
- Flask
- OpenCV
- NumPy
- Scikit-learn
- HTML
- CSS
- JavaScript
- TCP sockets
- Docker
- Cloud deployment configuration

## 4. Modules

### 4.1 Computer Vision

The CV module receives an image from the browser camera. OpenCV converts the image to grayscale and uses a Haar Cascade classifier to detect faces. The number of detected faces is returned to the web interface.

### 4.2 Natural Language Processing

The NLP module contains a small knowledge base of questions and answers. TF-IDF converts the questions into numerical vectors. Cosine similarity compares the user's question with the stored questions. The answer associated with the most similar question is returned.

### 4.3 Computer Networks

The web application acts as a TCP client when it sends a chat or CV event to the network server. The network server listens on port 5050 and displays received messages. This demonstrates basic client-server communication.

### 4.4 Cloud Computing

The application is packaged using Docker. The Dockerfile installs the Python dependencies and starts the Flask application using Gunicorn. This makes the application suitable for deployment to a cloud service that supports Docker containers.

## 5. System Architecture

Browser
  |
  v
Flask Application
  |
  +--> CV Module --> OpenCV
  |
  +--> NLP Module --> TF-IDF + Cosine Similarity
  |
  +--> CN Module --> TCP Server
  |
  +--> Docker --> Cloud Platform

## 6. Advantages

- Combines four academic subjects in one project.
- Easy browser-based demonstration.
- Uses commonly available open-source technologies.
- Can be extended with a larger NLP dataset.
- Can be extended with object detection and attendance features.

## 7. Limitations

- The NLP knowledge base is small.
- Face detection is not the same as identifying a person's identity.
- The TCP server is intended as an educational networking demonstration.
- Cloud deployment requires a cloud account and platform configuration.

## 8. Future Enhancements

- Add a larger question-answer dataset.
- Add database storage.
- Add teacher/student dashboards.
- Add object detection.
- Add authentication.
- Add real cloud database integration.
- Add analytics and charts.

## 9. Conclusion

The AI Smart Classroom Assistant demonstrates how different areas of BSc Artificial Intelligence can be combined into one practical application. Computer Vision handles visual input, NLP handles natural-language questions, Computer Networks handles communication, and Cloud Computing provides a path for remote deployment. The project therefore provides a compact demonstration of CV, NLP, CN and CC concepts in a single system.
