import Pyro4

uri = raw_input("URI object ").strip()

ticket_machine = Pyro4.Proxy(uri)

isContinue = True

while isContinue:
    print(ticket_machine.create_ticket())
    print("Create 5 ticket")

    option = raw_input("Choose [S] or [N] to receiver new ticket: ").upper()
    if option == 'N':
        isContinue = False
