#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct Node
{
    int data;
    struct Node *next;
} Node;
typedef struct Nodestrg
{
    char data;
    struct Nodestrg *next;
} Nodestrg; // Nodestrg Structur
typedef struct MinMax
{
    int max;
    int min;
} MinMax;
void printList(Node *Head)
{
    Node *temp = Head;
    printf("\n");
    while (temp != NULL)
    {
        if (temp->next == NULL)
        {
            printf("%d", temp->data);
        }
        else
        {
            printf("%d -", temp->data);
        }
        temp = temp->next;
    }
    printf("\n");
}
Node *createNewNode(int value)
{
    // creation of isolated Node
    Node *result = malloc(sizeof(Node));
    result->data = value;
    result->next = NULL;
    return result;
}
Node *insert_NodeAtHead(Node **Head, Node *newNode)
{
    newNode->next = *Head;
    *Head = newNode;
    return newNode;
}
void insert_TailNode(Node *head, Node *newNode)
{
    Node *temp = head;
    while (temp != NULL)
    {
        if (temp->next == NULL)
        {
            temp->next = newNode;
            newNode->next = NULL;
        }
        temp = temp->next;
    }
}
void insert_AfterNode(Node *nodeToIsertAfter, Node *newNode)
{
    newNode->next = nodeToIsertAfter->next;
    nodeToIsertAfter->next = newNode;
}
void insert_BeforeNode(Node *Head, Node *nodeToIsertBefore, Node *newNode)
{
    Node *temp = Head;
    while (temp != NULL)
    {
        if (temp->next == nodeToIsertBefore)
        {
            newNode->next = temp->next;
            temp->next = newNode;
            break;
        }
        temp = temp->next;
    }
}
void insert_NthPosition(Node *head, Node *newNode, int Position)
{
    Node *temp = head;
    int count = 1;
    while (temp != NULL)
    {
        if (count + 1 == Position)
        { // an other alternative is set the count +1 and call after function instaed of before
            insert_AfterNode(temp, newNode);
        }
        temp = temp->next;
        count++;
    }
}
Node *finde_Node(Node *Head, int value)
{
    Node *temp = Head;
    while (temp != NULL)
    {
        if (temp->data == value)
        {
            printf("search result %d \n", temp->data);
            return temp;
        }
        temp = temp->next;
    }
    printf("search result : introuvable\n");
    return NULL;
}
void modify_NodeValueByValue(Node *Head, int nodeValueToModify, int NewValue)
{
    Node *target = finde_Node(Head, nodeValueToModify);
    target->data = NewValue;
}
void modify_NodeValueByPosition(Node *Head, int Position, int NewValue)
{
    Node *temp = Head;
    int count = 0;
    while (temp != NULL)
    {
        if (count == Position)
        {
            temp->data = NewValue;
            break;
        }
        temp = temp->next;
        count++;
    }
}
void delete_HeadNode(Node **Head)
{
    Node *temp = *Head;
    *Head = (*Head)->next;
    free(temp);
}
void delete_NodeByValue(Node **Head, int valueToDelete)
{ // delete all occureces
    Node *temp = *Head;
    Node *prev = NULL;
    if (temp != NULL)
    {
        while (temp != NULL)
        {
            if ((*Head)->data == valueToDelete)
            {
                *Head = (*Head)->next;
            }
            if (temp->next != NULL)
            {
                if (temp->next->data == valueToDelete)
                {
                    temp->next = temp->next->next;
                }
                else
                {
                    temp = temp->next;
                }
            }
            else
            {
                temp = temp->next;
            }
        }
    }
    else
    {
        printf("The list is empty");
    }
}
void delete_NodeByPosition(Node **Head, int position)
{
    Node *temp = *Head;
    int count = 0;
    if (temp != NULL)
    {
        while (temp != NULL)
        {
            if (count == position)
            {
                temp->next = temp->next->next;
                break;
            }
            count++;
            temp = temp->next;
        }
    }
    else
    {
        printf("The list is empty");
    }
}
void delete_TailNode(Node **Head)
{
    Node *temp = *Head;
    while (temp != NULL)
    {
        if (temp->next->next == NULL)
            temp->next = NULL;
        temp = temp->next;
    }
}
int get_OccurencesNumber(Node **Head, int value)
{
    int count = 0;
    Node *temp = *Head;
    while (temp != NULL)
    {
        if (temp->data == value)
            count++;
        temp = temp->next;
    }
    return count;
}
MinMax get_MinMax(Node *Head)
{
    Node *temp = Head;
    MinMax minMax = {temp->data, temp->data};
    while (temp != NULL)
    {
        if (temp->data > minMax.max)
            minMax.max = temp->data;
        if (temp->data < minMax.min)
            minMax.min = temp->data;
        temp = temp->next;
    }
    return minMax;
}
int get_sum(Node *head)
{
    Node *temp = head;
    int Sum = 0;
    while (temp != NULL)
    {
        Sum += temp->data;
        temp = temp->next;
    }
    return Sum;
}
Node *reverse_LinkedList(Node *Head)
{
    // Initialize current, previous and
    // next pointers
    Node *current = Head;
    Node *prev = NULL, *next = NULL;

    while (current != NULL)
    {
        // Store next
        next = current->next;
        // Reverse current node's pointer
        current->next = prev;
        // Move pointers one position ahead.
        prev = current;
        current = next;
    }
    Head = prev;
}
void print_Middle(Node *Head)
{
    Node *First = Head;
    Node *second = Head;
    if (Head != NULL)
    {
        while (second != NULL && second->next != NULL)
        {
            second = second->next->next;
            First = First->next;
        }
        printf("\nThe midle is %d ", First->data);
    }
}
void detect_LoppFloyCycle(Node *Head)
{
    Node *first = Head;
    Node *second = Head;
    int found = 0;
    while (first->next && second && first)
    {
        first = first->next;
        second = second->next->next;
        if (first == second)
        {
            found == 1;
            printf("\nThere is a Loop");
        }
    }
    if (found == 0)
    {
        printf("\nThere is no Loop");
    }
}
void detect_delete_LoppFloyCycle(Node *Head)
{
    Node *first = Head;
    Node *second = Head;
    Node *prev = NULL; // Track the last Node which is responsible for the loop
    while (first && second && first->next)
    {
        first = first->next;
        prev = first;
        second = second->next->next;
        if (first == second)
        {
            prev->next->next = NULL;
        }
    }
}
int get_size(Node *Head)
{
    Node *temp = Head;
    int count = 0;
    while (temp != NULL)
    {
        count++;
        temp = temp->next;
    }
    return count;
}
int get_size_recursive(Node *Head)
{
    if (Head == NULL)
        return 0;
    return 1 + get_size_recursive(Head->next);
}
Node *addition_twoLinkedList(Node *l1, Node *L2)
{
    Node *temp1 = l1;
    Node *temp2 = L2;
    Node *res = NULL;
    if (temp1 == NULL)
    {
        res = temp2;
        return res;
    }
    if (temp2 == NULL)
    {
        res = temp1;
        return res;
    }
    int carry = 0;
    int sumI = 0;
    int size1 = get_size(temp1), size2 = get_size(temp2);
    if (size1 > size2)
    {
        while (temp1 != NULL)
        {
            sumI += temp1->data;
            temp1 = temp1->next;
            if (temp2 != NULL)
            {
                sumI += temp2->data;
                temp2 = temp2->next;
            }
            if (carry > 0)
            {
                sumI += carry;
                carry = 0;
            }
            if (sumI >= 10)
            {
                carry = sumI / 10;
                sumI = sumI - (carry * 10);
            }
            push(&res, sumI);
            sumI = 0;
        }
        if (carry > 0)
        {
            push(&res, carry);
        }
    }
    if (size2 > size1)
    {
        while (temp2 != NULL)
        {
            sumI += temp2->data;
            temp2 = temp2->next;
            if (temp1 != NULL)
            {
                sumI += temp1->data;
                temp1 = temp1->next;
            }
            if (carry > 0)
            {
                sumI += carry;
                carry = 0;
            }
            if (sumI >= 10)
            {
                carry = sumI / 10;
                sumI = sumI - (carry * 10);
            }
            push(&res, sumI);
            sumI = 0;
        }
        if (carry > 0)
        {
            push(&res, carry);
        }
    }
    if (size2 == size1)
    {
        while (temp2 != NULL)
        {
            sumI += temp2->data;
            temp2 = temp2->next;

            sumI += temp1->data;
            temp1 = temp1->next;
            if (carry > 0)
            {
                sumI += carry;
                carry = 0;
            }
            if (sumI >= 10)
            {
                carry = sumI / 10;
                sumI = sumI - (carry * 10);
            }
            push(&res, sumI);
            sumI = 0;
        }
        if (carry > 0)
        {
            push(&res, carry);
        }
    }
    return res;
}
void push(struct Node **head_ref, int new_data)
{
    /* allocate node */
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));

    /* put in the data  */
    new_node->data = new_data;

    /* link the old list off the new node */
    new_node->next = (*head_ref);

    /* move the head to point to the new node */
    (*head_ref) = new_node;
}
bool search_iterrative(Node *Head, int x)
{
    Node *temp = Head;
    while (temp != NULL)
    {
        if (temp->data == x)
            return true;
        temp = temp->next;
    }
    return false;
}
bool search_recursive(Node *Head, int x)
{
    if (Head == NULL)
        return false;
    if (Head->data == x)
    {
        return true;
    }
    return search_recursive(Head->next, x);
}
int search_indexIterrative(Node *Head, int index)
{ // O(index)
    int count = 0;
    Node *temp = Head;
    while (temp != NULL)
    {
        if (count == index)
            return temp->data;
        count++;
    }
    return -1;
}
int search_indexRecursive(Node *Head, int index)
{ // O(index)
    if (Head == NULL)
        return -1;
    if (index == 0)
        return Head->data;
    return search_indexRecursive(Head->next, index - 1);
}
void push_strg(struct Nodestrg **head_ref, int new_data)
{
    /* allocate node */
    struct Node *new_node = (Nodestrg *)malloc(sizeof(Nodestrg));

    /* put in the data  */
    new_node->data = new_data;

    /* link the old list off the new node */
    new_node->next = (*head_ref);

    /* move the head to point to the new node */
    (*head_ref) = new_node;
}
void printListh_strg(Nodestrg *Head)
{
    Nodestrg *temp = Head;
    printf("\n");
    while (temp != NULL)
    {
        if (temp->next == NULL)
        {
            printf("%c", temp->data);
        }
        else
        {
            printf("%c -", temp->data);
        }
        temp = temp->next;
    }
    printf("\n");
}
char search_indexFromEnd(Nodestrg *Head, int index)
{
    Nodestrg *temp = Head;
    int len = 0;
    while (temp != NULL)
    {
        temp = temp->next;
        len++;
    }
    temp = Head;
    int steps = len - 1 - index;
    while (temp != NULL)
    {
        if (steps != 0)
        {
            temp = temp->next;
            steps--;
        }
        else
        {
            return temp->data;
        }
    }
    return -1;
}
char search_indexFromEndTwoPointers(Nodestrg *Head, int index)
{
    Nodestrg *first = Head;
    Nodestrg *second = Head;
    int count = 0;
    while (second->next != NULL)
    {
        if (count != index)
        {
            second = second->next;
            count++;
        }
        else
        {
            first = first->next;
            second = second->next;
        }
    }
    if (index > count)
    {
        return 'F';
    }
    return first->data;
}
int get_LoopLength(Node *Head)
{
    int length = 0;
    Node *first = Head;
    Node *second = Head;
    while (first != NULL)
    {
        first = first->next;
        second = second->next->next;
        if (first == second)
        {
            second = second->next;
            while (first != second)
            {
                length++;
                second = second->next;
            }
            return length + 1;
        }
    }
    return -1;
}
void check_palindrome(Nodestrg *Head)
{
    // get count if odd not a palindrome
}

