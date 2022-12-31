// Tree traversal in C

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
  int item;
  struct node* left;
  struct node* right;
}tree_node;

void inorderTraversal(tree_node	*root) {
  if (root == NULL) return;
  inorderTraversal(root->left);
  printf("%d ->", root->item);
  inorderTraversal(root->right);
}

void preorderTraversal(tree_node *root) {
  if (root == NULL) return;
  printf("%d ->", root->item);
  preorderTraversal(root->left);
  preorderTraversal(root->right);
}

void postorderTraversal(tree_node *root) {
  if (root == NULL) return;
  postorderTraversal(root->left);
  postorderTraversal(root->right);
  printf("%d ->", root->item);
}

tree_node* createNode(value) {
  tree_node	*newNode = malloc(sizeof(tree_node));
  newNode->item = value;
  newNode->left = NULL;
  newNode->right = NULL;

  return newNode;
}

tree_node* insertLeft(tree_node *root, int value) {
  root->left = createNode(value);
  return root->left;
}

tree_node* insertRight(tree_node *root, int value) {
  root->right = createNode(value);
  return root->right;
}

bool isFullBinaryTree(tree_node *root) {
  if (root == NULL || (root->left == NULL && root->right == NULL))
    return true;
  if ((root->left) && (root->right))
    return (isFullBinaryTree(root->left) && isFullBinaryTree(root->right));
  return (false);
}

int depth(tree_node *node) {
  int d = 0;
  while (node != NULL) 
  {
    d++;
    node = node->left;
  }
  return (d);
}

bool is_perfect(struct node *root, int d, int level) {
  if (root == NULL)
    return true;
  if (root->left == NULL && root->right == NULL)
    return (d == level + 1);

  if (root->left == NULL || root->right == NULL)
    return false;
  return is_perfect(root->left, d, level + 1) &&
       is_perfect(root->right, d, level + 1);
}

bool is_Perfect(struct node *root) {
  int d = depth(root);
  return is_perfect(root, d, 0);
}

int main() {
  tree_node *root = createNode(1);
  insertLeft(root, 12);
  insertRight(root, 9);

  insertLeft(root->left, 5);
  insertRight(root->left, 6);

  printf("Inorder traversal \n");
  inorderTraversal(root);

  printf("\nPreorder traversal \n");
  preorderTraversal(root);

  printf("\nPostorder traversal \n");
  postorderTraversal(root);
}