from datetime import datetime
from collections import UserDict
import csv



class AddressBook(UserDict):


    def add_record(self, rec):

        self.data.update({rec.name.value: rec})


    def generator(self):

        for name, info in self.data.items():
            yield f"    > {name} {info}"

    
    def iterator(self, value):

        value = value
        gen = self.generator()

        while value > 0:
            try:
                print(next(gen))
                value -= 1
            except StopIteration:
                return ""
        return "    > Thats all!"
    

    def save(self):
        
        with open("book.csv", "w", newline="") as file:

            fields = ["Name", "Info"]
            writer = csv.DictWriter(file, fields)
            writer.writeheader()

            for name, info in self.data.items():

                writer.writerow({"Name": name, "Info": info})

            print("    > Saving data.")



    def load(self):

        try: 

            with open("book.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    saved = {row["Name"]: row["Info"]}
                    self.data.update(saved)

                print("    > Data loaded.")
        except:
            print("    > Data is not covered.")
        return ""
    

    def find(self, value: str):   
        value = value.lower()
        res = ""
        for name, info in self.data.items():
            if value in name.lower() or value in str(info).lower():
                res += (f"    > {name} {info}\n")
        if len(res) > 0:
            print(res.strip())
        else:
            print("    > Not found.")

         
        

        
        
class Field:
    

    def __init__(self, value):
        self._value = value


    def __str__(self):
        return self.value
    

    @property
    def value(self):
        return self._value
    

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):  

    def __str__(self):
        return self.value


class Phone(Field):


    def __init__(self, value):
        self.value = value

    
    def __repr__(self):

        return self.value
    
    
    @property
    def val(self):
        return self.value


    @val.setter
    def val(self, new_value):
        if len(new_value) == 10:
            self.value = new_value
        else:
            self.value = new_value
            print('    > Invalid phone!')




class Birthday(Field):


    def __init__(self, new_value):
        try:
            self.value = datetime.strptime(new_value, "%d/%m/%Y").date()
        except ValueError:
            print('    > Invalid date! DD/MM/YYYY')


    def __str__(self):
        return str(self.value)



    @property
    def val(self):
        return self.value


    @val.setter
    def val(self, new_value):
        try:
            self.value = datetime.strptime(new_value, "%d/%m/%Y").date()
        except ValueError:
            print('    > Invalid date! DD/MM/YYYY')


class Record:
    

    def __init__(self, name, birthday, *phones, ):
        self.name = name
        self.phone = phone
        self.phones = list(phones)
        self.birthday = birthday


    def days_to_birthday(self):
        if self.birthday != "-":
            now = datetime.now()
            birthday_date_now = datetime(year=now.year, month=self.birthday.val.month, day=self.birthday.val.day)
            print(f"    > {(birthday_date_now.date() - datetime.now().date()).days}" )
            return (birthday_date_now.date() - datetime.now().date()).days
        

    def new_phone(self, phone):
        self.phones.append(Phone(phone))       
        print(f"    > You have updated the contact {self.phones}.\n")


    def delete_phone(self, phone):

        for it in self.phones:
            if str(it) == phone:
                self.phones.remove(it)

        print(f"    > You deleted the contact's phone number: {phone}")
        print(f"    > {self.name}: {self.phones}")


    def __repr__(self):
        return f"phone: {self.phone}, birthday: {self.birthday}"
        
        
        


    

if __name__ == '__main__':
    name = Name("bob")
    phone = Phone("1234567890")
    bd = Birthday("12/4/2014")
    rec = Record(name, bd, phone)
    ab = AddressBook()
    ab.add_record(rec)


    name = Name("nic")
    phone = Phone("2649301748")
    bd = Birthday("20/3/2002")
    rec = Record(name, bd, phone)
    ab.add_record(rec)
    
    ab.find("264")





    