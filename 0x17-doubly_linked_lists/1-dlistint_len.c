#include "lists.h"

/**
 * dlistint_len - returns the number of elements in a linked dlistint_t list
 * @h: pointer to first node
 *
 * Return: number of nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *ptr = h;
	size_t count = 0;

	if (!h)
		return (0);
	while (ptr)
	{
		count++;
		ptr = ptr->next;
	}
	return (count);
}
