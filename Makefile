# Road_Rules Makefile
# Usage: make <target>
# Requires: Python 3, reportlab, pytest

.PHONY: build trip van test push clean archive help

help:
	@echo "Road_Rules build targets:"
	@echo "  make build    — Rebuild all PDFs (van + trip)"
	@echo "  make trip     — Rebuild trip PDFs only"
	@echo "  make van      — Rebuild van spec PDF only"
	@echo "  make test     — Run all tests"
	@echo "  make archive  — Archive current outputs, then rebuild"
	@echo "  make clean    — Remove current PDF outputs"
	@echo "  make push     — Commit and push (set msg= for commit message)"
	@echo ""
	@echo "  make push msg='Update Glacier dates'"

build:
	python build.py

trip:
	python build.py --trip

van:
	python build.py --van

test:
	python -m pytest tests/ -v

archive:
	python build.py --archive

clean:
	rm -f outputs/current/*.pdf
	@echo "Cleaned outputs/current/"

push:
	@if [ -z "$(msg)" ]; then echo "Usage: make push msg='Your commit message'"; exit 1; fi
	git add .
	git commit -m "$(msg)"
	git push origin main
