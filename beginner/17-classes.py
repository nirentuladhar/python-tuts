class Duck:
    def __init__ (self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quack!')

    def walk(self):
        print("walkie walkie")

    def set_variables(self, k, v):
        self.variables[k] = v

    def get_variables(self, k):
        return self.variables.get(k, None)

def main():
    donald = Duck(feet = "blue")
    print(donald.get_variables("feet"))

if __name__ == "__main__": main()
