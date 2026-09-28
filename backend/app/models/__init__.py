"""
Importing this package (or any single model from it) must register ALL
model classes with SQLAlchemy's declarative registry. Several models use
string-based relationship() references (e.g. relationship("CaseAnalysis")),
which SQLAlchemy only resolves once every referenced class has actually
been imported somewhere. Centralising the imports here — and having
app/db/database.py or app/main.py import this package before any model
is used — avoids "failed to locate a name" InvalidRequestError crashes.
"""
from app.models.user import User, UserRole  # noqa: F401
from app.models.case import CaseAnalysis, ChatSession, Petition  # noqa: F401
from app.models.case_management import CaseRecord, CaseStatus  # noqa: F401
