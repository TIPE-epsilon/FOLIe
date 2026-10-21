#include "main.h"

#define DFLAG 1
#define OFLAG 2
#define VFLAG 4

void help() {
  printf("Usage: asile [options] <file> [options]\n"
         "Options:\n"
         "  -h    Show this help and exit, ignoring all other options or"
	 "files.\n"
         "  -v    Print a version number which has not much meaning, then "
         "exit. Ignore all\n        other options or files except `-h`.\n"
         "  -o    Take one parameter and use it as name for the output, instead"
         " of `a.out`.\n"
         "  -k    Use the name of the input file without extension as name for "
         "the output.\n        This option is ignored if `-o` is in use.\n"
         "  -d    Create a debugger running the programm instead of a simple "
         "compiled\n        version of it. It is still an ELF file which can be"
         " run as usual. If\n        `-k` is in use, append the extension "
         "`.debug` to the output name. For\n        more info, try it.\n"
         "\n"
         "Source of this debugger available at\n"
         "<https://github.com/TIPE-epsilon/FOLIe/tree/main/asile>");
  exit(0);
}

void version() {
  printf("0.0.0\n");
}

void empty() {}

int main(int argc, char** argv) {
  unsigned char flags = 0;
  char* output = "a.out";
  
  char opt;
  while ((opt = getopt(argc, argv, ":dhko:v")) != -1)
    switch (opt) {
    case 100: flags |= DFLAG; break;
    case 104: help(); break;
    case 107: if (!(flags & OFLAG)) output = NULL; break;
    case 111: output = optarg; flags |= OFLAG; break;
    case 118: flags |= VFLAG; break;
    case 58:
      fprintf(stderr, "Error: Option -%c expect an argument\n", optopt);
      exit(1);
    case 63:
      fprintf(stderr, "Error: Unknown option -%c\n", optopt);
      exit(1);
    default:
      fprintf(stderr, "Error: Unreachable code reached\n");
      exit(1);
    }
  if (flags & VFLAG) version();

  char* input_file;
  if (optind == argc - 1) input_file = argv[optind];
  else if (optind == argc) fprintf(stderr, "Error: Missing input file\n");
  else fprintf(stderr, "Error: Too many input files\n");
  if (optind != argc - 1) exit(1);

  for (char* p = input_file; *p != 0; ++p)
    (*(p+1) == 0) ?
      (((p - input_file) < 2) || ((*p != 46)
				  || (*(p - 1) != 46)
				  || (*(p - 2) != 46))) ?
      exit(1 + (0 & fprintf(stderr, "Error: Unrecognized file extension\n"))) :
      ((p - input_file) == 2) ?
      exit(1 + (0 & fprintf(stderr, "Error: Empty file name\n"))) : (void)0
      : (void)0;

  // Trust me it works and write the good output name
  if (!(flags & OFLAG))
    if (output == NULL)
      for (char* i = input_file; *(i+2); ++i)
        if (!*(i+3))
          for (char* p = (output = (char*)malloc(i - input_file
                                                 + (flags & DFLAG) ? 9 : 1)
                          ) - 1;
               p-output < i-input_file + ((flags & DFLAG) ? 6 : 0);
               p-output < i-input_file ? (*p) = *(input_file + (p-output)) :
               p-output == i-input_file ? (*p) = (flags & DFLAG) ? 46 : 0 :
                 (*p = "debug"[p - output - (i - input_file) - 1])
               ) ++p;

  int input_fd = open(input_file, O_RDONLY);
  if (input_fd == -1) exit(1 + (0 & fprintf(stderr, "Error: %s\n",
                                            strerror(errno))));
  char** lines = parse_input(input_fd);

  int output_fd = open(output, O_WRONLY | O_CREAT | O_TRUNC);
  if (input_fd == -1) exit(1 + (0 & fprintf(stderr, "Error: %s\n",
                                            strerror(errno))));
  
  generate(output_fd, lines);
  exit(0);
}
