hdir = headers
sdir = src
odir = build
mdir = makefiles

sources = $(notdir $(wildcard $(sdir)/*))
objects = $(subst .c,.o,$(sources))
mkfiles = $(subst .c,.d,$(sources))
generated_dirs = $(odir) $(mdir)

vpath %.h $(hdir)
vpath %.c $(sdir)
vpath %.o $(odir)

asile: $(objects)
	gcc -o $@ $(addprefix $(odir)/,$(^F))

include $(addprefix $(mdir)/,$(mkfiles))

$(generated_dirs):
	mkdir $@

# Makefiles auto-generation depending on includes
$(mdir)/%.d: %.c | $(mdir)
	@set -e
	@echo "Generating dependency Makefile for $(<F)"
	gcc -MM $< -I $(hdir) > $(mdir)/$(@F)

# Rule for object files, prerequisites are included via the precedent rule
%.o: | $(odir)
	gcc -c -o $(odir)/$@ \$< -I $(hdir) @GCC_FLAGS

clean :
	rm -f asile
	rm -rf $(generated_dirs)

# ============================== Tests ==============================
#
# TODO
#
# Tests are made by two files :
#  - testname...        -> The FOLIe file
#  - testname.input     -> the input file
#  - testname.expected  -> The expected output
# The FOLIe file is the one defining the tests (file.input or file.expected
# without file... will not be read)
# A missing input file will be treated as emtpy, with a warning
# A missing expectation file will only test the fact that the FOLIe file compile
# and run without error

tdir = tests
tmpdir = temp

tests = $(patsubst %...,%,$(notdir $(wildcard $(tdir)/*)))

test : $(add_prefix $(tdir)/$(tmpdir)/,$(tests)) TODO
	@echo "tests : $(tests)"
#	print tests statistics and outputs
	rm -rf $(tdir)/$(tmpdir)

$(add_prefix $(tdir)/$(tmpdir)/,$(tests)): TODO | $(tmpdir)
	asile -o $@ $(tdir)/$(@F)... &> $@.compilation
	if [ $$$$ ]; then \
	  echo "Compiled"; \
	else \
	  echo "Compilation error"; \
	fi

TODO:
	echo "Feature not implemented"
	false

.PHONY : clean test TODO
.IGNORE : clean $(add_prefix $(tdir)/$(tmpdir)/,$(tests))
.SILENT : test $(addprefix $(mdir)/,$(mkfiles)) \
	$(add_prefix $(tdir)/$(tmpdir)/,$(tests)) TODO
