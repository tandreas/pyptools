import pytest

from mock import mock_open, MagicMock
from pyptools.objects import Parser


@pytest.fixture(scope='module')
def parser():
    class MockParser(Parser):

        def iterparse(self, iterator, **kwargs):
            for item in iterator:
                yield item

    return MockParser()


@pytest.fixture(params=['\n', '\r\n'],
                ids=['unix_line_endings', 'windows_line_endings'])
def simple_string_log(request):
    return request.param.join(['Line1', 'Line2', 'Line3', 'Line4', ''])


def test_parser_parse(parser, simple_string_log):
    result = parser.parse(simple_string_log)
    assert result == ['Line1', 'Line2', 'Line3', 'Line4']


def test_parser_iterparse(parser, simple_string_log):
    iterator = simple_string_log.splitlines()
    result = [item for item in parser.iterparse(iterator)]
    assert result == ['Line1', 'Line2', 'Line3', 'Line4']


def test_parser_parse_file(parser, mocker, simple_string_log):
    m = mock_open(read_data=simple_string_log)
    mocker.patch('pyptools.objects.open', m, create=True)
    result = parser.parse_file('dummy.txt')
    assert result == ['Line1', 'Line2', 'Line3', 'Line4']


def test_pasrer_iterparse_file(parser, mocker, simple_string_log):
    m = mock_open(read_data=simple_string_log)
    m.return_value.__iter__ = lambda self: iter(self.readline, '')
    mocker.patch('pyptools.objects.open', m, create=True)
    result = [item for item in parser.iterparse_file('dummy.txt')]
    assert result == ['Line1', 'Line2', 'Line3', 'Line4']
