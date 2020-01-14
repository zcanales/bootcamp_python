class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank:
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        for acc in self.account
            if origin == acc.ID_COUNT or origin == acc.name
                account_from = acc
#checksipastrouve
        for acc in self.account
            if dest == acc.ID_COUNT or dest == acc.name
                account_to = acc
#checksipastrouve
        if len([attr for attr in dir(account_from) if attr[0] != '_']) % 2 == 0
            print("Origin account has an even number of attribute")
        if len([attr for attr in dir(account_to) if attr[0] != '_']) % 2 == 0
            print("Destination account has an even number of attribute")

    def fix_account(self, account):
        print()


b = Bank()
print(len([attr for attr in dir(b) if attr[0] != '_']))
