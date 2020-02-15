class TextIO:
    def __init__(self):
        self.ai_name = ''
        self.user_name = ""

    def write(self, message):
        print(self.ai_name + '> ' + message)

    def read(self):
        message = input(self.user_name + '> ').lower()
        return message

    def set_ai_name(self, name):
        self.ai_name = name

    def set_user_name(self, name):
        self.user_name = name
