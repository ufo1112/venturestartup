from PyKakao import Message
from PyKakao import KoGPT

GPT = KoGPT(service_key = "2d1ded5ccb7c0bea2dc4097afb835b5f")

# 다음 문장 만들기
prompt = "인간처럼 생각하고, 행동하는 '지능'을 통해 인류가 이제까지 풀지 못했던"
max_tokens = 64
result = GPT.generate(prompt, max_tokens, temperature=0.7, top_p=0.8)
print(prompt)
print(result)