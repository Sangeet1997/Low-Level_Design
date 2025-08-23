from abc import ABC, abstractmethod

class _Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.username = "user"
        self.password = "123"

    def auth(self, username, password):
        if username != self.username or password != self.password:
            return False
        return True
    
    def update(self, username, password):
        self.username = username
        self.password = password

class DatabaseClient(ABC):
    def __init__(self):
        self.connections = {}
        self.currentConnection = None
        self.connectionStatus = False

    def _open_socket(self, host, port):
        if (host,port) not in self.connections:
            connection1 = _Connection(host, port)
            self.connections[(host, port)] = connection1
            self.currentConnection = connection1
        else:
            self.currentConnection = self.connections[(host,port)]
        print(" \t\tTrying to connect to:", host, port)
        
    def _authenticate(self, username, password):
        response = self.currentConnection.auth(username, password)
        if response:
            print("\t\tAuthentication Successfull...")
            self.connectionStatus = True
        else:
            print("\t\tAuthentication Failed...")
            self.connectionStatus = False
    
    def _checkConnection(self):
        if self.currentConnection and self.connectionStatus:
            return True
        return False
    
    def _closeConnection(self):
        self.connectionStatus = False
        self.currentConnection = None
        print("\t\tConnection closed successfully")
    
    def _updateCredentials(self, username, password):
        self.currentConnection.update(username,password)
        print ("\t\tCredentials updated succesfully")
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def terminate(self):
        pass

class TestSQL(DatabaseClient):
    def connect(self, host, port, username, password):
        if self._checkConnection():
            print("\t\tAlready connected to a server.")
        else:
            self._open_socket(host,port)
            self._authenticate(username, password)
    
    def query(self, query):
        if not self._checkConnection():
            print("\t\tFirst connect to a server")
        else:
            print("\t\t",query, " Executed successfully")

    def update(self, username, password):
        if not self._checkConnection():
            print("\t\tFirst connect to a server")
        else:
            self._updateCredentials(username, password)
    
    def terminate(self):
        if not self._checkConnection():
            print("\t\tFirst connect to a server")
        else:
            self._closeConnection()
    
if __name__ == "__main__":
    testServer = TestSQL()
    while True:
        operation = input("Operation: connect, query, update, terminate, exit :")
        
        if operation == "connect":
            host = input("\tHost:")
            port = int(input("\tPort:"))
            username = input("\tUsername:")
            password = input("\tPassword:")
            testServer.connect(host, port, username, password)

        elif operation == "query":
            query = input("\tQuery:")
            testServer.query(query)

        elif operation == "update":
            username = input("\tEnter new Username:")
            password = input("\tEnter new Password:")
            testServer.update(username, password)
        
        elif operation == "terminate":
            check = int(input("\tTerminate 1-Yes 0-No :"))
            if check == 1:
                testServer.terminate()
        
        elif operation == "exit":
            break
    
            
