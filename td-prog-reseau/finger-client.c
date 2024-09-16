#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netdb.h>

#define PORT 4242
#define SERVER "127.0.0.1"

void usage(char *program)
{
    printf("Usage: %s hostname username [port]\n", program);
    exit(EXIT_FAILURE);
}

struct sockaddr * resolveHostname(char *hostame, char* stringIP, int stringSize)
{
    struct addrinfo hints;
    memset(&hints, 0, sizeof(hints));

    hints.ai_flags = AF_INET;
    hints.ai_family = AF_INET;

    struct addrinfo *peer;

    if (getaddrinfo(hostame, 0, &hints, &peer) != 0)
    {
        perror("getaddrinfo error!");
        exit(1);
    }

    struct addrinfo *address = peer;

    getnameinfo(address->ai_addr, address->ai_addrlen, stringIP, stringSize,
                    0, 0, NI_NUMERICHOST);

    return address->ai_addr;
}

int main(int argc, char *argv[])
{
    if (argc > 5 || argc < 2)
    {
        usage(argv[0]);
        return EXIT_FAILURE;
    }

    char *hostname = argv[1];
    char *username = argv[2];
    char ipStr[20];
    struct sockaddr * server_ip = resolveHostname(hostname,ipStr, 20);
    int port = PORT;

    if (argc == 4)
    {
        port = strtol(argv[3], NULL, 10);
    }
    printf("Summary:\n\tHotname: %s (%s)\n\tUsername: %s\n\tPort: %d\n\n", hostname, ipStr, username, port);

    int s, ret;
    struct sockaddr_in server_addr;
    char buf[100];
    char *msg = "Hello, server!";
    // create a tcp socket
    s = socket(AF_INET, SOCK_STREAM, 0);
    if (s == -1)
    {
        perror("socket");
    }
    // fill a structure with the server's address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = inet_addr(ipStr);
    // connect to the server
    ret = connect(s, (struct sockaddr *)&server_addr, sizeof(server_addr));
    if (ret == -1)
    {
        perror("connect");
    }

    write(s, username, strlen(username));

    char firstname[100];
    read(s, firstname, 100);

    printf("First name: %s\n", firstname);

    close(s);
    return EXIT_SUCCESS;
}