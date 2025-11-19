#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipedf[2];
    if (pipe(pipedf) == -1) {
        perror("pipe");
        return 1;
    }
    printf("Pipe created with read end: %d, write end: %d\n", pipedf[0], pipedf[1]);
    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        return 1;
    }
    if (pid == 0) { // Child process
        close(pipedf[1]); // Close unused write end
        char buffer[100];
        read(pipedf[0], buffer, sizeof(buffer));
        printf("Child received: %s\n", buffer);
        close(pipedf[0]);
    } else { // Parent process
        close(pipedf[0]); // Close unused read end
        const char *message = "Hello from parent";
        write(pipedf[1], message, strlen(message) + 1);
        close(pipedf[1]);
    }

    return 0;
}