from pathlib import Path

from django.test import TestCase

# Create your tests here.
BASE_DIR = Path(__file__).resolve().parent.parent
print("hi",BASE_DIR)