#include <stdio.h>            /*  standard I/O  */
#include <stdlib.h>           /*  standard library */
#include <string.h>           /*  string library */
#include <sys/socket.h>       /*  socket definitions */
#include <sys/types.h>        /*  socket types       */
#include <arpa/inet.h>        /*  inet (3) funtions         */
#include <winsock2.h>


#define PORT 12345 // the port client will be connecting to
#define MAXDATASIZE 100 // max number of bytes we can get at once
int main(int argc, char *argv[])
{
    int sockfd, numbytes;
    char buf[MAXDATASIZE];
    struct sockaddr_in server_addr; // connector’s address information

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
       perror("socket");
       exit(1);
    }

    server_addr.sin_family = AF_INET; // host byte order
    server_addr.sin_port = htons(PORT); // short, network byte order
    server_addr.sin_addr.s_addr = inet_addr("140.118.126.50");
    memset(&(server_addr.sin_zero), 0, 8); // zero the rest of the struct
    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(struct sockaddr)) == -1) {
       perror("connect");
       exit(1);
    }

    if ((numbytes=recv(sockfd, buf, MAXDATASIZE-1, 0)) == -1) {
       perror("recv");
       exit(1);
    }

    buf[numbytes] = 0;
    printf("Received: %s",buf);

    close(sockfd);
    return 0;
}

