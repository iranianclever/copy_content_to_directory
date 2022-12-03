import json
from distutils.dir_util import copy_tree


class CopyContentToDirectory:
    """Copy contents of a directory to another"""

    def __init__(self):
        """Initialization"""
        self.__PATH_SOURCE = 'sources.json'
        self.__PATH_DESTINATION = 'destinations.json'

    def push(self):
        """Push all sources to destinations"""
        sources = self.__fetch_sources()
        desitnations = self.__fetch_destinations()
        # Pushing all sources to destinations
        for source in sources.values():
            for destination in desitnations.values():
                status = self.__copy(source, destination)
                if status:
                    print(f'Done! Source: {source} Destination: {destination}')
                else:
                    print(
                        f'Not push! Source: {source}: Destination: {destination}')

    def __copy(self, source, destination):
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

    def delete_source(self, key):
        """Delete source with key"""
        sources = self.__fetch_sources()
        # Checkout key with sources key
        if key in sources.keys():
            # Open source path
            with open(self.__PATH_SOURCE, 'w') as f:
                # Delete source
                del sources[key]
                # Convert to json format
                json_format = json.dumps(sources)
                # Writing to file
                f.write(json_format)

    def delete_destination(self, key):
        """Delete destination with key"""
        destinations = self.__fetch_destinations()
        # Checkout key with destinations key
        if key in destinations.keys():
            # Open destination path
            with open(self.__PATH_DESTINATION, 'w') as f:
                # Delete destination
                del destinations[key]
                # Convert to json format
                json_format = json.dumps(destinations)
                # Writing to file
                f.write(json_format)

    def all_sources(self):
        """Return all sources"""
        sources = self.__fetch_sources()
        format_sources = '================= Start All Sources =================\n\r'
        for key, source in sources.items():
            format_sources += f'{key} : {source}\n\r'
        format_sources += '================= End All Sources ================='
        return format_sources

    def all_destinations(self):
        """Return all destinations"""
        destinations = self.__fetch_destinations()
        format_destination = '================= Start All Destinations =================\n\r'
        for key, destination in destinations.items():
            format_destination += f'{key} {destination}\n\r'
        format_destination += '================= End All Destinations ================='
        return format_destination


# Main running...
if __name__ == '__main__':
    copy_content = CopyContentToDirectory()
    command_help = """
    as => Add source
    ad => Add destination
    ds => Delete source
    dd => Delete destination
    ss => Show sources
    sd => Show destinations
    p => Push sources to destinations
    q => Quit
    """
    while True:
        command = input('Enter command(Help "h" key): ')
        command.lower()
        if command == 'h':
            print(command_help)
        elif command == 'as':
            key = input('Enter key: ')
            source = input('Enter source: ')
            # Add source
            copy_content.add_source(key, source)
        elif command == 'ad':
            key = input('Enter key: ')
            destination = input('Enter destination: ')
            # Add destination
            copy_content.add_destination(key, destination)
        elif command == 'ds':
            key = input('Enter key to delete source: ')
            # Delete source
            copy_content.delete_source(key)
        elif command == 'dd':
            key = input('Enter key to delete destination: ')
            # Delete destination
            copy_content.delete_destination(key)
        elif command == 'ss':
            ss = copy_content.all_sources()
            print(ss)
        elif command == 'sd':
            sd = copy_content.all_destinations()
            print(sd)
        elif command == 'p':
            # Push all sources to destinations
            copy_content.push()
        elif command == 'q':
            # Quit
            print('Bye')
            break
