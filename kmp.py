def build_lps(pattern):
    lps = [0] * len(pattern)
    i = 1
    j = 0

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j > 0:
            # Pokušavamo sa kraćim prefiksom.
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    # Prazan obrazac se pojavljuje na svakoj granici teksta.
    if m == 0:
        return list(range(n + 1))

    lps = build_lps(pattern)
    positions = []
    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                positions.append(i - m)
                # Zadržavamo mogući preklop za sledeće pojavljivanje.
                j = lps[j - 1]

        elif j > 0:
            # Isto slovo teksta poredimo sa ranijom pozicijom obrasca.
            j = lps[j - 1]
        else:
            i += 1

    return positions


if __name__ == "__main__":
    text = "ABABABC"
    pattern = "ABABC"

    print("Text:", text)
    print("Pattern:", pattern)
    print("LPS:", build_lps(pattern))
    print("Positions:", kmp_search(text, pattern))