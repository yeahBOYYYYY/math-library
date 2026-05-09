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

    We'll formalize the sentence "Today is not Tuesday, today is Monday and tommorow will be Tuesday", to do that we will define three sentences,

    $$\begin{aligned}
    a & =\text{"Today is Tuesday"} & b & =\text{"Today is Monday"} & c & =\text{"Tommorow is Tuesday"}
    \end{aligned}$$

    Then our original sentence takes the following form, "(not $a$) and ($b$ and $c$)".

!!! def "_Definition_: Atomic Sentence"

    A self-contained sentence that can be either $\true$ or $\false$.

!!! mexample "_Example_"

    "It is raining outside" Is an atomic sentence because it can be $\true$ or $\false$ and is not composed of sub-sentences that can be $\true$ or $\false$.

#### Logical Connectives

Until now we talked about atomic sentence in mathematics but we still can't express complex sentences, for that we need connectives between atomic sentences.

!!! def "_Definition_: Negation Connective"

    Given a sentence $A$ we express "not $A$" symbolically as $\neg A$.

!!! def "_Definition_: Conjunction Connective"

    Given two sentences $A$ and $B$ we express "$A$ and $B$" symbolically as $A \land B$.

!!! def "_Definition_: Disjunction Connective"

    Given two sentences $A$ and $B$ we express "$A$ or $B$" symbolically as $A \lor B$.

!!! def "_Definition_: Implication Connective"

    Given two sentences $A$ and $B$ we express "if $A$ then $B$" symbolically as $A \implies B$, and we call $A$ the "**Prefix**" and $B$ the "**Suffix**" of the sentence.

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

!!! exercise "_Exercise_"

    Formalize and determine if the following sentence is true, false or not a sentence, "Today is Tuesday and Tomorrow will also be Tuesday".

!!! claim "_Claim_"

    Let $A_1, \ldots, A_n$ be atomic sentences then there are overall $2^n$ possible assignments of all the atomic sentences to truth values.

    ??? proof "_Proof_"

        Each atomic sentence $A_i$ can be assigned to either $\true$ or $\false$, therefore each $A_i$ has two options for it's assignment, and the atomic sentences don't have any connection between then (since they are atomic, and therefore the choice of their values is arbitrary). Hence overall there are

        $$\underbrace{2\cdot\ldots\cdot2}_{n}=2^{n}$$

        assignments of truth values to $A_1, \ldots, A_n$.

Now because we know that there are only finite number of assignments possible for a collection of atomic sentences, we can create a table that summarizes the truthfulness of each logical connective!
