
#include <unistd.h>
#include <stdio.h>

static void do_print_usage(){
        printf("usage: [OPTIONS]\n"
                    "Options are: \n"
                    "   -a, no parameters required \n"
                    "   -b, parameters required \n"
                    "   -c, parameters required \n"
                    "   -d, no parameters required\n"
                    "   -e, optional parameters\n"
                    "   -h, no parameters required, display this help\n");


}

int main(int argc, char * argv[])
{
#ifdef GETOPT
    int opt;
    if (argc < 2) {
            printf("Please make sure your input is right. '-h' to see help.\n");
            return -1;
    }
       while ((opt = getopt(argc, argv, "ab:c:de::h")) != -1)
       {
        switch (opt)
        {
               case 'a':
                       printf("HAVE option: -a\n\n");
                       break;
               case 'b':
                       printf("HAVE option: -b\n");
                       printf("The argument of -b is %s\n\n", optarg);
                       break;
               case 'c':
                       printf("HAVE option: -c\n");
                       printf("The argument of -c is %s\n\n", optarg);
                       break;
               case 'd':
                       printf("HAVE option: -d\n");
                       break;
              case 'e':
                       printf("HAVE option: -e\n");
                       printf("The argument of -e is %s\n\n", optarg);
                       break;
              case 'h':
                       do_print_usage();
                       break;
              case '?':
                       printf("Unknown option: %c\n",(char)optopt);
                       do_print_usage();
                       break;

               }
       }
#else
      int opt;
      char *string = "a::b:c:d";
      while((opt = getopt(argc, argv, string)) != -1){
      printf("opt = %c\t\t", opt);
      printf("optarg = %s\t\t", optarg);
      printf("optind = %d\t\t", optind);
      printf("argv[optind] = %s\n", argv[optind]);

     }


#endif

}
