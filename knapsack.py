def knapsack(weights, values, W):
    n = len(weights)

    # tabela sa n + 1 redova i W + 1 kolona.
    DP = [[0] * (W + 1) for _ in range(n + 1)]

    # Popunjavanje tabele
    for i in range(1, n + 1):
        for k in range(1, W + 1):

            # predmet ne staje u trenutni kapacitet.
            if weights[i - 1] > k:
                DP[i][k] = DP[i - 1][k]

            else:
                excluded = DP[i - 1][k]

                included = (
                    values[i - 1]
                    + DP[i - 1][k - weights[i - 1]]
                )

                DP[i][k] = max(excluded, included)

    # pronalazenje izabranih predmeta
    chosen_items = []
    k = W

    for i in range(n, 0, -1):
        if DP[i][k] != DP[i - 1][k]:
            chosen_items.append(i - 1)
            k -= weights[i - 1]

    # vracanje predmeta u prvobitni redosled
    chosen_items.reverse()

    return DP[n][W], chosen_items


# Primer: izbor predmeta za ranac kapaciteta 5 kg.
items = ["A", "B", "C"]
weights = [2, 3, 4]
values = [6, 10, 12]
capacity = 5
max_value, chosen_items = knapsack(
    weights, values, capacity
)

print("Najveća ukupna vrednost:", max_value)
print("Izabrani predmeti:", ", ".join(items[j] for j in chosen_items))
print("Ukupna težina:", sum(weights[j] for j in chosen_items), "kg")