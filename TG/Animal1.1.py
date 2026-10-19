class Animal:
    def __init__(self, name, species, age, weight, diet):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight
        self.diet = diet 

    def make_sound(self):
        return f"{self.name} издает естественный звук."

    def eat(self, food):
        return f"{self.name} с аппетитом ест {food}."

    def __str__(self):
        return (f"Кличка: {self.name} | Вид: {self.species} | " 
                f"Возраст: {self.age} лет | Вес: {self.weight} кг | Питание: {self.diet}")


class Reptiles(Animal):  
    def __init__(self, name, species, age, weight, diet, scale_color, is_venomous, is_constrictor):
        super().__init__(name, species, age, weight, diet)
        self.scale_color = scale_color
        self.is_constrictor = is_constrictor
        self.is_venomous = is_venomous

    def hunt(self):
        if self.is_constrictor:
            return f"{self.name} — душитель (constrictor), обвивает жертву кольцами!"
        elif self.is_venomous:
            return f"{self.name} атака укусом и парализует ядом!"
        else:
            return f"{self.name} стремительно атаковал добычу!"

    def shed_skin(self):
        return f"{self.name} сбрасывает старую чешую."


class Amphibians(Animal):  
    def __init__(self, name, species, age, weight, diet, skin_moisture, can_swim):
        super().__init__(name, species, age, weight, diet)
        self.skin_moisture = skin_moisture
        self.can_swim = can_swim

    def jump(self):
        return f"{self.name} совершает самый высокий прыжок в воду!"

    def breathe_through_skin(self):
        return f"{self.name} поглощает кислород через влажную кожу."



class ZooShow:
    def __init__(self, reptile_star, amphibian_star):
        self.reptile_star = reptile_star
        self.amphibian_star = amphibian_star

    def start_show(self):
        print("\n--- ДОБРО ПОЖАЛОВАТЬ В ЗООШОУ! ---")
        print("Какое шоу вы хотите посетить?")
        print("1 — Шоу Пресмыкающихся")
        print("2 — Шоу Земноводных")
        
        choice = input("Ваш выбор (1 или 2): ").strip()

        if choice == "1":
            show_type = "Шоу пресмыкающихся"
            performer = self.reptile_star
            trick = f"{performer.hunt()} Затем гигантский питон гипнотизирует зрителей и пролезает через огненное кольцо!"
        elif choice == "2":
            show_type = "Шоу земноводных"
            performer = self.amphibian_star
            trick = f"{performer.jump()} Додо исполняет синхронный танец в воде и ловит мух на лету!"
        else:
            print("Неверный выбор. Завершение программы.")
            return

        print(f"\nВы выбрали шоу: {show_type}")
        print("\nВыберите тип билета:")
        print("1 — Обычный (700 сом / доллар)")
        print("2 — VIP (1700 сом / доллар)")

        ticket_choice = input("Введите номер типа билета (1 или 2): ").strip()

        if ticket_choice == "1":
            ticket_type = "Обычный"
            price = 700
            seat = "Сектор Б, ряд 7"
        elif ticket_choice == "2":
            ticket_type = "VIP"
            price = 1700
            seat = "VIP-ложа, 1 ряд прямо перед ареной"
        else:
            print("Неверный выбор билета.")
            return

        print("\n" + "=" * 50)
        print("ВАШ БИЛЕТ УСПЕШНО ОФОРМЛЕН!")
        print(f"Категория: {ticket_type} | Цена: {price} | Место: {seat}")
        print("=" * 50)
        print(f"\n🎉 «ШОУ {performer.name.upper()}» 🎉")
        print(f"Программа: {trick}")




if __name__ == "__main__":
    python_snake = Reptiles(
        name="Нейтири", 
        species="Сетчатый питон", 
        age=7, 
        weight=24.0, 
        diet="Хищник", 
        scale_color="Изумрудно-золотой", 
        is_venomous=False,
        is_constrictor=True
    )

    giant_frog = Amphibians(
        name="Додо", 
        species="Лягушка-бык", 
        age=3, 
        weight=2.2, 
        diet="Насекомоядное", 
        skin_moisture="Высокая", 
        can_swim=True
    )

   
    show = ZooShow(reptile_star=python_snake, amphibian_star=giant_frog)
    show.start_show()