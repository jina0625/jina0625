import feedparser
import datetime

# 🔹 티스토리 블로그 RSS 주소
TISTORY_BLOG_URL = "https://jina0625.tistory.com/rss"

# 🔹 RSS 피드 가져오기
feed = feedparser.parse(TISTORY_BLOG_URL)

# 🔹 README.md 기본 내용
markdown_text = """# Hello, World!
(여기에 자기소개 추가)

## 📌 최근 블로그 글
"""  

# 🔹 RSS에서 최신 글 목록 가져오기
for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d")
    markdown_text += f"- [{i['title']}]({i['link']}) - {dt}\n"

    # 콘솔 출력 (디버깅용)
    print(f"추가된 글: {i['title']}")

# 🔹 README.md 파일 업데이트
with open("README.md", mode="w", encoding="utf-8") as f:
    f.write(markdown_text)

print("✅ README.md가 성공적으로 업데이트되었습니다!")
