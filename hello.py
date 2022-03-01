import unittest
import subprocess

TARGET = "hello"

class HelloTest(unittest.TestCase):

    def test1(self):
        """
        Testea si el programa existe
        """
        stdout = subprocess.run("ls", stdout = subprocess.PIPE).stdout.decode('utf-8')
        try:
            self.assertIn("hello.c", stdout)
        except (AssertionError):
            print()
            print("[ERROR] El archivo 'hello.c' no existe")

    def test2(self):
        """
        Testea si el programa compila
        """
        subprocess.run(f"gcc -o {TARGET} {TARGET}.c", stdout = subprocess.PIPE)
        stdout = subprocess.run("ls", stdout = subprocess.PIPE).stdout.decode('utf-8')
        try:
            self.assertIn(f"{TARGET}\n", stdout)
        except (AssertionError):
            print()
            print("[ERROR] El programa no compila")
            print(f"[TIP] Ejecute: gcc {TARGET} {TARGET}.c en la consola para ver los errores")

    def test3(self):
        """
        Ejecuta el programa sin argumentos y compara la salida
        """
        stdout = subprocess.run("./hello", stdout = subprocess.PIPE).stdout.decode('utf-8')
        try:
            self.assertEqual(stdout, "Uso: ./hello [nombre]")
        except (AssertionError):
            print()
            print("[ERROR] El mensaje de salida para el nombre '' no es 'Uso: ./hello [nombre]'")

    def test4(self):
        """
        Ejecuta el programa con un argumento y compara la salida
        """
        stdout = subprocess.run("./hello Pepe", stdout = subprocess.PIPE).stdout.decode('utf-8')
        try:
            self.assertEqual(stdout, "Hola Pepe!")
        except (AssertionError):
            print()
            print("[ERROR] El mensaje de salida para el nombre 'Pepe' no es 'Hola Pepe!'")

if __name__ == '__main__':
    unittest.main()