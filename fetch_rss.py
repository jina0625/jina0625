import feedparser
import datetime

# 🔹 자신의 티스토리 블로그 RSS 주소 입력
TISTORY_BLOG_URL = "https://jina0625.tistory.com/rss"

# 🔹 RSS 피드 가져오기
feed = feedparser.parse(TISTORY_BLOG_URL)

# 🔹 README.md 기본 내용
markdown_text = """# Hello, World!
(자기소개를 여기에 작성하세요)

## 📌 Recent Blog Posts
"""  # 블로그 글 목록이 여기에 추가됨

# 🔹 RSS에서 최신 글 목록 가져오기
for i in feed['entries']:
    # 날짜 변환 (티스토리 RSS의 날짜 포맷을 변환)
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d")
    
    # Markdown에 추가
    markdown_text += f"- [{i['title']}]({i['link']}) - {dt}\n"

    # 콘솔 출력
    print(i['link'], i['title'])

# 🔹 README.md 파일 업데이트
with open("README.md", mode="w", encoding="utf-8") as f:
    f.write(markdown_text)

print("✅ README.md 파일이 성공적으로 업데이트되었습니다!")