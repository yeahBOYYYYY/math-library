!!! warning "This page is still under construction"

## Logic

Mathematical logic is a branch of mathematics that deals with the expression of simple and complex mathematical statements. It allows for the removal of the multiplicity of meanings that exists in human languages by establishing precise rules for presenting different statements in a way that can be understood in only one way. Logic also deals with systems of rules for drawing valid conclusions from data or assumptions in our possession.

!!! mexample "_Example_: Uncertainty in Language"

    When you are in a restaurant and ask for a Coke, the waitress asks, "Would you like regular *or* zero?" Of course, the word *or* in this case refers to the choice between one of the two and not both, on the other hand, when asked, "Are you hungry *or* thirsty?" You can mean either one of the two or perhaps both at the same time, meaning that the word *or* has a double meaning depending on the context.

Logic began its journey in ancient Greece as a branch of philosophy, but following many significant developments in its formal directions, it is now also considered a branch of mathematics. Logic serves as the central theoretical basis for computer science. It is necessary, for example, when we want to "talk" to a machine (such as a computer), because communication with a computer must be very precise and unambiguous, and must comply with predetermined logical rules. Developing logical thinking is also necessary for dealing with various and diverse problems, especially in the fields of science and technology, which require precise and orderly analysis of processes and ideas. In addition, the ability to justify arguments accurately while avoiding logical fallacies that would harm the validity of conclusions is a central tool in mathematics and computer science.

!!! mnote "_Note_: Base Assumptions"

    All logic in this chapter is based on a system of axioms called $\mathrm{ZF}$, beyond this chapter we will always use the axiom system $\mathrm{ZFC}$ (we assume the axiom of choice in this course).

### Propositional logic

!!! def "_Definition_: Formalization"

    The transformation of a literal verse into a language of mathematical forms.

!!! mexample "_Example_"

    We'll formalize the sentence "Today is not Tuesday, today is Monday and tomorrow will be Tuesday", to do that we will define three sentences,

    $$\begin{aligned}
    a & =\text{"Today is Tuesday"} & b & =\text{"Today is Monday"} & c & =\text{"Tomorrow is Tuesday"}
    \end{aligned}$$

    Then our original sentence takes the following form, "(not $a$) and ($b$ and $c$)".

!!! def "_Definition_: Atomic Sentence"

    A self-contained sentence that can be either $\true$ or $\false$.

!!! mexample "_Example_"

    "It is raining outside" Is an atomic sentence because it can be $\true$ or $\false$ and is not composed of sub-sentences that can be $\true$ or $\false$.

#### Logical Connectives

Until now we talked about atomic sentence in mathematics but we still can't express complex sentences, for that we need connectives between atomic sentences.

!!! def "_Definition_: Negation Connective"

    Given a sentence $A$ we express "not $A$" symbolically as "$\neg A$".

    ??? mnote "_Note_"

        It is also common to use the notation "$\sim A$" or "$\overline{A}$" for negation, but we will use only "$\neg A$".

!!! def "_Definition_: Conjunction Connective"

    Given two sentences $A$ and $B$ we express "$A$ and $B$" symbolically as "$A \land B$".

!!! def "_Definition_: Disjunction Connective"

    Given two sentences $A$ and $B$ we express "$A$ or $B$" symbolically as "$A \lor B$".

!!! def "_Definition_: Implication Connective"

    Given two sentences $A$ and $B$ we express "if $A$ then $B$" symbolically as "$A \implies B$", and we call $A$ the "**Prefix**" and $B$ the "**Suffix**" of the sentence.

##### Sentence

Now after defining the atomic sentences and the connectives we can define what a sentence is formally,

!!! def "_Definition_: Sentence"

    A claim that is composed by atomic sentences and connectives between them.

!!! mexample "_Example_"

    The phrase "Today is Tuesday" is a sentence, while "What is the time?", "Close the door!" and "1 + 1" are not.

!!! mexample "_Example_"

    Let $A$, $B$ and $C$ be atomic sentences, then the following phrases are also sentences,

    - $A \implies B$
    - $\left(A\lor B\right)\land\left(C\lor B\right)$
    - $\left(\left(A\lor B\right)\implies\neg A\right)\implies C$

!!! mnote "_Note_"

    Phrases of the form,

    - $A\implies$
    - $A\land\lor B$
    - $A\land B\implies C$
    - $A \neg$
    
    Which are phrases without mathematical meaning or with dual meaning are not considered as sentence in propositional logic, and such phrases are called "**abuse of notation**".

#### Values of Sentences

Now that we have sentences in our mathematical language we want to give them meaning, for that we have to talk about truth and falseness of sentences.

!!! def "_Definition_: Truth Assignment"

    Let $A$ be an atomic sentence, then we assign to $A$ a value of either $\true$ or $\false$. Moreover we'll use the notation $V\left(A\right)$ for the truth assignment of $A$.

!!! mnote "_Note_"

    In our logic system a sentence is either $\true$ or $\false$ but never both.

    And mathematically, for all atomic sentences $A$ the following holds,

    $$\left(\left(V\left(A\right)=\true\right)\land\left(V\left(A\right)\ne\false\right)\right)\lor\left(\left(V\left(A\right)=\false\right)\land\left(V\left(A\right)\ne\true\right)\right)$$

