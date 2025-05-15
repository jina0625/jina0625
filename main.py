import feedparser
import datetime

TISTORY_BLOG_URL = "https://jina0625.tistory.com/rss"
feed = feedparser.parse(TISTORY_BLOG_URL)

markdown_text = """# Hello, World!
(자기소개를 여기에 작성하세요)

## 📌 Recent Blog Posts
"""

for entry in feed.entries[:10]:
    published_date = datetime.datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    formatted_date = published_date.strftime("%Y-%m-%d")
    markdown_text += f"- [{entry.title}]({entry.link}) - {formatted_date}\n"

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
markdown_text += f"\n\n_Last updated: {now}_\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)

print("✅ README.md가 성공적으로 업데이트되었습니다!")
