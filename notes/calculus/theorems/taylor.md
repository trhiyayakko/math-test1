---
id: thm:taylor
title: テイラーの定理
kind: theorem
requires: [def:taylor_polynomial, thm:mean_value]
status: draft
authors: [mathbot]
refs: []
tags: [calculus]
---

**Theorem.** 関数 $f$ が $[a,b]$ 上で $n+1$ 回微分可能とする。任意の $x\in[a,b]$ に対し，ある $\xi$ が $a$ と $x$ の間に存在して
\[
f(x)=P_n(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
\]
となる。ここで $P_n$ は $f$ の $a$ まわりの $n$ 次テイラー多項式である。

**Proof outline.** 平均値の定理を反復して剰余項を得る。

---

### Proofs

#### Proof 1
**Proof.** 関数
\[
R(x)=f(x)-P_n(x)
\]
を考えると $R(a)=R'(a)=\cdots=R^{(n)}(a)=0$ である。平均値の定理を $n+1$ 回適用すると，ある $\xi$ が $a$ と $x$ の間に存在して
\[
R(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
\]
が得られる。したがって定理の式が成立する。$\square$

---

#tags #theorem #proof
