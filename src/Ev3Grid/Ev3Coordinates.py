class Ev3Coordinates:
    """
    Beep
    """

    #TODO: Convert to Google Style Docstrings -- http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    #TODO: Add docstring tests
    #TODO: Find Docstring Generator

    #Declares Class Variables
    #Coordinates
    __xCoordinate: int
    __yCoordinate: int
    #Property List
    __propertyList: list

    #Initializer
    def __init__(self, targetx : int, targety : int, *targetproperties: str):
        """
        Inititialises a two interger graph point, x and y, for use of a 2D grid. X an Y must be integers.
        Target Properties (such as 'Point of Obstruction' or 'Point of Path') are optionally added as strings).

        :param targetx: Vertical
        :type targetx:
        :param targety:
        :type targety:
        :param targetproperty:
        :type targetproperty:
        """
        self.__xCoordinate = targetx
        self.__yCoordinate = targety
        self.__propertyList = []
        for tp in targetproperties:
            self.__propertyList.append(tp)

    #Variable Specific Functions
    #xCoordinate Specific Functions
    def get_xcoordinate(self) -> int:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        Returns xCoordinate Value.
        :return:
        :rtype:
        """
        return self.__xCoordinate

    def set_xcoordinate(self, targetx : int):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        Sets xCoordinate to target value.

        :param targetx:
        :type targetx:
        :return:
        :rtype:
        """
        self.__xCoordinate = targetx

    #yCoordinate Specific Functions
    def get_ycoordinate(self) -> int:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        Returns yCoordinate Value
        :return:
        :rtype:
        """
        return self.__yCoordinate

    def set_ycoordinate(self, targety: int):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        Sets yCoordinate to target value.
        :param targety:
        :type targety:
        :return:
        :rtype:
        """
        self.__yCoordinate = targety

    #propertyList Specfic Functions
    def get_propertylist(self) -> list:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        Returns propertyList
        :return:
        :rtype:
        """
        return self.__propertyList

    def set_properylist(self, targetlist):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        Sets propertyList to new targetList
        :param targetlist:
        :type targetlist:
        :return:
        :rtype:
        """
        self.__propertyList = targetlist

    def add_property_propertylist(self, *targetproperties: str):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        Adds property strings to the target property list

        :param targetproperties:
        :type targetproperties:
        :return:
        :rtype:
        """
        for tp in targetproperties:
            self.__propertyList.append(tp)

    def remove_property_propertylist(self, targetproperty : str):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        Finds and removes target property from property list.

        :param targetproperty:
        :type targetproperty:
        :return:
        :rtype:
        """
        if targetproperty in self.__propertyList:
            self.__propertyList.remove(targetproperty)


    #Rich Comparisons < , <= , == , >=, >

    def __lt__ (self, other) -> bool:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        <
        Returns whether other (x,y) are less than vales of self.

        :param other:
        :type other:
        :return:
        :rtype:
        """

        if self.get_xcoordinate() < other.get_xcoordinate() and self.get_ycoordinate() < other.get_ycoordinate:
            return True
        else:
            return False

    def __le__(self, other):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        <=
        Returns whether other (x,y) are less or equal to vales of self.

        :param other:
        :type other:
        :return:
        :rtype:
        """
        if self.get_xcoordinate() <= other.get_xcoordinate() and self.get_ycoordinate() <= other.get_ycoordinate:
            return True
        else:
            return False

    def __eq__(self, other) -> bool :
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        ==
        What to compare when determining whether an Ev3Coordinate object is equal to target object.

        :param other:
        :type other:
        :return:
        :rtype:
        """
        if self.get_xcoordinate() == other.xCoordinate and self.get_xcoordinate() == other.yCoordinate:
            return True
        else:
            return False

    def __ge__(self, other) -> bool :
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        >=
        Returns whether target coordinates is great or equal to (x,y) values than self.

        :param other:
        :type other:
        :return:
        :rtype:
        """
        if self.get_xcoordinate() >= other.get_xcoordinate() and self.get_ycoordinate() >= other.get_ycoordinate:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        >
        Returns whether target coordinates is great (x,y) values than self.

        :param other:
        :type other:
        :return:
        :rtype:
        """
        if self.get_xcoordinate() > other.get_xcoordinate() and self.get_ycoordinate() > other.get_ycoordinate:
            return True
        else:
            return False

    #String Representations of Ev3Coordinates Class

    def __str__(self) -> str :
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        """
        String Representation of Ev3Coordinate object

        :return:
        :rtype:
        """
        return '(' + str(self.get_xcoordinate()) + ',' + str(self.get_ycoordinate()) + ')'
