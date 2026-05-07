from datetime import datetime
from pydantic import BaseModel
from app.models.vulnerability import EnrichedVulnerability


class AnalysisSummary(BaseModel):
    total: int
    critical: int
    high: int
    medium: int
    low: int


class AnalysisReport(BaseModel):
    scan_id: str
    repo_url: str
    scanned_at: datetime
    summary: AnalysisSummary
    vulnerabilities: list[EnrichedVulnerability]
