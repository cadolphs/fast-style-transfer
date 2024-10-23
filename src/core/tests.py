# Create your tests here.
from pytest_django.asserts import assertTemplateUsed


def test_home_page_has_title(client):
    response = client.get("/")
    assert "Fast Style" in str(response.content)


def test_home_page_uses_correct_template(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")
