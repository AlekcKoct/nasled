# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#
# Требования:#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администратора
        self.admin_level = admin_level  # Дополнительный уровень доступа для администраторов
        self.__users = []  # Список пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: объект не является пользователем.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Ошибка: пользователь не найден.")

    def list_users(self):
        if not self.__users:
            print("Нет зарегистрированных пользователей.")
            return
        print("Список пользователей:")
        for user in self.__users:
            print(f"Индивидуальный номер: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


if __name__ == "__main__":
    admin = Admin(user_id=1, name="Алексей", admin_level="super")

    user1 = User(user_id=2, name="Иван")
    user2 = User(user_id=3, name="Мария")

    admin.add_user(user1)
    admin.add_user(user2)

    admin.list_users()

    admin.remove_user(2)

    admin.list_users()