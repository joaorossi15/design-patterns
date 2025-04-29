from random import randrange

class Observer():
    def update(self, value):
        pass


class Subject():
    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self, message):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        self._observers: list[Observer] = []
    
    def attach(self, observer):
        self._observers.append(observer)
        print(f"attached observer: {observer.name}")

    def detach(self, observer):
        self._observers.remove(observer)
        print(f"\ndetached observer: {observer.name}")

    def notify(self, message):
        print("notifying observers...")
        for observer in self._observers:
            observer.update(message)

    def logic(self):
        print('\n[subject] doing something important')
        v = randrange(0,1000)
        print(f'[subject] value changed to: {v}')
        self.notify(v)


class ConcreteObserver(Observer):
    def __init__(self, name, treshold):
        self.name = name
        self.treshold = treshold

    def update(self, value):
        if value >= self.treshold:
            print(f"[{self.name}] reacted to the update")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserver("observer A", 1)
    observer_b = ConcreteObserver("observer B", 256)
    
    subject.attach(observer_a)
    subject.attach(observer_b)

    subject.logic()

    subject.detach(observer_a)

    subject.logic()
