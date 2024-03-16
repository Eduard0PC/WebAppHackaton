
class SignUp:
    def __init__(self,name,lastName,password,email,phone,adress,position):
        self.name = name
        self.lastName = lastName
        self.password = password
        self.email = email
        self.phone = phone
        self.adress = adress
        self.position = position
                    
    def toDBCollection(self):
        return{
            "Nombre": self.name,
            "Apellido": self.lastName,
            "Password": self.password,
            "Email": self.email,
            "Telefono": self.phone,
            "Direccion": self.adress,
            "Posicion": self.position
        }