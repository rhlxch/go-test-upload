import json
import random
import time

import requests

url: str = "https://gateoverflow.in//quickeditajax"


# FIXME: Update cookie
cookie: str = ""


headers: dict[str, str] = {
    "Host": "gateoverflow.in",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://gateoverflow.in/quickedit",
    # "Content-Type": "application/x-www-form-urlencoded",
    # "Content-Length": "37",
    "Origin": "https://gateoverflow.in",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": #Enter cookie value,
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "TE": "trailers",
}

with open("new.json", "r") as f:
    new: list[dict] = json.load(f)


for i, question in enumerate(new, start=1):
    post_id = question["postID"]
    question_title = question["questionTitle"]
    tag = question["tag"]

    question_data: dict[str, str] = {
        "ajaxdata": json.dumps(
            {"id": 1, "postid": f"{post_id}", "data": f"{question_title}"}
        )
    }
    tag_data: dict[str, str] = {
        "ajaxdata": json.dumps({"id": 2, "postid": f"{post_id}", "data": f"{tag}"})
    }

    print(f"Question {i} question_data: {question_data}")
    print(f"Question {i} tag_data: {tag_data}")

    time.sleep(random.uniform(10, 15))
    response = requests.post(url, headers=headers, data=question_data, timeout=30)
    print(f"Question {i} question: {response.status_code}")

    time.sleep(random.uniform(10, 15))
    response = requests.post(url, headers=headers, data=tag_data, timeout=30)
    print(f"Question {i} tag: {response.status_code}\n")
