#include "lists.h"

/**
 * add_dnodeint_end - adds a new node at the end of a dlistint_t list.
 * @head: pointer to pointer of first node
 * @n: value n of new node
 *
 * Return: the address of the new element, or NULL if it failed
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *ptr = *head;
	dlistint_t *new_node = malloc(sizeof(dlistint_t));

	if (!new_node)
		return (NULL);
	new_node->n = (int)n;
	new_node->next = NULL;
	new_node->prev = NULL;
	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}
	while (ptr->next)
		ptr = ptr->next;
	ptr->next = new_node;
	new_node->prev = ptr;
	return (new_node);
}
