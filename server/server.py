import Pyro4


@Pyro4.expose
class TicketMachine(object):
    def create_ticket(self):
        global counter_ticket
        counter_ticket += 1

        return "Ticket {0}".format(counter_ticket)


counter_ticket = 0
daemon = Pyro4.Daemon()
uri = daemon.register(TicketMachine)

print("Ready. Object uri = ", uri)

daemon.requestLoop()
