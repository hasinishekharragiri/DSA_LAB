class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.rear = None

    # Enqueue operation (Insert element at the end)
    def enqueue(self, item):
        new_node = Node(item)
        
        # If the queue is empty
        if self.rear is None:
            self.rear = new_node
            self.rear.next = self.rear  # Point to itself to maintain circularity
        else:
            # New node points to the front node
            new_node.next = self.rear.next
            # Current rear node points to the new node
            self.rear.next = new_node
            # Move the rear pointer to the new node
            self.rear = new_node
            
        print(item, "inserted into the circular queue")

    # Dequeue operation (Delete element from the front)
    def dequeue(self):
        # Condition for Underflow
        if self.rear is None:
            print("Queue Underflow")
        else:
            front = self.rear.next
            item = front.data
            
            # If the queue has only one node
            if self.rear == front:
                self.rear = None
            else:
                # Rear bypasses the old front to point to the next node
                self.rear.next = front.next
                
            print(f"{item} deleted from the circular queue")

    # Peek operation (View the front element)
    def peek(self):
        if self.rear is None:
            print("Queue is empty")
        else:
            front = self.rear.next
            print("Front element:", front.data)

    # Display operation
    def display(self):
        if self.rear is None:
            print("Queue is empty")
        else:
            print("The elements of the circular queue are:")
            front = self.rear.next
            temp = front
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                # Stop when we loop back to the front node
                if temp == front:
                    break
            print()  # For a new line

# Main Program Loop
cq = CircularQueueLinkedList()

while True:
    print("\n----- CIRCULAR QUEUE (LINKED LIST) MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = int(input("Enter the element to enqueue: "))
            cq.enqueue(item)
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.peek()
        elif choice == 4:
            cq.display()
        elif choice == 5:
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")
    except ValueError:
        print("Please enter a valid integer number.")
