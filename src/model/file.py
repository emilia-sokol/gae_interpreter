# we use this class for displaying mapper and reducer implementation files
# name - name of the file
# type - type of the file, can be helpful to distinguish implementation language for mapper and reducer
# key - unique id for the file


class DisplayFile:
    def __init__(self, name, file_type, file_key, user_id):
        self.name = name
        self.file_type = file_type
        self.file_key = file_key
        self.user_id = user_id
