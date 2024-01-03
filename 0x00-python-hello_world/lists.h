#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list node
 * @n: integer data stored in the node
 * @next: pointer to the next node in the list
 *
 * Description: A structure representing a node in a singly linked list.
 *              It contains an integer data field 'n' and a pointer to the
 *              next node in the list ('next').
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/* Function prototypes for singly linked list operations */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
