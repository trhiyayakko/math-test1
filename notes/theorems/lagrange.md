---
id: thm:lagrange
title: ラグランジュの定理
kind: theorem
requires: [def:group, def:subgroup, def:order, def:index]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Theorem.** 有限群 $G$ とその部分群 $H$ に対し，$|G| = [G:H]\,|H|$ が成り立つ。特に $|H|$ は $|G|$ を割り切る。

**Proof outline.** $G$ を $H$ の左剰余類で分割して数え上げればよい。

---

### Proofs

#### Proof 1 (直接的/constructive)
**Proof.**
$G$ を部分群 $H$ の左剰余類 $gH$ で分割すると，剰余類は互いに素でその和は $G$ 全体になる。各剰余類は写像 $h \mapsto gh$ により $H$ と同じ元数 $|H|$ をもつ。したがって剰余類の個数を $[G:H]$ と書けば
\[
|G| = [G:H]\\,|H|
\]
が成り立つ。特に $[G:H]$ は整数なので $|H|$ は $|G|$ を割り切る。 $\square$

---

#tags #theorem #proof

