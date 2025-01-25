import requests
import json
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime


USER_ID = "naoya1"
API_PATH = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions"


# 提出データを最大500件取得
# 過去1週間分
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
def get_submission_data(userID):
    unix_second = int(time.time()) - 7 * 24 * 60 * 60
    params = {"user": userID, "from_second": unix_second}
    response = requests.get(API_PATH, params=params)
    try:
        jsonData = response.json()
    except json.JSONDecodeError as e:
        raise ValueError(
            f"getSubmissionData: Failed to decode JSON.\nResponse text: '{response.text}'\nError: {e}"
        )
    return jsonData


def get_submission_code(contest_id, submission_id):
    try:
        url = f"https://atcoder.jp/contests/{contest_id}/submissions/{submission_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        code = soup.find("pre", id="submission-code")
        return url, code.text
    except Exception as e:
        return url, "error"


def git_commit_and_push():
    os.system("git pull")
    os.system("git add .")
    commit_message = f"log {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")


def main():
    submissions = get_submission_data(USER_ID)
    add_count = 0
    for submission in submissions:
        url, code = get_submission_code(submission["contest_id"], submission["id"])
        ext = "py" if "python" in submission["language"].lower() else "txt"

        dir_path = f"submissions/{submission['result']}"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_path = f"{dir_path}/{submission['problem_id']}_{submission['id']}.{ext}"
        if os.path.exists(file_path):
            continue
        with open(file_path, "w") as f:
            f.write(f"# URL: {url}\n")
            for key, value in submission.items():
                f.write(f"# {key}: {value}\n")
            f.write("\n")
            f.write("\n# submitted code\n")
            f.write(code)
        print(f"Saved: {file_path}")
        add_count += 1
    print(f"Added {add_count} files")
    # if add_count > 0:
    git_commit_and_push()
    return


if __name__ == "__main__":
    main()
