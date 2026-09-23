"""
Pytest conftest for the e2e test directory.
Adds design-skills engine and audit paths to sys.path so tests can import
director_engine and audit_code without package installation.
"""
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# director engine
sys.path.insert(0, os.path.join(PROJECT_ROOT, "skills", "design-director"))

# audit tool
sys.path.insert(0, os.path.join(PROJECT_ROOT, "skills", "design-audit"))
