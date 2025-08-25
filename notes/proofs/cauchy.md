---
id: proof:cauchy
title: コーシーの定理の証明
kind: proof
requires: [thm:cauchy, def:group, def:order, def:prime]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Proof of** `[thm:cauchy]`:

$|G|=p^km$（$p\nmid m$）と書く。$G$ が $p$ 個の元からなる集合 $X=G^p$ に対し左からの対角作用をするように考える。$X$ 上の $\mathbb{Z}/p\mathbb{Z}$ による円順作用
\[(g_1,\dots,g_p)\mapsto(g_2,\dots,g_p,g_1)
\]
を併せると，固定点は $g_1=\cdots=g_p$ の場合に限られ，そのとき $g_1^p=e$ が必要である。軌道は大きさ 1 または $p$ であり，総数 $|X|=|G|^p$ は $p$ の倍数であるから，円順作用に関して固定点が存在する。よって $g\in G$ で $g^p=e$ かつ $g\ne e$ が存在し，これは位数 $p$ の元である。$\square$

#tags #proof
