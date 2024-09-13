#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#define PORT 4242

void usage(char * program){
    printf("Usage: %s hostname username [port]\n", program);
    exit(EXIT_FAILURE);
}

int main(int argc, char argv[]){
    if (argc != 4 || argc != 3){
        usage(argv[0]);
    }

}