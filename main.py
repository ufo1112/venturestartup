import openai
from PyKakao import DaumSearch
from flask import Flask, request, render_template, redirect, url_for
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pickle
import re
DAUM = DaumSearch(service_key = "2d1ded5ccb7c0bea2dc4097afb835b5f")
openai.api_key = "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" 

def personalInterestingPredict():
    youtuber = []
    personalInteresting = ""
    with open('user.pickle', 'rb') as fr:
        user_loaded = pickle.load(fr)

    for i in range(len(user_loaded['items'])):
        youtuber.append(user_loaded['items'][i]['snippet']['title'])
    for i in youtuber:
        df = DAUM.search_web(i, dataframe=True)
        if 'contents' in list(df.columns):
            text = str(df['contents'].head(2))
            not_zamo_str = re.sub(r"[^가-힣]", "", text) 
            personalInteresting += not_zamo_str[:10] + " "
    return personalInteresting

if __name__ == "__main__":
    data = personalInterestingPredict()
    game_list = ['오딘: 발할라 라이징', '달빛조각사', '아레스: 라이즈 오브 가디언즈', 'PUBG: BATTLEGROUNDS', '패스 오브 엑자일', 'ELYON', '이터널 리턴', '디스테라', '프렌즈마블', '프렌즈팝콘', '프렌즈레이싱', '프렌즈팝', '프렌즈타운', '프렌즈사천성', '프렌즈타워', '프렌즈샷: 누구나골프', '프렌즈레이싱 듀오', '놀러와 마이홈', '아이러브니키', '블레이드2 for kakao', '의천도룡기' , '창세기전: 안타리아의 전쟁' , '여명 for kakao, Hello BT21', '그랜드체이스 for kakao', '뱅드림! 걸즈 밴드 파티!', '프린세스 커넥트! Re:Dive', '테라 클래식', '가디언 테일즈', '앨리스클로젯', '월드 플리퍼', '우마무스메 프리티 더비', '에버소울']
    command = "위 단어로 이 사람이 흥미있어 할 만한 게임을 추천해줘. '오딘: 발할라 라이징, 달빛조각사, 아레스: 라이즈 오브 가디언즈, PUBG: BATTLEGROUNDS, 패스 오브 엑자일, ELYON, 이터널 리턴, 디스테라, 프렌즈마블, 프렌즈팝콘, 프렌즈레이싱, 프렌즈팝, 프렌즈타운, 프렌즈사천성, 프렌즈타워, 프렌즈샷: 누구나골프, 프렌즈레이싱 듀오, 놀러와 마이홈, 아이러브니키, 블레이드2 for kakao, 의천도룡기 , 창세기전: 안타리아의 전쟁 , 여명 for kakao, Hello BT21, 그랜드체이스 for kakao, 뱅드림! 걸즈 밴드 파티!, 프린세스 커넥트! Re:Dive, 테라 클래식, 가디언 테일즈, 앨리스클로젯, 월드 플리퍼, 우마무스메 프리티 더비, 에버소울'중에서만 제발 선택해. 반드시 반드시 반드시 반드시 게임 이름만 작성해"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": data + ' ' + command}])
    for i in game_list:
        if i in completion.choices[0].message.content:
            print(i)
            break
"""
DAUM = DaumSearch(service_key = "2d1ded5ccb7c0bea2dc4097afb835b5f")
openai.api_key = "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"  # supply your API key however you choose

# 다음 문장 만들기
#completion = openai.Completion.create(model="davinci-002", prompt="Hello world")
#print(completion.choices[0].text)
df = DAUM.search_web("잇섭", dataframe=True)
print(df)
df = DAUM.search_blog("파이썬", dataframe=True)
print(df)
with open("TEST.txt", 'r', encoding='utf-8') as f:
    text = f.read()
print(text)
# 추가 텍스트
data = "이 사람은 IT, 축구에 관심이 있다. 위 리스트 중에서 추천할 만한 게임은 무엇인가?"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text + data}])
print(completion.choices[0].message.content)"""