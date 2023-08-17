#include "lists.h"

/**
 * delete_dnodeint_at_index - delete a node at a given position.
 * @head: pointer to first node
 * @index: index to delete node
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *ptr = *head;

	if (!*head)
		return (-1);

	if (index == 0)
	{
		if (!ptr->next)
		{
			free(*head);
			*head = NULL;
			return (1);
		}
		*head = (*head)->next;
		ptr->next->prev = NULL;
		free(ptr);
		return (1);
	}
	while (ptr || index)
	{
		if (index == 0)
		{
			ptr->prev->next = ptr->next;
			ptr->next->prev = ptr->prev;
			free(ptr);
			return (1);
		}
		index--;
		if (!ptr->next && !index)
		{
			ptr->prev->next = NULL;
			free(ptr);
			return (1);
		}
		ptr = ptr->next;
	}
	return (-1);
}
