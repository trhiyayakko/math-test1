---
id: thm:finite_index_intersection
title: ネーター–イサイの定理
kind: theorem
requires: [def:group, def:subgroup, def:index]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Theorem.** 群 $G$ の有限個の有限指数部分群の共通部分も有限指数をもつ。

**Proof outline.** 各部分群への剰余作用の対角線埋め込みを用いる。

---

### Proofs

#### Proof 1
**Proof.**
$H_1,\dots,H_n$ を $G$ の有限指数部分群とする。商写像の直積
\[
\varphi:G \longrightarrow \prod_{i=1}^n G/H_i
\]
を考えると，核は $\bigcap_i H_i$ であり，像の位数は各 $G/H_i$ の位数の積以下である。従って
\[
[G: \bigcap_i H_i] = |\varphi(G)| \le \prod_{i=1}^n [G:H_i]
\]
となり，右辺は有限なので $\bigcap_i H_i$ も有限指数をもつ。$\square$

---

#tags #theorem #proof
