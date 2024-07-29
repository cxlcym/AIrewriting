"""
Author: Jack Cao
Date: 2024-07-29
Copyright: © 2024 Jack Cao. All rights reserved.
Description: This script is used to convert web content into Markdown and interact with Qwen for grammar checking.
"""
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from openai import OpenAI
import os

# 直接在代码中提供API密钥
api_key = "api_key"  # 请替换为你的实际API密钥

# 初始化OpenAI客户端
client = OpenAI(
    api_key=api_key,  # 使用直接提供的API密钥
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务的base_url
)


def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch webpage, status code: {response.status_code}")


def html_to_markdown(html):
    return markdownify(html)


def save_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def send_to_qwen(content, user_prompt):
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': content + '\n\n' + user_prompt}
    ]
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=messages,
        temperature=0.8,
        top_p=0.8
    )
    return completion.choices[0].message.content


def main():
    url = "https://XXX.com"
    # 这里修改为目标网页
    html_content = fetch_webpage(url)
    markdown_content = html_to_markdown(html_content)

    # 保存网页内容为Markdown “”内的地址可以替换为目标文件夹
    save_to_file(markdown_content, r"C:XX\webpage.md")

    # 修改用户自定义指令
    user_prompt = "请帮我润色文章"

    # 发送Markdown内容到通义千问
    qwen_reply = send_to_qwen(markdown_content, user_prompt)

    # 保存通义千问的回复为Markdown “”内的地址替换为目标文件夹
    save_to_file(qwen_reply, r"C:XX\qwen_reply.md")


if __name__ == '__main__':
    main()
