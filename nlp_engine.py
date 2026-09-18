import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google import genai

# ---------------------------------------------------------
# GEMINI AI
# ---------------------------------------------------------

try:
    gemini_client = genai.Client()
    GEMINI_AVAILABLE = True
except Exception:
    gemini_client = None
    GEMINI_AVAILABLE = False


# ---------------------------------------------------------
# LOCAL NLP KNOWLEDGE BASE
# ---------------------------------------------------------

questions = [
    # AI - Definition
    "what is artificial intelligence",
    "what is AI",
    "define artificial intelligence",
    "explain AI",

    # AI - Working
    "how does artificial intelligence work",
    "how does AI work",
    "how does AI learn",

    # AI - Applications
    "where is artificial intelligence used",
    "where is AI used",
    "what are applications of AI",
    "give examples of AI",

    # Computer Vision - Definition
    "what is computer vision",
    "what is CV",
    "define computer vision",

    # Computer Vision - Working
    "how does computer vision work",
    "how does face detection work",
    "how are faces detected",
    "how does image recognition work",

    # Computer Vision - Applications / Examples
    "where is computer vision used",
    "what are applications of computer vision",
    "give examples of computer vision",
    "how is computer vision used in real life",

    # Computer Vision - Project
    "how does computer vision work in this project",
    "how does face detection work in this project",

    # NLP - Definition
    "what is natural language processing",
    "what is NLP",
    "define NLP",
    "explain natural language processing",

    # NLP - Working
    "how does NLP work",
    "how does natural language processing work",
    "how does NLP process language",
    "how does NLP understand text",

    # NLP - Applications / Examples
    "where is NLP used",
    "where can NLP be used",
    "what are applications of NLP",
    "what are real world applications of NLP",
    "give examples of NLP",
    "give real world examples of NLP",
    "how is NLP used in real life",

    # NLP - Project
    "how does NLP work in this project",
    "how does the chatbot work",

    # Computer Networks - Definition
    "what is computer networking",
    "what are computer networks",
    "what is CN",
    "define computer networking",

    # Computer Networks - Working
    "how does computer networking work",
    "how does a network work",
    "how does client server communication work",
    "how does TCP work",

    # Computer Networks - Applications / Examples
    "where are computer networks used",
    "what are applications of computer networks",
    "give examples of computer networks",
    "how are computer networks used in real life",

    # Computer Networks - Project
    "how does networking work in this project",
    "how does TCP communication work in this project",

    # Cloud Computing - Definition
    "what is cloud computing",
    "what is CC",
    "define cloud computing",

    # Cloud Computing - Working
    "how does cloud computing work",
    "how does cloud computing work in simple words",
    "how does cloud deployment work",

    # Cloud Computing - Applications / Examples
    "where is cloud computing used",
    "what are applications of cloud computing",
    "give examples of cloud computing",
    "how is cloud computing used in real life",

    # Cloud Computing - Project
    "how can this project be deployed",
    "how does cloud computing work in this project",

    # Project
    "what is the project",
    "explain the project",
    "tell me about the project",
    "what technologies are used",
    "how many modules are there",
    "what are the four modules",

]

