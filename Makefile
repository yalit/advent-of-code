build:
	tsc -p ./${year}/src/tsconfig.json

watch:
	tsc -p -w ./${year}/src/tsconfig.json