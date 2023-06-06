#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Inserts a new node into a sorted singly linked list.
 * @head: Pointer to a pointer to the head of the linked list.
 * @number: The number to be inserted.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
}
else
{
listint_t *current = *head;
while (current->next != NULL && number >= current->next->n)
{
current = current->next;
}

new_node->next = current->next;
current->next = new_node;
}

return (new_node);
}
