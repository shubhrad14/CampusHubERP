class NonEmptyName:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty.")

        instance.__dict__[self.name] = value.strip()


class ValidEmail:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Email must contain @.")

        instance.__dict__[self.name] = value


class ValidAge:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or not 16 <= value <= 80:
            raise ValueError("Age must be between 16 and 80.")

        instance.__dict__[self.name] = value

