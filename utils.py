from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
#import os

def generate_script(subject, video_len, creativity, api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", "請為'{subject}'這個主題的影片想一個吸引人的標題")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human", """你是一位短影片頻道的博主。根據以下標題和相關資訊，為短影片頻道寫一個影片腳本。
             影片標題：{title}，影片時長：{duration}分鐘，生成的腳本長度盡量符合影片時長的需求。
             要求開頭要抓住眼球，中段要提供有料的內容，結尾要有驚喜，腳本格式也請按照【開頭、中段、結尾】來分隔。
             整體內容的表達方式要盡量輕鬆有趣，吸引年輕觀眾。
             腳本內容可以結合以下維基百科搜尋到的資訊，但僅作為參考，只需結合相關的部分，無關的請忽略：
             ```{wikipedia_search}```""")
        ]
    )
    model = ChatOpenAI(api_key=api_key, temperature=creativity)

    title_chain = title_template | model
    script_chain = script_template | model

    title = title_chain.invoke({"subject":subject}).content

    search = WikipediaAPIWrapper(lang="zh-tw")
    search_result = search.run(subject)

    script = script_chain.invoke({"title":title, "duration":video_len,
                                  "wikipedia_search":search_result}).content
    return search_result, title, script

#print(generate_script("暴君的廚師", 1, 0.7, os.getenv("OPENAI_API_KEY")))








