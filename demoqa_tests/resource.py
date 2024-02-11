from pathlib import Path

import allure


@allure.step('Provide file path')
def path(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'resources/{file_name}'))
