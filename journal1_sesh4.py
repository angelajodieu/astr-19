#defining a class that describes my favorite animal
class DescribeFavAnimal:
    #initialization function
    def __init__(self, len_arms, len_legs, num_eyes, tail, furry):
        self.len_arms = len_arms
        self.len_legs = len_legs
        self.num_eyes = num_eyes
        self.tail = tail
        self.furry = furry

    #function for printing out the details
    def print_info(self):
        print(f"My animal's arms are {self.len_arms} feet long.")
        print(f"My animal's legs are {self.len_legs} feet long.")
        print(f"My animal has {self.num_eyes} eyes.")
        print(f"My animal has a tail: {self.tail}")
        print(f"My animal is furry: {self.furry}")

def main():
    print("My favorite animal is an orangutan")
    #class object creation
    animal = DescribeFavAnimal(7, 5, 2, False, True)
    #printing out the details
    animal.print_info()

if __name__=="__main__":
    main()

