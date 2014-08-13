from everclip import extract_links_from_text


def test_extract_links_from_text():

    links = extract_links_from_text('http://slashdot.org')
    assert 'http://slashdot.org' in links

    links = extract_links_from_text('This is a text, containing links like'
            'http://google.com followed by junk.')
    assert 'http://google.com' in links
