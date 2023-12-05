#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	struct listint_t *fast = head;
	struct listint_t *slow = slow;
	struct listint_t *prev = NULL;
	struct listint_t *next = NULL;
	struct listint_t *current = NULL;
	struct listint_t *firsthalf = head;
	struct listint_t *secondhalf = NULL;

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
		if (firsthalf->data != secondhalf->data)
		{
			return (0);
		}
		firsthalf = firsthalf->next;
		secondhalf = secondhalf->next;
	}

	return (1);
}
