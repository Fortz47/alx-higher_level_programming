#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - that inserts a number into a sorted singly linked list
 * @head: pointer to first node
 * @number: number to insert
 *
 * Return: address of inserted node or Null if failed
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *ptr;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	ptr = *head;
	if (ptr == NULL || ptr->n >= number)
	{
		new->next = ptr;
		*head = new;
		return (new);
	}
	while (ptr && ptr->next && ptr->next->n < number)
		ptr = ptr->next;

	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
