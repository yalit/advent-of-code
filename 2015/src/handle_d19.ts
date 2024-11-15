function handleInput_1(lines: Array<string>) {
  let mappings = {};

  lines.slice(0, lines.length - 2).forEach((r) => {
    const i = r.match(/(.+) => (.+)/);
    if (!(i[1] in mappings)) {
      mappings[i[1]] = [];
    }
    mappings[i[1]].push(i[2]);
  });

  const base = lines[lines.length - 1];

  let modifications = new Set<string>();
  base.split("").forEach((_, i) => {
    let matchedMappings = [];
    Object.keys(mappings).forEach((m) => {
      if (m === base.slice(i, i + m.length)) matchedMappings.push(m);
    });

    matchedMappings.forEach((m) => {
      mappings[m].forEach((v: string) => {
        modifications.add(base.slice(0, i) + v + base.slice(i + m.length));
      });
    });
  });

  return modifications.size;
}

function handleInput_2(lines: Array<string>) {
  const base = Array.from(lines[lines.length - 1]);

  // solution based on this text analysis : https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
  return (
    base.length -
    base.filter((c) => c === "(" || c === ")").length -
    2 * base.filter((c) => c === ",").length -
    1
  );
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}
