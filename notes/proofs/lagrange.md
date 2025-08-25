---
id: proof:lagrange
title: ラグランジュの定理の証明
kind: proof
requires: [thm:lagrange, def:group, def:subgroup, def:order, def:index]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Proof of** `[thm:lagrange]`:

$G$ を部分群 $H$ の左剰余類 $gH$ で分割すると，剰余類は互いに素でその和は $G$ 全体になる。各剰余類は写像 $h \mapsto gh$ により $H$ と同じ元数 $|H|$ をもつ。したがって剰余類の個数を $[G:H]$ と書けば
\[
|G| = [G:H]\,|H|
\]
が成り立つ。特に $[G:H]$ は整数なので $|H|$ は $|G|$ を割り切る。$\square$

#tags #proof
