// Push and pop time complexity are O(1)
// We can use stacks to reverse a text, In compilers, To brows history
#include<stdio.h>
#include<stdlib.h>

#define MAX 10

int count = 0;

typedef struct stack
{
    int data[MAX];
    int top;
}st;

void createEmptyStack(st *s)
{
    s->top = -1;
}

int isEmpty(st *s)
{
    if(s->top == -1)
        return(1);
    else
        return(0);
}

int isFull(st *s)
{
    if(s->top == MAX - 1)
        return(1);
    else
        return(0);
}

void push(st *s, int value)
{
    if(!(isFull(s)))
    {
        s->top++;
        s->data[s->top] = value;
        count++;
    }
    else
        printf("Stack is FULL");

}

void pop(st *s)
{
    if(!(isEmpty(s)))
    {
        printf("%d is deleted",s->data[s->top]);
        s->top--;
        count--;
    }
    else
        printf("Stack is Empty");
}

void printStack(st *st)
{
    int i;

    i = -1;
    printf("stack : \n");
    while(++i < count)
    {
        printf("%d ",st->data[i]);
    }
    printf("\n");
}

int peek(st *st, int index)
{
    int i;

    i = st->top;
    while(index != i && i != -1)
        i--;
    if(i == -1)
        printf(NULL);
    else
        return(st->data[i]);
}

// Driver code
int main() {
  int ch;
  int index = -1;
  st *s = (st *)malloc(sizeof(st));

  createEmptyStack(s);

  push(s, 1);
  push(s, 2);
  push(s, 3);
  push(s, 4);

  printStack(s);
  while(++index < 3)
    printf("\nValue at %d = %d\n", index, peek(s, index));

  pop(s);

  printf("\nAfter popping out\n");
  printStack(s);
}
