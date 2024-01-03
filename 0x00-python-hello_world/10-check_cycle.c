#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;  /* Initialize slow pointer */
	listint_t *fast = list;  /* Initialize fast pointer */

	if (!list)  /* If the list is empty, there's no cycle */
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;         /*  Move slow pointer by one step */
		fast = fast->next->next;   /* Move fast pointer by two steps */
		if (slow == fast)          /* If they meet, there's a cycle */
			return (1);
	}

	return (0);
}
