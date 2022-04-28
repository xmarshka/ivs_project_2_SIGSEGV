NAME_OF_PROJECT_FLDR="ivs_project_2_SIGSEGV1"
FLDR="xmarsa15_xvadov01_xsmata03"
PACK="xmarsa15_xvadov01_xsmata03.zip"

.PHONY: all pack clean run profile help

all: calc_qt.py
	python3 calc_qt.py

pack:
	make clean
	cd .. && if exist $(PACK) (del $(PACK) /q /s /f)
	cd .. && if exist $(FLDR) (rmdir $(FLDR) /s /q)
	cd .. && cd .. && mkdir $(FLDR) && xcopy /s $(NAME_OF_PROJECT_FLDR) $(FLDR) && move $(FLDR) $(NAME_OF_PROJECT_FLDR)
	cd .. && powershell Compress-Archive $(FLDR) $(PACK)
	cd .. && rmdir $(FLDR) /s /q

clean:
	cd .. && cd src && if exist __pycache__\ (rmdir __pycache__ /s /q)

run: calc_qt.py
	python3 calc_qt.py

profile: profiling.py
	python3 profiling.py
help:
	echo "Run make with: pack, clean, run, profile, help"

