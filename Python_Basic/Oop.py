# Object Oriented Programming
# Class


# Class : How my data should be shaped > define structure
class Puppy:
    # Puppy's data structure
    def __init__(self):
        self.name = "Ruffus"

    def __str__(self):
        return self.name


ruffus = Puppy()  # ruffus is kind of Puppy

print(ruffus.name)  # puppy object
print(ruffus)
