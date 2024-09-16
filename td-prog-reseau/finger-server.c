#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#define PORT 4242
#define MAX_USER 10

struct user{
    char* firstname;
    char* lastname;
};

struct user userList[MAX_USER] = {{"Titi", "Grominet"},{"Oscar", "Oscar"},{"Alice", "Alice"},{"Bob", "Bob"},{"Toto", "Toto"}};

char* findUser(char* lastname, int size){
    for(int i = 0; i < 5; i++){
        struct user u = userList[i];
        printf("%s\n", u.lastname);
        if(strncmp(lastname, u.lastname, size-1) == 0){
            printf("Find user, %s\n", u.firstname);
            return u.firstname;
        }
    }

    return "Unknown";
}

int main(void)
{
    printf("Finger server\n");

    int socket_fd;

    socket_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_fd == -1)
    {
        perror("Unable to create socket\n");
        return EXIT_FAILURE;
    }
    else
    {
        printf("Socket created\n");
    }

    struct sockaddr_in server_addr;
    bzero(&server_addr, sizeof(server_addr));

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(PORT);

    int bind_status = bind(socket_fd, (struct sockaddr *)&server_addr, sizeof(server_addr));
    if (bind_status != 0)
    {
        perror("Bind failed\n");
        return EXIT_FAILURE;
    }

    if ((listen(socket_fd, 5)) != 0) // authorise 5 connection simu
    {
        perror("Listen failed...\n");
        return EXIT_FAILURE;
    }

    struct sockaddr_in client_addr;
    int len = sizeof(client_addr);
    printf("Server ready!\n");
    while (1 == 1)
    {
        bzero(&client_addr, sizeof(client_addr));
        int client_fd = accept(socket_fd, (struct sockaddr *)&client_addr, &len);

        char buff[50];
        int recv_size = recv(client_fd, buff, 50, 0);
        
        printf("Receive from client (%d char): %s\n",recv_size, buff);


        
        char* firstname = findUser(buff, recv_size-1);
        printf("sizeof(firstname) = %d\n", sizeof(firstname));

        write(client_fd, firstname, strlen(firstname));

        close(client_fd);
    }

    close(socket_fd);

    return EXIT_SUCCESS;
}