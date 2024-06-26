from openai import OpenAI
import json


def get_api_key():
    with open('config.json', 'r') as f:
        return json.load(f)['OpenAI_key']


def gpt(prompt):
    client = OpenAI(api_key=get_api_key())
    try:
        # response = client.completions.create(
        #     model="gpt-3.5-turbo-instruct",
        #     prompt=prompt,
        #     max_tokens=2000,  # 调整生成的最大长度
        #     temperature=0.7,  # 调整温度以控制生成的多样性
        #     top_p=1.0,  # 可以控制生成结果的概率分布
        # )
        # return response.choices[0].text
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是写书的作家，"},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)


# print(gpt('介绍美国历史，100字以内'))
