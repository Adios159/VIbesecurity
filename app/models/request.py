from pydantic import BaseModel, field_validator


class AnalysisRequest(BaseModel):
    repo_url: str

    @field_validator("repo_url")
    @classmethod
    def validate_github_url(cls, v: str) -> str:
        if not v.startswith("https://github.com/"):
            raise ValueError("유효한 GitHub URL을 입력해주세요. (https://github.com/...)")
        return v
