from pyptools.objects import Parser


class MockParser(Parser):

    def iterparse(self, iterator, **kwargs):
        for item in iterator:
            yield item


def test_parser_parse():
    input_string = """Line 1
Line 2
Line 3
Line 4
"""
    expected = input_string.splitlines()

    parser = MockParser()
    actual = parser.parse(input_string)
    assert actual == expected
