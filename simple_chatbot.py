from flask import Flask, request, jsonify
from flask_cors import CORS
import os  # ✅ 新增 os 模組來獲取 Render 指定的 PORT

app = Flask(__name__)  # ✅ 確保這裡 `app` 變數名稱沒錯
CORS(app)

bot_responses = {
    "1": ("[Casual Introduction]\n"
          "Hi! I'm ChunCheng Liao (Jimmy). My MBTI type is INFJ.\n"
          "I'm a pretty easygoing and optimistic person, but I also like paying attention to details and making sure things are done right.\n\n"
          "In my free time, I enjoy playing games like Valorant and Apex keep that strategic thinking and reaction speed sharp! "
          "I also like staring at the sky and letting my mind wander (some call it daydreaming, I call it creativity in progress). "
          "And of course, coffee is a must—every day starts with a good cup to get me going!"),
    
    "2": "[Education]\n- Master's in Data Science with a specialization in Machine Learning, University of Sydney\n- Bachelor's in Computer Science and Information Management, Soochow University",
    
    "3": ("[Experience]\n"
          "During my master's, I worked on various academic projects, including steel defect detection, "
          "cardiovascular disease prediction, and more. These experiences helped me strengthen my skills in "
          "data analysis, machine learning, and problem-solving."),

    
    "4": ("[Master Project]\n"
          "My master's project focused on wildfire prediction in Canada using Machine Learning techniques. "
          "This experience taught me how to apply theoretical knowledge to real-world challenges, making my "
          "1.5 years in the master's program incredibly valuable."),

    
    "5": ("[University Project]\n"
          "My university's project was the Dementia Education Game (MEMENTO). This project not only deepened my understanding of dementia but also "
          "taught me the importance of teamwork and collaboration. It was a great experience in combining technology "
          "with healthcare education."),

    
    "6": ("[Reason for designing this website]\n"
          "I built this website entirely by self-learning. I developed it using JavaScript and sought assistance from "
          "ChatGPT for debugging and design improvements. After completing the coding, I deployed the site using GitHub Pages. "
          "The entire process took me about a week, with 3-4 days dedicated to coding and the rest focused on content planning and layout design.")
}

menu_text = """
🎉 I am awake! 🎉  

1⃣  [About Me]  
2⃣  [Education]  
3⃣  [Experience]  
4⃣  [Master Project]  
5⃣  [University Project]  
6⃣  [Reason for designing this website]  

🔹 Type a number (e.g., "1" for About Me)."""


@app.route("/")
def home():
    return "Chatbot is running on Render!"  # ✅ Render 會用這個測試 API 是否正常運行

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request:

def chat():
    data = request.json
    user_input = data.get("question", "").strip()

    if user_input == "menu":
        return jsonify({"answer": menu_text.replace("\n", "<br>")})  # 確保 \n 轉換為 <br>
    
    response = bot_responses.get(user_input, "⚠️ Invalid choice! Please enter a number from 1 to 6.")
    return jsonify({"answer": response.replace("\n", "<br>")})  # 確保 \n 轉換為 <br>

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ 使用 Render 指定的 PORT
    app.run(host="0.0.0.0", port=port, debug=True)  # ✅ `0.0.0.0` 讓外部可訪問
