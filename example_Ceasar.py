class record:
    def __init__(self, fn, ln, address):
        self.fn = fn
        self.ln = ln
        self.address = address

    def example_for_u(self):
        print("this is a function inside a class and the first name is " + self.fn)

guy = record("jake", "garcia", "69 suck my butt street")

print(guy.fn)
print(guy.ln)
print(guy.address)
guy.example_for_u()
