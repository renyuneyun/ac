Title: My research
slug: research
Date: 2018-08-01
Modified: 2022-08-17

> [My information and CV]({filename}about_me.md) may also interest you.

# In EWADA

My current work mainly involves improving the privacy and empowering users of data use in the decentralised data architectures like [SoLiD](solidproject.org/). That mainly lies on the following topics:

1. How to securely and efficiently (collaboratively) use multiple users' data in a decentralised data architecture?

2. How to empower users and give them more control and understanding of their data use?
   
   1. What governance requirements the users and the applications would have?
   
   2. How to use a sensible a data Terms of Use framework to lower the user's recognition overhead?

3. How to properly facilitate users to use the the technologies we provided?

That also bridges back with my PhD work on modelling and reasoning of data-use policies in decentralised contexts, as described below.

# PhD work -- Governance rules modeling

Terms and Conditions widely exist, and are usually written in natural languages. However, people tend to ignore them because of the complexity or large volume. The situation is the same for scientific research, especially for research data.  
We seek to solve this problem by modeling these terms and conditions (aka. data governance rules) using a logic form understood by machines and humans.  
The rules will propagate along with the data, and be checked accordingly.

<!-- PELICAN_END_SUMMARY -->

The two main objectives are:

1. Model data governance rules (aka. Terms and Conditions, in the field of research data)
2. Present a reasoning system over data-flow information (e.g. provenance)

<img src="{static}/images/data-flow-to-rule-flow.png" width="700" />

[<img src="{static}/images/one-page-summary.jpg" width="700" />]({static}/pdfs/one-page-summary.pdf)

Our solution, Dr.Aid (Data Rule Aid), differs from other research in:

1. Dr.Aid supports *obligations*, unlike other research focusing on *access controls*
2. Dr.Aid deals with multi-input-multi-output (MIMO) processes in multi-staged graphs, unlike other research focusing on linear / pipeline-style processing or a central server
3. Dr.Aid can derive the data-use rules for the **output** data based on the processing, so reasoning for further users works automatically
4. Dr.Aid's language model builds on top of *attribute*, an abstract construct. It can be extended to support other semantics (e.g. prohibitions, etc), out side of the current implemented semantics (obligations), withouth modifying the main part of the language features.

See [5-page slides]({static}/pdfs/poster - slides.pdf) for a summary on the current research results.

See the [doc archives](/category/docs) for more documents / papers describing my work.