int main()
{
    // Node* Head = NULL;// we start with a empty list
    // Node* temp;
    // for (int i = 0; i < 12; i++)
    // {
    //     temp = createNewNode(i+1);
    //     insert_NodeAtHead(&Head,temp);
    // }
    // printList(Head);
    // temp = finde_Node(Head,7);
    // insert_AfterNode(temp,createNewNode(12));
    // insert_BeforeNode(Head,temp,createNewNode(30));
    // insert_TailNode(Head,createNewNode(90));
    // insert_NthPosition(Head,createNewNode(80),5);
    // modify_NodeValueByValue(Head,1,10);
    // modify_NodeValueByPosition(Head,2,100);
    // printf("Occurences of 12 is %d",get_OccurencesNumber(&Head,12));
    // delete_NodeByValue(&Head,12);
    // delete_HeadNode(&Head);
    // delete_NodeByPosition(&Head,1);
    // delete_TailNode(&Head);
    // printList(Head);
    // printf("Occurences of 12 is %d",get_OccurencesNumber(&Head,12));
    // printf("\nThe Min of this List is %d and its Max is %d ",get_MinMax(Head).min,get_MinMax(Head).max);
    // printf("\nThe Sum of this List is %d",get_sum(Head));
    // printList(reverse_LinkedList(Head));
    // print_Middle(Head);
    // detect_LoppFloyCycle(Head);

    // detect_delete_LoppFloyCycle(head2);
    // printList(head2);

    // Node* res = NULL;
    // Node* first = NULL;
    // Node* second = NULL;
    // // create first list 7->5->9->4->6
    // push(&first, 6);
    // push(&first, 4);
    // push(&first, 9);
    // push(&first, 5);
    // push(&first, 7);
    // printf("First List is ");
    // printList(first);
    // // create second list 8->4
    // push(&second, 4);
    // push(&second, 8);
    // printf("Second List is ");
    // printList(second);
    // // Add the two lists and see result
    // res = addition_twoLinkedList(first, second);
    // printf("Resultant list is \n");
    // printList(res);
    // Node *head1 = NULL,*head3 = NULL, *result = NULL;
    // push(&head1, 1);
    // push(&head1, 0);
    // push(&head1, 0);
    // push(&head3, 9);
    // push(&head3, 1);
    // result = addition_twoLinkedList(head3,head1);
    // printList(result);
    // printf("size iterative : %d \n",get_size(result));
    // printf("size recursive : %d \n",get_size_recursive(result));
    // printf("search recursive : %d \n",search_recursive(result,2));
    // printf("search index iterative : %d \n",search_indexIterrative(result,2));
    // printf("search index recursive : %d \n",search_indexRecursive(result,1));
    // Nodestrg *headstrg = NULL;
    // push_strg(&headstrg, 'A');
    // push_strg(&headstrg, 'B');
    // push_strg(&headstrg, 'C');
    // push_strg(&headstrg, 'D');
    // push_strg(&headstrg, 'E');
    // printListh_strg(headstrg);
    // printf("index from end : %c \n",search_indexFromEnd(headstrg,4));
    // printf("index from end tw pointers: %c \n",search_indexFromEndTwoPointers(headstrg,1));

    /**
     * Auto-generated code below aims at helping you parse
     * the standard input according to the problem statement.
     **/
    int n = 5, x = 2, y = 1;
    char *array[n + 2][n + 2];
    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");
    printf("\n");
    int corner = 0, val = 0;
    for (int i = 0; i < n + 2; i++)
    {
        for (int j = 0; j < n + 2; j++)
        {
            if (i == 0 || i == n + 1)
            {
                if (j == 0 || j == n + 1)
                {
                    array[i][j] = "|";
                    corner = 1;
                }
            }
            if (j > 0)
            {
                if (array[i][j - 1] == "|")
                {
                    printf(" %d %d %c \n", i, j - 1, array[i][j - 1]);
                    array[i][j] = '-';
                    printf("%d %d %c \n", i, j, array[i][j]);
                    corner = 1;
                }
            }
            if (j == n + 1)
            {
                if (array[i][j] == "|")
                {
                    printf(" %d %d %c \n", i, j, array[i][j]);
                    array[i][j - 1] = "-";
                    printf("%d %d %c \n", i, j - 1, array[i][j - 1]);
                    corner = 1;
                }
            }
            if (i == x && j == y)
            {
                array[i][j] = "T";
                val = 1;
            }
            if (val = 0 && corner == 0)
            {
                array[i][j] = " ";
            }
            corner = 0;
            val = 0;
        }
    }
    // printing
    printf("On Target!\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%c", array[i][j]);
        }
        printf("\n");
    }

    return 0;
}
// 12 = 11 = 10 = 9 = 8 = 30 = 7    40=NULL