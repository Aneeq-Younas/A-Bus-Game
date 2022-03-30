order = ""
goes = False
while True:
    order = input("> ")

    if order.lower() == "go":
        print("Bus is ready to go..........")

    elif order.lower() == "end":
        print("Bus is ended..")

    elif order == "support":
        print("""
go - To start the bus
end - To stop the bus
exit - To exit the bus
        """)

    elif order.lower() == "exit":
        break

    else:
        print("Invailed, Try Again ")