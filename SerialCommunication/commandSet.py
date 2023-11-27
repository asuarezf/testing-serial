# Commands class
# TODO Implement command with two options
class Command:
    def __init__(self, name, command,expected):
        self.name = name
        # Command
        self.command = bytearray()
        self.command = command
        # Response
        self.response = bytearray()
        self.response = expected
        
class CommandSet:
    import csv as csv
    list_commands = []

    def __init__(self,filename):
        from textwrap import wrap
        with open(filename, newline='') as csvfile:
            reading = self.csv.reader(csvfile)
            for row in reading:
                if not (row[0] == 'Name'):
                    self.add_command(row[0],wrap(str(row[1]),2),wrap(str(row[2]),2))

    def add_command(self, name, command,expected):
        # Command
        parse_command = bytearray()
        for item in command:
            parse_command.append(int(item,16))
        #print("Command to send: "+str(self.command))
        #self.command.append(int(command,16))
        
        # Response
        parse_response = bytearray()
        for item in expected:
            parse_response.append(int(item,16))

        command = Command(name,parse_command,parse_response)
        self.list_commands.append(command)

    def find_command(self,command_search):
        for command in self.list_commands:
            if (command.name == command_search):
                return command





