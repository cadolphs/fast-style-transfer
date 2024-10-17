from seleniumbase import BaseCase
import pytest


class TestWebsite(BaseCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, live_server):
        self.live_server = live_server

    def test_basic(self):
        self.open(self.live_server.url)
        self.assert_title("Fast Style")
