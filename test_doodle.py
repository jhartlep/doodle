from doodle import extract_doodle_link


def test_extract_doodle_link():
    url = extract_doodle_link()
    assert len(url) > 0
    assert "googleusercontent.com" in url
