from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    # AI
    "what is artificial intelligence",
    "define artificial intelligence",
    "explain AI",
    "what is AI",

    # Computer Vision
    "what is computer vision",
    "what is CV",
    "define computer vision",
    "explain computer vision",
    "how does face detection work",
    "how does face detection work in this project",
    "how are faces detected",

    # NLP
    "what is natural language processing",
    "what is NLP",
    "define NLP",
    "explain natural language processing",
    "how does the chatbot work",

    # Computer Networks
    "what is computer networking",
    "what is computer networks",
    "what is CN",
    "define computer networking",
    "how does networking work",
    "how does client server communication work",

    # Cloud Computing
    "what is cloud computing",
    "what is CC",
    "define cloud computing",
    "what is cloud deployment",
    "how can this project be deployed",

    # Project
    "what is the project",
    "explain the project",
    "tell me about the project",
    "what technologies are used",
    "which technologies are used",
    "how many modules are there",
    "what are the four modules",
    "what are the project modules",

    # General
    "hello",
    "hi",
    "hey",
    "who are you",
    "what can you do",
    "thank you",
    "thanks"
]

answers = [
    # AI
    "Artificial Intelligence is the field of creating systems that can perform tasks requiring human-like intelligence.",
    "Artificial Intelligence is the field of creating systems that can perform tasks requiring human-like intelligence.",
    "AI enables computers to perform tasks such as learning, reasoning, prediction and decision-making.",
    "AI stands for Artificial Intelligence.",

    # CV
    "Computer Vision allows computers to understand images and video. In this project it is used for face detection.",
    "CV stands for Computer Vision.",
    "Computer Vision is a field of AI that enables computers to analyze and understand visual information.",
    "Computer Vision allows computers to process and understand images and videos.",
    "The project uses OpenCV and a Haar Cascade classifier to detect faces from a webcam image.",
    "The project captures an image from the webcam and uses OpenCV with a Haar Cascade classifier to detect faces.",
    "Faces are detected using OpenCV and a Haar Cascade classifier.",

    # NLP
    "Natural Language Processing allows computers to process and understand human language. It is used for the classroom chatbot.",
    "NLP stands for Natural Language Processing.",
    "NLP is a field of AI that enables computers to process and understand human language.",
    "Natural Language Processing helps computers work with human language in text or speech.",
    "The chatbot uses TF-IDF vectorization and cosine similarity to find the most relevant answer.",

    # CN
    "Computer Networking connects devices so that they can exchange data. This project uses a client-server connection for communication.",
    "Computer Networks connect devices so they can communicate and exchange data.",
    "CN stands for Computer Networks.",
    "Computer Networking enables communication and data exchange between connected devices.",
    "Networking allows devices to communicate using protocols and connections.",
    "This project demonstrates client-server communication using TCP sockets.",

    # CC
    "Cloud Computing provides computing resources such as servers and storage through the internet.",
    "CC stands for Cloud Computing.",
    "Cloud Computing provides computing resources such as servers, storage and applications over the internet.",
    "Cloud deployment allows an application to run on a remote server and be accessed through the internet.",
    "This project is designed so that the Flask application can be deployed to a cloud platform.",

    # Project
    "This is an AI Smart Classroom Assistant combining Computer Vision, NLP, Computer Networking and Cloud Computing.",
    "The project combines Computer Vision, Natural Language Processing, Computer Networking and Cloud Computing into one application.",
    "The AI Smart Classroom Assistant combines four areas: CV, NLP, CN and CC.",
    "The main technologies are Python, Flask, OpenCV, Scikit-learn, HTML, CSS, JavaScript and TCP sockets.",
    "The project uses Python, Flask, OpenCV, Scikit-learn, HTML, CSS, JavaScript and TCP sockets.",
    "There are four main academic modules: CV, NLP, CN and CC.",
    "The four main modules are Computer Vision, Natural Language Processing, Computer Networks and Cloud Computing.",
    "The project contains four main modules: CV, NLP, CN and CC.",

    # General
    "Hello! I am your AI Smart Classroom Assistant.",
    "Hi! Ask me something about the project or your AI subjects.",
    "Hey! How can I help you with the AI Smart Classroom project?",
    "I am an AI Smart Classroom Assistant created as a BSc AI project.",
    "I can answer questions about the project's CV, NLP, CN and CC modules.",
    "You're welcome!",
    "You're welcome!"
]

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

matrix = vectorizer.fit_transform(questions)


def answer_question(user_text):
    user_text = user_text.strip()

    if not user_text:
        return "Please type a question."

    user_vector = vectorizer.transform([user_text])
    scores = cosine_similarity(user_vector, matrix)[0]

    best_index = scores.argmax()
    best_score = scores[best_index]

    if best_score < 0.12:
        return (
            "I don't have an answer for that yet. "
            "Try asking about AI, CV, NLP, CN, CC, "
            "face detection, the project or its technologies."
        )

    return answers[best_index]