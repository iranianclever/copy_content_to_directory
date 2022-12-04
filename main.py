from copy_content_to_directory import CopyContentToDirectory

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
    p => Push content sources to destinations
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
