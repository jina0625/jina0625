import feedparser
import datetime
import pprint  # 디버깅용

# ✅ 티스토리 RSS 피드 주소
TISTORY_BLOG_URL = "https://jina0625.tistory.com/rss"

# ✅ RSS 피드 파싱
feed = feedparser.parse(TISTORY_BLOG_URL)

# ✅ 디버깅용: 실제 RSS 데이터 출력
print("📥 feed.entries (최신 블로그 글):")
pprint.pprint(feed.entries)

# ✅ README.md 기본 텍스트 시작
markdown_text = """# Hello, World!
(자기소개를 여기에 작성하세요)

## 📌 Recent Blog Posts
"""

# ✅ 최신 블로그 글 10개 추가
for entry in feed.entries[:10]:
    try:
        published_date = datetime.datetime(*entry.published_parsed[:6])
        formatted_date = published_date.strftime("%Y-%m-%d")
    except Exception as e:
        print(f"❌ 날짜 파싱 오류: {e}")
        formatted_date = "Unknown"

    markdown_text += f"- [{entry.title}]({entry.link}) - {formatted_date}\n"

# ✅ 마지막 업데이트 시간 추가
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
markdown_text += f"\n\n_Last updated: {now}_\n"

# ✅ README.md 파일 저장
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)

print("✅ README.md가 성공적으로 업데이트되었습니다!")
