# Most influential programming language papers

Inspired by [Ryan Marcus's blog post](https://rmarcus.info/blog/2023/07/25/papers.html) that explores what are the most influential papers in the field of databases, I wanted to explore the most influential papers in PL. Following Ryan's approach, this post explores the PageRank score of a PL paper in the citation graph.

The data is collected from DBLP's awesome [knowledge graph](https://sparql.dblp.org), which has integrated citation graphs from [OpenCitations](https://opencitations.net/), and only includes papers at POPL, PLDI, ICFP, and OOPSLA and citations among these papers. I then use the [NetworkX](https://networkx.org/) package for calculating the PageRank. For someone who seldom does data processing or program in Python like me, the work is fairly lightweight thanks to the help from Copilot.

Some disclaimers: All rankings are necessarily subjective, and this ranking is no exception. The inclusion of only papers from POPL/PLDI/ICFP/OOPSLA means some of the greatest PL papers are missed. I also don't know if I'm doing the calculation right.

The raw data is in the `*.csv` files.

Other lists

- [Great Works in Programming Languages](https://www.cis.upenn.edu/~bcpierce/courses/670Fall04/GreatWorksInPL.shtml)

## Most influential papers of all time

|   rank | paper                                                                                                                                                              |   year |       score |
|-------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------:|------------:|
|      1 | **Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints.** Radhia Cousot, Patrick Cousot. |   1977 | 0.00342997  |
|      2 | **Efficient Implementation of the Smalltalk-80 System.** Allan M. Schiffman, L. Peter Deutsch.                                                                     |   1984 | 0.0017812   |
|      3 | **Principal Type-Schemes for Functional Programs.** Luís Damas, Robin Milner.                                                                                      |   1982 | 0.00161426  |
|      4 | **Proof-Carrying Code.** George C. Necula.                                                                                                                         |   1997 | 0.00156085  |
|      5 | **The DaCapo benchmarks: java benchmarking development and analysis.** Antony L. Hosking, Asjad M. Khan, Maria Jump, Rotem Bentzur, et al.                         |   2006 | 0.00140245  |
|      6 | **Automatic Predicate Abstraction of C Programs.** Thomas Ball, Rupak Majumdar, Sriram K. Rajamani, Todd D. Millstein.                                             |   2001 | 0.0013983   |
|      7 | **QuickCheck: a lightweight tool for random testing of Haskell programs.** Koen Claessen, John Hughes.                                                             |   2000 | 0.00136171  |
|      8 | **Automatic Discovery of Linear Restraints Among Variables of a Program.** Nicolas Halbwachs, Patrick Cousot.                                                      |   1978 | 0.00135758  |
|      9 | **The Java memory model.** Jeremy Manson, Sarita V. Adve, William W. Pugh.                                                                                         |   2005 | 0.00133448  |
|     10 | **Precise Interprocedural Dataflow Analysis via Graph Reachability.** Thomas W. Reps, Shmuel Sagiv, Susan Horwitz.                                                 |   1995 | 0.00131033  |
|     11 | **The Essence of Compiling with Continuations.** Cormac Flanagan, Amr Sabry, Bruce F. Duba, Matthias Felleisen.                                                    |   1993 | 0.00128836  |
|     12 | **Lava: Hardware Design in Haskell.** Per Bjesse, Satnam Singh, Mary Sheeran, Koen Claessen.                                                                       |   1998 | 0.00125842  |
|     13 | **How to Make ad-hoc Polymorphism Less ad-hoc.** Philip Wadler, Stephen Blott.                                                                                     |   1989 | 0.00124247  |
|     14 | **DART: directed automated random testing.** Nils Klarlund, Patrice Godefroid, Koushik Sen.                                                                        |   2005 | 0.00123709  |
|     15 | **Extended Static Checking for Java.** Mark Lillibridge, Cormac Flanagan, K. Rustan M. Leino, James B. Saxe, et al.                                                |   2002 | 0.00123161  |
|     16 | **Functional Reactive Animation.** Conal Elliott, Paul Hudak.                                                                                                      |   1997 | 0.00115399  |
|     17 | **Self: The Power of Simplicity.** David M. Ungar, Randall B. Smith.                                                                                               |   1987 | 0.00114871  |
|     18 | **Using Prototypical Objects to Implement Shared Behavior in Object Oriented Systems.** Henry Lieberman.                                                           |   1986 | 0.00107024  |
|     19 | **Dependent Types in Practical Programming.** Hongwei Xi, Frank Pfenning.                                                                                          |   1999 | 0.00106245  |
|     20 | **Enforcing High-Level Protocols in Low-Level Software.** Robert DeLine, Manuel Fähndrich.                                                                         |   2001 | 0.00105685  |
|     21 | **Language support for lightweight transactions.** Tim Harris, Keir Fraser.                                                                                        |   2003 | 0.00105447  |
|     22 | **Automating string processing in spreadsheets using input-output examples.** Sumit Gulwani.                                                                       |   2011 | 0.00105322  |
|     23 | **CommonLoops: Merging Lisp and Object-Oriented Programming.** Mark Stefik, Kenneth M. Kahn, Larry Masinter, Gregor Kiczales, et al.                               |   1986 | 0.0010497   |
|     24 | **The Implementation of the Cilk-5 Multithreaded Language.** Keith H. Randall, Charles E. Leiserson, Matteo Frigo.                                                 |   1998 | 0.00104562  |
|     25 | **Points-to Analysis in Almost Linear Time.** Bjarne Steensgaard.                                                                                                  |   1996 | 0.00103218  |
|     26 | **Model Checking for Programming Languages using Verisoft.** Patrice Godefroid.                                                                                    |   1997 | 0.00102663  |
|     27 | **Systematic Design of Program Analysis Frameworks.** Radhia Cousot, Patrick Cousot.                                                                               |   1979 | 0.00102626  |
|     28 | **Realistic Compilation by Program Transformation.** Paul Hudak, Richard Kelsey.                                                                                   |   1989 | 0.00101166  |
|     29 | **Lazy abstraction.** Ranjit Jhala, Thomas A. Henzinger, Rupak Majumdar, Grégoire Sutre.                                                                           |   2002 | 0.00100401  |
|     30 | **A Data Locality Optimizing Algorithm.** Michael E. Wolf, Monica S. Lam.                                                                                          |   1991 | 0.000994261 |

## Most influential papers of the last decade (2010-2019)

|   rank | paper                                                                                                                                                                                                       |   year |       score |
|-------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------:|------------:|
|      1 | **Automating string processing in spreadsheets using input-output examples.** Sumit Gulwani.                                                                                                                |   2011 | 0.00105322  |
|      2 | **Finding and understanding bugs in C compilers.** Xuejun Yang, Yang Chen, Eric Eide, John Regehr.                                                                                                          |   2011 | 0.000971975 |
|      3 | **Mathematizing C++ concurrency.** Mark Batty, Susmit Sarkar, Tjark Weber, Scott Owens, et al.                                                                                                              |   2011 | 0.000837997 |
|      4 | **From program verification to program synthesis.** Jeffrey S. Foster, Sumit Gulwani, Saurabh Srivastava.                                                                                                   |   2010 | 0.000730589 |
|      5 | **Synthesizing data structure transformations from input-output examples.** John K. Feser, Swarat Chaudhuri, Isil Dillig.                                                                                   |   2015 | 0.000600567 |
|      6 | **Iris: Monoids and Invariants as an Orthogonal Basis for Concurrent Reasoning.** Filip Sieczkowski, Derek Dreyer, David Swasey, Ralf Jung, et al.                                                          |   2015 | 0.00058064  |
|      7 | **Replicated data types: specification, verification, optimality.** Alexey Gotsman, Hongseok Yang, Marek Zawirski, Sebastian Burckhardt.                                                                    |   2014 | 0.000577928 |
|      8 | **Verdi: a framework for implementing and formally verifying distributed systems.** James R. Wilcox, Doug Woos, Thomas E. Anderson, Xi Wang, et al.                                                         |   2015 | 0.000571382 |
|      9 | **Halide: a language and compiler for optimizing parallelism, locality, and recomputation in image processing pipelines.** Jonathan Ragan-Kelley, Sylvain Paris, Frédo Durand, Saman P. Amarasinghe, et al. |   2013 | 0.000564648 |
|     10 | **Understanding POWER multiprocessors.** Susmit Sarkar, Luc Maranget, Jade Alglave, Derek Williams, et al.                                                                                                  |   2011 | 0.000533082 |
|     11 | **Synthesis of loop-free programs.** Susmit Jha, Ashish Tiwari, Sumit Gulwani, Ramarathnam Venkatesan.                                                                                                      |   2011 | 0.00051459  |
|     12 | **Code completion with statistical language models.** Martin T. Vechev, Eran Yahav, Veselin Raychev.                                                                                                        |   2014 | 0.000498111 |
|     13 | **Quipper: a scalable quantum programming language.** Peter Selinger, Benoît Valiron, Alexander S. Green, Neil J. Ross, et al.                                                                              |   2013 | 0.000493401 |
|     14 | **Continuity analysis of programs.** Sumit Gulwani, Swarat Chaudhuri, Roberto Lublinerman.                                                                                                                  |   2010 | 0.000492084 |
|     15 | **FlashExtract: a framework for data extraction by examples.** Sumit Gulwani, Vu Le.                                                                                                                        |   2014 | 0.000490351 |
|     16 | **A lightweight symbolic virtual machine for solver-aided host languages.** Emina Torlak, Rastislav Bodík.                                                                                                  |   2014 | 0.000470568 |
|     17 | **Distance makes the types grow stronger: a calculus for differential privacy.** Benjamin C. Pierce, Jason Reed.                                                                                            |   2010 | 0.000452448 |
|     18 | **NetkAT: semantic foundations for networks.** Jean-Baptiste Jeannin, Dexter Kozen, David Walker, Cole Schlesinger, et al.                                                                                  |   2014 | 0.000441762 |
|     19 | **Refinement types for Haskell.** Niki Vazou, Eric L. Seidel, Dimitrios Vytiniotis, Simon L. Peyton Jones, et al.                                                                                           |   2014 | 0.000440562 |
|     20 | **Mostly-automated verification of low-level programs in computational separation logic.** Adam Chlipala.                                                                                                   |   2011 | 0.000438855 |
|     21 | **FlashMeta: a framework for inductive program synthesis.** Sumit Gulwani, Oleksandr Polozov.                                                                                                               |   2015 | 0.000435989 |
|     22 | **Type-and-example-directed program synthesis.** Steve Zdancewic, Peter-Michael Osera.                                                                                                                      |   2015 | 0.000431928 |
|     23 | **An executable formal semantics of C with applications.** Grigore Rosu, Chucky Ellison.                                                                                                                    |   2012 | 0.000424127 |
|     24 | **An abstract domain for certifying neural networks.** Martin T. Vechev, Markus Püschel, Gagandeep Singh, Timon Gehr.                                                                                       |   2019 | 0.000424124 |
|     25 | **Test-case reduction for C compiler bugs.** Eric Eide, John Regehr, Yang Chen, Chucky Ellison, et al.                                                                                                      |   2012 | 0.000423168 |
|     26 | **RustBelt: securing the foundations of the rust programming language.** Robbert Krebbers, Ralf Jung, Derek Dreyer, Jacques-Henri Jourdan.                                                                  |   2018 | 0.000418011 |
|     27 | **Secure distributed programming with value-dependent types.** Juan Chen, Pierre-Yves Strub, Cédric Fournet, Jean Yang, et al.                                                                              |   2011 | 0.000409424 |
|     28 | **Program synthesis from polymorphic refinement types.** Armando Solar-Lezama, Ivan Kuraj, Nadia Polikarpova.                                                                                               |   2016 | 0.000408485 |
|     29 | **Compiler validation via equivalence modulo inputs.** Vu Le, Zhendong Su, Mehrdad Afshari.                                                                                                                 |   2014 | 0.000406365 |
|     30 | **Frenetic: a network programming language.** Michael J. Freedman, David Walker, Alec Story, Rob Harrison, et al.                                                                                           |   2011 | 0.000406272 |

## Most influential authors

|   rank | name                  |      score |
|-------:|:----------------------|-----------:|
|      1 | Philip Wadler         | 0.00512011 |
|      2 | Sumit Gulwani         | 0.00462223 |
|      3 | Simon L. Peyton Jones | 0.0045637  |
|      4 | Matthias Felleisen    | 0.00441081 |
|      5 | Alex Aiken            | 0.00412043 |
|      6 | Cormac Flanagan       | 0.00407936 |
|      7 | Patrick Cousot        | 0.00390093 |
|      8 | Xavier Leroy          | 0.00386847 |
|      9 | Martin C. Rinard      | 0.00382284 |
|     10 | George C. Necula      | 0.00356125 |
|     11 | Adam Chlipala         | 0.00335555 |
|     12 | Benjamin C. Pierce    | 0.00326097 |
|     13 | Robert Harper         | 0.00317152 |
|     14 | Rastislav Bodík       | 0.00300441 |
|     15 | Thomas W. Reps        | 0.00293058 |
|     16 | Derek Dreyer          | 0.00291501 |
|     17 | Hans-Juergen Boehm    | 0.0028994  |
|     18 | Radhia Cousot         | 0.00286249 |
|     19 | Monica S. Lam         | 0.00280135 |
|     20 | David M. Ungar        | 0.0025668  |
|     21 | Zhong Shao            | 0.00256337 |
|     22 | Martin Odersky        | 0.0025215  |
|     23 | Patrice Godefroid     | 0.00251659 |
|     24 | Martin T. Vechev      | 0.00249168 |
|     25 | Frank Pfenning        | 0.00246236 |
|     26 | Stephanie Weirich     | 0.00243712 |
|     27 | Matthew Flatt         | 0.00239113 |
|     28 | Craig Chambers        | 0.00237796 |
|     29 | Kathryn S. McKinley   | 0.00235087 |
|     30 | J. Gregory Morrisett  | 0.00233302 |
