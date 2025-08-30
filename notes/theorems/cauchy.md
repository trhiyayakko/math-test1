---
id: thm:cauchy
title: コーシーの定理
kind: theorem
requires: [def:group, def:order, def:prime]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Theorem.** 有限群 $G$ の位数 $|G|$ が素数 $p$ を割り切るとき，$G$ には位数 $p$ の元が存在する。

**Proof outline.** $G$ が $p$-タプル全体に巡回置換する作用を考え，軌道の大きさから元を得る。

---

### Proofs

#### Proof 1
**Proof.**
$|G|=p^km$（$p\nmid m$）と書く。$G$ が $p$ 個の元からなる集合 $X=G^p$ に対し左からの対角作用をするように考える。$X$ 上の $\mathbb{Z}/p\mathbb{Z}$ による円順作用
\[(g_1,\dots,g_p)\mapsto(g_2,\dots,g_p,g_1)
\]
を併せると，固定点は $g_1=\cdots=g_p$ の場合に限られ，そのとき $g_1^p=e$ が必要である。軌道は大きさ 1 または $p$ であり，総数 $|X|=|G|^p$ は $p$ の倍数であるから，円順作用に関して固定点が存在する。よって $g\in G$ で $g^p=e$ かつ $g\ne e$ が存在し，これは位数 $p$ の元である。$\square$

---

#tags #theorem #proof
