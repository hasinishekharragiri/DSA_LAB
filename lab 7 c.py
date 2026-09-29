class CircularQueueEx:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue operation (Insert element)
    def enqueue(self, item):
        # Condition for Queue Overflow
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
        else:
            # If inserting the first element
            if self.front == -1:
                self.front = 0
            
            # Circularly increment rear index
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(item, "inserted into the circular queue")

    # Dequeue operation (Delete element)
    def dequeue(self):
        # Condition for Queue Underflow
        if self.front == -1:
            print("Queue Underflow")
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None  # Clear the slot
            
            # If the queue has only one element, reset pointers after deletion
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                # Circularly increment front index
                self.front = (self.front + 1) % self.size
                
            print(f"{item} deleted from the circular queue")

    # Peek operation (View the front element)
    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    # Display operation
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("The elements of the circular queue are:")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()  # For a new line

# Main Program Loop
size = int(input("Enter the size of the circular queue: "))
cq = CircularQueueEx(size)

while True:
    print("\n----- CIRCULAR QUEUE USING ARRAY MENU -----")
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
