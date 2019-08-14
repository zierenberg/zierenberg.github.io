ILL_FILES := $(wildcard fig_illustration_*.py)
PLT_FILES := $(filter-out $(ILL_FILES), $(wildcard *.py))
PLT_PNG 	:= $(PLT_FILES:%.py=%.png)

all: $(PLT_PNG) 

.PHONY: clean all

%.png: %.py
	python $<
