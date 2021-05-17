Notes: 10/27/2020

# Attributes!!

    class User:
        # Attributes
        def __init__(self):
            self.username = "awesome_pants"
            self.email = "fake@email.com"
            self.password = "123qweasd"

        # Methods

    john = User()
    print(john.username)
    print(john.email)
    print(john.password)

    mary = User()




    class User:
        # Attributes
        def __init__(self, username_from_user):
            self.username = username_from_user
            self.email = "fake@email.com"
            self.password = "123qweasd"

        # Methods

    john = User('mypinkponies')
    print(john.username)

    mary = User('littlelamgsaretasty')
    print(mary.username)



    # When you have specified attributes

    class User:
        # Attributes
        def __init__(self, username_from_user, email_from_user, password_from_user):
            self.username = username_from_user
            self.email = email_from_user
            self.password = password_from_user

        # Methods

    john = User('john', 'john@hotmail.com', 'alligator87')
    print(john.username)

    mary = User('mary', 'littlelamb@shopity.com', 'fuzzywuzzywasabear')
    print(mary.username)



    # Setting default parameters
    # Once u start a default, you have to add defaults for all items after (to the right)

    class User:
        # Attributes
        def __init__(self, username_from_user = "general_username", email_from_user = "place@holder.net", password_from_user = "passy_password"):
            self.username = username_from_user
            self.email = email_from_user
            self.password = password_from_user

        # Methods

    john = User('john', 'john@hotmail.com', 'alligator87')
    print(john.username)
    print(john.email)
    print(john.password)

    mary = User('mary')
    print(mary.username)
    print(john.email)
    print(john.password)






    class User:
        # Attributes
        def __init__(self, username_from_user = "general_username", email_from_user = "place@holder.net", password_from_user = "passy_password"):
            self.username = username_from_user
            self.email = email_from_user
            self.password = password_from_user

        # Methods

    john = User('john', 'john@hotmail.com', 'alligator87')
    # print(john.username)
    # print(john.email)
    # print(john.password)
    print(john.__dict__)        # This will print out the information as a dictionary!

    mary = User('mary')
    # print(mary.username)
    # print(john.email)
    # print(john.password)





# Methods!!!

    class User:
        # Attributes
        def __init__(self, username_from_user = "general_username", email_from_user = "place@holder.net", password_from_user = "passy_password"):
            self.username = username_from_user
            self.email = email_from_user
            self.password = password_from_user

        # Methods
        def say_hi(self):
            print("Hi, my name is", self.username)

    john = User('john', 'john@hotmail.com', 'alligator87')
    john.say_hi()

    mary = User('mary')
    mary.say_hi()




    class User:
        # Attributes
        def __init__(self, username_from_user = "general_username", email_from_user = "place@holder.net", password_from_user = "passy_password"):
            self.username = username_from_user
            self.email = email_from_user
            self.password = password_from_user

        # Methods
        def say_hi(self, person):
            print(f"Hi, {person} my name is, {self.username}")

    john = User('John', 'john@hotmail.com', 'alligator87')
    mary = User('Mary')
    
    john.say_hi("Mary")
    mary.say_hi("John")    




    class User:
        # Attributes
        def __init__(self, username_from_user = "general_username", email_from_user = "place@holder.net", password_from_user = "passy_password"):
            self.username = username_from_user
            self.email = email_from_user
            self.password = password_from_user

        # Methods
        def say_hi(self, person):
            print(f"Hi, {person} my name is, {self.username}")

        def wave(self, person):
            print()

    john = User('John', 'john@hotmail.com', 'alligator87')
    mary = User('Mary')
    
    john.say_hi("Mary")
    mary.say_hi("John")    