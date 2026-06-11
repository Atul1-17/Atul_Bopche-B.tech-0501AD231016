class AccountLockedError(Exception):
    pass

class Login_system:
    __password = "python@123"
    __attempts = 3

    def loginPassword(self, password):
        try:
            if password != self.__password:
                self.__attempts -= 1
                print(f"password attempts left: {self.__attempts}")
                if self.__attempts <= 0:
                    raise AccountLockedError("Account locked due to too many failed attempts")
            else:
                print("Login successful!")
        except AccountLockedError as ale:
            print(f"error occurred: {ale}")
        finally: 
            print("Login attempt complete.")


l = Login_system()
l.loginPassword("neww")
l.loginPassword("hdbsj")
l.loginPassword("jsjj")
l.loginPassword("python@123")