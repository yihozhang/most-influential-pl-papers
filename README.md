# Most influential programming language papers

Inspired by [Ryan Marcus's blog post](https://rmarcus.info/blog/2023/07/25/papers.html) that explores what are the most influential papers in the field of databases, I wanted to explore the most influential papers in PL. Following Ryan's approach, this post explores the PageRank score of a PL paper in the citation graph.

The data is collected from DBLP's awesome [knowledge graph](https://sparql.dblp.org), which has integrated citation graphs from [OpenCitations](https://opencitations.net/), and only includes papers at POPL, PLDI, ICFP, and OOPSLA and citations among these papers. I then use the [NetworkX](https://networkx.org/) package for calculating the PageRank. For someone who seldom does data processing or program in Python like me, the work is fairly lightweight thanks to the help from Copilot.

Some disclaimers: All rankings are necessarily subjective, and this ranking is no exception. The inclusion of only papers from POPL/PLDI/ICFP/OOPSLA means some of the greatest PL papers are missed. I also don't know if I'm doing the calculation right.

The raw data is in the `*.csv` files.

Other lists

- [Great Works in Programming Languages](https://www.cis.upenn.edu/~bcpierce/courses/670Fall04/GreatWorksInPL.shtml)

## Most influential papers of all time

|   rank | paper                                                                                                                           |   year |       score |
|-------:|:--------------------------------------------------------------------------------------------------------------------------------|-------:|------------:|
|      1 | Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints. |   1977 | 0.00342997  |
|        | Radhia Cousot, Patrick Cousot.                                                                                                  |        |             |
|      2 | Efficient Implementation of the Smalltalk-80 System.                                                                            |   1984 | 0.0017812   |
|        | Allan M. Schiffman, L. Peter Deutsch.                                                                                           |        |             |
|      3 | Principal Type-Schemes for Functional Programs.                                                                                 |   1982 | 0.00161426  |
|        | Luís Damas, Robin Milner.                                                                                                       |        |             |
|      4 | Proof-Carrying Code.                                                                                                            |   1997 | 0.00156085  |
|        | George C. Necula.                                                                                                               |        |             |
|      5 | The DaCapo benchmarks: java benchmarking development and analysis.                                                              |   2006 | 0.00140245  |
|        | Antony L. Hosking, Asjad M. Khan, Maria Jump, Rotem Bentzur, et al.                                                             |        |             |
|      6 | Automatic Predicate Abstraction of C Programs.                                                                                  |   2001 | 0.0013983   |
|        | Thomas Ball, Rupak Majumdar, Sriram K. Rajamani, Todd D. Millstein.                                                             |        |             |
|      7 | QuickCheck: a lightweight tool for random testing of Haskell programs.                                                          |   2000 | 0.00136171  |
|        | Koen Claessen, John Hughes.                                                                                                     |        |             |
|      8 | Automatic Discovery of Linear Restraints Among Variables of a Program.                                                          |   1978 | 0.00135758  |
|        | Nicolas Halbwachs, Patrick Cousot.                                                                                              |        |             |
|      9 | The Java memory model.                                                                                                          |   2005 | 0.00133448  |
|        | Jeremy Manson, Sarita V. Adve, William W. Pugh.                                                                                 |        |             |
|     10 | Precise Interprocedural Dataflow Analysis via Graph Reachability.                                                               |   1995 | 0.00131033  |
|        | Thomas W. Reps, Shmuel Sagiv, Susan Horwitz.                                                                                    |        |             |
|     11 | The Essence of Compiling with Continuations.                                                                                    |   1993 | 0.00128836  |
|        | Cormac Flanagan, Amr Sabry, Bruce F. Duba, Matthias Felleisen.                                                                  |        |             |
|     12 | Lava: Hardware Design in Haskell.                                                                                               |   1998 | 0.00125842  |
|        | Per Bjesse, Satnam Singh, Mary Sheeran, Koen Claessen.                                                                          |        |             |
|     13 | How to Make ad-hoc Polymorphism Less ad-hoc.                                                                                    |   1989 | 0.00124247  |
|        | Philip Wadler, Stephen Blott.                                                                                                   |        |             |
|     14 | DART: directed automated random testing.                                                                                        |   2005 | 0.00123709  |
|        | Nils Klarlund, Patrice Godefroid, Koushik Sen.                                                                                  |        |             |
|     15 | Extended Static Checking for Java.                                                                                              |   2002 | 0.00123161  |
|        | Mark Lillibridge, Cormac Flanagan, K. Rustan M. Leino, James B. Saxe, et al.                                                    |        |             |
|     16 | Functional Reactive Animation.                                                                                                  |   1997 | 0.00115399  |
|        | Conal Elliott, Paul Hudak.                                                                                                      |        |             |
|     17 | Self: The Power of Simplicity.                                                                                                  |   1987 | 0.00114871  |
|        | David M. Ungar, Randall B. Smith.                                                                                               |        |             |
|     18 | Using Prototypical Objects to Implement Shared Behavior in Object Oriented Systems.                                             |   1986 | 0.00107024  |
|        | Henry Lieberman.                                                                                                                |        |             |
|     19 | Dependent Types in Practical Programming.                                                                                       |   1999 | 0.00106245  |
|        | Hongwei Xi, Frank Pfenning.                                                                                                     |        |             |
|     20 | Enforcing High-Level Protocols in Low-Level Software.                                                                           |   2001 | 0.00105685  |
|        | Robert DeLine, Manuel Fähndrich.                                                                                                |        |             |
|     21 | Language support for lightweight transactions.                                                                                  |   2003 | 0.00105447  |
|        | Tim Harris, Keir Fraser.                                                                                                        |        |             |
|     22 | Automating string processing in spreadsheets using input-output examples.                                                       |   2011 | 0.00105322  |
|        | Sumit Gulwani.                                                                                                                  |        |             |
|     23 | CommonLoops: Merging Lisp and Object-Oriented Programming.                                                                      |   1986 | 0.0010497   |
|        | Mark Stefik, Kenneth M. Kahn, Larry Masinter, Gregor Kiczales, et al.                                                           |        |             |
|     24 | The Implementation of the Cilk-5 Multithreaded Language.                                                                        |   1998 | 0.00104562  |
|        | Keith H. Randall, Charles E. Leiserson, Matteo Frigo.                                                                           |        |             |
|     25 | Points-to Analysis in Almost Linear Time.                                                                                       |   1996 | 0.00103218  |
|        | Bjarne Steensgaard.                                                                                                             |        |             |
|     26 | Model Checking for Programming Languages using Verisoft.                                                                        |   1997 | 0.00102663  |
|        | Patrice Godefroid.                                                                                                              |        |             |
|     27 | Systematic Design of Program Analysis Frameworks.                                                                               |   1979 | 0.00102626  |
|        | Radhia Cousot, Patrick Cousot.                                                                                                  |        |             |
|     28 | Realistic Compilation by Program Transformation.                                                                                |   1989 | 0.00101166  |
|        | Paul Hudak, Richard Kelsey.                                                                                                     |        |             |
|     29 | Lazy abstraction.                                                                                                               |   2002 | 0.00100401  |
|        | Ranjit Jhala, Thomas A. Henzinger, Rupak Majumdar, Grégoire Sutre.                                                              |        |             |
|     30 | A Data Locality Optimizing Algorithm.                                                                                           |   1991 | 0.000994261 |
|        | Michael E. Wolf, Monica S. Lam.                                                                                                 |        |             |

## Most influential papers of the last decade (2010-2019)

|   rank | paper                                                                                                                  |   year |       score |
|-------:|:-----------------------------------------------------------------------------------------------------------------------|-------:|------------:|
|      1 | Automating string processing in spreadsheets using input-output examples.                                              |   2011 | 0.00105322  |
|        | Sumit Gulwani.                                                                                                         |        |             |
|      2 | Finding and understanding bugs in C compilers.                                                                         |   2011 | 0.000971975 |
|        | Xuejun Yang, Yang Chen, Eric Eide, John Regehr.                                                                        |        |             |
|      3 | Mathematizing C++ concurrency.                                                                                         |   2011 | 0.000837997 |
|        | Mark Batty, Susmit Sarkar, Tjark Weber, Scott Owens, et al.                                                            |        |             |
|      4 | From program verification to program synthesis.                                                                        |   2010 | 0.000730589 |
|        | Jeffrey S. Foster, Sumit Gulwani, Saurabh Srivastava.                                                                  |        |             |
|      5 | Synthesizing data structure transformations from input-output examples.                                                |   2015 | 0.000600567 |
|        | John K. Feser, Swarat Chaudhuri, Isil Dillig.                                                                          |        |             |
|      6 | Iris: Monoids and Invariants as an Orthogonal Basis for Concurrent Reasoning.                                          |   2015 | 0.00058064  |
|        | Filip Sieczkowski, Derek Dreyer, David Swasey, Ralf Jung, et al.                                                       |        |             |
|      7 | Replicated data types: specification, verification, optimality.                                                        |   2014 | 0.000577928 |
|        | Alexey Gotsman, Hongseok Yang, Marek Zawirski, Sebastian Burckhardt.                                                   |        |             |
|      8 | Verdi: a framework for implementing and formally verifying distributed systems.                                        |   2015 | 0.000571382 |
|        | James R. Wilcox, Doug Woos, Thomas E. Anderson, Xi Wang, et al.                                                        |        |             |
|      9 | Halide: a language and compiler for optimizing parallelism, locality, and recomputation in image processing pipelines. |   2013 | 0.000564648 |
|        | Jonathan Ragan-Kelley, Sylvain Paris, Frédo Durand, Saman P. Amarasinghe, et al.                                       |        |             |
|     10 | Understanding POWER multiprocessors.                                                                                   |   2011 | 0.000533082 |
|        | Susmit Sarkar, Luc Maranget, Jade Alglave, Derek Williams, et al.                                                      |        |             |
|     11 | Synthesis of loop-free programs.                                                                                       |   2011 | 0.00051459  |
|        | Susmit Jha, Ashish Tiwari, Sumit Gulwani, Ramarathnam Venkatesan.                                                      |        |             |
|     12 | Code completion with statistical language models.                                                                      |   2014 | 0.000498111 |
|        | Martin T. Vechev, Eran Yahav, Veselin Raychev.                                                                         |        |             |
|     13 | Quipper: a scalable quantum programming language.                                                                      |   2013 | 0.000493401 |
|        | Peter Selinger, Benoît Valiron, Alexander S. Green, Neil J. Ross, et al.                                               |        |             |
|     14 | Continuity analysis of programs.                                                                                       |   2010 | 0.000492084 |
|        | Sumit Gulwani, Swarat Chaudhuri, Roberto Lublinerman.                                                                  |        |             |
|     15 | FlashExtract: a framework for data extraction by examples.                                                             |   2014 | 0.000490351 |
|        | Sumit Gulwani, Vu Le.                                                                                                  |        |             |
|     16 | A lightweight symbolic virtual machine for solver-aided host languages.                                                |   2014 | 0.000470568 |
|        | Emina Torlak, Rastislav Bodík.                                                                                         |        |             |
|     17 | Distance makes the types grow stronger: a calculus for differential privacy.                                           |   2010 | 0.000452448 |
|        | Benjamin C. Pierce, Jason Reed.                                                                                        |        |             |
|     18 | NetkAT: semantic foundations for networks.                                                                             |   2014 | 0.000441762 |
|        | Jean-Baptiste Jeannin, Dexter Kozen, David Walker, Cole Schlesinger, et al.                                            |        |             |
|     19 | Refinement types for Haskell.                                                                                          |   2014 | 0.000440562 |
|        | Niki Vazou, Eric L. Seidel, Dimitrios Vytiniotis, Simon L. Peyton Jones, et al.                                        |        |             |
|     20 | Mostly-automated verification of low-level programs in computational separation logic.                                 |   2011 | 0.000438855 |
|        | Adam Chlipala.                                                                                                         |        |             |
|     21 | FlashMeta: a framework for inductive program synthesis.                                                                |   2015 | 0.000435989 |
|        | Sumit Gulwani, Oleksandr Polozov.                                                                                      |        |             |
|     22 | Type-and-example-directed program synthesis.                                                                           |   2015 | 0.000431928 |
|        | Steve Zdancewic, Peter-Michael Osera.                                                                                  |        |             |
|     23 | An executable formal semantics of C with applications.                                                                 |   2012 | 0.000424127 |
|        | Grigore Rosu, Chucky Ellison.                                                                                          |        |             |
|     24 | An abstract domain for certifying neural networks.                                                                     |   2019 | 0.000424124 |
|        | Martin T. Vechev, Markus Püschel, Gagandeep Singh, Timon Gehr.                                                         |        |             |
|     25 | Test-case reduction for C compiler bugs.                                                                               |   2012 | 0.000423168 |
|        | Eric Eide, John Regehr, Yang Chen, Chucky Ellison, et al.                                                              |        |             |
|     26 | RustBelt: securing the foundations of the rust programming language.                                                   |   2018 | 0.000418011 |
|        | Robbert Krebbers, Ralf Jung, Derek Dreyer, Jacques-Henri Jourdan.                                                      |        |             |
|     27 | Secure distributed programming with value-dependent types.                                                             |   2011 | 0.000409424 |
|        | Juan Chen, Pierre-Yves Strub, Cédric Fournet, Jean Yang, et al.                                                        |        |             |
|     28 | Program synthesis from polymorphic refinement types.                                                                   |   2016 | 0.000408485 |
|        | Armando Solar-Lezama, Ivan Kuraj, Nadia Polikarpova.                                                                   |        |             |
|     29 | Compiler validation via equivalence modulo inputs.                                                                     |   2014 | 0.000406365 |
|        | Vu Le, Zhendong Su, Mehrdad Afshari.                                                                                   |        |             |
|     30 | Frenetic: a network programming language.                                                                              |   2011 | 0.000406272 |
|        | Michael J. Freedman, David Walker, Alec Story, Rob Harrison, et al.                                                    |        |             |

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