answers = [
    # AI - Definition
    "Artificial Intelligence is the field of creating systems that can perform tasks requiring human-like intelligence.",
    "AI stands for Artificial Intelligence.",
    "Artificial Intelligence is the field of creating systems that can perform tasks requiring human-like intelligence.",
    "AI enables computers to perform tasks such as learning, reasoning, prediction and decision-making.",

    # AI - Working
    "AI systems work by using data, algorithms and models to identify patterns, learn from information and produce predictions or decisions.",
    "AI systems process data using algorithms and models to learn patterns and perform tasks.",
    "AI can learn patterns from training data and use those patterns to make predictions or decisions.",

    # AI - Applications
    "AI is used in healthcare, finance, education, transportation, recommendation systems, virtual assistants, robotics and many other fields.",
    "AI is used in areas such as virtual assistants, recommendation systems, fraud detection, healthcare and autonomous systems.",
    "Applications of AI include chatbots, recommendation systems, image recognition, fraud detection and robotics.",
    "Examples of AI include voice assistants, recommendation systems, face recognition and automated decision-making.",

    # CV - Definition
    "Computer Vision allows computers to understand and analyze images and videos.",
    "CV stands for Computer Vision.",
    "Computer Vision is a field of AI that enables computers to analyze and understand visual information.",

    # CV - Working
    "Computer Vision processes images or videos using techniques such as image processing, feature extraction and machine learning to identify useful information.",
    "The project uses OpenCV and a Haar Cascade classifier to detect faces from a webcam image.",
    "Faces can be detected by processing an image and using an object-detection model such as a Haar Cascade classifier.",
    "Image recognition uses computer vision techniques and machine learning models to identify objects, patterns or features in images.",

    # CV - Applications / Examples
    "Computer Vision is used in facial recognition, medical imaging, autonomous vehicles, security systems, quality inspection and smartphone cameras.",
    "Applications of Computer Vision include facial recognition, medical image analysis, autonomous vehicles, surveillance and industrial inspection.",
    "Examples of Computer Vision include face detection, object detection, medical image analysis and automatic number-plate recognition.",
    "Computer Vision is used in real life in smartphone cameras, security systems, healthcare, traffic monitoring and autonomous vehicles.",

    # CV - Project
    "In this project, the webcam captures an image and OpenCV with a Haar Cascade classifier detects the number of faces.",
    "The project captures an image from the webcam and uses OpenCV with a Haar Cascade classifier to detect faces.",

    # NLP - Definition
    "Natural Language Processing allows computers to process and understand human language.",
    "NLP stands for Natural Language Processing.",
    "NLP is a field of AI that enables computers to process and understand human language.",
    "Natural Language Processing helps computers work with human language in text or speech.",

    # NLP - Working
    "NLP processes human language using techniques such as tokenization, text representation, machine learning and language models to understand or generate text.",
    "NLP systems process text or speech, identify patterns and use language models or machine learning techniques to produce useful results.",
    "NLP can process language by converting text into representations that computers can analyze to identify meaning, patterns or relationships.",
    "NLP systems analyze words and sentences using language-processing techniques and machine learning to determine meaning or intent.",

    # NLP - Applications / Examples
    "NLP is used in chatbots, virtual assistants, machine translation, sentiment analysis, spam detection, text summarization, search engines and document analysis.",
    "NLP applications include chatbots, virtual assistants, translation, sentiment analysis, search engines and text summarization.",
    "Real-world examples of NLP include chatbots, voice assistants, Google Translate, email spam filtering and sentiment analysis.",
    "NLP is used in real life in voice assistants, customer-support chatbots, search engines, translation systems, email filtering and social-media analysis.",

    # NLP - Project
    "In this project, NLP uses TF-IDF vectorization and cosine similarity to find the most relevant answer from the knowledge base. Gemini can handle questions that do not have a suitable local match.",
    "The chatbot uses TF-IDF vectorization and cosine similarity to find the most relevant answer from the knowledge base, with Gemini available as a fallback.",

    # CN - Definition
    "Computer Networking connects devices so they can communicate and exchange data.",
    "Computer Networks are systems that connect devices so they can communicate and exchange data.",
    "CN stands for Computer Networks.",
    "Computer Networking enables communication and data exchange between connected devices.",

    # CN - Working
    "Computer networks work by allowing devices to exchange data using communication protocols such as TCP/IP.",
    "A network allows connected devices to exchange data using communication protocols and network connections.",
    "Client-server communication allows a client to send a request to a server, which processes the request and sends back a response.",
    "TCP provides reliable communication by establishing a connection and ensuring that data is delivered in the correct order.",

    # CN - Applications / Examples
    "Computer Networks are used in the internet, offices, schools, cloud systems, banking systems, communication platforms and online services.",
    "Applications of Computer Networks include internet communication, file sharing, cloud services, online banking and video conferencing.",
    "Examples of computer networks include the internet, Wi-Fi networks, school networks, office networks and data-center networks.",
    "Computer Networks are used in real life for internet access, messaging, video calls, online banking, cloud services and file sharing.",

    # CN - Project
    "This project demonstrates networking using TCP sockets. A client sends application information to a server listening on port 5050.",
    "The project demonstrates TCP client-server communication using Python sockets.",

    # CC - Definition
    "Cloud Computing provides computing resources such as servers, storage and applications through the internet.",
    "CC stands for Cloud Computing.",
    "Cloud Computing provides computing resources such as servers, storage and applications over the internet.",

    # CC - Working
    "Cloud Computing works by providing computing resources such as processing power, storage and software through remote servers accessed over a network.",
    "Cloud applications run on remote servers and users access their services through the internet.",
    "Cloud deployment allows an application to run on a remote cloud server and be accessed through the internet.",

    # CC - Applications / Examples
    "Cloud Computing is used for online storage, web hosting, databases, streaming, software services, backups and large-scale computing.",
    "Applications of Cloud Computing include cloud storage, web hosting, databases, online software and data backup.",
    "Examples of Cloud Computing include online storage, cloud-hosted websites, streaming services and cloud databases.",
    "Cloud Computing is used in real life for online storage, web applications, streaming platforms, cloud databases and backup services.",

    # CC - Project
    "This project includes a Dockerfile and Render configuration so the Flask application can be packaged and deployed to a cloud platform.",
    "The project is designed so that the Flask application can be deployed to a cloud platform.",

    # Project
    "This is an AI Smart Classroom Assistant combining Computer Vision, NLP, Computer Networking and Cloud Computing.",
    "The project combines Computer Vision, Natural Language Processing, Computer Networking and Cloud Computing into one application.",
    "The AI Smart Classroom Assistant combines four areas: CV, NLP, CN and CC.",
    "The main technologies are Python, Flask, OpenCV, Scikit-learn, HTML, CSS, JavaScript and TCP sockets.",
    "There are four main academic modules: Computer Vision, Natural Language Processing, Computer Networks and Cloud Computing.",
    "The four main modules are Computer Vision, Natural Language Processing, Computer Networks and Cloud Computing.",

]


