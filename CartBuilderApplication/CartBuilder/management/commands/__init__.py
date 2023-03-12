from .import_csv import Command as ImportCSV
from .gen_user import Command as GenerateUser
from .gen_allergies_db import Command as GenerateTopTenMockAllergies
from .gen_user2 import Command as GenerateUser2

commands = {
    'import_csv': ImportCSV,
    'gen_user': GenerateUser,
    'gen_allergies_db': GenerateTopTenMockAllergies,
    'gen_user2': GenerateUser2,
}
