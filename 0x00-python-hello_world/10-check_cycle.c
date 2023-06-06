#include "lists.h"

/**
 * check_cycle -  function that checks if has a cycle in it.
 * @list: header list pointer
 * Return: 0 or 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL || list->next == NULL)
		return (0);
	temp = list;
	while (temp && temp->next)
	{
		list = list->next;
		temp = (temp->next)->next;
		if (list == temp)
			return (1);
	}
	return (0);
}
