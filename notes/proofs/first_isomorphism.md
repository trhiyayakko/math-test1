---
id: proof:first_isomorphism
title: 第1準同型定理の証明
kind: proof
requires: [thm:first_isomorphism, def:group, def:homomorphism, def:kernel, def:quotient_group]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Proof of** `[thm:first_isomorphism]`:

群準同型 $f:G\to H$ に対し，写像
\[
\bar f: G/\ker f \to \mathrm{Im}(f),\quad g\ker f \mapsto f(g)
\]
を定義する。$g\ker f=g'\ker f$ なら $g^{-1}g'\in\ker f$ より $f(g)=f(g')$ であるから $\bar f$ は well-defined であり群準同型である。$\bar f$ は像の定義から全射であり，核は $\ker \bar f=\{g\ker f \mid f(g)=e\}=\{\ker f\}$ なので単射である。ゆえに $\bar f$ は同型写像であり，$G/\ker f\cong \mathrm{Im}(f)$ が従う。$\square$

#tags #proof
