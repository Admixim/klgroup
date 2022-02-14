# # YandexVision using experience
# # only free options (Images classificayion & Face detection)
# # read more https://cloud.yandex.ru/services/vision
#
# import base64
# import json
# import os
#
#
# # modified recommended function  https://cloud.yandex.ru/docs/vision/operations/face-detection/ (in Python)
# def encode_file(file):
#     with open(file, 'rb') as f:
#         file_content = f.read()
#     return base64.b64encode(file_content).decode('utf-8')
#
#
# outfile = encode_file('test.jpg')  # my image file
# out = {
#     "folderId": "b1g3fanopncese1f92t5",
#     "analyze_specs": [{
#         "content": outfile,
#         "features": [{
#             "type": "CLASSIFICATION",
#             "classificationConfig": {
#                 "model": "quality"
#             }
#         },
#             {
#                 "type": "CLASSIFICATION",
#                 "classificationConfig": {
#                     "model": "moderation"
#                 }
#             },
#             {
#                 "type": "FACE_DETECTION"
#             }]
#     }]
# }
#
# # make request
# with open('body.json', 'w') as f:
#     json.dump(out, f)
#
# # REAL IAM_TOKEN is REQUARED
# os.system(
#     "export IAM_TOKEN= AQAAAAAGMfUMAATuwZ5FGbQJI0sntWAniy5ZiVM")
# os.system(
#     "curl -X POST -H \"Content-Type: application/json\" -H \"Authorization: Bearer . \" -d @body.json https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze > output.json")


# coding: utf-8
from requests import post, get
import json
import argparse
import base64
import jwt,time

# curl -d "{\"yandexPassportOauthToken\":\"AQAAAAAGMfUMAATuwZ5FGbQJI0sntWAniy5ZiVM\"}" "https://iam.api.cloud.yandex.net/iam/v1/tokens"
TOKEN ='t1.9euelZrIxs-Ric7OzpeJj8qMyYuOkO3rnpWayJqPlY3Ix5uVnJWYz4zNx87l8_cgcQd3-e9tFwI0_N3z92AfBXf5720XAjT8.Z6gny-SM5FRFgWMhnPwHATqlO6EkLamYnjP-sflOyrvFNwX-OIXeiZW1I88X47k46havcaJJuzCcYj9_Gj1ADA'
FOLDER_ID = 'b1gvmob95yysaplct532'


def get_token():
    service_account_id = "ajee2ve53cluq3vmhopr"
    key_id = FOLDER_ID


    private_key = "AQAAAAAGMfUMAATuwZ5FGbQJI0sntWAniy5ZiVM"

    now = int(time.time())
    payload = {
            'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
            'iss': service_account_id,
            'iat': now,
            'exp': now + 360}

    # Формирование JWT.
    encoded_token = jwt.encode(
        payload,
        private_key,
        algorithm='PS256',
        headers={'kid': key_id})


    headers = {'Content-Type': 'application/json'}
    data = {"jwt": encoded_token}
    resp = post("https://iam.api.cloud.yandex.net/iam/v1/tokens", data=data, headers=headers)
    print(resp)
    print(resp.text)
    return resp


# Функция возвращает IAM-токен для аккаунта на Яндексе.
def get_iam_token(iam_url, oauth_token):
    response = post(iam_url, json={"yandexPassportOauthToken": oauth_token})
    json_data = json.loads(response.text)
    if json_data is not None and 'iamToken' in json_data:
        return json_data['iamToken']
    return None

# Функция отправляет на сервер запрос на распознавание изображения и возвращает ответ сервера.
def request_analyze(vision_url, image_data):
    response = post(vision_url, headers={'Authorization': 'Bearer '+ TOKEN}, json={
        'folderId': "b1g3fanopncese1f92t5",
        'analyzeSpecs': [
            {
                'content': image_data,
                'features': [
                    {
                        'type': 'TEXT_DETECTION',
                        'textDetectionConfig': {'languageCodes': ['ru']}
                    }
                ],
            }
        ]})
    return response.json()


def parse(response):
    blocks = response['results'][0]['results'][0]['textDetection']['pages'][0]['blocks']
    for block in blocks:
        for line in block['lines']:
            for item in line['words']:
                print(item['text'])


def main():
    # parser = argparse.ArgumentParser()
    #
    # parser.add_argument('--folder-id', required=True)
    # parser.add_argument('--oauth-token', required=True)
    # parser.add_argument('--image-path', required=True)
    # args = parser.parse_args()

    iam_url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
    vision_url = 'https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze'

    #iam_token = get_iam_token(iam_url, args.oauth_token)

    with open('test3.jpg', "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    response = request_analyze(vision_url, image_data)
    #print(response)
    parse(response)


if __name__ == '__main__':
    # main()
    get_token()


