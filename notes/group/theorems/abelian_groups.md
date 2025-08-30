---
id: thm:abelian_groups
title: アーベル群の基本定理
kind: theorem
requires: [def:abelian_group, def:prime, def:order]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Theorem.** 有限アーベル群 $A$ は素数冪位数の巡回群の直積に同型である。

**Proof outline.** 不変因子分解または初等因子分解を用いる。

---

### Proofs

#### Proof 1
**Proof.**
有限アーベル群 $A$ の位数を $|A|=p_1^{n_1}\cdots p_r^{n_r}$ と素因数分解する。$A$ の $p_i$-冪位数部分群を $A_{p_i}$ とすると，$A\cong A_{p_1}\times\cdots\times A_{p_r}$ に分解できる。各 $A_{p_i}$ は有限 $p$-群なので，中心が非自明であり，巡回群の直積として表現できることを帰納法で示すと，$A$ は素数冪位数の巡回群の直積に同型となる。$\square$

---

#tags #theorem #proof
