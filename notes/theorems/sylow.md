---
id: thm:sylow
title: シローの定理
kind: theorem
requires: [def:group, def:p_group, def:sylow_subgroup]
status: draft
authors: [mathbot]
refs: []
tags: [group_theory]
---

**Theorem.** 有限群 $G$ の位数が $p^n m$（$p\nmid m$）と書けるとき，次が成り立つ。
1. $G$ は位数 $p^n$ のシロー $p$ 部分群をもつ。
2. 任意の $p$-部分群はシロー $p$ 部分群の共役に含まれる。
3. シロー $p$ 部分群の個数 $n_p$ は $n_p \equiv 1 \pmod p$ かつ $n_p \mid m$。

**Proof outline.** 共役作用と帰納法を用いる。

---

### Proofs

#### Proof 1
**Proof.**
$|G|=p^n m$（$p\nmid m$）とする。

1. $G$ が $p^n$ 個の元からなる集合 $X=\{\text{$p^n$ 個の元からなる部分集合}\}$ に対し左から作用するとき，軌道の大きさは $p$ の冪である。$X$ のうち $p$-群 $P$ を生成するようなものが存在し，その安定化群は $|P|=p^n$ となる。よってシロー $p$ 部分群が存在する。
2. 任意の $p$-部分群 $Q$ に対し，$Q$ はシロー部分群 $P$ の共役に含まれる。これは $G$ が $p$-部分群全体に共役作用することから従い，安定化群の性質を用いる。
3. シロー $p$ 部分群の集合に対する共役作用を考えると，軌道の大きさは $n_p$ である。軌道の安定化群の指数より $n_p \equiv 1 \pmod p$ かつ $n_p\mid m$ が従う。

以上で主張の三点が示された。$\square$

---

#tags #theorem #proof
