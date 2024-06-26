import gpt


def gen_book(prompts):
    book = {}
    chapters = []

    # 处理书籍标题
    cnt = prompts['chapterCount']
    msg = prompts['msg']
    if 'title_prompt' in prompts:
        title = gpt.gpt(prompts['title_prompt'])
        msg = '\n书籍标题：' + title + msg

        print('书本标题已生成：\n' + title)

    else:
        title = prompts['title']
    book['title'] = title

    # 生成书籍大纲
    topic_prompt = ('书本严格包含' + str(cnt) + '个章节，' +
                    '根据以下信息为书本编写大纲：' + msg)
    topic = gpt.gpt(topic_prompt)

    print('书本大纲已生成：\n' + topic)

    # 生成每章主要内容
    for i in range(1, cnt + 1):
        chapter = {'title': '', 'content': ''}
        chapter_topic_prompt = ('根据以下信息，简要说明第' + str(i) +
                                '章的主要内容，200字左右：'
                                '\n书本大纲：' + topic)
        chapter_topic = gpt.gpt(chapter_topic_prompt)

        chapter_content_prompt = ('根据以下信息，编写书本的第' + str(i) +
                                  '章，不少于5000字：'
                                  '\n第' + str(i) +
                                  '章主要内容：' + chapter_topic)
        chapter['content'] = gpt.gpt(chapter_content_prompt)

        chapter_title_prompt = ('根据以下信息，直接给出书本第' + str(i) +
                                '的标题：'
                                '\n第' + str(i) +
                                '章主要内容：' + chapter_topic)
        chapter['title'] = gpt.gpt(chapter_title_prompt)
        chapters.append(chapter)

        print('第' + str(i) + '章已生成' + chapter['title'] + chapter['content'])

    book['chapters'] = chapters
    return book


def renew_chapter(chapter):

    print('收到重新生成的章节请求：')
    print(chapter)

    chapter_content_prompt = ('重新编写以下内容，不少于5000字：\n' +
                              chapter['title'] +
                              chapter['content'])
    chapter['content'] = gpt.gpt(chapter_content_prompt)

    chapter_title_prompt = ('根据以下内容，直接给出一个标题，要求简洁概要：\n' +
                            chapter['content'])
    chapter['title'] = gpt.gpt(chapter_title_prompt)

    print('重新生成的章节内容为：\n' + chapter['title'] + '\n' + chapter['content'])

    return chapter
