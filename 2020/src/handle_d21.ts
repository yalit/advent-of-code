import { argv0 } from "process";

const getIngredientsAndAllergens = (lines: Array<string>) => {
  let all_ingredients = {};
  let possible_pairs = {};

  lines.forEach((line: string) => {
    const [left, right] = line.slice(0, line.length - 1).split(" (contains ");

    const ingredients = left.split(" ");
    const allergens = right.split(", ");

    ingredients.forEach((ingredient) => {
      if (!(ingredient in all_ingredients)) {
        all_ingredients[ingredient] = 0;
      }

      all_ingredients[ingredient] += 1;
      allergens.forEach((allergen: string) => {
        const pair = ingredient + "-" + allergen;
        if (!(allergen in possible_pairs)) {
          possible_pairs[allergen] = {};
        }

        if (!(ingredient in possible_pairs[allergen])) {
          possible_pairs[allergen][ingredient] = 0;
        }

        possible_pairs[allergen][ingredient] += 1;
      });
    });
  });

  let allergens = {};

  while (Object.keys(allergens).length !== Object.keys(possible_pairs).length) {
    for (const allergen in possible_pairs) {
      if (allergen in allergens) {
        continue;
      }

      const maximum = Object.values(possible_pairs[allergen]).reduce(
        (m: number, n: number) => Math.max(m, n),
      );

      const maximums = Object.entries(possible_pairs[allergen]).filter(
        (entry) =>
          entry[1] === maximum && !Object.values(allergens).includes(entry[0]),
      );

      if (maximums.length === 1) {
        allergens[allergen] = maximums[0][0];

        for (const a in allergens) {
          delete allergens[a][allergen];
        }
      }
    }
  }

  return [all_ingredients, allergens];
};
function handleInput_1(lines: Array<string>) {
  const [ingredients, allergens] = getIngredientsAndAllergens(lines);

  return Object.entries(ingredients).reduce(
    (s, e: [string, number]) =>
      Object.values(allergens).includes(e[0]) ? s : s + e[1],
    0,
  );
}

function handleInput_2(lines: Array<string>) {
  const [ingredients, allergens] = getIngredientsAndAllergens(lines);

  return Object.entries(allergens)
    .sort()
    .map((e) => e[1])
    .join(",");
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}

