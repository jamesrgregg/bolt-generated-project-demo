import unittest
from my_app import app

def client():
    return app.test_client()
