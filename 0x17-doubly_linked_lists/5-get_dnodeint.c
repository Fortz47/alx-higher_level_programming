#include "lists.h"

/**
 * get_dnodeint_at_index - returns the nth node of a dlistint_t linked list
 * @head: pointer to first node
 * @index: index of node
 *
 * Return: node at index or Null if does not exist
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *ptr = head;

	if (!head)
		return (NULL);
	while (ptr || index)
	{
		if (index == 0)
			return (ptr);
		index--;
		if (!ptr->next && !index)
			return (ptr);
		ptr = ptr->next;
	}
	return (NULL);
}
