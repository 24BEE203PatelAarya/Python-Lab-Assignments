#7.Write a menu-driven program to implement the stack data structure.

stack = []

while True:
    print("\nSTACK OPERATIONS MENU:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        
        element = input("Enter element to push: ")
        stack.append(element)
        print(f"{element} pushed to stack.")
    
    elif choice == '2':
        
        if not stack:
            print("Stack is empty. Cannot pop.")
        else:
            popped = stack.pop()
            print(f"Popped element: {popped}")
    
    elif choice == '3':
        
        if not stack:
            print("Stack is empty.")
        else:
            print(f"Top element is: {stack[-1]}")
    
    elif choice == '4':
       
        if not stack:
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            for item in reversed(stack):
                print(item)
    
    elif choice == '5':
        
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select between 1-5.")
