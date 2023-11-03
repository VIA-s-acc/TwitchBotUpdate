import subprocess
import time

python_executable = ".venv/Scripts/python"

# Путь к вашей Python-программе, которую вы хотите перезапускать
program_path = "main.py"
process = None  # Инициализируем переменную для хранения процесса

while True:
    print("STARTED")

    # Закрываем предыдущий процесс, если он существует
    if process is not None:
        process.kill()
        process.wait()  # Ждем, пока процесс завершится

    # Запускаем новый процесс
    process = subprocess.Popen([python_executable, program_path])

    # Подождать 5 минут (300 секунд) перед следующим запуском
    time.sleep(300)
    print("RESTARTING")