#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: Always returns 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point of the program that creates zombie processes
 *
 * Description: Creates 5 zombie processes and enters an infinite loop
 *              to keep the program running.
 *
 * Return: Always returns 0
 */
int main(void)
{
	pid_t child_pid;
	int i;

    /* Loop to create 5 zombie processes */
	for (i = 0; i < 5; i++)
	{
		/* Create a new process */
		child_pid = fork();

		/* If we're in the child process (because fork() returns 0 in child)*/
		if (child_pid == 0)
		{
			/* Print the PID of the child (zombie) process */
			printf("Zombie process created, PID: %d\n", getpid());
			/* Immediately exit the child process, leaving it in a "zombie" state */
			exit(0);
		}
	}
	/**
	 * After creating the zombies, enter an infinite loop
	 * to keep the parent process alive
	 */
	infinite_while();
	return (0);
}
