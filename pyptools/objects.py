class Parser(object):
    """Base class for all parsers to inheret with common interface"""

    def iterparse(self, iterator, **kwargs):
        """
            Parses a iterator/generator.  Must be implemented by each parser.

            :param value: Iterable containing data

            :return: yeilds parsed data
        """
        raise NotImplementedError('Must implement iterparse method!')

    def parse(self, value, **kwargs):
        """
            Parses a stirng.  By default accumlates from the iterparse method.

            :param value:
                String containing the data to parse.

            :return: data structure containing parsed data
        """
        result = []
        value = value.splitlines()
        for item in self.iterparse(iter(value), **kwargs):
            result.append(item)

        if len(result) == 1:
            return result[0]
        else:
            return result

    def parse_file(self, filename, **kwargs):
        """
            Parses lines from a file.  By default accumlates from
            iterparse_file method by splitting the file by lines.

            :param filename: string with the path to the file.

            :return: data structure containing parsed data
        """
        with open(filename, 'rU') as value:
            return self.parse(value.read().splitlines(), **kwargs)

    def iterparse_file(self, filename, **kwargs):

        def file_generator(fname):
            with open(fname, 'rU') as f:
                for line in f:
                    yield line.strip('\r\n')

        generator = file_generator(filename)
        for value in self.iterparse(generator, **kwargs):
            yield value
