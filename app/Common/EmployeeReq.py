from setuptools.build_meta import _to_str


class EmployeeReq:
    # Username: str
    # Password: str
    def __init__(self):
        self.userName = None
        self.password = None
        self.lastName = None
        self.firstName = None
        self.identityCard = None
        self.phoneNumber = None
        self.birthDay = None
        self.gender = None
        self.address = None
        self.note = None

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self, value):
        self._userName = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = value

    @property
    def identityCard(self):
        return self._identityCard

    @identityCard.setter
    def identityCard(self, value):
        self._identityCard = value

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        self._phoneNumber = value

    @property
    def birthDay(self):
        return self._birthDay

    @birthDay.setter
    def birthDay(self, value):
        self._birthDay = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value

    def __str__(self):
        data = {"userName": self.userName,
                "password": self.password,
                "firstName": self.firstName,
                "lastName": self.lastName,
                "identityCard": self.identityCard,
                "phoneNumber": self.phoneNumber,
                "birthDay": self.birthDay,
                "gender": self.gender,
                "address": self.address,
                "note": self.note}
        return data
