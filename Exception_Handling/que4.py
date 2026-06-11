class UnderAgeError(Exception):
    pass

class InvalidAgeError(Exception):
    pass



class AgeVerification:
    def setAge(self, age):
        try:
            if age < 0:
                raise ValueError("Age cannot be negative")
            elif age < 18:
                raise UnderAgeError("Age must be at least 18")
            elif age > 100:
                raise InvalidAgeError("Invalid Age")
            else:
                print("Valid age!")

        except Exception as ve:
            print(f"error occurred: {ve}")

        finally:
            print("Age verification complete.")


A = AgeVerification()
A.setAge(25)
A.setAge(16)
A.setAge(-5)
