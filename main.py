from app.password.password import Password

from app.requirement.additions.middle_numbers_or_symbols import MiddleNumbersOrSymbols
from app.requirement.additions.minimum_requirements import MinimumRequirements
from app.requirement.additions.number_of_characters import NumberOfCharacters
from app.requirement.additions.symbols import Symbols
from app.requirement.additions.uppercase_letters import UppercaseLetters
from app.requirement.additions.lowercase_letters import LowercaseLetters
from app.requirement.additions.numbers import Numbers

from app.requirement.deductions.letters_only import LettersOnly
from app.requirement.deductions.numbers_only import NumbersOnly

total = 0

# _PASSWORD = Password('asd123DFG!@#')
_PASSWORD = Password('asdaaaaaaa')

_LIST_ADDITIONS_TESTS = [
    NumberOfCharacters(_PASSWORD),
    UppercaseLetters(_PASSWORD),
    LowercaseLetters(_PASSWORD),
    Numbers(_PASSWORD),
    Symbols(_PASSWORD),
    MiddleNumbersOrSymbols(_PASSWORD),
    MinimumRequirements(_PASSWORD)
]

_LIST_DEDUCTIONS_TESTS = [
    LettersOnly(_PASSWORD),
    NumbersOnly(_PASSWORD)
]


print('\033[1;32m')
print(format(' ADDITIONS TEST ', '=^50'))
print()
for test in _LIST_ADDITIONS_TESTS:
    print(format(str(type(test)).split('.')[-1][:-2], '<25'), end='\t')
    print(format(f"Count: {test.get_count()}",'>10'), end='\t')
    print(format(f"Bonus: +{test.get_bonus()}", '>10'))
    print()
    total += test.get_bonus()
print('\033[m')



print('\033[1;31m')
print(format(' DEDUCTIONS TEST ', '=^50'))
print()
for test in _LIST_DEDUCTIONS_TESTS:
    print(format(str(type(test)).split('.')[-1][:-2], '<25'), end='\t')
    print(format(f"Count: {test.get_count()}",'>10'), end='\t')
    print(format(f"Bonus: {test.get_bonus()}", '>10'))
    print()
    total += test.get_bonus()
print('\033[m')


print('\033[1;36m')
print(format(' TOTAL: ', '.<40'), format(f'{total}', '<4'))
print('\033[m')
