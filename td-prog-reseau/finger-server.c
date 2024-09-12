#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>

#define PORT 4242

int main (void){
    printf("Finger server\n");

    int sock = socket(PF_INET, SOCK_STREAM, 0); //IPV4, ???, protocol
    struct sockaddr_in adress_sock;
    adress_sock.sin_family = AF_INET; //IPV4
    adress_sock.sin_port = htons(PORT); //port
    adress_sock.sin_addr.s_addr = htonl(INADDR_ANY); //anybody

    int bind_status = bind(sock, &adress_sock, sizeof(adress_sock));

    if(bind_status != 0){
        fprintf(stderr, "Unable to bind, error code: %d\n", bind_status);
        return EXIT_FAILURE;
    } else {
        printf("Server listening on port %d", PORT);
        struct sockaddr client_addr;
        int len = sizeof(client_addr);
        char input[50] = "-1";
        while(1==1){
            memset(&client_addr, 0, len);
            
        }
    }

    

    return EXIT_SUCCESS;
}