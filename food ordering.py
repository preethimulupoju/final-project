print("Welcome to the restaurant ordering system!")
users = {
    "admin": "password",
    "user1": "password1"
}

# Prompt the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the entered username and password match those of the admin or a user
if username == "admin" and password == users["admin"]:
    print("Welcome, admin!")
elif username in users and password == users[username]:
    print("Welcome, user!")
else:
    print("Invalid username or password.")
# User class to store user information
class User:
    def __init__(self, name, phone, email, address, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.password = password

# Function to register a new user
def register():
    name = input("Enter your full name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")
    return User(name, phone, email, address, password)

# Function to log in an existing user
def login(users):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None

# Example usage
food_items = {}

def add_food_item(food_id, name, quantity, price, discount, stock):
  food_items[food_id] = {
    "name": name,
    "quantity": quantity,
    "price": price,
    "discount": discount,
    "stock": stock
  }

def edit_food_item(food_id, name=None, quantity=None, price=None, discount=None, stock=None):
  # Check if the FoodID exists in the dictionary
  if food_id in food_items:
    food_item = food_items[food_id]
    # Update the values if they are provided
    if name:
      food_item["name"] = name
    if quantity:
      food_item["quantity"] = quantity
    if price:
      food_item["price"] = price
    if discount:
      food_item["discount"] = discount
    if stock:
      food_item["stock"] = stock
  else:
    print(f"Food item with FoodID {food_id} does not exist.")

def remove_food_item(food_id):
  # Check if the FoodID exists in the dictionary
  if food_id in food_items:
    del food_items[food_id]
  else:
    print(f"Food item with FoodID {food_id} does not exist.")

def view_food_items():
  for food_id, food_item in food_items.items():
    print(f"FoodID: {food_id}")
    print(f"Name: {food_item['name']}")
    print(f"Quantity: {food_item['quantity']}")
    print(f"Price: {food_item['price']}")
    print(f"Discount: {food_item['discount']}")
    print(f"Stock: {food_item['stock']}")
    print()

# Add a few food items
add_food_item(1, "Pizza", "1 slice", 10, 0, 10)
add_food_item(2, "Burger", "1 piece", 5, 0, 5)
add_food_item(3, "Pasta", "1 bowl", 8, 0, 8)

# View all food items
view_food_items()

# Edit a food item
edit_food_item(2, name="Veg Burger", price=7)

# View all food items
view_food_items()

# Remove a food item
remove_food_item(3)

# View all food items
view_food_items()


from msilib.schema import SelfReg
from tkinter import Menu, Menubutton


class Restaurant:
    
    def __init__(self, name):
        self.restro_name=name
        self.food={}
        self.food_ID=len(self.food)+1
        self.admin_details={}
        self.user_details={}
        self.ordered_item=[]

        
    # admin functionalities
    
    
    def admin_register(self):
        try:
            self.admin_email=input("Enter your email id : ")
            self.admin_pass=input("Enter your password : ")
            self.admin_details={"Email_ID":self.admin_email,"Password":self.admin_pass}
            print("\n!! Admin Account is Created Successfully !!\n")
            print(f"Welcome TO {self.restro_name} Restaurant\n")
            print("Admin Details : ")
            for i in self.admin_details:
                print(i, ":", self.admin_details[i])
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")
            
            
    def admin_login(self):
        try:
            print(f"Welcome TO {self.restro_name} Restaurant\n\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.admin_details.values())!=0:
                if email==self.admin_email and pas==self.admin_pass:
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Add Food Item \n2. Edit Food Item\n3. View Food Item\n4. Delete Food Item\n5. Exit")
                        z=input()
                        if z=="1":
                            self.add_food_item()
                        elif z=="2":
                            self.edit_food_item()
                        elif z=="3":
                            self.view_food_item()
                        elif z=="4":
                            self.delete_food_item()
                        elif z=="5":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no Admin Account with this Email ID !\n\n!! Please Creat Your Account First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")
            
        
    def add_food_item(self):
        try:
            name=input("Enter the food name : ")
            quantity=float(input("Enter the quantity in values only : "))
            price=float(input("Enter the price in Rs only : "))
            discount=float(input("Enter the discount in Rs only : "))
            stock=float(input("Enter the available stock in values only : "))
            food_item={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item
            print("\n!! Food Item added successfully !!\n")
            print("Newly Added items :", self.food,"\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
        
        
    def edit_food_item(self):
        try:
            x=int(input("Enter the Food ID you want to update : \n"))
            if x in self.food.keys():
                print("1. Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock \n")
                y= input("Enter the number only : ")
                if y=="1":
                    self.food[x]["Name"]=input("Updated Food name : ")
                    print("\n!! Successfully Updated !!\n")
                elif y=="2":
                    self.food[x]["Quantity"]=float(input("Updated Quantity in values only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="3":
                    self.food[x]["Price"]=float(input("Updated Price in Rs only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="4":
                    self.food[x]["Discount"]=float(input("Updated Discount in Rs only : "))
                    print("\n!! successfully Updated !!\n")
                elif y=="5":
                    self.food[x]["Stock"]=float(input("Updated Stock in values only : "))
                    print("\n!! Successfully Updated !!\n")
                else:
                    print("!! Sorry Invalid Number !!\n")
            else:
                print("\n!! Incorrect Food ID !!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")  
            
            
    def view_food_item(self):
        print("List of Food Items : \n")
        if len(self.food)!=0:    
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("!! Sorry No Food Items is Added !!\n")
            

    def delete_food_item(self):
        try:
            print("!! Warning !!\nFood Item will Delete Permanently\n")
            print("Enter the Food ID ")
            x=int(input())
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List\n",self.food)
            else:
                print("!! Incorrect Food ID!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
                
                
    # user functionalities
                   
        
    def user_register(self):
        try:
            user_name=input("Enter your full name : ")
            phone_no=int(input("Enter your 10 digit phone number : "))
            email=input("Enter your email id : ")
            password=input("Enter your password : ")
            address=input("Enter your address with area PIN code ")
            self.user_details={"User Name":user_name,"Phone No.":phone_no,"Email_ID":email,"Password":password,"Address":address}
            print("\n!! Your Account is Created Successfully !!\n")
            print(f"Welcome TO {self.restro_name} Restaurant\n")
            print("User Details : ")
            for i in self.user_details:
                print(i, ":", self.user_details[i])        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")      
            
               
    def user_login(self):
        try:
            print(f"Welcome TO {self.restro_name} Restaurant\n\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.user_details.values())!=0:                                                            #we can same as admin by using self.email..etc
                if email==self.user_details["Email_ID"] and pas==self.user_details["Password"]:      # we can make it either object level or local level inside def fun
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Exit")
                        z=input()
                        if z=="1":
                            self.place_order()
                        elif z=="2":
                            self.ordered_history()
                        elif z=="3":
                            self.update_details()
                        elif z=="4":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no User Account with this Email ID !\n\n!! Please Creat Your Account First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")  
            
            
def place_order(self):
        try:
            if len(self.food)!=0:
                print("list of Availabe Food Items :\n")
                menu=[]
                for items in self.food:
                    menu.append([self.food[items],["1"],["Truffle Cake"], self.food[items]["quantity,500gm"],self.food[items]["price,INR 900"]]) 
                    menu.append([self.food[items],["2"]["Vegan Burger"], self.food[items]["quantity,1 piece"],self.food[items]["price,INR 320"]]) 
                    menu.append([self.food[items],["3"],["Tandoori Chicken"], self.food[items]["quantity,4 pieces"],self.food[items]["price,INR 240"]]) 
                for i in range(len(menu)):
                    print(i+1,".",menu[i])
                while True:
                    print("\nEnter 1 to Place the Order\nEnter 2 to Exit ")
                    x=input()
                    if x=="1":
                        print("Truffle cake", "quantity,500gm","price,INR900")
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-1])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                                print("\nList of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x=="2":
                        print("Vegan Burger", "quantity,1 piece","price,INR320")
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-2])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                                print("\nList of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x=="3":
                         print("Tandoori chicken", "quantity,4 piece","price,INR240")
                         y=input().split(",")
                         for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-3])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                                print("\nList of food item you selected : \n")
                         for j in self.ordered_item:
                            print(j)
                    elif x=="4":
                         break
                    else:
                        print("!! Invalid Number !!\n")
            
                        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")     
                
                
    
            
       # defining the Main function    

try:
    def main():
        obj=Restaurant("taj")
        print(f"!!  Welcome To {obj.restro_name} Restaurant  !!\n")
       
        
        while True:
            print("1. Admin\n2. User\n3. Exit\n")
            x=input()
            if x=="1":
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y=input()
                    if y=="1":
                        obj.admin_register()
                    elif y=="2":
                        obj.admin_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")
                    
            elif x=="2":
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y=input()
                    if y=="1":
                        obj.user_register()
                    elif y=="2":
                        obj.user_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")        
            elif x=="3":
                break
            else:
                print("Invalid Number")
except Exception as e:
    print("Something went wrong please give input carefully")
            
        
        # calling the main function 
        
if __name__=='__main__':
    main()

print("THANK YOU SIR")

# Define a class to represent a user
class User:
  def __init__(self, full_name, phone_number, email, address, password):
    self.full_name = full_name
    self.phone_number = phone_number
    self.email = email
    self.address = address
    self.password = password

# Define a dictionary to store the users
users = {}

# Define a function to handle user registration
def register_user():
  # Prompt the user to enter their information
  full_name = input("Enter your full name: ")
  phone_number = input("Enter your phone number: ")
  email = input("Enter your email: ")
  address = input("Enter your address: ")
  password = input("Enter your password: ")

  # Create a new user and add them to the dictionary
  new_user = User(full_name, phone_number, email, address, password)
  users[email] = new_user

  print("Thank you for registering! You may now log in.")

# Define a function to handle user login
def login_user():
  # Prompt the user to enter their email and password
  email = input("Enter your email: ")
  password = input("Enter your password: ")

  # Check if the email and password match a user in the dictionary
  if email in users and users[email].password == password:
    print("Welcome back, {}!".format(users[email].full_name))
  else:
    print("Sorry, the email and password you entered do not match any registered users. Please try again.")

# Define a function to display the main menu
def display_menu():
  print("1. Register")
  print("2. Login")
  print("3. Quit")

# Define the main function
def main():
  while True:
    # Display the menu
    display_menu()

    # Prompt the user to choose an option
    choice = input("Enter your choice: ")

    # Handle the user's choice
    if choice == "1":
      register_user()
    elif choice == "2":
      login_user()
    elif choice == "3":
      break
    else:
      print("Invalid choice. Please try again.")

# Run the main function
main()
food_items = [
    {"name": "Tandoori Chicken", "price": 240, "pieces": 4},
    {"name": "Vegan Burger", "price": 320, "pieces": 1},
    {"name": "Truffle Cake", "price": 900, "pieces": 500},
]

order_history = []

def display_menu():
    print("Welcome to our restaurant!")
    print("Please choose from the following options:")
    print("1. Place New Order")
    print("2. Order History")
    print("3. Update Profile")

def place_new_order():
    print("Here is our menu:")
    for i, item in enumerate(food_items):
        print(f"{i+1}. {item['name']} ({item['pieces']} pieces) [INR {item['price']}]")

    order = input("Please enter the numbers corresponding to the items you want to order, separated by a comma: ")
    order = [int(x.strip()) for x in order.split(",")]

    print("You have ordered the following items:")
    total_price = 0
    for i in order:
        item = food_items[i-1]
        print(f"{item['name']} ({item['pieces']} pieces) [INR {item['price']}]")
        total_price += item['price']

    print(f"Total price: INR {total_price}")
    confirm = input("Would you like to place this order? (y/n) ")
    if confirm == "y":
        # Add the order to the order history
        order_history.append({"items": order, "total_price": total_price})
        print("Your order has been placed!")
    else:
        print("Your order has been cancelled.")

def show_order_history():
    if not order_history:
        print("You have no previous orders.")
        return

    print("Here is a list of your previous orders:")
    for order in order_history:
        print("Items:")
        for i in order['items']:
            item = food_items[i-1]
            print(f"{item['name']} ({item['pieces']} pieces) [INR {item['price']}]")
        print(f"Total price: INR {order['total_price']}")
        print()

def update_profile():
    print("Sorry, this feature is not yet implemented.")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        place_new_order()
    elif choice == "2":
        show_order_history()
    elif choice == "3":
        update_profile()
    else:
        print("Invalid choice. Please try again.")


  
# Create an instance of the User class
user = User("John", "john@example.com")


# Update the user's profile
user.update_profile(name="NIKU ENDHKU", email="NIKUENDHUKU@gmail.com")

# View updated profile
print(f"Name: {user.name}")
print(f"Email: {user.email}")