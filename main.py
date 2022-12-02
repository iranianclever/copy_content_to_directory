import json
from distutils.dir_util import copy_tree


class CopyContentToDirectory:
    """Copy contents of a directory to another"""

    def __init__(self):
        """Initialization"""
        self.__PATH = 'sources.json'

    def copy(self, source, destination):
        """Copy to another"""
        try:
            copy_tree(source, destination)
            return True
        except Exception as e:
            print(e)
            return False

    def add_source(self, key, source):
        """Play while impact command"""
        sources = self.__fetch_sources()
        try:
            # Add source to sources
            with open(self.__PATH, 'a') as f:
                # Add last source
                sources[key] = source
                # Convert to json format
                last_sources = json.dumps(sources)
                # Write to file path
                f.write(last_sources)
            return True
        except Exception as e:
            print(e)
            return False

    def __fetch_sources(self):
        """return all sources.json"""
        try:
            # Init sources
            sources = {}
            # Open file sources
            with open(self.__PATH) as f:
                # Load sources to data
                data = f.read()
                # Checkout data for load to json format
                if data:
                    sources = json.loads(data)
            return sources
        # If file sources not found, create file and recursive the function
        except FileNotFoundError:
            open(self.__PATH, 'w')
            return self.__fetch_sources()


# Main running...
if __name__ == '__main__':
    copy = CopyContentToDirectory()
    copy.add_source('windows', 'c:\\user\\Desktop')
