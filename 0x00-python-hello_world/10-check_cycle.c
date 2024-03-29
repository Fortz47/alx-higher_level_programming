#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: pointer to struct listint_t
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;
	listint_t *ptrFast = list;

	if (!list)
		return (0);
	while (ptr->next)
	{
		if (!ptrFast->next || !ptrFast->next->next || !ptrFast->next->next->next)
			return (0);
		ptrFast = ptrFast->next->next;
		if (ptr == ptrFast)
			return (1);
		ptr = ptr->next;
		if (ptr == ptrFast)
			return (1);
	}
	return (0);
}