!!! mexample "_Example_"

    This are a few sentences and their truth assignments,

    - $V\left(1<3\right) = \true$
    - $V\left(1+ 1 = 3\right) = \false$
    - $V\left(\left(1+1=3\right)\implies\left(10-1=4\right)\right) = \true$

**TODO (explain false implication intuitively)** Wait but how is the third one got assigned to true? Well if we think it through with a simpler example ... This is actually a bigger phenomena in logic that we can note and formalize!

!!! mnote "_Note_: Falseness Implies All"

    Let $A$ and $B$ be atomic sentences then,

    $$\left(V\left(A\right) = \false\right) \implies \left(V\left(A \implies B\right) = \true\right)$$

???+ exercise "_Exercise_"

    Formalize and determine if the following sentence is true, false or not a sentence, "Today is Tuesday and Tomorrow will also be Tuesday".

    ??? solution

        We will define two sentences,

        $$\begin{aligned}
        A & =\text{"Today is Tuesday"} & B & =\text{"Tomorrow is Tuesday"}
        \end{aligned}$$

        Then our original sentence is $A \land B$, but we also note that only of them can be true by our understanding of the week days, hence we can that

        $$V\left(A\land B\right) = \false$$

!!! claim "_Claim_"

    Let $A_1, \ldots, A_n$ be atomic sentences then there are overall $2^n$ possible assignments of all the atomic sentences to truth values.

    ??? proof "_Proof_"

        Each atomic sentence $A_i$ can be assigned to either $\true$ or $\false$, therefore each $A_i$ has two options for it's assignment, and the atomic sentences don't have any connection between then (since they are atomic, and therefore the choice of their values is arbitrary). Hence overall there are

        $$\underbrace{2\cdot\ldots\cdot2}_{n}=2^{n}$$

        assignments of truth values to $A_1, \ldots, A_n$.

Now because we know that there are only finite number of assignments possible for a collection of atomic sentences, we can create a table that summarizes the truthfulness of each logical connective!

!!! def "_Definition_: Truth Table"

    A table that summarizes the truth value of a complex sentence given a change in the truth assignment of each of the atomic sentences that he's composed of.

!!! mexample "_Example_: Truth Tables For the Logical Connectives"

    Let $A$ and $B$ be atomic sentences then,

    ??? mexample "_Example_: Negation Connective"

        | $A$      | $\neg A$ |
        |----------|----------|
        | $\true$  | $\false$ |
        | $\false$ | $\true$  |
    
    ??? mexample "_Example_: Conjunction Connective"

        | $A$      | $B$      | $A\land B$ |
        |----------|----------|---------------|
        | $\true$  | $\true$  | $\true$       |
        | $\true$  | $\false$ | $\false$      |
        | $\false$ | $\true$  | $\false$      |
        | $\false$ | $\false$ | $\false$      |

    ??? mexample "_Example_: Disjunction Connective"

        | $A$      | $B$      | $A\lor B$ |
        |----------|----------|---------------|
        | $\true$  | $\true$  | $\true$       |
        | $\true$  | $\false$ | $\true$       |
        | $\false$ | $\true$  | $\true$       |
        | $\false$ | $\false$ | $\false$      |

    ??? mexample "_Example_: Implication Connective"

        | $A$      | $B$      | $A\implies B$ |
        |----------|----------|---------------|
        | $\true$  | $\true$  | $\true$       |
        | $\true$  | $\false$ | $\false$      |
        | $\false$ | $\true$  | $\true$       |
        | $\false$ | $\false$ | $\true$       |

???+ exercise "_Exercise_: Deducing From Truth Tables"

    Try to deduce the truth assignment from the following given data,

    1. Given that $A \lor \left(\neg B\right)$ is a false sentence, what can we deduce?
          1. $A$ is true, $B$ is true.
          2. $A$ is true, $B$ is false.
          3. $A$ can't be determined, $B$ is true.
          4. $A$ is false, $B$ is true.
          5. $A$ is false, $B$ can't be determined.
    2. Given that $A$ and $B$ are both false, what can we infer about $\left(A\implies B\right) \land \left(B\implies A\right)$?
          1. It's a true sentence.
          2. It's a false sentence.
          3. It can't be determined.

    ??? solution

        1. The solution is answer "**d**", by the truth table of the disjunction connective we know that for the result to be false both the sentenced being or-ed must be false themselves, hence $A$ is false, and $\neg B$ is false, then by the truth table of the negation connective we know that for $\neg B$ to be false it must follow that $B$ is true.
        2. The solution is answer "**a**". First of all we need to look at $A \implies B$ and $B \implies A$ separately to infer about the whole complex sentence, since we know that $A$ is false we know by the truth table of the implication connective that $A \implies B$ is true, likewise because $B$ is false we know by the truth table of the implication connective that $B \implies A$ is true. Now, we can see that by the truth table of the conjunction connective that $\left(A\implies B\right) \land \left(B\implies A\right)$ must be true.
