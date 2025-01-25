import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from datetime import datetime
import json
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Contest:
    name: str = ""
    url: str = ""
    start_time: datetime = ""
    duration: str = ""
    target_rating: str = ""

    def get_upcoming_contests(self):
        url = "https://atcoder.jp"
        try:
            response = requests.get(url + "/contests/")
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"get_next_contest: Failed to fetch {url} - {e}")

        try:
            soup = BeautifulSoup(response.text, "html.parser")
            # 予定されたコンテスト
            table = soup.find("div", id="contest-table-upcoming").find_all("table")[0]
            tbody = table.find("tbody")
            contests = []
            for tr in tbody.find_all("tr"):
                # 開催日時
                start_time_str = tr.find_all("td")[0].text.strip()
                start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S%z")
                # コンテスト名
                contest_name_tag = tr.find_all("td")[1].find("a")
                contest_name = contest_name_tag.text.strip()
                contest_url = url + contest_name_tag["href"]
                # コンテスト期間
                duration = tr.find_all("td")[2].text.strip()
                # レーティング対象
                target_rating = tr.find_all("td")[3].text.strip()
                contests.append(
                    Contest(
                        start_time=start_time,
                        name=contest_name,
                        url=contest_url,
                        duration=duration,
                        target_rating=target_rating,
                    )
                )

            return contests
        except Exception as e:
            raise Exception(f"get_next_contest: Failed to parse contest data - {e}")

    def get_today_contests(self):
        all_contests = self.get_upcoming_contests()
        today_contests = []
        today_date = datetime.now().strftime("%Y-%m-%d")

        for contest in all_contests:
            if today_date == contest.start_time.strftime("%Y-%m-%d"):
                today_contests.append(contest)

        return today_contests

    def __str__(self):
        text = (
            f"[{self.name}]({self.url})\n"
            f"{self.start_time.strftime('%Y/%m/%d %H:%M')} ~\n"
            f"時間: {self.duration}\n"
            f"Rated対象: {self.target_rating}"
        )

        return text


def send_discord_message(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    main_content = {"content": message}
    headers = {"Content-Type": "application/json"}

    response = requests.post(webhook_url, json.dumps(main_content), headers=headers)
    if response.status_code not in [200, 201, 204]:
        raise Exception(f"Failed to send message to Discord - {response.status_code}")


def main():
    contest = Contest()
    contests = contest.get_today_contests()
    for contest in contests:
        send_discord_message(contest.__str__())
        print(contest)


if __name__ == "__main__":
    main()
