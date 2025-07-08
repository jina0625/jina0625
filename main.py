import feedparser
import datetime

# ✅ 티스토리 RSS 피드 주소
TISTORY_BLOG_URL = "https://jina0625.tistory.com/rss"

# ✅ RSS 피드 파싱
feed = feedparser.parse(TISTORY_BLOG_URL)

# 🔍 로그로 RSS 데이터 확인
print("📥 feed.entries =")
print(feed.entries)

# ✅ README.md 기본 텍스트 시작
markdown_text = """# Hello, World!
(자기소개를 여기에 작성하세요)

## 📌 Recent Blog Posts
"""

# ✅ 최신 블로그 글 10개 추가
for entry in feed.entries[:10]:
    published_date = datetime.datetime(*entry.published_parsed[:6])published_date = datetime.datetime(*entry.published_parsed[:6])
    formatted_date = published_date.strftime("%Y-%m-%d")
    markdown_text += f"- [{entry.title}]({entry.link}) - {formatted_date}\n"

# ✅ 마지막 업데이트 시간 추가 (잔디용)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
markdown_text += f"\n\n_Last updated: {now}_\n"

# ✅ README.md 파일에 작성
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)

print("✅ README.md가 성공적으로 업데이트되었습니다!")
