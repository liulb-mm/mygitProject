import json

import requests


def test_jsonpath():
    r=requests.get("https://www.nowcoder.com/tutorial/97/")
    return print(r.text)

schema
pydantic