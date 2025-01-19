import requests
import json

userID = "naoya1"
unix_second = 0
api_path = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={userID}&from_second={unix_second}"


def getSubmissionData(userID):
    response = requests.get(api_path + userID)
    jsonData = response.json()
    return jsonData


submissions = getSubmissionData(userID)
