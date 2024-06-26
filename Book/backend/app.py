import os

from flask import Flask, request, jsonify, make_response, abort, send_file
from flask_cors import *
from pyfiglet import Figlet
import book
import prompt
import save

app = Flask(__name__)


@app.route('/generate_book', methods=['POST'])
@cross_origin(origins='http://localhost:5173')
def generate_book():
    # 获取请求参数,产生prompt
    prompts = prompt.prompt(request.get_json())

    # 调用大语言模型产生书籍内容
    generated_content = book.gen_book(prompts)

    # 将生成的内容返回给前端
    response_json = jsonify(generated_content)
    resp = make_response(response_json)
    return resp


@app.route('/renew_chapter', methods=['POST'])
@cross_origin(origins='http://localhost:5173')
def renew_chapter():
    # 获取请求参数,产生prompt
    json_data = request.get_json()
    chapter = json_data.get('chapter')

    # 调用大语言模型产生书籍内容
    generated_content = book.renew_chapter(chapter)

    # 将生成的内容返回给前端
    response_json = jsonify(generated_content)
    resp = make_response(response_json)
    return resp


@app.route('/save_book', methods=['POST'])
@cross_origin(origins='http://localhost:5173')
def save_book():
    docx_filepath = save.save_docx(request.get_json())
    if os.path.isfile(docx_filepath):
        return send_file(docx_filepath, as_attachment=True)
    else:
        abort(404, 'File not found')


if __name__ == '__main__':
    print(Figlet().renderText('B O O K'))
    app.run(debug=True)
