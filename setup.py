from setuptools import setup, find_packages

setup(
    name='check_double_quotes',  # Название вашего хука
    version='1.0',
    py_modules=['check_double_quotes'],  # Укажите здесь имя вашего модуля
    entry_points={
        'console_scripts': [
            'check-double-quotes = check_double_quotes:main',  # Это указывает на точку входа в вашем скрипте
        ],
    },
)
