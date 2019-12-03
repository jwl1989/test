import requests
from bs4 import BeautifulSoup
import json
def get_response():
    URL = "https://tieba.baidu.com/p/6372327480"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    r = requests.get(URL,headers=headers)
    # print(r.text)
    soup = BeautifulSoup(r.text,'lxml')
    match = soup.find_all(name="div",attrs={"class":"d_post_content j_d_post_content"})
    print(match)
    print(match[-1])
    return str(match[-1])

def get_command(class_content):
    string1 = r'style="display:;">'
    string2 = r'</div>'
    content = class_content.split(string1)[-1].split(string2)[0].strip()
    print(content)
    return content

if __name__ == '__main__':
    print("="*20)
    class_content =get_response()
    content = get_command(class_content)
    command = json.loads(content)
    print(command)