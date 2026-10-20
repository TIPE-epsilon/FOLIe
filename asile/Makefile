objects = main.o parser.o elf_gen.o
objdir = build
cflags = -Werror -Wpedantic -Wall -Wextra -Wstrict-prototypes

vpath %.h headers
vpath %.c src
vpath %.o build

asile: $(objects)
	gcc -o $@ $^ -B build

$(objdir):
	mkdir $@

# TODO : auto-generate this rule to take care of includes
%.o: %.c %.h $(objdir)
	gcc -c -o build/$@ $< -I headers $(cflags)

.PHONY : clean cleanobj cleantest
.IGNORE : clean cleanobj cleantest
.SILENT : test

clean :
	rm -f asile
	rm -rf build

cleanobj :
	rm -rf build

cleantest :
	rm -rf tests/build

test : asile cleantest
	echo "ok"

