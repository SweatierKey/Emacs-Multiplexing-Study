.PHONY: prepare smoke test report serve verify package
prepare:
	python3 scripts/prepare.py
smoke:
	python3 scripts/run-suite.py --smoke
test:
	python3 scripts/run-suite.py
report:
	python3 scripts/build-report.py
serve:
	python3 -m http.server 8000 --bind 127.0.0.1
verify:
	python3 scripts/verify.py
package:
	python3 scripts/package.py
