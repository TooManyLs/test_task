import csv
class Contact:
    def __init__(self, surname, name, patronymic, organization, work_phone, personal_phone):
        """Класс для представления контакта."""
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

class PhoneBook:
    """Класс для представления телефонной книги."""
    def __init__(self):
        self.contacts = []
        self.hr = "-" * 110
        try:
            with open("phone_book.csv", 'r', encoding="utf-8") as f:
                reader = csv.reader(f)
                self.contacts = [Contact(*row) for row in reader]
        except:
            pass

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, index, contact):
        if index == 0:
            return "Шапку изменять нельзя!"
        self.contacts[index] = contact

    def search_contacts(self, **kwargs):
        return [
            print(f"{i:3}. \t{"Фамилия: " + contact.surname:<35}{"Имя: " + contact.name:<35}{"Отчество: " + contact.patronymic:<35}\n\t{"Орг.: " + contact.organization:<35}{"Раб.телефон: " + contact.work_phone:<35}{"Сот.телефон: " + contact.personal_phone:<35}\n{self.hr}")\
            for i, contact in enumerate(self.contacts) if all(getattr(contact, key).lower() == value.lower() for key, value in kwargs.items())]

    def display_contacts(self, page, contacts_per_page=10):
        start_index = (page - 1) * contacts_per_page
        end_index = start_index + contacts_per_page
        contacts = self.contacts[start_index:end_index]
        for i, contact in enumerate(contacts):
            print(f"{i + (contacts_per_page * (page - 1)):3}. \t{"Фамилия: " + contact.surname:<35}{"Имя: " + contact.name:<35}{"Отчество: " + contact.patronymic:<35}\n\t{"Орг.: " + contact.organization:<35}{"Раб.телефон: " + contact.work_phone:<35}{"Сот.телефон: " + contact.personal_phone:<35}\n{self.hr}")

    def save(self):
        with open("phone_book.csv", 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            for contact in self.contacts:
                writer.writerow([
                    contact.surname, 
                    contact.name, 
                    contact.patronymic, 
                    contact.organization, 
                    contact.work_phone, 
                    contact.personal_phone
                    ])

command_list = [
    "1. Добавить контакт",
    "2. Изменить контакт",
    "3. Поиск контакта",
    "4. Отобразить страницу",
    "5. Сохранить изменения",
    "6. Выйти"
]
def main():
    pb = PhoneBook()
    while True:
        for cmd in command_list:
            print(cmd)
        action = input("Выберите действие из списка: ")
        if action == "6":
            break
        elif action == "1":
            surname = input("Фамилия: ")
            name = input("Имя: ")
            patronymic = input("Отчество: ")
            organization = input("Организация: ")
            work_phone = input("Рабочий телефон: ")
            personal_phone = input("Личный телефон: ")
            contact = Contact(surname, name, patronymic, organization, work_phone, personal_phone)
            pb.add_contact(contact)
        elif action == "2":
            index = 0
            while not int(index) in range(1, len(pb.contacts)):
                index = input("Индекс контакта для редактирования: ")
                if index.lower == "q":
                    index = 0
                    break
            index = int(index)
            if index == 0:
                continue
            surname = input("Фамилия: ")
            name = input("Имя: ")
            patronymic = input("Отчество: ")
            organization = input("Организация: ")
            work_phone = input("Рабочий телефон: ")
            personal_phone = input("Личный телефон: ")
            contact = Contact(surname, name, patronymic, organization, work_phone, personal_phone)
            pb.edit_contact(index, contact)
        elif action == "3":
            search_params = {}
            while True:
                inputs = "surname, name, patronymic, organization, work_phone, personal_phone, q"
                field = "0"
                while field not in inputs:
                    field = input("Введите поле для поиска (surname, name, patronymic, organization, work_phone, personal_phone)\nили 'q' для завершения поиска: ")
                if field.lower() == "q":
                    break
                value = input(f"Введите значение для поиска в поле {field}: ")
                search_params[field] = value
            pb.search_contacts(**search_params)
        elif action == "4":
            page = int(input("Номер страницы: "))
            pb.display_contacts(page)
        elif action == "5":
            pb.save()


if __name__ == "__main__":
    main()