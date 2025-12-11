# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
maxs=5
queue=[1,2,3,4]
rear= -1
front= 0

def enqueue(custom):
    try:
        global rear
        if(rear+1)> maxs:
            print('Error, queue is full')
        else:
            rear+=1
            queue[rear]=custom
        
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def dequeue():
    try:
        global front, rear
        if rear < front:
            print('Error, queue is empty')
        else:
            item= queue[front]
            queue[front]= None
            front+=1
        if front > rear:
            front=0
            rear= -1
        return item  
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def peek():
    try:
        if rear < front:
            print('Error, queue is empty')
        else:
            print(queue[front])
        return queue[front]
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def size():
    try:
        
        if rear<front:
            print('the size is 0')
        else:
            sizin = rear-front+1
            print('the size of queue is', sizin)
        pass   
    except Exception as e:
        print("Error occurred:", e )


# [comment]
def main():
    try:
        global front, rear, queue
        front = 0
        rear = 2
        queue=[10,20,30, None, None]
        print('Starting queue is:', queue,'The front is:', front, 'The rear is:', rear)
        size()
        print("Lookie here", peek())         
        print("When dequeue it is now:", dequeue())   
        print("after dequeue, queue:", queue, "The front is:", front, "The rear is:", rear)
        size()
        x=int(input('add a number to a queue: '))
        enqueue(x)
        print('The new front is now:',peek())
        print('After dequeue:',dequeue())
        print("after dequeue, queue:", queue, "The fron is:", front, "The rear is:", rear)
        size()

        
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
