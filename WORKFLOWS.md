# Workflows

## Markdown Lint / [lint.yml](.github/workflows/lint.yml)

This workflow uses the `markdownlint` CLI to lint markdown files.
It helps ensure that the markdown files adhere to a consistent style and format.

## LaTeX CV to PDF / [cv.yml](.github/workflows/cv.yml)

Original Repo: [onurravli/resume](https://github.com/onurravli/resume)

This workflow compiles LaTeX CV files to PDF using the `pdflatex` command.
It is triggered when a LaTeX file is modified,
and the resulting PDF is uploaded and committed back to the repository
as [cv/Mert_Sismanoglu_CV.pdf](./cv/Mert_Sismanoglu_CV.pdf).

## Sync Blog Posts / [sync.yml](.github/workflows/sync.yml)

This workflow syncs blog posts with an RSS feed
using the `feedparser` Python library.
It checks for new posts in the feed and updates the README.md in the repository.
