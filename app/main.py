import sys


def main():
    # Esperar el input del usuario
    while True:
        sys.stdout.write("$ ")
        command = input()
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
