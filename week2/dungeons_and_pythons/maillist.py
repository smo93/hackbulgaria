import user


class MailList():
    """docstring for MailList"""
    def __init__(self, name):
        super(MailList, self).__init__()
        self.__name = name
        self.__users = []

    def get_name(self):
        return self.name

    def add_user(self, user_name, user_email):
        pass
