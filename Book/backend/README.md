作者：李蔚
更新时间：2024.3.27

1.文件结构说明
    app.py---后端flask服务框架
    book.py---由prompt生成书籍的逻辑
    gpt.py---openai服务封装
    prompt.py---前端请求处理为输入大模型的prompt
    save.py---将生成的书本保存为word文件
    config.json---保存openai_key
    requirements.txt---项目依赖

2.使用说明
    第一步，部署python环境，安装依赖库
        pip install -r requirements.txt
    第二步，运行app.py，启动后端服务
        python app.py
