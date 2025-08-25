---
id: proof:cayley
title: ケイリーの定理の証明
kind: proof
requires: [thm:cayley, def:group]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Proof of** `[thm:cayley]`:

各 $g\in G$ に対し左乗作用 $L_g:G\to G$, $L_g(x)=gx$ を考える。$L_g$ は全単射であり，写像
\[
\varphi:G\to S_G,\quad g\mapsto L_g
\]
は群準同型である。もし $\varphi(g)=\mathrm{id}$ ならば $gx=x$ が全ての $x$ について成り立つので $g=e$ である。よって $\varphi$ は単射であり，像は $S_G$ の部分群である。従って $G$ は $S_G$ の部分群と同型である。$\square$

#tags #proof
