// The complexity of enqueue and dequeue are of O(1)
// We can appy it at Schedueling, synchronization, handling the interrupts in real-time systems, to keep order
#include<stdlib.h>
#include<stdio.h>

#define MAX 10

int count = 0;
typedef	struct queue
{
    int data[MAX];
    int front;
    int rear;
}q;

void createEmptyQueue(q *queue)
{
    queue->front = queue->rear = -1;
}

int isEmpty(q *queue)
{
    if(queue->front == queue->rear == -1)
        return(1);
    else
        return(0);
}

int isFull(q *queue)
{
    if(queue->rear == MAX - 1)
        return(1);
    else
        return(0);
}

void enQueue(q* queue, int value)
{
    if(!(isFull(queue)))
    {
        if(queue->front == -1)
            queue->front ++;
        queue->rear++;
        queue->data[queue->rear] = value;
    }
    else
        printf("Queue is Full\n");
}

void deQueue(q* queue)
{
    if(!isEmpty(queue))
    {
        if(queue->front == queue->rear)
            queue->front = queue->rear = -1;
        else
            queue->front++;
    }
    else
        printf("Queue is Empty");
}

int peek(q *queue)
{
    if(!isEmpty(queue))
        return(queue->data[queue->front]);
    else
        return(NULL);
}

int getValueAt(q *queue, int index)
{
    int i;
    if(index < queue->front && index > queue->rear)
        return(NULL);
    i = queue->front;
    while (i < queue->rear && i != index)
        i++;
    return(queue->data[i]);
}

void printQueue(q *queue)
{
    int i;

    i = queue->front;
    while (i <= queue->rear)
    {
        printf("%d ", queue->data[i]);
        i++;
    }
    printf("\n");
}
// Driver code
int main() 
{
    int ch;
    int index;

    q *s = (q *)malloc(sizeof(q));
    index = -1;
    createEmptyQueue(s);
    enQueue(s, 5);
    enQueue(s, 6);
    enQueue(s, 8);
    enQueue(s, 10);
    printQueue(s);
    printf("\n peek = %d\n", peek(s));
    while(++index < 3)
        printf("\ngetValue at %d = %d\n", index, getValueAt(s, index));
    deQueue(s);
    printf("\nAfter popping out\n");
    printQueue(s);
}
