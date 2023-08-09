#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to first node
 * @number: number
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *ptr, *tmp;

	ptr = *head;
	tmp = *head;

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (!*head)
		return (new_node);
	if (number <= ptr->n)
	{
		new_node->next = ptr;
		*head = new_node;
		return (new_node);
	}
	while (ptr->next)
	{
		if (number <= ptr->n)
		{
			new_node->next = ptr;
			tmp->next = new_node;
			return (new_node);
		}
		tmp = ptr;
		ptr = ptr->next;
	}
	ptr->next = new_node;
	return (new_node);
}
