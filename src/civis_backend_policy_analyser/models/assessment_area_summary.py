from sqlalchemy import Column, Text, String, Integer, ForeignKey, TIMESTAMP, func
from civis_backend_policy_analyser.models.base import Base

class AssessmentAreaSummary(Base):
    __tablename__ = "assessment_area_summary"

    summary_id = Column(Integer, primary_key=True, autoincrement=True)
    doc_id = Column(String(100), ForeignKey('document_metadata.doc_id', ondelete='CASCADE'), nullable=False)
    assessment_id = Column(Integer, ForeignKey('assessment_area.assessment_id', ondelete='CASCADE'), nullable=False)
    summary_text = Column(Text)
    created_on = Column(TIMESTAMP, default=func.now())
    created_by = Column(String(100))
