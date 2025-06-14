import json
import random
import re
from nltk.tokenize import word_tokenize
import os

with open(os.path.join("config", "responses.json"), "r", encoding="utf-8") as f:
    responses = json.load(f)

def get_response(message):
    tokens = word_tokenize(message.lower())
    if any(word in tokens for word in ["hi", "hello", "你好", "喂"]):
        return responses["greeting"]
    elif any(word in tokens for word in ["bye", "再見", "拜拜"]):
        return responses["bye"]
    elif any(word in tokens for word in ["help", "幫我", "救命"]):
        return responses["help"]
    else:
        return responses["unknown"]

def main():
    print("AI回覆機械人已啟動！輸入訊息開始對話。")
    while True:
        user_input = input("你：")
        if user_input.lower() in ["exit", "quit", "走啦"]:
            break
        print("機械人：", get_response(user_input))

if __name__ == "__main__":
    main()

