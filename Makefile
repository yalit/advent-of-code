init:
	./pyaoc init $(filter-out $@,$(MAKECMDGOALS))

test:
	./pyaoc test $(filter-out $@,$(MAKECMDGOALS))

run:
	./pyaoc run $(filter-out $@,$(MAKECMDGOALS))

build: #make build year=XXXX
	tsc -p ./${year}/src/tsconfig.json

watch: #make watch year=XXXX
	tsc-watch --noClear -p ./${year}/src/tsconfig.json