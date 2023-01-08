#include "lists.h"

/**
 * str_rev - reverses a string
 * @str: string
 *
 * Return: reversed string or NULL if fail
 */

int *str_rev(int *str)
{
	int i = 0, j = 0;
	int *list;

	while (str[i] != '\0')
		i++;
	list = malloc(sizeof(int) * i);
	i -= 1;
	while (i >= 0)
	{
		list[j] = str[--i];
		j++;
	}
	return (list);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to first node
 *
 * Return: 0 if not palindrome, or 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int *list1, *list2, count = 0, i = 0, k;

	ptr = *head;
	while (ptr)
	{
		ptr = ptr->next;
		count++;
	}
	list1 = malloc(sizeof(int) * count);
	list2 = malloc(sizeof(int) * count);
	ptr = *head;

	while (ptr != NULL)
	{
		list1[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}
	list2 = str_rev(list1);
	for (k = 0; list2[k] != '\0'; k++)
	{
		if (list1[k] == list2[k])
			continue;
		else
			return (0);
	}
	return (1);
}
