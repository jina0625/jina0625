# main.py
import feedparser
import datetime

# ✅ 티스토리 RSS 주소 입력
TISTORY_RSS_URL = "https://jina0625.tistory.com/rss"

# ✅ RSS 피드 가져오기
feed = feedparser.parse(TISTORY_RSS_URL)

# ✅ README.md 초기 텍스트
markdown_text = """# 👋 Hello, World!
여기에 간단한 자기소개를 작성할 수 있어요.

## 📝 최근 블로그 글
"""

# ✅ 최신 글 5~10개 추출
for entry in feed.entries[:10]:
    try:
        # 날짜 형식 정리
        published_date = datetime.datetime(*entry.published_parsed[:6])
        formatted_date = published_date.strftime("%Y-%m-%d")
    except:
        formatted_date = "날짜 없음"

    # 마크다운에 추가
    markdown_text += f"- [{entry.title}]({entry.link}) - {formatted_date}\n"

# ✅ 마지막 업데이트 날짜 추가
updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
markdown_text += f"\n\n_Last updated: {updated}_"

# ✅ README.md 파일 쓰기
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)

print("✅ README.md 업데이트 완료")
