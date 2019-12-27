from app.password.password import Password


from app.requirement.additions.number_of_characters import NumberOfCharacters
from app.requirement.additions.uppercase_letters import UppercaseLetters
from app.requirement.additions.lowercase_letters import LowercaseLetters
from app.requirement.additions.numbers import Numbers


_PASSWORD = Password('SNDAUOibdswqai218937')

_ADDITIONS_TESTS = [
    NumberOfCharacters(_PASSWORD),
    UppercaseLetters(_PASSWORD),
    LowercaseLetters(_PASSWORD),
    Numbers(_PASSWORD)
]

print(format(' ADDITIONS TEST ', '=^50'))
for test in _ADDITIONS_TESTS:
    print(f"Count: {test.get_count()}")
    print(f"Bonus: {test.get_bonus()}")


