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

| Option | Description |
| --- | --- |
| `-h` | Show an help (usage and list of options) and exit, ignoring all other options or files. |
| `-v` | Print a version number which has not much meaning, then exit. Ignore all other options or files except `-h`. |
| `-o` | Take one parameter and use it as name for the output, instead of `a.out`. |
| `-k` | Use the name of the input file without extension as name for the output. This option is ignored if `-o` is in use |
| `-d` *TODO* | Create a debugger running the programm instead of a simple compiled version of it. It is still an ELF file which can be run as usual. If `-k` option is in use, append the extension `.debug` to the output name. |
