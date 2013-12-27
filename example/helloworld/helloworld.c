/* File : example.c */
#include <stdio.h> 
#include <string.h>

char buffer[20];

char *getString() {
    memset(buffer, 0, sizeof(buffer));
    sprintf(buffer, "hello world");
    //printf("%s\n", buffer);
    return buffer;
}

void setString(char *str) {
	printf("%s\n", str);
}

/*
int main() {
    print();
    return 0;
}
*/