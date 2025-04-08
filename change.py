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
    "Cookie": "qa_noticed=1; qa_id=11881048078863535583; dsq__u=1vt6g741oge3jm; dsq__s=1vt6g741oge3jm; _ga=GA1.1.1303172624.1739174181; _ga_FNE0H8TQYR=GS1.1.1741074196.2.0.1741074199.57.0.0; _ga_0K3KGBFMD5=GS1.1.1741074196.2.0.1741074199.0.0.0; qa_session=GO%20Classes%2Fpwvkk28k%2F1; PHPSESSID=e28hjl0uer8m9c7vt7qtrgggjg; ec_exam_postids=WyI0NjMxNzciLCI0NjMxNzUiLCI0NjMxNzMiLCI0NjMxNzEiLCI0NjMxNjkiLCI0NjMxNjciLCI0NjMxNjUiLCI0NjMxNjMiLCI0NjMxNjEiLCI0NjMxNTkiLCI0NjMxNTciLCI0NjMxNTUiLCI0NjMxNTMiLCI0NjMxNTEiLCI0NjMxNDkiLCI0NjMxNDciLCI0NjMxNDUiLCI0NjMxNDQiLCI0NjMxNDIiLCI0NjMxNDAiLCI0NjMxMzgiLCI0NjMxMzYiLCI0NjMxMzQiLCI0NjMxMzIiLCI0NjMxMzAiLCI0NjMxMjgiLCI0NjMxMjYiLCI0NjMxMjQiLCI0NjMxMjIiLCI0NjMxMjAiLCI0NjMxMTgiLCI0NjMxMTYiLCI0NjMxMTQiLCI0NjMxMTIiLCI0NjMxMTAiLCI0NjMxMDgiLCI0NjMxMDYiLCI0NjMxMDQiLCI0NjMxMDIiLCI0NjMxMDAiLCI0NjMwOTgiLCI0NjMwOTYiLCI0NjMwOTMiLCI0NjMwOTEiLCI0NjMwODkiLCI0NjMwODciLCI0NjMwODUiLCI0NjMwODMiLCI0NjMwODEiLCI0NjMwNzkiLCI0NjMwNjciLCI0NjMwNjYiLCI0NjMwNjUiLCI0NjMwNjQiLCI0NjMwNjMiLCI0NjMwNjIiLCI0NjMwNjEiLCI0NjMwNjAiLCI0NjMwNTkiLCI0NjMwNTgiLCI0NjMwNTciLCI0NjMwNTYiLCI0NjMwNTUiLCI0NjMwNTQiLCI0NjMwNTMiLCI0NjMwNTIiLCI0NjMwNTEiLCI0NjMwNTAiLCI0NjMwNDkiLCI0NjMwNDgiLCI0NjMwNDciLCI0NjMwNDYiLCI0NjMwNDUiLCI0NjMwNDQiLCI0NjMwNDMiLCI0NjMwNDIiLCI0NjMwNDEiLCI0NjMwNDAiLCI0NjMwMzkiLCI0NjMwMzgiLCI0NjMwMzciLCI0NjMwMzYiLCI0NjMwMzUiLCI0NjMwMzQiLCI0NjMwMzMiLCI0NjMwMzIiLCI0NjMwMzEiLCI0NjMwMzAiLCI0NjMwMjkiLCI0NjMwNzgiLCI0NjMwNzciLCI0NjMwNzYiLCI0NjMwNzUiLCI0NjMwNzQiLCI0NjMwNzMiLCI0NjMwNzIiLCI0NjMwNzEiLCI0NjMwNzAiLCI0NjMwNjkiLCI0NjMwNjgiXQ%3D%3D; ec_exam_spostids=WyI0NjMxMzAiLCI0NjMwOTMiLCI0NjMxMDgiLCI0NjMwODkiLCI0NjMwNDkiLCI0NjMxMTgiLCI0NjMxNTEiLCI0NjMwMzQiLCI0NjMwODMiLCI0NjMwOTYiLCI0NjMxNDkiLCI0NjMwNTYiLCI0NjMxMDQiLCI0NjMxNzciLCI0NjMwMzUiLCI0NjMxNDQiLCI0NjMxNjciLCI0NjMxMTIiLCI0NjMwNTUiLCI0NjMwNjIiLCI0NjMxMjIiLCI0NjMxNDciLCI0NjMwMzciLCI0NjMwNDAiLCI0NjMxMjgiLCI0NjMwNjEiLCI0NjMwODciLCI0NjMwMzIiLCI0NjMxNzEiLCI0NjMwNTAiLCI0NjMwMzAiLCI0NjMwNjAiLCI0NjMxNDIiLCI0NjMwNTciLCI0NjMwNjQiLCI0NjMxMjYiLCI0NjMxMTAiLCI0NjMxMjQiLCI0NjMwOTgiLCI0NjMwNDQiLCI0NjMwNjUiLCI0NjMwNjMiLCI0NjMwNTEiLCI0NjMxMDYiLCI0NjMxMDAiLCI0NjMwNzkiLCI0NjMwNDciLCI0NjMxMzQiLCI0NjMwNTIiLCI0NjMxNTkiLCI0NjMwMzgiLCI0NjMxMzgiLCI0NjMwNDgiLCI0NjMxNTciLCI0NjMwNDEiLCI0NjMwNjciLCI0NjMwMzkiLCI0NjMwODUiLCI0NjMxNjkiLCI0NjMxMjAiLCI0NjMxNTMiLCI0NjMwMzYiLCI0NjMwNTgiLCI0NjMxMzIiLCI0NjMxNDAiLCI0NjMwMzEiLCI0NjMxNDUiLCI0NjMwNDUiLCI0NjMxNjUiLCI0NjMwMjkiLCI0NjMxMzYiLCI0NjMxNzUiLCI0NjMxNjEiLCI0NjMwOTEiLCI0NjMwNTkiLCI0NjMwNDIiLCI0NjMwNjYiLCI0NjMwNDYiLCI0NjMxMDIiLCI0NjMwMzMiLCI0NjMxMTYiLCI0NjMxNjMiLCI0NjMwNTQiLCI0NjMwNTMiLCI0NjMwODEiLCI0NjMwNDMiLCI0NjMxNzMiLCI0NjMxMTQiLCI0NjMxNTUiLCI0NjMwNzIiLCI0NjMwNjgiLCI0NjMwNzMiLCI0NjMwNjkiLCI0NjMwNzQiLCI0NjMwNzAiLCI0NjMwNzgiLCI0NjMwNzciLCI0NjMwNzUiLCI0NjMwNzYiLCI0NjMwNzEiXQ%3D%3D; ec_exam_resultid=335339; ckCsrfToken=Q886hrFwSU59450j5AIaK4vvkdCCJl34717NNxil; cf_clearance=25su0bV9oJAil8w1znpSx77IfQ_LtbSWCaW9EYWp9Tk-1743755259-1.2.1.1-qPMgMA7.a7V3nlGhPGlwrkn22TbA5hQEA6aOkarC3p74EWgYfc2z.tMIvD7ZXF6hDxgpET70Vs8sAycHh7czvYnXYGrgsQTrEj0oANQMNh43UlScCHvGnRd4V0NeAyHkjqCH8KWDtx9qeaO7ql.RWOD7FUJhLnVzCKxno1xbSi8BCeVvR6d.dhvuMlY2vTYEPMyNKosKL2JPCWNPs1SsIMbts3tH8tJaqx5ORvdVT8vlKsIT.XC9QHKn2iNA1ByfpliUPbz4bqFPYm1LQXRXyvyvOPgGRYi0vYNbXyl5zkVBJtVcQZeJeJflVxDBljOjKRyCo8iFoAg8IijOZiswk5QIU9mzWFzvplEWy2yJ8M4",
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

    time.sleep(random.uniform(3, 5))
    response = requests.post(url, headers=headers, data=question_data, timeout=30)
    print(f"Question {i} question: {response.status_code}")

    time.sleep(random.uniform(3, 5))
    response = requests.post(url, headers=headers, data=tag_data, timeout=30)
    print(f"Question {i} tag: {response.status_code}\n")
