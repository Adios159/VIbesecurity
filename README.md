# Vibe Security

비전공자도 이해할 수 있는 보안 취약점 분석 서비스

## 개요

GitHub 저장소 URL을 입력하면 취약점을 분석하고, LLM이 쉬운 설명과 공격 시나리오, 수정 가이드를 생성해 우선순위와 함께 제공한다.

## 기술 스택

| 영역 | 기술 |
|------|------|
| Backend | FastAPI, Uvicorn, Pydantic |
| LLM | OpenAI API (gpt-4o-mini) |
| Caching | Redis |
| Database | PostgreSQL, SQLAlchemy, Alembic |
| Task Queue | Celery |
| Scanner | Semgrep, Bandit, Gitleaks, Trivy |

## 시작하기

### 요구사항

- Python 3.11+
- Redis (캐싱용, 없어도 동작함)

### 설치

```bash
git clone https://github.com/username/vibe-security.git
cd vibe-security

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 환경변수 설정

```bash
cp .env.example .env
```

`.env` 파일에 아래 값을 입력한다.

```
OPENAI_API_KEY=sk-...
REDIS_URL=redis://localhost:6379
```

### 실행

```bash
uvicorn app.main:app --reload
```

서버가 뜨면 `http://localhost:8000/docs`에서 API 문서를 확인할 수 있다.

## 사용법

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/username/repository"}'
```

### 응답 예시

```json
{
  "scan_id": "550e8400-e29b-41d4-a716-446655440000",
  "repo_url": "https://github.com/username/repository",
  "scanned_at": "2026-05-07T12:00:00Z",
  "summary": {
    "total": 5,
    "critical": 1,
    "high": 2,
    "medium": 1,
    "low": 1
  },
  "vulnerabilities": [
    {
      "id": "...",
      "type": "SQL Injection",
      "severity": "critical",
      "location": "app/db/query.py:42",
      "description": "사용자 입력이 SQL 쿼리에 직접 삽입되어 데이터베이스 전체가 노출될 수 있습니다.",
      "attack_scenario": "공격자가 로그인 폼에 ' OR 1=1 --를 입력해 인증을 우회하고 모든 사용자 정보에 접근할 수 있습니다.",
      "remediation": "1. 파라미터화된 쿼리를 사용하세요.\n2. ORM(SQLAlchemy)을 통해 쿼리를 처리하세요.",
      "priority_score": 95,
      "priority_reason": "인증 우회로 이어질 수 있어 즉시 수정이 필요합니다."
    }
  ]
}
```

## 단계별 로드맵

| 단계 | 상태 | 주요 내용 |
|------|------|-----------|
| MVP | 🚧 진행 중 | mock 데이터 + LLM 설명 + JSON 응답 |
| 학술제 | 📋 예정 | 실제 스캐너 연동 + HTML 리포트 |
| 확장 | 📋 예정 | Celery 비동기 파이프라인 + DB 저장 + 프론트엔드 |

## 프로젝트 구조

```
vibe-security/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── api/
│   │   └── routes/
│   │       └── analyze.py
│   ├── models/
│   │   ├── request.py
│   │   ├── vulnerability.py
│   │   └── report.py
│   └── services/
│       ├── scanner.py
│       ├── llm.py
│       ├── cache.py
│       └── scoring.py
├── tests/
├── docs/
├── requirements.txt
└── .env.example
```

## 문서

- [마스터 문서](docs/vibe-security-master.md) — 전체 아키텍처 및 기능 명세
- [개발 계획](docs/dev-plan.md) — 커밋 단위 구현 계획
