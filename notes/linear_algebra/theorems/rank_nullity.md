---
id: thm:rank_nullity
title: 次元定理
kind: theorem
requires: [def:linear_map, def:kernel_linear, def:image_linear, def:dimension]
status: draft
authors: [mathbot]
refs: []
tags: [linear_algebra]
---

**Theorem.** 有限次元ベクトル空間 $V$ と線形写像 $T:V\to W$ に対し，
\[
\dim V = \dim(\ker T) + \dim(\operatorname{Im} T)
\]
が成り立つ。

---

### Proofs

#### Proof 1 (概略/outline)
**Proof.**
(1) $V$ の基底を $\ker T$ の基底とその補集合に分ける。  
(2) 補集合の像は $\operatorname{Im} T$ の基底を与える。  
(3) 元数を数え上げれば等式が得られる。 $\square$

---

#tags #theorem #proof
