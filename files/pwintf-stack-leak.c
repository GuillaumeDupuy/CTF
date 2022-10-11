#include <stdio.h>
#include <assert.h>
#include <string.h>

int main() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);

	FILE *flag_file = fopen("flag.txt", "r");
	assert(flag_file != NULL);

	char attempt[0x100] = { 0 };
	char flag[0x100] = { 0 };

	puts("What is the flag?");

	assert(fgets(attempt, sizeof attempt, stdin) != NULL);
	assert(fgets(flag, sizeof flag, flag_file) != NULL);

	fclose(flag_file);

	flag[strcspn(flag, "\n")] = 0;
	attempt[strcspn(attempt, "\n")] = 0;

	if (strcmp(flag, attempt) == 0) {
		printf("This is the flag!\n");
	} else {
		printf(attempt);
		printf(" is not the flag!\n");
	}
}
