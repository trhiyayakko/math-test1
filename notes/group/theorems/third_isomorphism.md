---
id: thm:third_isomorphism
title: 第3準同型定理
kind: theorem
requires: [def:group, def:normal_subgroup, def:quotient_group]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Theorem.** 正規部分群 $K \subseteq H \subseteq G$ に対し，$(G/K)/(H/K) \cong G/H$。

**Proof outline.** 商群の普遍性から直ちに従う。

---

### Proofs

#### Proof 1
**Proof.**
正規部分群 $K \subseteq H \subseteq G$ に対し，商写像 $\pi:G\to G/K$ を考える。$H/K$ は $G/K$ の部分群であり，再び商をとると $(G/K)/(H/K)$ が得られる。一方 $\pi$ を $G$ から $G/H$ への自然射 $\rho$ と合成すると $G/K \to G/H$ の全射準同型が得られ，核は $H/K$ である。第1準同型定理より
\[
(G/K)/(H/K) \cong G/H.
\]
$\square$

---

#tags #theorem #proof
