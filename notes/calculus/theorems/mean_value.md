---
id: thm:mean_value
title: 平均値の定理
kind: theorem
requires: [def:derivative]
status: draft
authors: [mathbot]
refs: []
tags: [calculus]
---

**Theorem.** 関数 $f$ が閉区間 $[a,b]$ で連続，開区間 $(a,b)$ で微分可能ならば，$c\in(a,b)$ が存在して
\[
f'(c)=\frac{f(b)-f(a)}{b-a}.
\]

**Proof outline.** ロルの定理を用いる。

---

### Proofs

#### Proof 1
**Proof.** 関数
\[g(x)=f(x)-\frac{f(b)-f(a)}{b-a}(x-a)\]
を考えると $g(a)=g(b)$ である。ロルの定理により $(a,b)$ に $g'(c)=0$ となる $c$ が存在する。計算すると $f'(c)=\frac{f(b)-f(a)}{b-a}$ が得られる。$\square$

---

#tags #theorem #proof
