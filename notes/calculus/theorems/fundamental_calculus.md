---
id: thm:fundamental_calculus
title: 微積分の基本定理
kind: theorem
requires: ["def:integral", "def:derivative", "thm:mean_value"]
status: draft
authors: [mathbot]
refs: []
tags: [calculus]
---

**Theorem.** $f$ を閉区間 $[a,b]$ で連続とする。$F(x)=\int_a^x f(t)\,dt$ とおくと $F$ は $(a,b)$ で微分可能で $F'(x)=f(x)$ である。さらに $F$ が $f$ の任意の原始関数ならば
\[
\int_a^b f(x)\,dx = F(b)-F(a)
\]
が成り立つ。

**Proof outline.** 積分の定義と平均値の定理を用いる。

---

### Proofs

#### Proof 1
**Proof.** $F$ の定義より
\[
\frac{F(x+h)-F(x)}{h} = \frac{1}{h}\int_x^{x+h} f(t)\,dt
\]
となる。$f$ の連続性と平均値の定理からこの極限は $f(x)$ に収束し，前半が示される。後半は原始関数の定義から従う。$\square$

---

#tags #theorem #proof
