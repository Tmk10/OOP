

class Property:
    def __init__(self, square_feet='', beds ='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))


    def prompt_init():
        return dict(square_feet = input("Enter the square feet: "), beds = input("Enter number of beedroms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)

class Apartment(Property):

    valid_laundires = {"coin", "ensuite", "none"}
    valid_balconies = {"yes", "no", "solarium"}

    def __init__(self, balcony = '', laundry = '', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.lanudry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s".format(self.lanudry))
        print("has balcony: {}".format(self.balcony))

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundires:
            laundry = input("What laundry facilities does the property have? ({})".format(", ".join(Apartment.valid_laundires)))
        balcony = ''
        while balcony.lower() not in Apartment.valid_laundires:
            balcony = input("Does the property have a balcony" "({})".format(", ".join(Apartment.valid_balconies)))
        parent_init.update({"laundry":laundry, "balcony":balcony})
        return parent_init
    prompt_init = staticmethod(prompt_init())

 
