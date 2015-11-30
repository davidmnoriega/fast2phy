class Writer(object):
    def __init__(self, file_name=None, stdout=False):
        if file_name is None and stdout is False:
            raise ValueError("Must specify output")
        self.file_name = file_name
        self.stdout = stdout

    def __enter__(self):
        if self.file_name:
            self.file = open(self.file_name, 'w+b')
        return self

    def __exit__(self, type, value, traceback):
        if hasattr(self, 'file'):
            self.file.close()

    def write(self, data):
        if self.stdout:
            print data,
        elif self.file:
            self.file.write(data)

    def flush(self):
        if self.stdout:
            pass
        else:
            self.file.flush()
