#include<stdio.h>
#include<stdlib.h>

#define MAX 3
typedef struct circularQueue
{
    int data[MAX];
    int front;
    int rear;
}circularQueue;

void createEmptyQueue(circularQueue *cq)
{
    cq->front = cq->rear = -1;
}
int isFull(circularQueue *cq)
{
    if((cq->front == cq->rear + 1) || (cq->front == 0 && cq->rear == MAX - 1))
    {
        printf("Queue is Full %d %d\n",cq->front, cq->rear);
        return(1);
    }
    else
        return(0);
}

int isEmpty(circularQueue *cq)
{
    if(cq->front == -1)
    {
        printf("The Queue is Empty\n");
        return(1);
    }
    else
        return(0);
}

void enQueue(circularQueue *cq, int value, int displayInfo)
{
    printf("Front =  %d\n", cq->front);
    printf("Rear = %d\n", cq->rear);
    if(!isFull(cq))
    {
        if(cq->front == -1)
            cq->front++;
        cq->rear = (cq->rear + 1) % MAX;
        cq->data[cq->rear] = value;
        if(displayInfo)
            printf("Inserted %d to the queue at index %d\n", value, cq->rear);
    }
}

int deQueue(circularQueue *cq, int displayInfo)
{
    int value;
    
    if(!isEmpty(cq))
    {
        value = cq->data[cq->front];
        if(cq->front == cq->rear)
            cq->front = cq->rear = -1;
        else
            cq->front = (cq->front + 1) % MAX;
        if(displayInfo)
            printf("\n Deleted %d from the Queue \n", value);
        return(value);
    }
    else
        return(-1);
}

int peek(circularQueue *cq, int displayInfo)
{
    if(!isEmpty(cq))
        return(cq->data[cq->front]);
    else
    {
        if(displayInfo)
            printf("Nothing to peek Queue is Empty\n");
        return(-1);
    }
}

void display(circularQueue *cq)
{
    int i;

    if(!isEmpty(cq))
    {
        i = cq->front;
        while(i != cq->rear)
        {
            printf("%d ",cq->data[i]);
            i = (i + 1) % MAX;
        }
        printf("%d ",cq->data[i]);
        printf("\n");
    }
    else
        printf("Queue is Empty\n");
}

int getValueAt(circularQueue *cq, int index)
{
    int i;
    i = cq->front;
    while (i != cq->rear && i != index)
        i = (i + 1) % MAX;
    return(cq->data[i]);
}
// Driver code
int main() 
{
    int ch;
    int index;
    int displayInfo;

    displayInfo = 1;
    circularQueue *s = (circularQueue *)malloc(sizeof(circularQueue));
    index = -1;
    createEmptyQueue(s);
    enQueue(s, 5, displayInfo);
    enQueue(s, 6, displayInfo);
    enQueue(s, 8, displayInfo);
    deQueue(s, displayInfo);
    enQueue(s, 10, displayInfo);
    display(s);
    printf("\n peek = %d\n", peek(s, displayInfo));
    while(++index < 3)
        printf("\ngetValue at %d = %d\n", index, getValueAt(s, index));
    deQueue(s, displayInfo);
    printf("\nAfter popping out\n");
    display(s);
}
