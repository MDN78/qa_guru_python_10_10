import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str


oleg = User(
    first_name="Ivan",
    last_name="Ivanov",
    email="Ivanov@test.com",
    gender="Male",
    phone_number="1234567890",
    date_of_birth_year='1980',
    date_of_birth_month='January',
    date_of_birth_day='10',
    subjects="Physics",
    hobbies="Sports",
    picture="picture.jpg",
    current_address="111999, St Hall avenue 34",
    state="Haryana",
    city="Karnal",
)

@dataclasses.dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


semen = SimpleUser(
    full_name='Semen Semenov',
    email='semeov@gmail.de',
    current_address='111999, St Hall avenue 34',
    permanent_address='123456, St Persons street 42'
)
