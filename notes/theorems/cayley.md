---
id: thm:cayley
title: ケイリーの定理
kind: theorem
requires: [def:group]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Theorem.** 任意の群 $G$ は集合 $G$ 上の対称群 $S_G$ の部分群と同型である。

**Proof outline.** 左乗作用による単射準同型 $G\to S_G$ を用いる。

---

### Proofs

#### Proof 1
**Proof.**
各 $g\in G$ に対し左乗作用 $L_g:G\to G$, $L_g(x)=gx$ を考える。$L_g$ は全単射であり，写像
\[
\varphi:G\to S_G,\quad g\mapsto L_g
\]
は群準同型である。もし $\varphi(g)=\mathrm{id}$ ならば $gx=x$ が全ての $x$ について成り立つので $g=e$ である。よって $\varphi$ は単射であり，像は $S_G$ の部分群である。従って $G$ は $S_G$ の部分群と同型である。$\square$

---

#tags #theorem #proof
