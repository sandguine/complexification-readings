# LaTeX companions

Two companions with notation tables, worked mathematics, claim status, and full version-specific citations. `references.bib` is shared. Private draft entries record verified metadata only; original files are not distributed.

Build from this directory with Tectonic (tested with 0.17.0):

```sh
tectonic 01-conceptual-companion.tex
tectonic 02-organizational-companion.tex
```

Alternatively, use `latexmk -pdf`. Both documents use `plainnat` and BibTeX. The first Tectonic build needs network access for TeX resources. Shell escape is not required.

Generated PDFs are stored in `output/pdf/`, outside routine Git tracking. The public reading repository deliberately includes these two authored PDFs and presentations. Downloaded papers, private drafts, and the meeting conversation are excluded.


Research revision 3 (18 November 2026) incorporates Hammond/Jørgensen, Lauffer, the public Ehrlich et al. feedback paper, and contrasting agency accounts. Page counts can change between revisions. The companions distinguish established source results, checked elementary illustrations, and unrun comparisons. Full source coverage appears in each companion and in the online reading guide.
