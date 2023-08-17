#include "lists.h"

/**
 * insert_dnodeint_at_index - inserts a new node at a given position.
 * @h: pointer to first node
 * @idx: index to add new node
 * @n: value of n for new node
 *
 * Return: the address of the new node, or NULL if it failed
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *ptr = *h;
	dlistint_t *new_node = malloc(sizeof(dlistint_t));

	if (!new_node)
		return (NULL);
	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = NULL;
	if (idx == 0)
	{
		new_node->next = *h;
		if (*h)
			(*h)->prev = new_node;
		*h = new_node;
		return (new_node);
	}
	while (ptr || idx)
	{
		if (idx == 0)
		{
			new_node->next = ptr;
			new_node->prev = ptr->prev;
			ptr->prev->next = new_node;
			ptr->prev = new_node;
			return (new_node);
		}
		idx--;
		if (!ptr->next && !idx)
		{
			ptr->next = new_node;
			new_node->prev =  ptr;
			return (new_node);
		}
		ptr = ptr->next;
	}
	return (NULL);
}
