#ifndef DLL_H
#define DLL_H

struct node
{
	int data;
	struct node *next;
	struct node *prev;
};

typedef struct node node_t;

struct doubly_linked_list
{
	node_t *head;
	node_t *tail;
	int size;
};

typedef struct doubly_linked_list list_t;

list_t *create_list();								 // return a newly created empty doubly linked list
void insert_front(list_t *list, int data);			 // inserts data to the beginning of the linked list
void insert_back(list_t *list, int data);			 // inserts data to the end of the linked list
void insert_after(list_t *list, int data, int prev); // inserts data after the node with data “prev”
void delete_front(list_t *list);					 // delete the start node from the linked list.
void delete_back(list_t *list);						 // delete the end node from the linked list.
void delete_node(list_t *list, int data);			 // delete the node with “data” from the linked list.
node_t *search(list_t *list, int data);				 // returns the pointer to the node with “data” field
int is_empty(list_t *list);							 // return true or 1 if the list is empty; else returns false or 0
int size(list_t *list);								 // returns the number of nodes in the linked list.
void delete_list(list_t *list);						 // free all the contents of the linked list
void display_list(list_t *list);					 // print the linked list by separating each item by a space and a new line at the end of the linked list.

#endif
