import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    second_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: str
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state_city: str


Oleg = User(
    first_name="Ivan",
    second_name="Ivanov",
    email="Ivanov@test.com",
    gender="Male",
    phone_number="1234567890",
    date_of_birth="10 January,1980",
    subjects="Physics",
    hobbies="Sports",
    picture="picture.jpg",
    current_address="111999, St Hall avenue 34",
    state_city="Haryana Karnal"
)
