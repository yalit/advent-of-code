build: #make build year=XXXX
	tsc -p ./${year}/src/tsconfig.json

watch: #make watch year=XXXX
	tsc-watch --noClear -p ./${year}/src/tsconfig.json