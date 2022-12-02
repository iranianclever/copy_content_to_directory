import json
from distutils.dir_util import copy_tree


class CopyContentToDirectory:
    """Copy contents of a directory to another"""

    def __init__(self):
        """Initialization"""
        self.__PATH_SOURCE = 'sources.json'
        self.__PATH_DESTINATION = 'destinations.json'

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
        if key not in sources.keys():
            try:
                # Add source to sources
                with open(self.__PATH_SOURCE, 'w') as f:
                    # Add last source
                    sources[key] = source
                    # Convert to json format
                    json_format = json.dumps(sources)
                    # Write to file path
                    f.write(json_format)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            print('Your key is repetitive')

    def add_destination(self, key, destination):
        """Play while impact command"""
        destinations = self.__fetch_destinations()
        if key not in destinations.keys():
            try:
                # Add destination to destinations
                with open(self.__PATH_DESTINATION, 'w') as f:
                    # Add last destination
                    destinations[key] = destination
                    # Convert to json format
                    json_format = json.dumps(destinations)
                    # Write to file path
                    f.write(json_format)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            print('Your key is repetitive')

    def __fetch_sources(self):
        """return all sources.json"""
        try:
            # Init sources
            sources = {}
            # Open file sources
            with open(self.__PATH_SOURCE) as f:
                # Load sources to data
                data = f.read()
                # Checkout data for load to json format
                if data:
                    sources = json.loads(data)
                return sources
        # If file sources not found, create file and recursive the function
        except FileNotFoundError:
            open(self.__PATH_SOURCE, 'w')
            return self.__fetch_sources()

    def __fetch_destinations(self):
        """return all destinations.json"""
        try:
            # Init destinations
            destinations = {}
            # Open file destinations
            with open(self.__PATH_DESTINATION) as f:
                # Load destinations to data
                data = f.read()
                # Checkout data for load to json format
                if data:
                    destinations = json.loads(data)
                return destinations
        # If file destinations not found, create file and recursive the function
        except FileNotFoundError:
            open(self.__PATH_DESTINATION, 'w')
            return self.__fetch_destinations()


# Main running...
if __name__ == '__main__':
    copy = CopyContentToDirectory()
    copy.add_destination('linux', 'c:\\user\\Desktop')
