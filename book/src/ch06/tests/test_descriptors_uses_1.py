"""Clean Code in Python - Chapter 6: Descriptors

> Tests for descriptors_uses_1.py

"""
from datetime import datetime
from unittest import TestCase, main

from descriptors_uses_1 import LoginEvent

DATE_TIME = datetime(2016, 7, 20, 15, 45)


class TestLoginEvent(TestCase):
    def test_serialization(self):
        event = LoginEvent(
            username="username",
            password="password",
            ip="127.0.0.1",
            timestamp=DATE_TIME,
        )
        expected = {
            "username": "username",
            "password": "**redacted**",
            "ip": "127.0.0.1",
            "timestamp": "2016-07-20 15:45",
        }
        self.assertEqual(event.serialize(), expected)

    def test_retrieve_transformed_value(self):
        event = LoginEvent(
            username="username",
            password="password",
            ip="127.0.0.1",
            timestamp=DATE_TIME,
        )
        self.assertEqual(event.password, "**redacted**")
        self.assertEqual(event.timestamp, "2016-07-20 15:45")
        self.assertEqual(event.username, "username")
        self.assertEqual(event.ip, "127.0.0.1")

    def test_object_keeps_original_values(self):
        event = LoginEvent(
            username="username",
            password="password",
            ip="127.0.0.1",
            timestamp=DATE_TIME,
        )
        self.assertEqual(event.__dict__["password"], "password")


if __name__ == "__main__":
    main()
