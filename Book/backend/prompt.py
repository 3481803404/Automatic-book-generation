def prompt(json_data):

    print('接收到的请求信息：')
    print(json_data)

    key = str(json_data.get('key'))
    chapter_count = int(json_data.get('chapterCount'))
    title = str(json_data.get('title'))
    other = str(json_data.get('other'))

    # 信息提取
    msg = ''
    if key == '1':
        msg = '\n书籍类型：小说'
        background = str(json_data.get('background'))
        characters = str(json_data.get('characters'))
        relationships = str(json_data.get('relationships'))
        plot = str(json_data.get('plot'))
        if background != '':
            msg += '\n故事背景：' + background
        msg += '\n主要人物：' + characters
        if relationships != '':
            msg += '\n人物关系：' + relationships
        msg += '\n主要情节：' + plot
    elif key == '2':
        msg = '\n书籍类型：人物传记'
        character = str(json_data.get('character'))
        information = str(json_data.get('information'))
        life_stages = str(json_data.get('lifeStages'))
        focus_points = str(json_data.get('focusPoints'))
        msg += '\n主角人物：' + character
        msg += '\n人物信息：' + information
        msg += '\n主要人生阶段：' + life_stages
        msg += '\n人物介绍侧重点：' + focus_points
    elif key == '3':
        msg = '\n书籍类型：历史书'
        country = str(json_data.get('country'))
        time_period = str(json_data.get('timePeriod'))
        focus_points = str(json_data.get('focusPoints'))
        msg += '\n国家或地区：' + country
        if time_period != '':
            msg += '\n时间段：' + time_period
        msg += '\n历史介绍侧重点：' + focus_points
    elif key == '4':
        msg = '\n书籍类型：百科书'
        domains = str(json_data.get('domains'))
        main_content = str(json_data.get('mainContent'))
        msg += '\n百科书领域：' + domains
        msg += '\n百科书主要内容：' + main_content
    elif key == '5':
        msg = '\n书籍类型：教科书'
        teaching_content = str(json_data.get('teachingContent'))
        teaching_steps = str(json_data.get('teachingSteps'))
        teaching_methods = str(json_data.get('teachingMethods'))
        msg += '\n教学内容：' + teaching_content
        if teaching_steps != '':
            msg += '\n教学步骤：' + teaching_steps
        if teaching_methods != '':
            msg += '\n教学方法：' + teaching_methods
    elif key == '6':
        msg = '\n书籍类型：议论文/方法论'
        goal = str(json_data.get('goal'))
        argument = str(json_data.get('argument'))
        evidence = str(json_data.get('evidence'))
        msg += '\n论证目标：' + goal
        msg += '\n论点：' + argument
        msg += '\n论据：' + evidence
    elif key == '7':
        book_class = str(json_data.get('bookClass'))
        requirement = str(json_data.get('requirement'))
        msg += '\n书籍主类型：' + book_class
        msg += '\n书籍主要内容：' + requirement

    # prompt生成
    prompts = {}
    if other != '':
        msg += '\n其他内容或要求：' + other
    if title != '':
        msg = '\n书本标题：' + title + msg
        prompts['title'] = title
    else:
        prompts['title_prompt'] = '根据以下信息，为书本编写标题：' + msg
    prompts['msg'] = msg
    prompts['chapterCount'] = chapter_count

    print('信息分析结果：')
    print(prompts)

    return prompts
