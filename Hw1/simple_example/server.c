#include <stdio.h>            /*  standard I/O  */
#include <stdlib.h>           /*  standard library */
#include <string.h>           /*  string library */
#include <sys/socket.h>       /*  socket definitions */
#include <sys/types.h>        /*  socket types       */
#include <arpa/inet.h>        /*  inet (3) funtions         */
#include <winsock2.h>

#define  MYPORT    12345
#define  BACKLOG   5

int main(void)
{
   int  sockfd, new_fd; // listen on sock_fd, new connection on new_fd
   struct sockaddr_in   my_addr; // my address information
   struct sockaddr_in   their_addr; // connector’s address information
   int sin_size;

   if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
      perror("socket");
      exit(1);
   }

   my_addr.sin_family = AF_INET; // host byte order
   my_addr.sin_port = htons(MYPORT); // short, network byte order
   my_addr.sin_addr.s_addr = INADDR_ANY; // automatically fill with my IP
   memset(&(my_addr.sin_zero), 0, 8); // zero the rest of the struct

  if (bind(sockfd, (struct sockaddr *)&my_addr, sizeof(struct sockaddr)) == -1) {
      perror("bind");
      exit(1);
  }
  if (listen(sockfd, BACKLOG) == -1) {
      perror("listen");
      exit(1);
  }

  while(1) {                     // main accept() loop

      sin_size = sizeof(struct sockaddr_in);
      if ((new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &sin_size)) == -1) {
          perror("accept");
          continue;
      }

      if (send(new_fd, "Hello, world!\n", 14, 0) == -1)
           perror("send");

      close(new_fd); 

   } // end of while
   return 0;
}

