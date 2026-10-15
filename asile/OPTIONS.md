# Options of the Asile compiler

You can pass options to the compiler anywhere on the compilation line by writing
the corresponding letter after a "-".
```bash
$ asile -k example...
$ asile example... -k
```

If you want to pass multiple options, you can group them after a single "-", or
keep them separated.
```bash
$ asile -kd example...
$ asile -k -d example...
```

If an option take a parameter, give it directly after the option, separated by a
space:
```bash
$ asile -o my_exec example...
```

## List of options
Here is a list of options. Options not implemented yet are marked by a *TODO*.

| `-h` | Print an help (usage and list of options) and exit, ignoring all other options or files |
| `-v` | Print a version number which has not much meaning, then exit. Ignore all other options or files, except the `-h` option |
| `-o` | Take one parameter. Write the output using its parameter as file name instead of `a.out` |
| `-k` | Use the name of the input without extension as output file name instead of `a.out`. This option is ignored if the `-o` option is set |
| `-d` *TODO* | Create a debugger running the programm instead of an actual executable. If the `-k` option is set, append the extension `.debug` to the output file name. It is still a classic ELF file that can be executed like the usual output. For more info, try it. |

