from distutils.dir_util import copy_tree


class CopyContentToDirectory:
    """Copy contents of a directory to another"""

    def __init__(self, source, destination):
        """Initialization"""
        self.source = source
        self.destination = destination

    def copy(self):
        """Copy to another"""
        try:
            copy_tree(self.source, self.destination)
        except Exception as e:
            print(e)
            return False
        finally:
            return True


if __name__ == '__main__':
    while True:
        source = input('Source directory: ')
        destination = input('Destination directory: ')
        copy_content = CopyContentToDirectory(source, destination)

        status = copy_content.copy()
        if status:
            print('Done!')
        else:
            print('Your operation broken!')
