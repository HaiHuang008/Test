
#include <unistd.h>
#include <stdio.h>

#define  GETOPT_FMT "alhd:v"

static struct option long_opt[] = {
    /* These options set a flag. */
    {"version",    no_argument,       0, 'v'},
    {"all",        no_argument,       0, 'a'},
    {"help",       no_argument,       0, 'h'},
    {"dev",        required_argument, 0, 'd'},
    {"list",       no_argument,       0, 'l'},
    {0, 0, 0, 0}
};


static void do_show_help(char * prog)
{
    printf("usage: %s [OPTIONS]\n"
           "Options are: \n"
           "    -a  --all             Test all configure options\n"
           "    -v, --version         show Version\n"
           "    -l, --list            Show Device list\n"
           "    -d, --dev             Device id\n"
           "    -h, --help            Display this help text and exit\n", prog);

    printf("Example:             \n"
           "       --all         \n"
           "       -d 1          \n"
           "       -h            \n"
           );
}

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
    int opt;
    int option_index = 0;
    if (argc < 2) {
            printf("Please make sure your input is right. '-h' to see help.\n");
            return -1;
    }
        
#ifdef GETOPT
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
#endif
        
#ifdef GETOPT_T
      char *string = "a::b:c:d";
      while((opt = getopt(argc, argv, string)) != -1){
      printf("opt = %c\t\t", opt);
      printf("optarg = %s\t\t", optarg);
      printf("optind = %d\t\t", optind);
      printf("argv[optind] = %s\n", argv[optind]);

     }

#endif

#ifdef GETOPT_LONG_T
      int digit_optind = 0;
      char *string = "a::b:c:d";
      static struct option long_options[] = {

             {"reqarg", required_argument, NULL, 'r'},
             {"optarg", optional_argument, NULL, 'o'},
             {"noarg",  no_argument, NULL, 'n'},
             {"NULL", 0, NULL, 'r'},




       };

       while((opt = getopt_long_only(argc, argv, string, long_options, &option_index) ) != -1){
        printf("opt = %c\t\t", opt);
        printf("optarg = %s\t\t",optarg);
        printf("optind = %d\t\t",optind);
        printf("argv[optind] =%s\t\t", argv[optind]);
        printf("option_index = %d\n",option_index);

        }


#endif
 
#ifdef GETOPT_LONG

     while((opt = getopt_long_only(argc, argv, GETOPT_FMT, long_opt, &option_index)) != -1 ){

      switch(opt){
       case 'v':
                printf("Show version \n");
                break;
       case 'a':
                printf("Test all configure options \n");
                break;
       case 'h':
                do_show_help(argv[0]);
                break;
       case 'd':
                printf("Input Device id\n");
                break;
       case 'l':
                printf("Show Device list\n");
                break;
        case '?':
                printf("Unknown option: %c\n",(char)optopt);
                do_show_help(argv[0]);
                break;

            }
}


#endif
        

}
