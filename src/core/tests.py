# Create your tests here.


def test_home_page_has_title(client):
    response = client.get("/")
    assert "Fast Style" in str(response.content)
