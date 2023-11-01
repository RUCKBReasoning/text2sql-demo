from text2sql import ChatBot
from flask import Flask, render_template, request
from langdetect import detect
from utils.translate_utils import translate_zh_to_en
from utils.db_utils import add_a_record
from langdetect.lang_detect_exception import LangDetectException

text2sql_bot = ChatBot()
# replace None with your API token
baidu_api_token = None

app = Flask(__name__)

@app.route("/chatbot")
def home():
    return render_template("index.html")

@app.route("/get_db_ids")
def get_db_ids():
    global text2sql_bot
    return text2sql_bot.db_ids

@app.route("/get_db_ddl")
def get_db_ddl():
    global text2sql_bot
    db_id = request.args.get('db_id')
    
    return text2sql_bot.db_id2ddl[db_id]

@app.route("/get")
def get_bot_response():
    global text2sql_bot
    question = request.args.get('msg')
    db_id = request.args.get('db_id')
    add_a_record(question, db_id)
    
    if question.strip() == "":
        return "Sorry, your question is empty."
    
    try:
        if baidu_api_token is not None and detect(question) != "en":
            print("Before tanslation:", question)
            question = translate_zh_to_en(question, baidu_api_token)
            print("After tanslation:", question)
    except LangDetectException as e:
        print("language detection error:", str(e))

    predicted_sql = text2sql_bot.get_response(question, db_id)
    print("predicted sql:", predicted_sql)

    response = "<b>Database:</b><br>" + db_id + "<br><br>"
    response += "<b>Predicted SQL query:</b><br>" + predicted_sql
    return response

app.run(host = "0.0.0.0", debug = False)