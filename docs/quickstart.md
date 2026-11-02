# Quickstart

decoupler infers enrichment scores from omics data and a prior-knowledge network of sources (e.g. transcription factors or pathways) and their target features.
The example below scores five sources in a toy dataset with a univariate linear model and ranks them by group.

```python
import decoupler as dc
import scanpy as sc

adata, net = dc.ds.toy()

dc.mt.ulm(data=adata, net=net, tmin=3)
scores = dc.pp.get_obsm(adata, key="score_ulm")

sc.pl.matrixplot(scores, var_names=scores.var_names, groupby="group", cmap="RdBu_r")
markers = dc.tl.rankby_group(scores, groupby="group")
```

`dc.mt.show()` lists every enrichment method, and `dc.op` loads networks from OmniPath, e.g. CollecTRI for transcription factors.
The {doc}`notebooks/index` cover single-cell, spatial and bulk data, and {doc}`api/index` lists every function.
