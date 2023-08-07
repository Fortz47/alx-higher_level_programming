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

	while (ptr->next)
		(ptr->next == list) ? return (1) : ptr = ptr->next;
	return (0);
}
