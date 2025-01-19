import requests
import json
from bs4 import BeautifulSoup
import os

USER_ID = "naoya1"
API_PATH = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions"


# 提出データの取得
# id: 提出ID
# epoch_second: 提出時間
# problem_id: 問題ID
# contest_id: コンテストID
# user_id: ユーザID
# language: 言語
# point: 得点
# length: コード長
# result: 結果
# execution_time: 実行時間
def getSubmissionData(userID):
    params = {"user": userID, "from_second": 0}
    response = requests.get(API_PATH, params=params)
    try:
        jsonData = response.json()
    except json.JSONDecodeError as e:
        raise ValueError(
            f"getSubmissionData: Failed to decode JSON.\nResponse text: '{response.text}'\nError: {e}"
        )
    return jsonData


def getSubmissionCode(contest_id, submission_id):
    url = f"https://atcoder.jp/contests/{contest_id}/submissions/{submission_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    code = soup.find("pre", id="submission-code")
    return url, code.text


def main():
    submissions = getSubmissionData(USER_ID)
    for submission in submissions:
        url, code = getSubmissionCode(submission["contest_id"], submission["id"])
        ext = "py" if "python" in submission["language"].lower() else "txt"

        dir_path = f"submissions/{submission['result']}"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_path = f"{dir_path}/{submission['problem_id']}_{submission['id']}.{ext}"
        if os.path.exists(file_path):
            continue
        with open(file_path, "w") as f:
            f.write(f"# URL: {url}\n")
            f.write(f"# Language: {submission['language']}\n\n")
            f.write("# submitted code\n")
            f.write(code)
        print(f"Saved: {file_path}")
    return


if __name__ == "__main__":
    main()
