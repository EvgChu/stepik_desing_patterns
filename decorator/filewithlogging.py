

class FileWithLoggine:
    def __init__(self, file) -> None:
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f'wrote {len(strings)} lines')

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()

    def __getattr__(self, item):
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key, value):
        if key == 'file':
            self.__dict__["file"] = value
        else:
            setattr(self.__dict__["file"], key, value)

    def __delattr__(self, item):
        delattr(self.__dict__["file"], item)


if __name__ == "__main__":
    file = FileWithLoggine(open('log.txt', 'w'))
    file.writelines(['str1', 'str1'])
    file.write('str1')
    file.close()