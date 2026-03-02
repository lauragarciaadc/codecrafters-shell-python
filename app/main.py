import sys


def main():
    sys.stdout.write("$ ")
    # Esperar el input del usuario
    command = input()
    print(f"{command}: command not found")


if __name__ == "__main__":
    main()
