import json
import requests

COURSE_ID = "1074744"
ASSIGNMENT_ID = "6974837"
ENDPOINT = f"https://www.gradescope.com/courses/{COURSE_ID}/assignments/{ASSIGNMENT_ID}/submissions"

COOKIES = {
    "_gradescope_session": "T0x6RkhOQkZ6UU03TEJoM2pjUi83VUV0TGt3b2Y3VWFoM0xHeU1ZUVRmb2p2RS9Tb1hjL0dNMFdyT3hBOGh1MFhpaGRsVzc2dVg1VDR6bkNjTll1QVFOS1BSZEV1SmZ5SjBXeThXQ0FrWWg0eDNmM1hZdUhyaWNVRzYyWlY1UTN2YjJ3aUtkOUJpS25EQWd3Y1hTMFpTUWRQN2wyVEVzZFlxMkJuV1JxY3dqd2Jzd2lUMUZyY1dIVldGTHJhcVF4NWp5Z3J5dlBpQWttdko4aDVnU2ovWlFUUisxWmgyaEg0L2g0QlJEeFE5dHdBT09XcThtdGs2dGp3Q0VIUGxuWW9NV0IrckgyRzE4b2M4b1ZsU1d1ajJHY1RsUEZDbEc0VkRSRVJZajhJaFE9LS1ycm9jdmZLaGpOQThMSk50VHlyREF3PT0%3D--6db5564d8eccc448ac256d62f2ded89606954bfb",
    "signed_token": "WEhlN0xTSzFmTVU5Y1FzRTg2L1VRaVlFYWltZncrQmNDeXExQU9RY0QvMD0tLVQ5K2RMTlNveHNMaG1aUzY0b3BRVEE9PQ%3D%3D--75e351a37a25d7f50f9f3f7f1cca8b890ff51e2c",
    "remember_me": "eVFzSC9TKzdacHdoMFJnQ0FkaXNOZz09LS1lY3VYb3RiSDhYc2VxaUtjd1Q0Si9nPT0%3D--77395fbc9da7d12c1c36d4b7d2cae12bac58a566",
    "apt.sid": "AP-1BQVLBSZC216-2-1761268544721-38549189",
    "apt.uid": "1BQVLBSZC216-2-1761268544722-41128195.0.2.d185bee4-1cd3-4bab-9a0d-6336c5502f9f",
}
CSRF = "YKzm0XN1o4g3ad+2MiwBuTlbvUg4P7BSGAEYFNNnHffQcO5GXTyzsaB7cHsensY7UpIzTF+/P7WpOMZ79ao2jw=="
OWNER_ID = "6700506"
OUTLINE_HASH = "dbe3f713559acd4934cff4fdae4bd9c0"

HEADERS = {
    "Origin": "https://www.gradescope.com",
    "Referer": f"https://www.gradescope.com/courses/{COURSE_ID}/assignments/{ASSIGNMENT_ID}/submissions/new",
    "X-Requested-With": "XMLHttpRequest",
    "X-CSRF-Token": CSRF,
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0",
}
def submit_answer(qid: int, value: str):
    questions_obj = {str(qid): {"0": value}}
    questions_json = json.dumps(questions_obj, separators=(",", ":"))

    files = {
        "authenticity_token": (None, CSRF),
        "questions": (None, questions_json),
        "owner_id": (None, OWNER_ID),
        "outline_hash": (None, OUTLINE_HASH),
    }

    with requests.Session() as s:
        s.cookies.update(COOKIES)
        r = s.post(ENDPOINT, headers=HEADERS, files=files, allow_redirects=False)

        print("HTTP:", r.status_code, r.reason)
        print("Content-Type:", r.headers.get("content-type"))

        try:
            # Pretty-print the full JSON response
            parsed = r.json()
            # print(json.dumps(parsed, indent=2))
        except Exception:
            print("Body (first 500):", r.text[:500])
        return parsed


# Example: the same question/answer you captured
# submit_answer(59188675, "0.489")

def try_many_answers():
    for i in range(10):
        for j in range(1):
            for k in range(1):
                for l in range(1):
                    parsed =submit_answer(59188675, f"{i}.{j}{k}{l}")
                    if parsed['question_submissions']['59188675']['score'] == "1.0":
                        print(f"{i}.{j}{k}{l}")
                        print("success")
                        return
                    # else:
                    #     print(parsed['question_submissions']['59188675']['score'])

try_many_answers()