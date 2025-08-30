---
id: thm:rolle
title: ロルの定理
kind: theorem
requires: ["def:derivative"]
status: draft
authors: [mathbot]
refs: []
tags: [calculus]
---

**Theorem.** 関数 $f$ が閉区間 $[a,b]$ で連続，開区間 $(a,b)$ で微分可能で $f(a)=f(b)$ とする。このとき $(a,b)$ に $c$ が存在して
\[
f'(c)=0.
\]

**Proof outline.** $f$ の極値をとる点に着目し，微分係数の性質を用いる。

---

### Proofs

#### Proof 1
**Proof.** $f$ は $[a,b]$ で連続なので最大値と最小値を取る。$f(a)=f(b)$ であるから，いずれかの極値は内部 $(a,b)$ で達成される。そこで $c$ をその極値をとる点とすると $f'(c)=0$ である。$\square$

---

#tags #theorem #proof
