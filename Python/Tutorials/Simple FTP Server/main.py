from twisted.cred.checkers import InMemoryUsernamePasswordDatabaseDontUse, AllowAnonymousAccess
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPRealm, FTPFactory

checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("Tommy11", "12345")
checker.addUser("Thomas", "12345")
checker.addUser("ExampleUser", "12345")

# portal = Portal(FTPRealm('./public', './myusers'), [AllowAnonymousAccess(), checker])
portal = Portal(FTPRealm('./public', '/home'), [AllowAnonymousAccess(), checker])

factory = FTPFactory(portal)

reactor.listenTCP(21, factory)
reactor.run()








