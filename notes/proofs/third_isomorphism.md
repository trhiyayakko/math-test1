---
id: proof:third_isomorphism
title: 第3準同型定理の証明
kind: proof
requires: [thm:third_isomorphism, def:group, def:normal_subgroup, def:quotient_group]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Proof of** `[thm:third_isomorphism]`:

正規部分群 $K \subseteq H \subseteq G$ に対し，商写像 $\pi:G\to G/K$ を考える。$H/K$ は $G/K$ の部分群であり，再び商をとると $(G/K)/(H/K)$ が得られる。一方 $\pi$ を $G$ から $G/H$ への自然射 $\rho$ と合成すると $G/K \to G/H$ の全射準同型が得られ，核は $H/K$ である。第1準同型定理より
\[
(G/K)/(H/K) \cong G/H.
\]
$\square$

#tags #proof
