---
id: proof:second_isomorphism
title: 第2準同型定理の証明
kind: proof
requires: [thm:second_isomorphism, def:group, def:subgroup, def:normal_subgroup, def:quotient_group]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Proof of** `[thm:second_isomorphism]`:

$H$ を $G$ の部分群，$N$ を正規部分群とする。商写像 $\pi:G\to G/N$ を考えると，$\pi(H)=HN/N$ である。$H$ から $G/N$ への制限 $\pi|_H$ の核は $H\cap N$ であり，像は $HN/N$ である。第1準同型定理より
\[
H/(H\cap N) \cong HN/N.
\]
これが主張である。$\square$

#tags #proof
