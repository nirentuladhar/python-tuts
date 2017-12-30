class Duck:
    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("Walks like a duck!")

    def bark(self):
        print("No bark")

    def fur(self):
        print("No fur")

class Dog:
    def bark(self):
        print("Woof!")

    def fur(self):
        print("The dog has brown and white fur")

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

    fido = Dog()
    fido.bark()
    fido.fur()

if __name__ == "__main__": main()