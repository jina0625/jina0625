import feedparser
import datetime

# ✅ 1. 티스토리 블로그 RSS 주소 입력
TISTORY_RSS_URL = "https://jina0625.tistory.com/rss"  # 본인 블로그 주소로 변경 가능

# ✅ 2. RSS 피드 가져오기
feed = feedparser.parse(TISTORY_RSS_URL)

# ✅ 3. README.md 초기 텍스트
markdown = """# 👋 Hello, World!
여기에 간단한 자기소개를 작성할 수 있어요.

## 📝 최근 블로그 글
"""

# ✅ 4. RSS에서 글 10개 추출
for entry in feed.entries[:10]:
    try:
        published_date = datetime.datetime(*entry.published_parsed[:6])
        formatted_date = published_date.strftime("%Y-%m-%d")
    except Exception as e:
        print(f"❌ 날짜 파싱 오류: {e}")
        formatted_date = "Unknown"

    markdown += f"- [{entry.title}]({entry.link}) - {formatted_date}\n"

# ✅ 5. 마지막 업데이트 시간 추가
updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
markdown += f"\n\n_Last updated: {updated}_"

# ✅ 6. 강제로 커밋 유도용 줄 추가 (변경 감지 위해)
markdown += "\n\n<!-- force update line -->"

# ✅ 7. README.md 파일 쓰기
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("✅ README.md가 성공적으로 업데이트되었습니다!")
