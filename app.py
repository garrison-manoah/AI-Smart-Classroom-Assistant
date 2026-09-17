from flask import Flask, render_template, request, jsonify
from nlp_engine import answer_question
from cv_module import detect_faces_from_image
from network_client import send_to_server

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("message", "")
    answer = answer_question(question)
    # CN component: send a small log message to the local network server.
    send_to_server("CHAT: " + question[:100])
    return jsonify({"answer": answer})

@app.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image received"}), 400

    image_bytes = request.files["image"].read()
    result = detect_faces_from_image(image_bytes)

    # CN component: send CV result to the local network server.
    send_to_server(f"CV: detected {result['count']} face(s)")

    return jsonify(result)

if __name__ == "__main__":
    print("AI Smart Classroom Assistant running at http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
