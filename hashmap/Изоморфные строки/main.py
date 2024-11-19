def isIsomorphic(self, s: str, t: str) -> bool:
	if len(s) != len(t): return False

	posS = {}  # кл - символ, зн - массив того, где встречаются
	posT = {}  # кл - символ, зн - массив того, где встречаются

	for i in range(len(s)):
		if s[i] in posS:
			posS[s[i]].append(i)
		else:
			posS[s[i]] = [i]

		if t[i] in posT:
			posT[t[i]].append(i)
		else:
			posT[t[i]] = [i]

	for (ks, vs), (kt, vt) in zip(posS.items(), posT.items()):
		if vs != vt:
			return False

	return True