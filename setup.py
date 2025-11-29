import subprocess
import sys


def run(cmd):
    print(f"\n$ {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Erro ao executar: {cmd}")
        sys.exit(result.returncode)


if __name__ == "__main__":
    # Aplica migrações
    run("uv run python manage.py migrate")

    # Roda o servidor de desenvolvimento
    run("uv run python manage.py runserver")
