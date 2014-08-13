from everclip import extract_urls_from_text


def test_extract_urls_from_text():

    urls = extract_urls_from_text('http://slashdot.org')
    assert 'http://slashdot.org' in urls

    urls = extract_urls_from_text('This is a text, containing links like'
            'http://google.com followed by junk.')
    assert 'http://google.com' in urls
