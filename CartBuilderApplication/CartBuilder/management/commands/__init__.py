from .import_csv import Command as ImportCSV
from .generate_user import Command as GenerateUser
from .gen_allergies_db import Command as GenerateTopTenMockAllergies

commands = {
    'import_csv': ImportCSV,
    'gen_user': GenerateUser,
    'gen_allergies_db': GenerateTopTenMockAllergies,
}
