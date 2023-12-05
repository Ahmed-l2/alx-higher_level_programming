#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *current = NULL;
	listint_t *firsthalf = *head;
	listint_t *secondhalf = NULL;

	if(*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow-> next;
	}

	current = slow;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	secondhalf = prev;

	while (secondhalf != NULL)
	{
		if (firsthalf->n != secondhalf->n)
		{
			return (0);
		}
		firsthalf = firsthalf->next;
		secondhalf = secondhalf->next;
	}

	return (1);
}
