#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head, *tmp;
	int count = 0, i, len;

	if (!*head || !(*head)->next)
		return (1);
	while (ptr)
	{
		count++;
		ptr = ptr->next;
	}
	ptr = *head;
	if (count % 2 != 0)
		count -= 1;
	len = count / 2;
	while (len)
	{
		tmp = *head;
		for (i = 1; i < count; i++)
			tmp = tmp->next;
		if (tmp->n != ptr->n)
			return (0);
		ptr = ptr->next;
		count--;
		len--;
	}
	return (1);
}
