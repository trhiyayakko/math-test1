---
id: thm:steinitz_exchange
title: シュタイニッツの交換補題
kind: theorem
requires: [def:basis, def:linear_independence]
status: draft
authors: [mathbot]
refs: []
tags: [linear_algebra]
---

**Theorem.** ベクトル空間 $V$ の線形独立な集合 $L$ と基底 $B$ に対して，$L$ の各元は $B$ の元を置き換えることで基底に拡張できる。特に有限次元の場合，任意の2つの基底は同じ個数の元をもつ。

---

### Proofs

#### Proof 1 (概略/outline)
**Proof.**
(1) $B$ を用いて $V$ の任意の元を表せることから，$L$ の各元は $B$ の線形結合で表される。  
(2) その係数の1つが非零であるような $b\in B$ を選び，$b$ を対応する $l\in L$ と交換する。  
(3) この操作を $L$ の各元について繰り返すと，得られた集合は基底となる。 $\square$

---

#tags #theorem #proof
