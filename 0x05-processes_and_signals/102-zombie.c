#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
int infinite_while(void);

/**
 * main - spawn 5 zomibe process
 *
 * Return: 0
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", child_pid);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - infinite sleep
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
