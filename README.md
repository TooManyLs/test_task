# Телефонная книга

## Описание
Этот скрипт представляет собой телефонную книгу, позволяющую управлять и хранить контакты.

## Классы
- `Contact`: Класс для представления контакта.
- `PhoneBook`: Класс для представления телефонной книги.

## Методы
### Методы класса `PhoneBook`
- `__init__`: Инициализирует телефонную книгу, загружая контакты из файла "phone_book.csv".
- `add_contact`: Добавляет контакт в телефонную книгу.
- `edit_contact`: Редактирует контакт в телефонной книге по указанному индексу.
- `search_contacts`: Возвращает список контактов, которые соответствуют заданным критериям поиска.
- `display_contacts`: Отображает контакты на указанной странице.
- `save`: Сохраняет текущие контакты в файл "phone_book.csv".

### Главные методы
- `main`: Главная функция, которая запускает интерактивное меню для управления телефонной книгой.

## Использование
Чтобы использовать этот скрипт, просто запустите его. Вам будет представлено меню с возможностями добавления, редактирования, поиска, отображения и сохранения контактов.