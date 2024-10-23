from seleniumbase import BaseCase
import pytest


class TestWebsite(BaseCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, live_server):
        self.live_server = live_server

    def test_basic(self):
        self.set_time_limit(1)
        # Our awesome user, Alice, opens up her web browser
        self.open(self.live_server.url)

        # She notices the title of the page is "Fast Style"
        self.assert_title("Fast Style")

        return
        # She sees a drag-and-drop area on the page that says "Drop an image here"
        self.assert_element("div#drop-area")

        # In the code, she sees that there's an input field
        file_input = self.find_element('input[type="file"]')

        # She manually sets the value of the input field to a test image
        file_input.send_keys("test_image.jpg")

        # She sees a thumbnail of the image she uploaded
        self.assert_element("img#thumbnail")
