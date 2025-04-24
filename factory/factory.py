from colorama import Fore, Style, init
import time

init(autoreset=True)

class Shape():
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        print(Fore.GREEN + r"""
        +-------+
        |       |
        |       |
        |       |
        +-------+
        """)
        self._animate("drawing a square...")

    def _animate(self, msg):
        for ch in msg:
            print(Fore.GREEN + ch, end='', flush=True)
            time.sleep(0.03)
        print()

class Triangle(Shape):
    def draw(self):
        print(Fore.YELLOW + r"""
           /\
          /  \
         /    \
        /______\
        """)
        self._animate("drawing a triangle...")

    def _animate(self, msg):
        for ch in msg:
            print(Fore.YELLOW + ch, end='', flush=True)
            time.sleep(0.03)
        print()


class ShapeFactory:
    def create_shape(shape_type: str) -> Shape:
        if shape_type == "square":
            return Square()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError("unknown shape")


if __name__ == "__main__":
    print(Fore.LIGHTMAGENTA_EX + "choose your shape")
    print("square / triangle")
    choice = input(": ").strip().lower()

    try:
        shape = ShapeFactory.create_shape(choice)
        print()
        shape.draw()
    except ValueError as e:
        print(Fore.RED + str(e))

