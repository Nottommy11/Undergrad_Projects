class Employee:
    # Makes it easier to know the amount of employees instead of having to find the size of these other attributes
    _numEmps = 0
    # Used to track the active employee's position in the _position list
    _activePos = None
    # Makes it easier to get the employee's name
    _fullName = []
    # A list that contains each instance of the Employee class, makes referencing those employees possible
    _position = []

    def __init__(self, fullName, userName, pwd):
        # Increase the number of employees in the Employee class with each instance
        Employee._numEmps += 1
        # Pass the employee's name into this list
        self._fullName.append(fullName)
        # Pass the instance of the Employee class into this list
        self._position.append(self)
        self.fullName = fullName
        self.userName = userName
        self.pwd = pwd

