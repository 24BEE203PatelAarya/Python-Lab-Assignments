#8.Write a menu-driven program to implement the Queue data structure

queue = []

while True:
    print("\nQUEUE OPERATIONS MENU:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        
        element = input("Enter element to enqueue: ")
        queue.append(element)
        print(f"{element} enqueued to queue.")
    
    elif choice == '2':
       
        if not queue:
            print("Queue is empty. Cannot dequeue.")
        else:
            dequeued = queue.pop(0)
            print(f"Dequeued element: {dequeued}")
    
    elif choice == '3':
        # Peek operation
        if not queue:
            print("Queue is empty.")
        else:
            print(f"Front element is: {queue[0]}")
    
    elif choice == '4':
        
        if not queue:
            print("Queue is empty.")
        else:
            print("Queue elements (front to rear):")
            for item in queue:
                print(item)
    
    elif choice == '5':
        
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select between 1-5.")
