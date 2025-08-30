---
id: thm:burnside_lemma
title: バーンサイドの補題
kind: theorem
requires: [def:group_action, def:orbit, def:order]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Theorem.** 有限群 $G$ が集合 $X$ に作用するとき，軌道の個数は
\[
\frac{1}{|G|}\sum_{g\in G} |X^g|
\]
に等しい。ただし $X^g$ は $g$ により固定される元の集合である。

**Proof outline.** 固定点の数を作用で数え上げる。

---

### Proofs

#### Proof 1
**Proof.**
集合 $X$ への $G$ の作用を考える。対 $(g,x)$ で $gx=x$ を満たすものの集合を $Y$ とすると，一方で $g$ ごとに $|X^g|$ 個，もう一方で $x$ ごとに $|G_x|$ 個の要素がある。したがって
\[
\sum_{g\in G} |X^g| = \sum_{x\in X} |G_x|.
\]
軌道・安定化群の公式より $|G_x|=|G|/|Gx|$ なので
\[
\sum_{g\in G}|X^g| = |G|\sum_{x\in X} \frac{1}{|Gx|} = |G|\,\#(X/G).
\]
両辺を $|G|$ で割れば主張が得られる。$\square$

---

#tags #theorem #proof
