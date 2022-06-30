from flask import Flask, request, jsonify
from notion.client import NotionClient
from notion.block import TodoBlock
from notion.block import PageBlock

# login
token_v2 = 'df12860ecd0f07e1d4caacf1c0710bc8079cff57e6029c0d665df2b7a126ac6e1ea5436ffe614c5b391c3eb6a4a10c221da5bcfd289bdb2498a6323d2b36b852053ca02d75f94a9ff3fd716036dd' # token_v2
client = NotionClient(token_v2=token_v2)

# 페이지 URL
url = "https://www.notion.so/dkdkdkdkkdkdk-e7c8261c3b7c48d49ce606d985f2685e"
page = client.get_block(url)


application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/notion_test",methods=['POST'])
def notion_test():
    input_data = request.get_json()
    req = input_data["action"]["detailParams"]["notion_test"]["value"]
    input_text = input_data['userRequest']["utterance"]
    text = input_text.split(" ")
    
    if len(text) == 2:
        page.children.add_new(PageBlock, title='아 자고싶다 으아아ㅏ아ㅏ아ㅏ')

    else:
        titles = " ".join(text[2:])
        
        page.children.add_new(PageBlock, title=titles)

    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "완료했습니다!"
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)


@application.route("/animal",methods=['POST'])
def animal():
    req = request.get_json()
    
    animal_type = req["action"]["detailParams"]["animal_type"]["value"]	# json파일 읽기

    answer = animal_type
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)


@application.route("/admins",methods=['POST'])
def admins():
    req = request.get_json()
    
    admin_info = req["action"]["detailParams"]["admin_info"]["value"]	# json파일 읽기

    answer = admin_info
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)




if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
