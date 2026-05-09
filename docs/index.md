---
hide:
  - navigation
---
!!! warning "This page is still under construction"

## About

This is a library for free math education, it includes material from a bunch of courses given in all the major israeli universities.

This project is created by [MkDocs](https://www.mkdocs.org/) and uses the [Material for MkDocs theme](https://squidfunk.github.io/mkdocs-material/), all the documentation from there can be applied for this project.

### Contributing

If you want to contribute to this project and help math be as accessible as possible you can do so by creating a **pull request** on any of the pages in the project (and even create your own!), or you can open a [new issue on the github page of this project](https://github.com/yeahBOYYYYY/math-library/issues).

To contribute directly you need to clone the project using,

```bash
git clone https://github.com/yeahBOYYYYY/math-library/
```

From that alone you now can now create new `.md` files under the folder `docs/` to be displayed in the site, but note that you won't be able to locally view your changes.

#### Setting Up the Project Locally

For starters you need to have `Python 3.x` installed on your machine since all the libraries involved in the project are downloaded with `pip`.

After setting up python, you need to install `MkDocs` and the `Material` theme using,

```bash
pip install mkdocs
pip install mkdocs-material
```

Then you'll need to install the plugins used to deploy this site,

```bash
pip install mkdocs-git-authors-plugin
pip install mkdocs-git-revision-date-localized-plugin
```

Now you can run the project locally by running the following command from the folder with the `mkdocs.yml` file,

```bash
mkdocs serve
```

This will open a new **local** server on your machine (default is port 8000), and will show in the console the URL for the local site, like so,

```
INFO    -  [16:32:38] Serving on http://127.0.0.1:8000/math-library/
```

And from now on all the changes you make locally will show up **live** at this URL.

#### Syntax

The structure of this site allows for either `.md` file types or `.html` to be viewed, but be aware that all `html` code will be displayed as is in the final site while `markdown` will be parsed by `Python-Markdown`.

##### Admonitions

While `Python-Markdown` supports the full GitHub Markdown flavour, it also provides extra functionality, the main one being "admonitions",

```
!!! quote "This is an admonition"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

    ??? tip "This is a nested opening admonition"

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.
```

And visually,

!!! quote "This is an admonition"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

    ??? tip "This is a nested opening admonition"

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

For extended documentation on this feature visit the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/reference/admonitions/?h=#custom-admonitions-docsstylesheetsextracss).

##### Custom Admonitions

This project defines extra admonitions for math use, in LaTex you can use environments like "Proof" or "Example", but this doesn't have a markdown counterpart, hence we use admonitions to display those environments.

###### Definition

This uses the "def" keyword,

!!! def "_Definition_: This is a definition block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

###### Theorem

This uses the "thm" keyword,

!!! thm "_Theorem_: This is a theorem block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

To give extensive information about a "Theorem", "Lemma" or "Claim" we use the following syntax for the title,

```
_Theorem_ [ < list of last names and year of authors > ]: < name of the theorem >
```

For example,

!!! thm "_Theorem_ [Jones-Brown 2025, Smith 2026]: Three Broomstick Theorem"

And hyperlinks to give the authors contribution are encouraged!

###### Lemma

This uses the "lemma" keyword,

!!! lemma "_Lemma_: This is a lemma block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

###### Claim

This uses the "claim" keyword,

!!! claim "_Claim_: This is a claim block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

###### Proof

This uses the "proof" keyword,

!!! proof "_Proof_: This is a definition block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

Note that proofs **should** (by convention) be enclosed in another admonitions, like "Theorem", "Lemma" or "Claim", as follows,

!!! claim "_Claim_: This is an enclosing claim block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

	??? proof

		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

###### Example

This uses the "mexample" keyword,

!!! mexample "_Example_: This is a example block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

###### Note

This uses the "mnote" keyword,

!!! mnote "_Note_: This is a note block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

###### Exercise

This uses the "exercise" keyword,

!!! exercise "_Exercise_: This is a exercise block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

###### Solution

This uses the "solution" keyword,

???+ solution "_Solution_: This is a solution block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

Note that solutions **should** (by convention) be enclosed in another admonitions, like "Exercise", as follows,

???+ exercise "_Exercise_: This is an enclosing exercise block"

	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

	??? solution

		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

## License

The license of this project is [Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/deed.en), it allows anyone to use this freely unless they're trying to monotize the information in this site (for more information click on the link given).
