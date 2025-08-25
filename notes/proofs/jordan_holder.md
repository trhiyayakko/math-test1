---
id: proof:jordan_holder
title: ジョルダン–ヘルダーの定理の証明
kind: proof
requires: [thm:jordan_holder, def:group, def:composition_series, def:simple_group]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Proof of** `[thm:jordan_holder]`:

$G$ の 2 つの合成列を
\[G=G_0 \trianglerighteq G_1 \trianglerighteq \cdots \trianglerighteq G_n=\{e\},\qquad
G=H_0 \trianglerighteq H_1 \trianglerighteq \cdots \trianglerighteq H_m=\{e\}
\]
とする。シュライアーの補題により，これらの合成列は共通の精密化をもち，各列の因子は互いに同型な単純群に対応する。したがって $n=m$ であり，$\{G_{i-1}/G_i\}$ と $\{H_{j-1}/H_j\}$ は順序を入れ替えれば互いに同型になる。$\square$

#tags #proof
