NAME_OF_PROJECT_FLDR="ivs_project_2_SIGSEGV"
FLDR="xmarsa15_xvadov01_xsmata03"
PACK="xmarsa15_xvadov01_xsmata03.zip"

.PHONY: all pack clean run profile help

all: calc_qt.py
	pyinstaller -F -w --onefile --add-data "res/calc.ui;res." --add-data "res/LogoCalc.png;res." calc_qt.py
	cd dist && calc_qt.exe

pack:
	make clean
	cd .. && if exist $(PACK) (del $(PACK) /q /s /f)
	cd .. && if exist $(FLDR) (rmdir $(FLDR) /s /q)
	cd .. && cd .. && mkdir $(FLDR) && xcopy /s $(NAME_OF_PROJECT_FLDR) $(FLDR) && move $(FLDR) $(NAME_OF_PROJECT_FLDR)
	cd .. && cd $(FLDR) && mkdir install && mkdir repo
	cd .. && cd $(FLDR) && if exist setup.exe (move setup.exe install) && move *.* repo && move .idea repo && move mockup repo && move plan repo && move profiling repo && move src repo
	cd .. && powershell Compress-Archive $(FLDR) $(PACK)
	cd .. && rmdir $(FLDR) /s /q

clean:
	cd .. && cd src && if exist __pycache__\ (rmdir __pycache__ /s /q)
	if exist build\ (rmdir build /s /q)
	if exist dist\ (rmdir dist /s /q)

run:
	cd dist && calc_qt.exe

profile: profiling.py
	python3 profiling.py
help:
	echo "Run make with: pack, clean, run, profile, help"

