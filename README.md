<h1 align="center">文章自动AI改写润色</h1>

<p align="center">
  <img src="https://img.shields.io/github/languages/code-size/cxlcym/AIrewriting" alt="code size"/><img src="https://img.shields.io/github/languages/count/cxlcym/AIrewriting" alt="languages"/><img src="https://img.shields.io/github/last-commit/cxlcym/AIrewriting" alt="last commit"/>
  <br>![](https://img.shields.io/github/forks/cxlcym/AIrewriting?style=social)![](https://img.shields.io/github/watchers/cxlcym/AIrewriting?style=social )![](https://img.shields.io/github/stars/cxlcym/AIrewriting?color=green&style=social)
 <br> <img src="https://img.shields.io/badge/Author-JackCao-orange" alt="Author" />
  
  
## 简介
最近看了很多用AI成文章搞外快的，那就用AI实现了一个小功能，可以将目标网页直接按照自己的提示词改写并以MD格式保存至本地，希望能帮助到大家。

This script is used to convert web content into Markdown and interact with AI（Qwen） for rewriting.

本人非专业选手，不足之处请见谅。
## 功能
1.将目标网页转成MD格式保存至本地;
2.然后根据Prmot和文章内容与AI（本案例使用的是通义千问：max)交互;
3.根据AI输出的结果将文章以MarkDown保存至本地

## 特点
简简单单
## 使用
### 1.确保安装以下库：
`pip install orequests BeautifulSoup markdownify openai`
### 2.需要API调用大模型
（1）内容使用 Openai 进行调用，可以更换模型，本项目使用通义千问；
（2）注册大模型API：[Qwen](https://tongyi.aliyun.com/ "Qwen")
### 3.修改py文件中的4个地方 api、目标网站地址、用户自定义指令、目标文件夹

`    # 直接在代码中提供API密钥
    api_key = "XXXX"  # 请替换为你的实际API密钥`
	
  `  def main():
               url = "www.XX.com" # 这里修改为目标网页
               html_content = fetch_webpage(url)`

  `  # 保存网页内容为Markdown “”内的地址可以替换为目标文件夹
    save_to_file(markdown_content, r"C:XX\webpage.md")`

  `   # 修改用户自定义指令
     user_prompt = `
	 
4.直接运行或者在 PyCharm 里跑就行。


## Blog

[Now Or Never](https://cxlcym.github.io/ "Now Or Never")  


</p>
<hr>
