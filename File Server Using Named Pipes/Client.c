#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
   int client_to_server;
   char *myfifo = "/tmp/client_to_server_fifo";
   int server_to_client;
   char *myfifo2 = "/tmp/server_to_client_fifo";
   char str[BUFSIZ];
   printf("Input File Name: ");
   scanf("%s", str);
   client_to_server = open(myfifo, O_WRONLY);
   server_to_client = open(myfifo2, O_RDONLY);
   write(client_to_server, str, sizeof(str));
   read(server_to_client,str,sizeof(str));
   printf("Contents of File as recieved from Server are: %s\n",str);
   close(client_to_server);
   close(server_to_client);
   return 0;
}