# ---------------------------------------------------------
# TF-IDF NLP MODEL
# ---------------------------------------------------------

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

matrix = vectorizer.fit_transform(questions)


# ---------------------------------------------------------
# GEMINI FALLBACK
# ---------------------------------------------------------

def ask_gemini(user_text):
    """Send unknown questions to Gemini."""

    if not GEMINI_AVAILABLE:
        return (
            "I couldn't connect to Gemini right now. "
            "Please try asking about AI, CV, NLP, CN or CC."
        )

    try:
        prompt = f"""
You are the AI assistant inside a BSc Artificial Intelligence
project called AI Smart Classroom Assistant.

Answer the user's question clearly and concisely.

If the question is related to AI, Computer Vision, NLP,
Computer Networks, Cloud Computing, Python or technology,
give a helpful educational explanation.

User question:
{user_text}
"""

        response = gemini_client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={"automatic_function_calling": {"disable": True}}
        )

        if response.text:
            return response.text.strip()

        return "Gemini did not return an answer."

    except Exception as e:
        print("Gemini error:", e)

        return (
            "I couldn't get an answer from Gemini right now. "
            "Please try again."
        )


# ---------------------------------------------------------
# MAIN QUESTION FUNCTION
# ---------------------------------------------------------

def answer_question(user_text):
    user_text = user_text.strip()

    if not user_text:
        return "Please type a question."

    # ---------------------------------------------------------
    # 1. BASIC / GREETING QUESTIONS
    # ---------------------------------------------------------

    simple_questions = {
    "hello": "Hello! I am your AI Smart Classroom Assistant.",
    "hi": "Hi! Ask me something about the project or your AI subjects.",
    "hey": "Hey! How can I help you with the AI Smart Classroom project?",
    "who are you": "I am an AI Smart Classroom Assistant created as a BSc AI project.",
    "what can you do": "I can answer questions about the project's CV, NLP, CN and CC modules.",
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
}

    normalized_text = re.sub(r"\s+", " ", user_text.lower()).strip()

    if normalized_text in simple_questions:
        return simple_questions[normalized_text]

    # ---------------------------------------------------------
    # 2. TF-IDF LOCAL NLP MATCHING
    # ---------------------------------------------------------

    user_vector = vectorizer.transform([user_text])
    scores = cosine_similarity(user_vector, matrix)[0]

    best_index = scores.argmax()
    best_score = scores[best_index]

    # Get the second-best match for comparison
    sorted_scores = sorted(scores, reverse=True)
    second_best_score = sorted_scores[1] if len(sorted_scores) > 1 else 0

    # Only trust the local answer when it is clearly better
    # than the other possible matches.
    confidence_gap = best_score - second_best_score
    # ---------------------------------------------------------
    # 3. HIGH-CONFIDENCE LOCAL ANSWER
    # ---------------------------------------------------------
    #
    # Only use the local knowledge base when the question is
    # sufficiently similar to a stored question.
    #
    # Otherwise Gemini gets a chance to understand the user's
    # actual meaning.
    # ---------------------------------------------------------

    if best_score >= 0.60 and confidence_gap >= 0.15:
        return answers[best_index]

    # ---------------------------------------------------------
    # 4. GEMINI FOR NATURAL / NEW QUESTIONS
    # ---------------------------------------------------------
    #
    # This allows questions such as:
    #
    # "How is NLP used in real life?"
    # "Where do companies use computer vision?"
    # "How does TCP actually work?"
    # "Why do people use cloud computing?"
    #
    # without needing to hard-code every possible sentence.
    # ---------------------------------------------------------

    return ask_gemini(user_text)