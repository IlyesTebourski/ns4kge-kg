# Rapport-preuve — KGE Models (provenance : évalué vs mentionné)

Corpus : **55 articles**. Évalués validés vs `tables_only`, mentionnés vs `no_tables` (prose). Matching déterministe.

## Scores

| Score | Valeur |
|---|---|
| Précision évalués | **94.5%** |
| Précision mentionnés | **97.9%** |
| Recall évalués (indicatif) | **89.5%** |
| Recall mentionnés (indicatif) | **95.5%** |
| Évalués vérifiés / mentionnés vérifiés | 344 / 238 |

## A. Preuve — modèles/méthodes ÉVALUÉS (344)

| Article | Entité | Trouvé | Extrait (tableau) |
|---|---|:---:|---|
| AdaptativeNS.md | ComplEx | oui | t}$</td> </tr> <tr> <td>ComplEx</td> <td>$Re(\mathbf{h}^T \text |
| AdaptativeNS.md | ConvE | oui | })$</td> </tr> <tr> <td>ConvE</td> <td>$f(vec(f([\mathbf{r}, |
| AdaptativeNS.md | DistMult | oui | t}$</td> </tr> <tr> <td>DistMult</td> <td>$\mathbf{h}^T \text{di |
| AdaptativeNS.md | MuRP | oui | ))$</td> </tr> <tr> <td>MuRp</td> <td>$-d_{\mathbb{B}}(exp_{ |
| AdaptativeNS.md | RotatE | oui | 2}$</td> </tr> <tr> <td>RotatE</td> <td>$\|\|\mathbf{h} \odot \m |
| AdaptativeNS.md | TransE | oui | d>-</td> </tr> <tr> <td>transE</td> <td>0.226</td> <td |
| ADNS.md | DistMult | oui | e 3. Evaluation of Negative Sampling on DistMult <table> <thead> <tr> <th> |
| ADNS.md | TransE | oui | 2.** Evaluation of Negative Sampling on TransE <table> <thead> <tr> <th> |
| ASA.md | ComplEx | oui | </thead> <tbody> <tr> <td>ComplEx</td> <td>53.18(10)</td> |
| ASA.md | ConvE | oui | (8)</td> </tr> <tr> <td>ConvE</td> <td>49.65(11)</td> |
| ASA.md | DistMult | oui | 10)</td> </tr> <tr> <td>DistMult</td> <td>53.94(9)</td> |
| ASA.md | GATNE | oui | (9)</td> </tr> <tr> <td>GATNE</td> <td><u>96.25</u>(5)</td> |
| ASA.md | HAN | oui | 11)</td> </tr> <tr> <td>HAN</td> <td>87.57(7)</td> |
| ASA.md | metapath2vec | oui | (5)</td> </tr> <tr> <td>metapath2vec</td> <td><u>94.15</u>(6)</td> |
| ASA.md | R-GCN | oui | (6)</td> </tr> <tr> <td>R-GCN</td> <td>97.16(4)</td> |
| ASA.md | RelGNN | oui | (3)</td> </tr> <tr> <td>RelGNN - ASA</td> <td>98.84(2)</td> |
| BatchNS.md | ComplEx | oui | gt;</td> </tr> <tr> <td>ComplEx</td> <td>x ⊙ θᵣ</td> <t |
| BatchNS.md | DeepWalk | oui | </thead> <tbody> <tr> <td>DeepWalk*</td> <td>0.691</td> <t |
| BatchNS.md | HolE | oui | 749</td> </tr> <tr> <td>HolE (Nickel et al., 2016b)</td> <td |
| BatchNS.md | MILE (1 level) | oui | GB</td> </tr> <tr> <td>MILE (1 level)*</td> <td>0.629</td> < |
| BatchNS.md | MILE (5 levels) | oui | GB</td> </tr> <tr> <td>MILE (5 levels)*</td> <td>0.505</td> < |
| BatchNS.md | PBG | oui | GB</td> </tr> <tr> <td>PBG (1 partition)</td> <td>0.749</t |
| BatchNS.md | PBG (ComplEx) | oui | 785</td> </tr> <tr> <td>PBG (ComplEx)</td> <td>0.242</td> <t |
| BatchNS.md | PBG (TransE) | oui | 910</td> </tr> <tr> <td>PBG (TransE)</td> <td>0.265</td> <t |
| BatchNS.md | R-GCN+ | oui | 840</td> </tr> <tr> <td>R-GCN+ (Schlichtkrull et al., 2018)</td> |
| BatchNS.md | Reciprocal ComplEx-N3 | oui | 838</td> </tr> <tr> <td>Reciprocal ComplEx-N3 (Lacroix et al., 2018)</td> <td |
| BatchNS.md | RESCAL | oui | </thead> <tbody> <tr> <td>RESCAL</td> <td>Aᵣx</td> <td>& |
| BatchNS.md | StarSpace | oui | 842</td> </tr> <tr> <td>StarSpace (Wu et al., 2018)</td> <td>-</t |
| BatchNS.md | TransE | oui | gt;</td> </tr> <tr> <td>TransE</td> <td>x + θᵣ</td> <t |
| CAKE.md | HAKE | oui | ng></td> </tr> <tr> <td>HAKE</td> <td>34</td> <td>0. |
| CAKE.md | RotatE | oui | ng></td> </tr> <tr> <td>RotatE</td> <td>35</td> <td>0. |
| CAKE.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>35</td> <td>0. |
| CANS.md | CKRL | oui | 9.9</td> </tr> <tr> <td>CKRL(LT)</td> <td>230</td> < |
| CANS.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>249</td> <td>1 |
| CCS.md | Op-TransD | oui | 873</td> </tr> <tr> <td>Op-TransD</td> <td>3352</td> <td> |
| CCS.md | Op-TransE | oui | </thead> <tbody> <tr> <td>Op-TransE</td> <td>4171</td> <td> |
| CCS.md | Op-TransH | oui | 852</td> </tr> <tr> <td>Op-TransH</td> <td>4404</td> <td> |
| CCS.md | Op-TransR | oui | 815</td> </tr> <tr> <td>Op-TransR</td> <td>3685</td> <td> |
| CCS.md | TransD | oui | g functions for TransE, TransH, TransR, TransD. <table> <thead> <tr> <th |
| CCS.md | TransE | oui | 4. Definition of scoring functions for TransE, TransH, TransR, TransD. <table> <the |
| CCS.md | TransH | oui | nition of scoring functions for TransE, TransH, TransR, TransD. <table> <thead> |
| CCS.md | TransR | oui | f scoring functions for TransE, TransH, TransR, TransD. <table> <thead> <tr> |
| ConceptDriven.md | DistMult | oui | >81.4</td> <td>4.15</td> </tr> <tr> <td>DistMult [18]</td> <td>88.4</td> <td>86.1</td> < |
| ConceptDriven.md | DKRL | oui | d>44.5</td> <td>52.2</td> </tr><tr> <td>DKRL [16]</td> <td>26.0</td> <td>100.00</td> |
| ConceptDriven.md | RotatE | oui | d>43.2</td> <td>50.7</td> </tr><tr> <td>RotatE [17]</td> <td>47.6</td> <td>100.00</td> |
| ConceptDriven.md | TransE | oui | 0↑</th> </tr> </thead> <tbody> <tr> <td>TransE [3]</td> <td>24.3</td> <td>100.00</td> |
| ConceptDriven.md | TransH | oui | d>40.6</td> <td>47.6</td> </tr><tr> <td>TransH [14]</td> <td>23.1</td> <td>100.00</td> |
| ConceptDriven.md | TransR | oui | d>44.5</td> <td>52.2</td> </tr><tr> <td>TransR [15]</td> <td>23.2</td> <td>100.00</td> |
| CondConstraints.md | TransE | **NON** | — |
| dans.md | ComplEx | oui | RGCN) and decoders (DistMult, RotatE or ComplEx). The best results are in bold, and the |
| dans.md | DistMult | oui | the same backbone (RGCN) and decoders (DistMult, RotatE or ComplEx). The best results a |
| dans.md | RotatE | oui | backbone (RGCN) and decoders (DistMult, RotatE or ComplEx). The best results are in bo |
| DeMix.md | ComplEx | oui | ng></td> </tr> <tr> <td>ComplEx+Uniform</td> <td>0.429</td> |
| DeMix.md | DistMult | oui | </thead> <tbody> <tr> <td>DistMult+Uniform</td> <td>0.412</td> |
| DeMix.md | HAKE | oui | ng></td> </tr> <tr> <td>HAKE+Uniform<sup>Δ</sup></td> <td>0. |
| DeMix.md | RotatE | oui | </thead> <tbody> <tr> <td>RotatE+Uniform<sup>Δ</sup></td> <td>0. |
| DeMix.md | TransE | oui | les</td> </tr> <tr> <td>TransE+Uniform</td> <td>0.175*</td> |
| DHNS.md | AdaMF | oui | .88</td> </tr> <tr> <td>AdaMF</td> <td><u>32.51</u></td> |
| DHNS.md | ComplEx | oui | .80</td> </tr> <tr> <td>ComplEx</td> <td>27.48</td> <td |
| DHNS.md | DistMult | oui | .68</td> </tr> <tr> <td>DistMult</td> <td>23.03</td> <td |
| DHNS.md | GC-OTE | oui | .71</td> </tr> <tr> <td>GC-OTE</td> <td>31.85</td> <td |
| DHNS.md | IKRL | oui | wspan="8">MMKGC Models</td> <td>IKRL</td> <td>26.82</td> <td |
| DHNS.md | MMKRL | oui | .72</td> </tr> <tr> <td>MMKRL</td> <td>26.81</td> <td |
| DHNS.md | OTKGE | oui | .62</td> </tr> <tr> <td>OTKGE</td> <td>23.86</td> <td |
| DHNS.md | PairRE | oui | .73</td> </tr> <tr> <td>PairRE</td> <td>31.13</td> <td |
| DHNS.md | RotatE | oui | r framework DHNS</mark> integrated with RotatE model and some state-of-the-art baselin |
| DHNS.md | RSME | oui | .44</td> </tr> <tr> <td>RSME</td> <td>29.76</td> <td |
| DHNS.md | TBKGC | oui | .07</td> </tr> <tr> <td>TBKGC</td> <td>28.08</td> <td |
| DHNS.md | TransAE | oui | .58</td> </tr> <tr> <td>TransAE</td> <td>28.09</td> <td |
| DHNS.md | TransD | oui | .23</td> </tr> <tr> <td>TransD</td> <td>21.52</td> <td |
| DHNS.md | TransE | oui | 7">Unimodal KGC Models</td> <td>TransE</td> <td>24.86</td> <td |
| DHNS.md | VBKGC | oui | .83</td> </tr> <tr> <td>VBKGC</td> <td>30.61</td> <td |
| DMNS.md | ARVGA | oui | 005</td> </tr> <tr> <td>ARVGA</td> <td>.732 ± .011</td> |
| DMNS.md | GAT | oui | </thead> <tbody> <tr> <td>GAT</td> <td>.766 ± .006</td> |
| DMNS.md | GCN | oui | link prediction against baselines using GCN as the base encoder. <table> <thead> |
| DMNS.md | GraphGAN | oui | 004</td> </tr> <tr> <td>GraphGAN</td> <td>.739 ± .003</td> |
| DMNS.md | GVAE | oui | 003</td> </tr> <tr> <td>GVAE</td> <td><u>.783 ± .003</u></td |
| DMNS.md | KBGAN | oui | 009</td> </tr> <tr> <td>KBGAN</td> <td>.615 ± .004</td> |
| DMNS.md | SAGE | oui | ng></td> </tr> <tr> <td>SAGE</td> <td>.598 ± .014</td> |
| DMNS.md | ScaLed | oui | 001</td> </tr> <tr> <td>ScaLed</td> <td>.676 ± .004</td> |
| DMNS.md | SEAL | oui | 002</td> </tr> <tr> <td>SEAL</td> <td>.751 ± .007</td> |
| DNS.md | RESCAL | oui | parameters. RNS results for TransE and RESCAL are borrowed from Nickel et al. [2016b] |
| DNS.md | TransE | oui | its default parameters. RNS results for TransE and RESCAL are borrowed from Nickel et |
| DomainNS.md | CTransR | oui | 8.7</td> </tr> <tr> <td>CTransR (Lin et al., 2015b)</td> <td>No |
| DomainNS.md | DISTMULT | oui | 1.4</td> </tr> <tr> <td>DISTMULT (Yang et al., 2015)</td> <td>No |
| DomainNS.md | IRN | oui | 4.7</td> </tr> <tr> <td>IRN (Shen et al., 2016)</td> <td>Ex |
| DomainNS.md | ITransF | oui | </tr> <tr> <td><strong>ITransF</strong></td> <td>No</td> |
| DomainNS.md | NLFeat | oui | 4.6</td> </tr> <tr> <td>NLFeat (Toutanova and Chen, 2015)</td> |
| DomainNS.md | PTransE | oui | 6.2</td> </tr> <tr> <td>PTransE (Lin et al., 2015a)</td> <td>Pa |
| DomainNS.md | Random Walk | oui | 7.0</td> </tr> <tr> <td>Random Walk (Wei et al., 2016)</td> <td>Pat |
| DomainNS.md | RTransE | oui | ng></td> </tr> <tr> <td>RTransE (García-Durán et al., 2015)</td> |
| DomainNS.md | STransE | oui | the brackets are another set of results STransE reported. <table> <thead> <tr> |
| DomainNS.md | TATEC | oui | 7.3</td> </tr> <tr> <td>TATEC (García-Durán et al., 2016)</td> |
| DomainNS.md | TransD | oui | 4.0</td> </tr> <tr> <td>TransD (Ji et al., 2015)</td> <td>No</ |
| DomainNS.md | TransE | oui | 6.3</td> </tr> <tr> <td>TransE (Bordes et al., 2013)</td> <td> |
| DomainNS.md | TransH | oui | 7.1</td> </tr> <tr> <td>TransH (Wang et al., 2014)</td> <td>No |
| DomainNS.md | TransR | oui | 4.4</td> </tr> <tr> <td>TransR (Lin et al., 2015b)</td> <td>No |
| EANS.md | ComplEx | oui | </tr> <tr> <td rowspan="6">ComplEx<br/>(Trouillon et al., 2016)</td> |
| EANS.md | DistMult | oui | </tr> <tr> <td rowspan="7">DistMult<br/>(Yang et al., 2014)</td> <t |
| EANS.md | RotatE | oui | </tr> <tr> <td rowspan="5">RotatE<br/>(Sun et al., 2019)</td> <td |
| EANS.md | TransD | oui | </tr> <tr> <td rowspan="6">TransD<br/>(Ji et al., 2015)</td> <td> |
| EANS.md | TransE | oui | tbody> <tr> <td rowspan="7">TransE<br/>(Bordes et al., 2013)</td> |
| ERDNS.md | CompGCN (ConvE) | oui | </tr> <tr> <td rowspan="3">CompGCN (ConvE)</td> <td>unif</td> <td |
| ERDNS.md | CompGCN (DistMult) | oui | </tr> <tr> <td rowspan="3">CompGCN (DistMult)</td> <td>unif</td> <td |
| ERDNS.md | CompGCN (TransE) | oui | </tr> <tr> <td rowspan="3">CompGCN (TransE)</td> <td>unif</td> <td |
| ERDNS.md | ComplEx | oui | 3. Performance comparison on DistMult, ComplEx, TransE and RotatE. <table> <thead> |
| ERDNS.md | ConvE | oui | le> Table 4. Performance comparison on ConvE and CompGCN. <table> <thead> <tr> |
| ERDNS.md | DistMult | oui | le> Table 3. Performance comparison on DistMult, ComplEx, TransE and RotatE. <table> |
| ERDNS.md | RotatE | oui | arison on DistMult, ComplEx, TransE and RotatE. <table> <thead> <tr> <th |
| ERDNS.md | TransE | oui | rmance comparison on DistMult, ComplEx, TransE and RotatE. <table> <thead> <tr> |
| eTruncatedUNS.md | AlignE | oui | 320</td> </tr> <tr> <td>AlignE</td> <td>47.18</td> <td |
| eTruncatedUNS.md | BootEA | oui | 707</td> </tr> <tr> <td>BootEA</td> <td><strong>62.94</strong> |
| eTruncatedUNS.md | IPTransE | oui | 334</td> </tr> <tr> <td>IPTransE</td> <td>40.59</td> <td |
| eTruncatedUNS.md | JAPE | oui | 386</td> </tr> <tr> <td>JAPE</td> <td>41.18</td> <td |
| eTruncatedUNS.md | MTransE | oui | </thead> <tbody> <tr> <td>MTransE</td> <td>30.83</td> <td |
| GHN.md | DistMult | oui | 4.1</td> </tr> <tr> <td>DistMult</td> <td>44.4</td> <td> |
| GHN.md | DKRL | oui | em></td> </tr> <tr> <td>DKRL</td> <td>16.0</td> <td> |
| GHN.md | KEPLER | oui | es$</td> </tr> <tr> <td>KEPLER</td> <td>21.0</td> <td> |
| GHN.md | KG-BERT | oui | ods</td> </tr> <tr> <td>KG-BERT</td> <td>21.6</td> <td> |
| GHN.md | MTL-KGC | oui | 2.0</td> </tr> <tr> <td>MTL-KGC</td> <td>33.1</td> <td> |
| GHN.md | RotatE | oui | 4.6</td> </tr> <tr> <td>RotatE</td> <td>47.6</td> <td> |
| GHN.md | SimKGC | oui | 8.2</td> </tr> <tr> <td>SimKGC</td> <td>66.6</td> <td> |
| GHN.md | StAR | oui | 5.8</td> </tr> <tr> <td>StAR</td> <td>40.1</td> <td> |
| GHN.md | TransE | oui | ods</td> </tr> <tr> <td>TransE</td> <td>24.3</td> <td> |
| GHN.md | Tucker | oui | 3.3</td> </tr> <tr> <td>TuckER</td> <td>47.0</td> <td> |
| GibbsNS.md | ComplEx | oui | 533</td> </tr> <tr> <td>ComplEx</td> <td>0.323</td> <td |
| GibbsNS.md | ConvE | oui | 526</td> </tr> <tr> <td>ConvE</td> <td>0.325</td> <td |
| GibbsNS.md | DistMult | oui | d>-</td> </tr> <tr> <td>DistMult</td> <td>0.308</td> <td |
| GibbsNS.md | InteractE | oui | .52</td> </tr> <tr> <td>InteractE</td> <td>0.354</td> <td |
| GibbsNS.md | KGE-EML | oui | 569</td> </tr> <tr> <td>KGE-EML [11]</td> <td>0.36</td> |
| GibbsNS.md | KGE-EML+GNS | **NON** | — |
| GibbsNS.md | PairRE | oui | ng></td> </tr> <tr> <td>PairRE</td> <td>0.351</td> <td |
| GibbsNS.md | PROCRUSTES | oui | 528</td> </tr> <tr> <td>PROCRUSTES</td> <td>0.345</td> <td |
| GibbsNS.md | RotatE | oui | 529</td> </tr> <tr> <td>RotatE</td> <td>0.338</td> <td |
| GibbsNS.md | TransD | oui | </tr> <tr> <td rowspan="5">TransD</td> <td>Uniform</td> < |
| GibbsNS.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>0.33</td> <td> |
| GibbsNS.md | TuckER | oui | 554</td> </tr> <tr> <td>TuckER</td> <td>0.358</td> <td |
| GNDN.md | ConvE | oui | 5.8</td> </tr> <tr> <td>ConvE [19]*</td> <td>0.46</td> |
| GNDN.md | ConvKB | oui | 9.1</td> </tr> <tr> <td>ConvKB [20]</td> <td>0.248</td> |
| GNDN.md | KBGAN | oui | </thead> <tbody> <tr> <td>KBGAN [19]*</td> <td>0.213</td> |
| GNDN.md | Knowledge Completion GAN | **NON** | — |
| GNDN.md | NTN | oui | 5.2</td> </tr> <tr> <td>NTN [8]*</td> <td>70.6</td> |
| GNDN.md | Path-KCGAN [2 hop] | oui | 4.6</td> </tr> <tr> <td>Path-KCGAN[2 hop]</td> <td>0.58</td> <td |
| GNDN.md | Path-KCGAN [3 hop] | oui | 7.1</td> </tr> <tr> <td>Path-KCGAN[3 hop]</td> <td>0.60</td> <td |
| GNDN.md | PathG-RNN [2 hop] | oui | </thead> <tbody> <tr> <td>PathG-RNN [2 hop]</td> <td>0.41</td> <td |
| GNDN.md | PathG-RNN [3 hop] | oui | 6.3</td> </tr> <tr> <td>PathG-RNN [3 hop]</td> <td>0.43</td> <td |
| GNDN.md | PTransE [2 hop] | oui | 8.5</td> </tr> <tr> <td>PTransE [2 hop]</td> <td>0.49</td> <td |
| GNDN.md | PTransE [3 hop] | oui | 2.2</td> </tr> <tr> <td>PTransE [3 hop]</td> <td>0.54</td> <td |
| GNDN.md | TransE | oui | </thead> <tbody> <tr> <td>TransE [9]*</td> <td>70.9</td> |
| GNDN.md | TransG | oui | 8.9</td> </tr> <tr> <td>TransG [16]*</td> <td>87.4</td> |
| GNS.md | KG-BERT | **NON** | — |
| GraphGAN.md | DeepWalk | oui | </thead> <tbody> <tr> <td>DeepWalk</td> <td>0.841</td> <td |
| GraphGAN.md | GraphGAN | oui | 776</td> </tr> <tr> <td>GraphGAN</td> <td><strong>0.855</strong> |
| GraphGAN.md | LINE | oui | 812</td> </tr> <tr> <td>LINE</td> <td>0.820</td> <td |
| GraphGAN.md | Node2vec | oui | 761</td> </tr> <tr> <td>Node2vec</td> <td>0.845</td> <td |
| GraphGAN.md | Struc2vec | oui | 842</td> </tr> <tr> <td>Struc2vec</td> <td>0.821</td> <td |
| HaSa.md | ComplEx | **NON** | — |
| HaSa.md | DistMult | oui | ng></td> </tr> <tr> <td>DistMult [36]</td> <td>7,000</td> |
| HaSa.md | HaSa+ | oui | /tr> <tr> <td>$\mathcal{L}_{HaSa}$ (6)</td> <td><u>123</u></td> |
| HaSa.md | KBGAN | oui | 450</td> </tr> <tr> <td>KBGAN [4]</td> <td>-</td> <td |
| HaSa.md | KG-BERT | oui | KGE</td> </tr> <tr> <td>KGBERT [38]</td> <td>97</td> < |
| HaSa.md | LASS | oui | 482</td> </tr> <tr> <td>LASS [25]</td> <td>55</td> < |
| HaSa.md | RotatE | oui | 441</td> </tr> <tr> <td>RotatE [26]</td> <td>3,340</td> |
| HaSa.md | sentence-BERT | oui | 6$). All methods use the pre-trained LM sentence-BERT as the initialization. Boldface is the |
| HaSa.md | StAR | oui | 420</td> </tr> <tr> <td>StAR [30]</td> <td><strong>51</stron |
| HaSa.md | TransE | oui | KGE</td> </tr> <tr> <td>TransE [3]</td> <td>2,300</td> |
| HTENS.md | ComplEx | oui | )d$</td> </tr> <tr> <td>ComplEx</td> <td>$&lt; \mathbf{h}, \mat |
| HTENS.md | DistMult | oui | )d$</td> </tr> <tr> <td>DistMult</td> <td>$&lt; \mathbf{h}, \mat |
| HTENS.md | TransD | oui | )d$</td> </tr> <tr> <td>TransD</td> <td>$\\| (\mathbf{I} + \mat |
| HTENS.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>$\\| \mathbf{h} + \math |
| IGAN.md | Single Layer Model | **NON** | — |
| IGAN.md | SME(Bilinear) | oui | ng></td> </tr> <tr> <td>SME(Bilinear) (Bordes et al. 2012)</td> <td> |
| IGAN.md | Structured Embedding | **NON** | — |
| IGAN.md | TransD | oui | ng></td> </tr> <tr> <td>TransD (Ji et al. 2015)</td> <td>91</t |
| IGAN.md | TransE | oui | 5.7</td> </tr> <tr> <td>TransE (Bordes et al. 2013)</td> <td>< |
| IGAN.md | TransE + A-LSTM | **NON** | — |
| IGAN.md | TransH | oui | ng></td> </tr> <tr> <td>TransH (Wang et al. 2014)</td> <td>87< |
| IGAN.md | TransR | oui | ng></td> </tr> <tr> <td>TransR (Lin et al. 2015)</td> <td><str |
| IGAN.md | Unstructured Model | **NON** | — |
| KBGAN.md | ComplEx | oui | re considered in this paper. Except for COMPLEX, all boldface lower case letters repres |
| KBGAN.md | DistMult | oui | }\|$</td> </tr> <tr> <td>DISTMULT</td> <td>$\langle \mathbf{h}, \ |
| KBGAN.md | TransD | oui | }\|$</td> </tr> <tr> <td>TRANSD</td> <td>$\\|(\mathbf{I} + \math |
| KBGAN.md | TransE | oui | </thead> <tbody> <tr> <td>TRANSE</td> <td>$\\|\mathbf{h} + \mathb |
| KSGAN.md | ComplEx | oui | ^d$</td> </tr> <tr> <td>ComplEx</td> <td>$Re(\mathbf{h}, \mathb |
| KSGAN.md | TransD | oui | d}$</td> </tr> <tr> <td>TransD</td> <td>$-\\|(w_r w_h^\top + I) |
| KSGAN.md | TransE | oui | br/>distance<br/>model</td> <td>TransE</td> <td>$-\\|\mathbf{h} + \math |
| LAS.md | ComplEx | oui | 462</td> </tr> <tr> <td>ComplEx (pretrained)</td> <td>0.264</td |
| LAS.md | ConvE | oui | d>-</td> </tr> <tr> <td>ConvE [23]</td> <td><strong>31.6</str |
| LAS.md | DistMult | oui | </thead> <tbody> <tr> <td>DistMult [18]</td> <td>24.1</td> |
| LAS.md | R-GCN | oui | 1.0</td> </tr> <tr> <td>R-GCN [28]</td> <td>24.8</td> |
| LAS.md | TransD* | oui | 431</td> </tr> <tr> <td>TransD (pretrained)</td> <td>0.244</td |
| LAS.md | TransE | oui | </thead> <tbody> <tr> <td>TransE (pretrained)</td> <td>0.243</td |
| LEMON.md | RotatE | oui | tbody> <tr> <td rowspan="4">RotatE</td> <td>Uniform</td> < |
| LEMON.md | TransE | oui | </tr> <tr> <td rowspan="4">TransE</td> <td>Uniform</td> < |
| Localcognitive.md | ComplEx | oui | $\circ$ denotes element-wise (Hadamard) complex product, $\otimes$ denotes element-wise |
| Localcognitive.md | ConvE | oui | 599</td> </tr> <tr> <td>ConvE</td> <td>374</td> <td>. |
| Localcognitive.md | DistMult | oui | ="3">Semantic matching</td> <td>DistMult</td> <td>$\langle \mathbf{r}, \ |
| Localcognitive.md | HolE | oui | d>-</td> </tr> <tr> <td>HolE</td> <td>-</td> <td>.93 |
| Localcognitive.md | QuatE | oui | d>-</td> </tr> <tr> <td>QuatE</td> <td>$\mathbf{h} \otimes \m |
| Localcognitive.md | RatE | oui | d>✗</td> </tr> <tr> <td>RatE</td> <td>$-\\|\mathbf{h} \odot_{ |
| Localcognitive.md | RotatE | oui | d>✗</td> </tr> <tr> <td>RotatE</td> <td>$-\\|\mathbf{h} \circ \ |
| Localcognitive.md | TransE | oui | owspan="3">Trans-based</td> <td>TransE</td> <td>$-\\|\mathbf{h} + \math |
| Localcognitive.md | TuckER | oui | Table 9: Performance comparison between TuckER and RatE on WN18RR/FB15k-237. “#θ” deno |
| LTS.md | CTransR | oui | 8.7</td> </tr> <tr> <td>CTransR(unif/bern)</td> <td>243/231</td |
| LTS.md | SE | oui | ilt</th> </tr> <tr> <td>SE</td> <td>1011</td> <td> |
| LTS.md | TransD | oui | 0.2</td> </tr> <tr> <td>TransD(unif/bern)</td> <td>242/224</td |
| LTS.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>7.01</td> <td> |
| LTS.md | TransE-LTS | oui | .71</td> </tr> <tr> <td>TransE-LTS</td> <td>13.89</td> <td |
| LTS.md | TransE-SNS | oui | >74</td> </tr> <tr> <td>TransE-SNS(unif/bern)</td> <td>220/207</td |
| LTS.md | TransH | oui | 7.1</td> </tr> <tr> <td>TransH(unif/bern)</td> <td>318/401</td |
| LTS.md | TranSparse | oui | 7.3</td> </tr> <tr> <td>TranSparse(unif/bern)</td> <td>233/223</td |
| LTS.md | TransR | oui | 4.4</td> </tr> <tr> <td>TransR(unif/bern)</td> <td>232/238</td |
| M2ixKG.md | ComplEx | oui | ct, $\bar{\cdot}$ denotes conjugate for complex vectors <table> <thead> <tr> |
| M2ixKG.md | DistMult | oui | ="2">semantic matching</td> <td>DistMult</td> <td>$\langle \mathbf{r}, \ |
| M2ixKG.md | RotatE | oui | \\|$</td> </tr> <tr> <td>RotatE</td> <td>$\\|\mathbf{h} \odot \m |
| M2ixKG.md | TransE | oui | translational distance</td> <td>TransE</td> <td>$\\|\mathbf{h} + \mathb |
| MCNS.md | DeepWalk | oui | <tr> <th> </th> <th>DeepWalk</th> <th>GCN</th> <th>G |
| MCNS.md | GCN | oui | > <th>DeepWalk</th> <th>GCN</th> <th>GraphSAGE</th> |
| MCNS.md | GraphSAGE | oui | k</th> <th>GCN</th> <th>GraphSAGE</th> <th>DeepWalk</th> |
| MDNCaching.md | ComplEx | oui | ^n$</td> </tr> <tr> <td>ComplEx [11]</td> <td>$Re(h \cdot diag( |
| MDNCaching.md | DistMult | oui | tic<br/>matching-based</td> <td>DistMult [16]</td> <td>$h \cdot diag(r) |
| MDNCaching.md | TransD | oui | ^n$</td> </tr> <tr> <td>TransD [6]</td> <td>$\left\\|h + w_r w_ |
| MDNCaching.md | TransE | oui | nal<br/>distance-based</td> <td>TransE [2]</td> <td>$\\|h + r - t\\|_i$< |
| NMiss.md | DistMult | oui | -06</td> </tr> <tr> <td>DistMult</td> <td>0.001</td> <td |
| NMiss.md | RESCAL | oui | -06</td> </tr> <tr> <td>Rescal</td> <td>0.001</td> <td |
| NMiss.md | TransE | oui | 084</td> </tr> <tr> <td>TransE</td> <td>0.001</td> <td |
| NoiGAN.md | Attention | oui | 507</td> </tr> <tr> <td>Attention</td> <td><strong>436</strong></ |
| NoiGAN.md | DistMult | oui | <td rowspan="10">0%</td> <td>DistMult</td> <td>.218</td> <td> |
| NoiGAN.md | KBGAN | oui | 507</td> </tr> <tr> <td>KBGAN</td> <td>.266</td> <td> |
| NoiGAN.md | RotatE | oui | 503</td> </tr> <tr> <td>RotatE</td> <td>.326</td> <td> |
| NoiGAN.md | TransE | oui | > </tr> <tr> <td>NoiGAN-TransE (soft)</td> <td><strong>.949</s |
| NSCaching.md | ComplEx | oui | op$</td> </tr> <tr> <td>ComplEx [38]</td> <td>$\text{Re}(\mathb |
| NSCaching.md | DistMult | oui | ="2">semantic matching</td> <td>DistMult [46]</td> <td>$\mathbf{h} \cdot |
| NSCaching.md | TransD | oui | _1$</td> </tr> <tr> <td>TransD [20]</td> <td>$\\|\mathbf{h} + \ |
| NSCaching.md | TransE | oui | translational distance</td> <td>TransE [7]</td> <td>$\\|\mathbf{h} + \m |
| NSCaching.md | TransH | oui | _1$</td> </tr> <tr> <td>TransH [42]</td> <td>$\\|\mathbf{h} - \ |
| PNS.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>263</td> <td>0 |
| PNS.md | TransH | oui | 349</td> </tr> <tr> <td>TransH(bern)</td> <td>401</td> |
| PNS.md | TransR | oui | <th>Epoch</th> <th>Modified TransR</th> <th>Original TransR</th> |
| RAAKGC.md | ComplEx | oui | 9.2</td> </tr> <tr> <td>ComplEx</td> <td>46.8</td> <td> |
| RAAKGC.md | ConvE | oui | 5.9</td> </tr> <tr> <td>ConvE</td> <td>45.6</td> <td> |
| RAAKGC.md | DistMult | oui | 9.7</td> </tr> <tr> <td>DistMult</td> <td>44.4</td> <td> |
| RAAKGC.md | HaSa | oui | 4.9</td> </tr> <tr> <td>HaSa</td> <td>53.8</td> <td> |
| RAAKGC.md | InsKGC | oui | s for the text-based methods, we choose InsKGC (Jiang, Drummond, and Cohn 2023) and Si |
| RAAKGC.md | KG-BERT | oui | ods</td> </tr> <tr> <td>KG-BERT</td> <td>21.6</td> <td> |
| RAAKGC.md | MTL-KGC | oui | d>-</td> </tr> <tr> <td>MTL-KGC</td> <td>33.1</td> <td> |
| RAAKGC.md | QuatE | oui | 9.0</td> </tr> <tr> <td>QuatE</td> <td>48.1</td> <td> |
| RAAKGC.md | RAA-KGC | oui | d>-</td> </tr> <tr> <td>RAA-KGC</td> <td><strong><u>59.74</u></ |
| RAAKGC.md | RGCN | oui | d>-</td> </tr> <tr> <td>RGCN</td> <td>42.7</td> <td> |
| RAAKGC.md | RotatE | oui | d>-</td> </tr> <tr> <td>RotatE</td> <td>47.6</td> <td> |
| RAAKGC.md | SimKGC | oui | d>-</td> </tr> <tr> <td>SimKGC</td> <td>55.31</td> <td |
| RAAKGC.md | StAR | oui | d>-</td> </tr> <tr> <td>StAR</td> <td>40.1</td> <td> |
| RAAKGC.md | TransE | oui | ods</td> </tr> <tr> <td>TransE</td> <td>24.3</td> <td> |
| RandomCorrupt.md | ComplEx | oui | modifications to adapt this task; (2) **ComplEx** achieves the best performance on all |
| RandomCorrupt.md | DistMult | oui | ficantly and consistently outperforms **DistMult** which matches the observations for th |
| RandomCorrupt.md | TransE | oui | of link prediction; (2) Surprisingly, **TransE** has competitive performance with **Co |
| RCWC.md | ComplEx | oui | 946</td> </tr> <tr> <td>ComplEx [Trouillon et al., 2016]</td> < |
| RCWC.md | ConvE | oui | 947</td> </tr> <tr> <td>ConvE [Dettmers et al., 2018]</td> <t |
| RCWC.md | DistMult | oui | 943</td> </tr> <tr> <td>DistMult [Yang et al., 2014]</td> <td>42 |
| RCWC.md | InteractE | oui | .54</td> </tr> <tr> <td>InteractE [Vashishth et al., 2020]</td> < |
| RCWC.md | KGBoost-R | oui | 951</td> </tr> <tr> <td>KGBoost-R (Ours)</td> <td>16</td> |
| RCWC.md | KGBoost-T | oui | ng></td> </tr> <tr> <td>KGBoost-T (Ours)</td> <td><strong>15</str |
| RCWC.md | RotatE | oui | 956</td> </tr> <tr> <td>RotatE [Sun et al., 2019]</td> <td>40< |
| RCWC.md | SACN | oui | ng></td> </tr> <tr> <td>SACN [Shang et al., 2019]</td> <td>- |
| RCWC.md | TransE | oui | </thead> <tbody> <tr> <td>TransE [Bordes et al., 2013]</td> <td> |
| ReasonKGE.md | ComplEx | oui | </tr> <tr> <td rowspan="3">ComplEx</td> <td>LUBM3U</td> <t |
| ReasonKGE.md | TransE | oui | tbody> <tr> <td rowspan="3">TransE</td> <td>LUBM3U</td> <t |
| RUGA.md | ComplEx | oui | 546</td> </tr> <tr> <td>ComplEx</td> <td>0.690</td> <td |
| RUGA.md | DistMult | oui | 468</td> </tr> <tr> <td>DistMult</td> <td>0.634</td> <td |
| RUGA.md | HolE | oui | 570</td> </tr> <tr> <td>HolE</td> <td>0.608</td> <td |
| RUGA.md | RUGA | oui | </tr> <tr> <td><strong>RUGA</strong></td> <td><strong>0.779 |
| RUGA.md | RUGE | oui | 601</td> </tr> <tr> <td>RUGE</td> <td>0.767</td> <td |
| RUGA.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>h, t</td> <td> |
| SANS.md | DistMult | oui | </tr> <tr> <td rowspan="6">DistMult</td> <td>KBGAN</td> <td |
| SANS.md | RotatE | oui | </tr> <tr> <td rowspan="4">RotatE</td> <td>Uniform</td> < |
| SANS.md | TransE | oui | tbody> <tr> <td rowspan="6">TransE</td> <td>KBGAN (Cai and Wang, 2 |
| SelfAdv.md | ComplEx | oui | \overline{\cdot}$ denotes conjugate for complex vectors, and 2D reshaping for real vect |
| SelfAdv.md | ConvE | oui | s, and 2D reshaping for real vectors in ConvE model. TransX represents a wide range o |
| SelfAdv.md | DistMult | oui | \in R^k$</td> </tr> <tr> <td>DistMult (Yang et al., 2014)</td> <td>$\la |
| SelfAdv.md | HolE | oui | \in C^k$</td> </tr> <tr> <td>HolE (Nickel et al., 2016)</td> <td>$\ |
| SelfAdv.md | pRotatE | oui | <td>.956</td> </tr> <tr> <td>pRotatE</td> <td>43</td> <td><b>.79 |
| SelfAdv.md | RotatE | oui | \in R^k$</td> </tr> <tr> <td>RotatE</td> <td>$-\\|h \circ r - t\\|^2$</ |
| SelfAdv.md | TransE | oui | odel. TransX represents a wide range of TransE’s variants, such as TransH (Wang et al. |
| SNS.md | DistMult | oui | ^2$</td> </tr> <tr> <td>DistMult [12]</td> <td>$\mathbf{h}^d, \m |
| SNS.md | TransH | oui | </thead> <tbody> <tr> <td>TransH [11]</td> <td>$\mathbf{h}^d, \m |
| SparseNSG.md | ANALOGY | oui | 0.1</td> </tr> <tr> <td>ANALOGY</td> <td>d = 200, α = 0.1</td> |
| SparseNSG.md | ComplEx | oui | 0.1</td> </tr> <tr> <td>COMPLEX</td> <td>d = 200, α = 0.1</td> |
| SparseNSG.md | DistMult | oui | 001</td> </tr> <tr> <td>DISTMULT</td> <td>d = 200, α = 0.1</td> |
| SparseNSG.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>d=100, γ = 1, α = 0.00 |
| SparseNSG.md | TransH | oui | 001</td> </tr> <tr> <td>TransH</td> <td>d = 100, γ = 1, α = 0. |
| STC.md | LFM | oui | 1.3</td> </tr> <tr> <td>LFM</td> <td>283</td> <td>1 |
| STC.md | RESCAL | oui | </thead> <tbody> <tr> <td>RESCAL</td> <td>828</td> <td>6 |
| STC.md | SE | oui | 4.1</td> </tr> <tr> <td>SE</td> <td>273</td> <td>1 |
| STC.md | SME (bilinear) | oui | 0.8</td> </tr> <tr> <td>SME (bilinear)</td> <td>284</td> <td> |
| STC.md | SME (linear) | oui | 9.8</td> </tr> <tr> <td>SME (linear)</td> <td>274</td> <td> |
| STC.md | TKRL (RHE) | oui | 7.2</td> </tr> <tr> <td>TKRL (RHE)</td> <td><strong>184</strong>< |
| STC.md | TKRL (RHE+STC) | **NON** | — |
| STC.md | TKRL (RHE+STC+TCE) | **NON** | — |
| STC.md | TKRL (WHE) | oui | 9.4</td> </tr> <tr> <td>TKRL (WHE)</td> <td>186</td> <td> |
| STC.md | TKRL (WHE+STC) | **NON** | — |
| STC.md | TKRL (WHE+STC+TCE) | **NON** | — |
| STC.md | TransE | oui | 3.1</td> </tr> <tr> <td>TransE</td> <td>238</td> <td>1 |
| STC.md | TransE+STC+TCE | **NON** | — |
| STC.md | TransE+TCE | **NON** | — |
| STC.md | TransR | oui | 2.1</td> </tr> <tr> <td>TransR</td> <td>199</td> <td>7 |
| STC.md | TransR+STC+TCE | **NON** | — |
| STC.md | TransR+TCE | **NON** | — |
| TANS.md | ComplEx | oui | <td>FB15k-237</td> <td>ComplEx</td> <td>25.0</td> <td> |
| TANS.md | DistMult | oui | <td>FB15k-237</td> <td>DistMult</td> <td>24.0</td> <td> |
| TANS.md | HAKE | oui | <td>FB15k-237</td> <td>HAKE</td> <td>33.0</td> <td> |
| TANS.md | HousE | oui | <td>FB15k-237</td> <td>HousE</td> <td>33.5</td> <td> |
| TANS.md | RotatE | oui | <td>FB15k-237</td> <td>RotatE</td> <td>33.0</td> <td> |
| TANS.md | TransE | oui | <td>FB15k-237</td> <td>TransE</td> <td>33.0</td> <td> |
| TruncatedNS.md | IPTransE | oui | 258</td> </tr> <tr> <td>IPTransE</td> <td>32.73</td> <td |
| TruncatedNS.md | JAPE | oui | 412</td> </tr> <tr> <td>JAPE</td> <td>14.45</td> <td |
| TruncatedNS.md | MTransE | oui | 007</td> </tr> <tr> <td>MtransE</td> <td>16.51</td> <td |
| TruncatedNS.md | TransE | oui | </thead> <tbody> <tr> <td>TransE</td> <td>8.35</td> <td> |
| TruncatedNS.md | Truncated Negative Sampling | **NON** | — |
| TuckerDNCaching.md | ComplEx | oui | ^n$</td> </tr> <tr> <td>ComplEx</td> <td>$Re(h^\top \cdot diag( |
| TuckerDNCaching.md | DistMult | oui | tic<br/>matching-based</td> <td>DistMult</td> <td>$h^\top \cdot diag(r) |
| TuckerDNCaching.md | TransD | oui | ^n$</td> </tr> <tr> <td>TransD</td> <td>$\left\\|h + w_r w_h^\t |
| TuckerDNCaching.md | TransE | oui | nal<br/>distance-based</td> <td>TransE</td> <td>$\\|h + r - t\\|_{1/2}$< |
| TypeAugmented.md | ComplEx | oui | td> </tr> <tr> <td>TaKE+ComplEx</td> <td>O(d + k)</td> |
| TypeAugmented.md | DistMult | oui | td> </tr> <tr> <td>TaKE+Distmult</td> <td>O(d + k)</td> |
| TypeAugmented.md | RotatE | oui | td> </tr> <tr> <td>TaKE+RotatE</td> <td>O(d + k)</td> |
| TypeAugmented.md | SimplE | oui | td> </tr> <tr> <td>TaKE+SimplE</td> <td>O(d + k)</td> |
| TypeAugmented.md | TaKE-ComplEx | oui | 428</td> </tr> <tr> <td>TaKE-ComplEx</td> <td>0.778</td> <td |
| TypeAugmented.md | TaKE-DistMult | oui | 419</td> </tr> <tr> <td>TaKE-DistMult</td> <td>0.757</td> <td |
| TypeAugmented.md | TaKE-RotatE | oui | 533</td> </tr> <tr> <td>TaKE-RotatE</td> <td>0.804</td> <td |
| TypeAugmented.md | TaKE-SimplE | oui | 476</td> </tr> <tr> <td>TaKE-SimplE</td> <td><strong>0.806</strong> |
| TypeAugmented.md | TaKE-TransE | oui | 465</td> </tr> <tr> <td>TaKE-TransE</td> <td>0.490</td> <td |
| TypeAugmented.md | TransE | oui | td> </tr> <tr> <td>TaKE+TransE</td> <td>O(d + k)</td> |
| TypeAugmented.md | TypeComplex | oui | R\|)</td> </tr> <tr> <td>TypeComplex</td> <td>O(d + k)</td> |
| TypeAugmented.md | TypeDM | oui | </thead> <tbody> <tr> <td>TypeDM</td> <td>O(d + k)</td> |
| TypeConstraints.md | mwNN | oui | omparison of AUPRC and AUROC result for mwNN [8] with and without exploiting prior k |
| TypeConstraints.md | RESCAL | oui | omparison of AUPRC and AUROC result for RESCAL with and without exploiting prior knowl |
| TypeConstraints.md | TransE | oui | omparison of AUPRC and AUROC result for TransE with and without exploiting prior knowl |
| Uniform.md | LFM | oui | .06</td> </tr> <tr> <td>LFM [6]</td> <td>$O(n_e k + n_r k + |
| Uniform.md | RESCAL | oui | .75</td> </tr> <tr> <td>RESCAL [11]</td> <td>$O(n_e k + n_r k^ |
| Uniform.md | SME(bilinear) | oui | .82</td> </tr> <tr> <td>SME(BILINEAR) [2]</td> <td>$O(n_e k + n_r k |
| Uniform.md | SME(linear) | oui | .47</td> </tr> <tr> <td>SME(LINEAR) [2]</td> <td>$O(n_e k + n_r k |
| Uniform.md | Structured Embeddings | **NON** | — |
| Uniform.md | TransE | oui | .84</td> </tr> <tr> <td>TransE</td> <td>$O(n_e k + n_r k)$</td |
| Uniform.md | Unstructured | oui | </thead> <tbody> <tr> <td>Unstructured [2]</td> <td>$O(n_e k)$</td> |

## B. Preuve — MENTIONNÉS seulement (238)

| Article | Entité | Trouvé | Extrait (prose) |
|---|---|:---:|---|
| AdaptativeNS.md | HAKE | oui | relationships in knowledge graphs. The HAKE [20] model is designed for graph embedd |
| AdaptativeNS.md | MEI | oui | ent intricacies of the knowledge graph. MEI [13] and MEIM [14] partition each embed |
| AdaptativeNS.md | MEIM | oui | es of the knowledge graph. MEI [13] and MEIM [14] partition each embedding into mult |
| AdaptativeNS.md | RESCAL | oui | ressed in vector space representations. RESCAL [10] introduced a tensor factorization |
| AdaptativeNS.md | TransD | oui | between entities and relationships. The TransD [18] model further improves upon TransR |
| AdaptativeNS.md | TransG | oui | and relationships more effectively. The TransG [17] model proposes a solution to the c |
| AdaptativeNS.md | TransH | oui | many and many-to-one relationships, the TransH [16] model extends it by introducing re |
| AdaptativeNS.md | TransR | oui | omes the shortcomings of TransE. In the TransR [7] model, a relation mapping matrix is |
| ADNS.md | ComplEx | oui | t years. e.g, TransE [2], DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost |
| ADNS.md | RotatE | oui | , DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost all of these models dep |
| ADNS.md | TransH | oui | , TransE [2], DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost all of thes |
| BatchNS.md | DistMult | oui | n operators allows PBG to train RESCAL, DistMult, TransE, and ComplEx models (Nickel et |
| BatchNS.md | word2vec | oui | this literature are algorithms such as word2vec which allowed word embedding methods to |
| CAKE.md | ComplEx | oui | se together with the characteristics of complex relations. Furthermore, a multi-view li |
| CAKE.md | DistMult | oui | osition-based** score function, such as DistMult (Yang et al., 2015): $$E(h, r, t) = \m |
| CAKE.md | JOIE | oui | hand, although some KGE models such as JOIE (Hao et al., 2019) employ the ontology |
| CAKE.md | KBGAN | oui | 2014). (2) Adversarial-based sampling: KBGAN (Cai and Wang, 2018) integrates the KGE |
| CAKE.md | RESCAL | oui | s such as TransE (Bordes et al., 2013), RESCAL (Nickel et al., 2011), ComplEx (Trouill |
| CAKE.md | TransH | oui | amely 1-1, 1-N, N-1, and N-N defined in TransH (Wang et al., 2014) for negative sampli |
| CANS.md | GTrans | oui | iple as a manifold rather than a point. GTrans [20] used dynamic and static weighting |
| CANS.md | ManifoldE | oui | ctors of entities into various spaces. ManifoldE [19] embedded a triple as a manifold ra |
| CANS.md | puTransE | oui | d the noise from other relation spaces. puTransE [21] generated multiple embedding space |
| CANS.md | TransD | oui | ame vector space. Then TransR [17], and TransD [18], extended TransE, by projecting th |
| CANS.md | TransH | oui | th 1-to-N, N-to-1, or N-to-N relations. TransH [10] proposed to project the entity to |
| CANS.md | TransR | oui | ons were in the same vector space. Then TransR [17], and TransD [18], extended TransE, |
| CCS.md | HAKE | oui | on translation of the vectors in space. HAKE [31] maps the entities into spatial pol |
| CCS.md | NTN | oui | SME) [16] model, neural tensor network (NTN) [17] model, and matrix factorization ( |
| CCS.md | OTE | oui | ntities into spatial polar coordinates. OTE [32] exploits the orthogonality relatio |
| CCS.md | PTransE | oui | TransE [26], TransA [27], TransAt [28], PTransE [29], etc. Recently, RotatE [30] has ch |
| CCS.md | RESCAL | oui | ) [17] model, and matrix factorization (RESCAL) [18] model. However, these KGE models |
| CCS.md | RotatE | oui | nsAt [28], PTransE [29], etc. Recently, RotatE [30] has changed the translation proces |
| CCS.md | SE | oui | tion, such as the structured embedding (SE) [15] model, semantic matching energy ( |
| CCS.md | SME | oui | ) [15] model, semantic matching energy (SME) [16] model, neural tensor network (NTN |
| CCS.md | STransE | oui | nsD [23], TransM [24], TranSparse [25], STransE [26], TransA [27], TransAt [28], PTrans |
| CCS.md | TransA | oui | sM [24], TranSparse [25], STransE [26], TransA [27], TransAt [28], PTransE [29], etc. |
| CCS.md | TransAt | oui | Sparse [25], STransE [26], TransA [27], TransAt [28], PTransE [29], etc. Recently, Rota |
| CCS.md | TransM | oui | TransH [21], TransR [22], TransD [23], TransM [24], TranSparse [25], STransE [26], Tr |
| CCS.md | TranSparse | oui | TransR [22], TransD [23], TransM [24], TranSparse [25], STransE [26], TransA [27], TransA |
| CondConstraints.md | RESCAL | oui | nly explores their applicability to the RESCAL model [2]. On the other hand, the work |
| CondConstraints.md | TransH | oui | cheme was introduced by Wang et al. for TransH and is sometimes called the Bernoulli t |
| CondConstraints.md | TRESCAL | oui | exploiting type information [6]. While TRESCAL explicitly tries to make use of type co |
| dans.md | RGCN | oui | relational graph convolutional network (RGCN) [26] to serve as our base embedding mo |
| dans.md | TransE | oui | xt{China} \rangle$ and a classic method TransE [2]. TransE maps each entity and relati |
| DeMix.md | TransH | oui | amely 1-N, N-1, 1-1, and N-N defined in TransH [24], we record the num of positive tri |
| DHNS.md | KGDM | oui | idering the query node's context, while KGDM [16] applies DDPM to estimate the proba |
| DHNS.md | LAFA | oui | y in an adversarial training framework. LAFA [24] considers the relationships betwee |
| DHNS.md | QuatE | oui | ntisymmetric relations. RotatE [25] and QuatE [36] introduce rotational and quaternio |
| DHNS.md | RESCAL | oui | ar interaction-based KGE models such as RESCAL [22] and DistMult [35], formulated as: |
| DHNS.md | TransH | oui | based KGE models such as TransE [3] and TransH [31], formulated as: $$C(\mathbf{x}_e, |
| DHNS.md | VISTA | oui | aggregation of multi-modal information. VISTA [11] designs three transformer-based en |
| DNS.md | ComplEx | oui | ued embeddings into their corresponding complex variants, and performs Hermitian dot pr |
| DNS.md | HolE | oui | teractions within the triples for their HolE system. Trouillon et al. [2016] represe |
| DNS.md | Neural Tensor Network | oui | h as *RESCAL* Nickel et al. [2011] and *Neural Tensor Network* Socher et al. [2013] employ higher ord |
| DNS.md | TransH | oui | Wang et al. [2014] define an algorithm *TransH* that behaves like *TransE* with a mino |
| EANS.md | RESCAL | oui | relation vectors into various spaces. RESCAL (Nickel et al., 2011), DistMult (Yang e |
| EANS.md | TransH | oui | . Various extensions of TransE, such as TransH (Wang et al., 2014), TransR (Lin et al. |
| EANS.md | TransR | oui | sE, such as TransH (Wang et al., 2014), TransR (Lin et al., 2015) and TransD (Ji et al |
| ERDNS.md | CompGCN | oui | ], ConvE [5], and InteractE [24], while CompGCN [5] is a generalized version of several |
| ERDNS.md | ConvKB | oui | odels. Examples of CNN-based models are ConvKB [18], ConvE [5], and InteractE [24], wh |
| ERDNS.md | InteractE | oui | models are ConvKB [18], ConvE [5], and InteractE [24], while CompGCN [5] is a generalize |
| ERDNS.md | SimplE | oui | ples and lower scores to negative ones. Simple negative sampling methods like uniform |
| ERDNS.md | TransD | oui | amples of TD models include TransE [2], TransD [8], TransR [15], and RotatE [21], whil |
| ERDNS.md | TransR | oui | models include TransE [2], TransD [8], TransR [15], and RotatE [21], while popular SM |
| eTruncatedUNS.md | KR-EAR | oui | tes reverse triples and relation paths. KR-EAR [Lin et al., 2016] introduces categoric |
| eTruncatedUNS.md | PTransE | oui | 2014], TransR [Lin et al., 2015b] and PTransE [Lin et al., 2015a]. Most existing KG |
| eTruncatedUNS.md | TransE | oui | nherent KG semantics. As an early work, TransE [Bordes et al., 2013] interprets a rela |
| eTruncatedUNS.md | TransH | oui | further improved by many works, such as TransH [Wang et al., 2014], TransR [Lin et al |
| eTruncatedUNS.md | TransR | oui | s, such as TransH [Wang et al., 2014], TransR [Lin et al., 2015b] and PTransE [Lin et |
| GHN.md | ComplEx | oui | al., 2013), TransH (Wang et al., 2014), Complex (Trouillon et al., 2016), and RotatE (S |
| GHN.md | TransH | oui | s include TransE (Bordes et al., 2013), TransH (Wang et al., 2014), Complex (Trouillon |
| GibbsNS.md | KG-BERT | oui | ed pre-trained models to tackle issues. KG-BERT [14], for instance, is a BERT-based kno |
| GibbsNS.md | RESCAL | oui | . An eminent contender in this class is RESCAL proposed by Nickel et al. [24], which c |
| GibbsNS.md | TransH | oui | gh similarity. To overcome challenges, TransH, introduced by [9], utilizes hyperplane |
| GNDN.md | DistMult | oui | ions over entities and relations, and a DistMult based decoder for factorization. The GC |
| GNDN.md | ELECTRA | oui | ecently developed language model called ELECTRA [37], which is a compute-efficient GAN- |
| GNDN.md | HypER | oui | igm and reports better overall results. HypER [26] uses a 1D-relation-specific convol |
| GNDN.md | KCGAN | oui | iscriminative belief prediction models. KCGAN thus invokes a game between generator-n |
| GNDN.md | KG-BERT | oui | ansformer-based encoding models such as KG-BERT [35] are inspired by transformer-based |
| GNDN.md | PTransE | oui | red as PathG-RNNs. We also compare with PTransE which is a variant of TransE for integr |
| GNS.md | BERT | oui | state-of-the-art embedding method - KG-BERT for triple classification task - on a b |
| GNS.md | ComplEx | oui | n KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMult [20] and KG-BERT [21], a |
| GNS.md | DistMult | oui | TransE [5], Rescal [12], ComplEx [16], DistMult [20] and KG-BERT [21], and all these me |
| GNS.md | ReasonKGE | oui | o pick head or tail entity to corrupt. ReasonKGE [9] with its Iterative Negative Samplin |
| GNS.md | Rescal | oui | embeddings in KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMult [20] and K |
| GNS.md | TransE | oui | and relation embeddings in KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMul |
| GNS.md | TransOWL | oui | e sampling for triple classification 5 TransOWL [7] leverages ontology axioms in order |
| GraphGAN.md | PPNE | oui | nder the supervision of edge existence. PPNE (Li et al. 2017b) directly learns verte |
| GraphGAN.md | SDNE | oui | aining data in the graph. For instance, SDNE (Wang, \*M. Guo is the corresponding a |
| IGAN.md | Neural Tensor Network | oui | ag{8}$$ where g() is tanh function. **Neural Tensor Network** (Socher et al. 2013) extends Single L |
| KBGAN.md | ConvE | oui | o combine the two entities in a triple. CONVE (Dettmers et al., 2017) uses a convolut |
| KBGAN.md | HolE | oui | iple as a manifold rather than a point. HOLE (Nickel et al., 2016) employs circular |
| KBGAN.md | ManifoldE | oui | ent models achieve strong performances. MANIFOLDE (Xiao et al., 2016) embeds a triple as |
| KBGAN.md | RESCAL | oui | graph embedding (KGE) techniques (e.g., RESCAL (Nickel et al., 2011), TRANSE (Bordes e |
| KBGAN.md | TransH | oui | ased embedding. Later variants, such as TRANSH (Wang et al., 2014), TRANSR (Lin et al. |
| KBGAN.md | TransR | oui | ts, such as TRANSH (Wang et al., 2014), TRANSR (Lin et al., 2015) and TRANSD (Ji et al |
| KSGAN.md | DistMult | oui | ng model (e.g., TransE [6], TransD [7], DistMult [8], ComplEx [9]). However, previous w |
| KSGAN.md | GTrans | oui | (or **t** − **r**). As a generic model, GTrans [17] introduces eigenstate and mimesis |
| KSGAN.md | ManifoldE | oui | ict magnitude constraints between them. ManifoldE [16] uses a manifold function to constr |
| KSGAN.md | MLP | oui | ic matching models such as NTN [21] and MLP [22], focus on neural network architect |
| KSGAN.md | NTN | oui | Other semantic matching models such as NTN [21] and MLP [22], focus on neural netw |
| KSGAN.md | RESCAL | oui | from the translational distance model, RESCAL [18] is a classic semantic matching mod |
| KSGAN.md | SimplE | oui | complex space rather than a real space. SimplE [19] simplifies ComplEx by considering |
| KSGAN.md | TransF | oui | ons. Targeting at more flexible models, TransF [15] ensures that **t** (or **h**) has |
| KSGAN.md | TransH | oui | t $(h, r, t)$. Various variants such as TransH [12], TransM [13], TransR [14] and Tran |
| KSGAN.md | TransM | oui | . Various variants such as TransH [12], TransM [13], TransR [14] and TransD [7] have b |
| KSGAN.md | TransR | oui | iants such as TransH [12], TransM [13], TransR [14] and TransD [7] have been developed |
| KSGAN.md | TuckER | oui | different similarity scoring function. TuckER [20] is based on Tucker decomposition a |
| LAS.md | ANALOGY | oui | bability-based models, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also achieve good |
| LAS.md | DKRL | oui | ] exploit relation paths, TEKE [33] and DKRL [34] embed knowledge graph with textual |
| LAS.md | HolE | oui | dels (e.g., RESCAL [17], DistMult [18], HolE [19], ComplEx [20], and ConvE [23] etc) |
| LAS.md | ITransF | oui | [13], STransE [14], puTransE [15], and ITransF [16]) define an energy function accordi |
| LAS.md | KALE | oui | owledge graph with textual information, KALE [35] and RUGE [36] utilize logical rule |
| LAS.md | KG2E | oui | 6], TransH [7], TransR [8], TransD [9], KG2E [10], TransA [11], TranSparse [12], Tra |
| LAS.md | ProjE | oui | ny other probability-based models, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also |
| LAS.md | PTransE | oui | and TKRL [30] consider the entity type, PTransE [31] and RTransE [32] exploit relation |
| LAS.md | puTransE | oui | Sparse [12], TransG [13], STransE [14], puTransE [15], and ITransF [16]) define an energ |
| LAS.md | RESCAL | oui | models Probability-based models (e.g., RESCAL [17], DistMult [18], HolE [19], ComplEx |
| LAS.md | RTransE | oui | sider the entity type, PTransE [31] and RTransE [32] exploit relation paths, TEKE [33] |
| LAS.md | RUGE | oui | with textual information, KALE [35] and RUGE [36] utilize logical rules. In this pa |
| LAS.md | SSE | oui | further improve the task. For example, SSE [29] and TKRL [30] consider the entity |
| LAS.md | STransE | oui | nsA [11], TranSparse [12], TransG [13], STransE [14], puTransE [15], and ITransF [16]) |
| LAS.md | TEKE | oui | nd RTransE [32] exploit relation paths, TEKE [33] and DKRL [34] embed knowledge grap |
| LAS.md | TKRL | oui | ove the task. For example, SSE [29] and TKRL [30] consider the entity type, PTransE |
| LAS.md | TransA | oui | [7], TransR [8], TransD [9], KG2E [10], TransA [11], TranSparse [12], TransG [13], STr |
| LAS.md | TransG | oui | G2E [10], TransA [11], TranSparse [12], TransG [13], STransE [14], puTransE [15], and |
| LAS.md | TransH | oui | slation-based models (e.g., TransE [6], TransH [7], TransR [8], TransD [9], KG2E [10], |
| LAS.md | TranSparse | oui | 8], TransD [9], KG2E [10], TransA [11], TranSparse [12], TransG [13], STransE [14], puTran |
| LAS.md | TransR | oui | d models (e.g., TransE [6], TransH [7], TransR [8], TransD [9], KG2E [10], TransA [11] |
| Localcognitive.md | Relation-adaptive translating Embedding | oui | 10.04863v1 [cs.CL] 10 Oct 2020 # RatE: Relation-Adaptive Translating Embedding for Knowledge Graph Completion **Hao H |
| Localcognitive.md | TorusE | **NON** | — |
| Localcognitive.md | TransD | **NON** | — |
| Localcognitive.md | TransH | **NON** | — |
| Localcognitive.md | TransR | **NON** | — |
| LTS.md | GAN | oui | c distribution sampling, represented by GAN[2], is used to provide high quality neg |
| MCNS.md | FastGCN | oui | lleviate the receptive field expansion. FastGCN [5] adopts importance sampling in each |
| MCNS.md | LINE | oui | Embedding methods (e.g. DeepWalk [27], LINE [32]) and Graph Neural Networks (e.g. G |
| MCNS.md | node2vec | oui | s, such as DeepWalk [27], LINE [32] and node2vec [11], actually assign each node two emb |
| NMiss.md | ComplEx | oui | methods – RESCAL, TransE, DistMult and ComplEx – and evaluate on benchmark datasets – |
| NMiss.md | HolE | oui | s as well as the Holographic Embedding (HolE) model, so HolE was not included<sup>1< |
| NMiss.md | Neural Tensor Networks | oui | ns. Methods such as **Rescal** [21] and Neural Tensor Networks [24] learn millions of parameters that |
| NoiGAN.md | CKRL | oui | 19)), (3) noise aware KGE models (e.g., CKRL (Xie et al., 2018)) and (4) KGE models |
| NoiGAN.md | ComplEx | oui | 2011), DistMult (Yang et al., 2014) and ComplEx (Trouillon et al., 2016). To optimize t |
| NoiGAN.md | RESCAL | oui | esentations. The typical models include RESCAL (Nickel et al., 2011), DistMult (Yang e |
| NoiGAN.md | TransH | oui | relation. TransE (Bordes et al., 2013), TransH (Wang et al., 2014) and TransR (Lin et |
| NoiGAN.md | TransR | oui | , 2013), TransH (Wang et al., 2014) and TransR (Lin et al., 2015) are the representati |
| NSCaching.md | ANALOGY | oui | DistMult [46], HolE [31], ComplEx [38], ANALOGY [27], etc. All these methods are summar |
| NSCaching.md | HolE | oui | e variants of RESCAL are DistMult [46], HolE [31] and ComplEx [38]. DistMult simplif |
| NSCaching.md | ManifoldE | oui | nsD [20], TranSparse [21], TransM [11], ManifoldE [45], etc., and semantic matching model |
| NSCaching.md | RESCAL | oui | e plausibility of triplets $(h, r, t)$. RESCAL [32] is the most original model. The en |
| NSCaching.md | TransM | oui | nsR [26], TransD [20], TranSparse [21], TransM [11], ManifoldE [45], etc., and semanti |
| NSCaching.md | TranSparse | oui | TransH [42], TransR [26], TransD [20], TranSparse [21], TransM [11], ManifoldE [45], etc. |
| NSCaching.md | TransR | oui | his problem, variants like TransH [42], TransR [26], TransD [20] are introduced to pro |
| PNS.md | TransG | oui | o the current state-of-the-art approach TransG[4] to further improve its performance. |
| RAAKGC.md | BERTRL | oui | lation-aware neighborhood of the query. BERTRL (Zha, Chen, and Yan 2022) collects poss |
| RAAKGC.md | ConKGC | oui | he query as extra context to the model. ConKGC (Shang et al. 2023) introduces a sampli |
| RAAKGC.md | DKRL | oui | . 2024). The pioneer text-based method, DKRL (Xie et al. 2016), initially integrates |
| RAAKGC.md | GenKGC | oui | sion. Besides the mentioned algorithms, GenKGC (Xie et al. 2022) and KICGPT (Wei et al |
| RAAKGC.md | KEPLER | oui | ng KG-BERT (Yao, Mao, and Luo 2019) and KEPLER (Wang et al. 2021b), utilize a Pre-trai |
| RAAKGC.md | KG-S2S | oui | KGT5-context (Kochsiek et al. 2023) and KG-S2S (Chen et al. 2022a) model the link pred |
| RAAKGC.md | KGT5-context | oui | r encoding text descriptions. Moreover, KGT5-context (Kochsiek et al. 2023) and KG-S2S (Chen |
| RAAKGC.md | KICGPT | oui | lgorithms, GenKGC (Xie et al. 2022) and KICGPT (Wei et al. 2023) go beyond the neighbo |
| RAAKGC.md | LMKE | oui | s by the decoder directly. Furthermore, LMKE (Wang et al. 2022b) introduces a contra |
| RandomCorrupt.md | ConvE | oui | combine the two entities in a triple. **ConvE** (Dettmers et al., 2017) uses a convol |
| RandomCorrupt.md | HOLE | oui | **DistMult** into the complex space. **HOLE** (Nickel et al., 2016) employs circula |
| RandomCorrupt.md | ManifoldE | oui | tors of entities into various spaces. **ManifoldE** (Xiao et al., 2016) embeds a triple a |
| RandomCorrupt.md | PTransE | oui | ), **TransR** (Lin et al., 2015b) and **PTransE** (Lin et al., 2015a). However, limited |
| RandomCorrupt.md | RESCAL | oui | le as a manifold rather than a point. **RESCAL** (Nickel et al., 2011) is one of the e |
| RandomCorrupt.md | TransD | oui | ), **TransR** (Lin et al., 2015b) and **TransD** (Ji et al., 2015), extend **TransE** |
| RandomCorrupt.md | TransH | oui | ed embedding. Later variants, such as **TransH** (Wang et al., 2014), **TransR** (Lin |
| RandomCorrupt.md | TransR | oui | ch as **TransH** (Wang et al., 2014), **TransR** (Lin et al., 2015b) and **TransD** (J |
| RCWC.md | RESCAL | oui | trix $M_r$ is used to model a relation. RESCAL [Nickel et al., 2011] suffers from mode |
| RCWC.md | TransH | oui | $r \approx 0$ for symmetric relations. TransH [Lin et al., 2015] and TransR [Lin et a |
| RCWC.md | TransR | oui | elations. TransH [Lin et al., 2015] and TransR [Lin et al., 2015] model symmetric rela |
| ReasonKGE.md | Embed2Reason | oui | mpling. For example, a related method *Embed2Reason (E2R)* has been proposed by Garg *et al |
| RUGA.md | RESCAL | oui | coring function. Typical models include RESCAL<sup>[13]</sup>, DistMult<sup>[14]</sup> |
| RUGA.md | TransD | oui | H<sup>[9]</sup>, TransR<sup>[10]</sup>, TransD<sup>[11]</sup> and so on. As shown in F |
| RUGA.md | TransH | oui | ne to expand and apply TranE, including TransH<sup>[9]</sup>, TransR<sup>[10]</sup>, T |
| RUGA.md | TransR | oui | TranE, including TransH<sup>[9]</sup>, TransR<sup>[10]</sup>, TransD<sup>[11]</sup> a |
| SelfAdv.md | KG2E | oui | We also compare an additional approach KG2E_KL (He et al., 2015), which is a probab |
| SelfAdv.md | STransE | oui | 2014), TransR (Lin et al., 2015b), and STransE (Nguyen et al., 2016), where $g_{r,i}(\ |
| SelfAdv.md | TorusE | oui | and concurrent work to our work is the TorusE (Ebisu & Ichise, 2018) model, which def |
| SelfAdv.md | TransH | oui | ide range of TransE’s variants, such as TransH (Wang et al., 2014), TransR (Lin et al. |
| SelfAdv.md | TransR | oui | ts, such as TransH (Wang et al., 2014), TransR (Lin et al., 2015b), and STransE (Nguye |
| SparseNSG.md | NTN | oui | other kinds of models, such as SE, SME, NTN. However, a practical knowledge graph i |
| SparseNSG.md | SE | oui | 15], and other kinds of models, such as SE, SME, NTN. However, a practical knowled |
| SparseNSG.md | SME | oui | ter contains, Semantic Matching Energy (SME) [10], Semantically Smooth Embedding (S |
| SparseNSG.md | SSE | oui | E) [10], Semantically Smooth Embedding (SSE) [11], and translation-based methods [1 |
| SparseNSG.md | TransA | oui | sing, some presentation models, such as TransA [16], TransG [19], replace the relation |
| SparseNSG.md | TransD | oui | ls, such as TransE, TransH, TransR, and TransD [15], and other kinds of models, such a |
| SparseNSG.md | TransG | oui | esentation models, such as TransA [16], TransG [19], replace the relation of a triplet |
| SparseNSG.md | TranSparse | oui | ment, widely used in TransR, TransD and TranSparse [18], can effectively reduce the probab |
| SparseNSG.md | TransR | oui | s, such as TransE [12], TransH [13] and TransR [14], are the most used knowledge graph |
| STC.md | DKRL | oui | s, entity names or entity descriptions. DKRL [Xie *et al.*, 2016] proposes descripti |
| STC.md | NTN | oui | triples, is significant for RL in KGs. NTN [Socher *et al.*, 2013] encodes 3-way t |
| STC.md | SME | oui | 2011; 2012], SE [Bordes et al., 2011], SME [Bordes et al., 2012; 2014] and LFM [Je |
| STC.md | TransD | oui | judging the distance between entities. TransD [Ji *et al.*, 2015] proposes dynamic ma |
| STC.md | TransH | oui | o-1 and N-to-N. To address this issue, TransH [Wang *et al.*, 2014b] interprets relat |
| STC.md | Type-embodied Knowledge Representation Learning | oui | paper, we propose a novel method named Type-embodied Knowledge Representation Learning (TKRL) to take advantages of hie… |
| TANS.md | BERT | oui | s, Clark et al. (2020a) indicate that a BERT (Devlin et al., 2019)-like model ELECTR |
| TANS.md | ELECTRA | oui | a BERT (Devlin et al., 2019)-like model ELECTRA (Clark et al., 2020b) uses the NS loss |
| TANS.md | GenKGC | oui | ods like KGT5 (Saxena et al., 2022) and GenKGC (Xie et al., 2022) are unique in direct |
| TANS.md | KEPLER | oui | guage model (PLM)-based approaches like KEPLER (Wang et al., 2021) and SimKGC (Wang et |
| TANS.md | KGT5 | oui | ning. Generation-based KGC methods like KGT5 (Saxena et al., 2022) and GenKGC (Xie e |
| TANS.md | SimKGC | oui | hes like KEPLER (Wang et al., 2021) and SimKGC (Wang et al., 2022) also have an import |
| TANS.md | word2vec | oui | n et al. (2019) import subsampling from word2vec (Mikolov et al., 2013) to KGE. Subsampl |
| TruncatedNS.md | BootEA | oui | ame, relationship, and attribute views. BootEA [24] proposes iterative entity alignmen |
| TruncatedNS.md | CrossE | oui | sed in the entity triple, respectively. CrossE [13] believes that bidirectional effect |
| TruncatedNS.md | DAT | oui | y updated using newly aligned entities. DAT [21] encodes both entity names and enti |
| TruncatedNS.md | HAKE | oui | modelled entities in hyperbolic space. HAKE [16] believes that polar coordinates ar |
| TruncatedNS.md | KD-CoE | oui | been abstracted to related data types. KD-CoE [26] jointly learns multi-lingual entit |
| TruncatedNS.md | MultiKE | oui | function of the interaction embeddings. MultiKE [23] uses multiple views of entities to |
| TruncatedNS.md | MuRP | oui | d as rotation changes in complex space. MuRP [15] points out that the relationships |
| TruncatedNS.md | RESCAL | oui | ions to gauge the rationality of facts. RESCAL [11] was the earliest semantic matching |
| TruncatedNS.md | RotatE | oui | ntities and relationships. According to RotatE [14], which can model and infer differe |
| TruncatedNS.md | SimplE | oui | ons between latent factors of entities. SimplE [12] restricts the relationship matrix |
| TruncatedNS.md | TransD | oui | wo different projection matrices by the TransD [17] model, respectively. According to |
| TruncatedNS.md | TransEdge | oui | erforms well in handling tail entities. TransEdge [22] interacts with embeddings between |
| TruncatedNS.md | TransH | oui | n the corresponding relationship space. TransH [19] thinks an entity can have many rep |
| TruncatedNS.md | TransR | oui | [17] model, respectively. According to TransR [18], each entity is made up of several |
| TuckerDNCaching.md | RESCAL | **NON** | — |
| TuckerDNCaching.md | RotatE | oui | ich has an impact on efficiency. Later, RotatE (Sun et al., 2019) introduced a self-ad |
| TuckerDNCaching.md | TorusE | oui | lational distance-based models, such as TorusE (Ebisu et al., 2018), by addressing the |
| TuckerDNCaching.md | TuckER | oui | ng: high-quality negative sampling with tucker decomposition Tiroshan Madushanka<sup> |
| TypeAugmented.md | CAKE | oui | esides, Niu et al.<sup>33</sup> propose CAKE which automatically extract commonsense |
| TypeAugmented.md | HAKE | oui | g to tail embedding. Soon after RotatE, HAKE<sup>16</sup> and RatE<sup>17</sup> make |
| TypeAugmented.md | JOIE | oui | ons to model the semantic transitivity. JOIE<sup>24</sup> directly represents a KG a |
| TypeAugmented.md | RatE | oui | oon after RotatE, HAKE<sup>16</sup> and RatE<sup>17</sup> make slight improvements t |
| TypeAugmented.md | TaKE | oui | ed Knowledge graph Embedding framework (TaKE) which could utilize type features to e |
| TypeAugmented.md | TaRP | oui | two views. Both TransT<sup>30</sup> and TaRP<sup>32</sup> collect relation types fro |
| TypeAugmented.md | TKRL | oui | xploring the usage of type information. TKRL<sup>22</sup> extends traditional TransE |
| TypeAugmented.md | TransC | oui | nct representations in different types. TransC<sup>23</sup> clearly distinguish concep |
| TypeAugmented.md | TransH | oui | of TransE have been developed. Such as, TransH<sup>13</sup> projects entity embeddings |
| TypeAugmented.md | TransR | oui | stead of relation-specific hyperplanes, TransR<sup>14</sup> directly projects entity e |
| TypeAugmented.md | TransT | oui | d jointly encodes these two views. Both TransT<sup>30</sup> and TaRP<sup>32</sup> coll |
| TypeConstraints.md | Neural Tensor Network | oui | deling of KGs. [20] recently proposed a neural tensor network, which we did not consider in our study |
| TypeConstraints.md | TransH | oui | network proposed in [20]. [23] proposed TransH which improves TransE’s capability to m |
| TypeConstraints.md | TransR | oui | further extended in [14] by introducing TransR which separates representations of enti |
| Uniform.md | Neural Tensor Model | oui | point. Another related approach is the Neural Tensor Model [14]. A special case of this model corr |

## C1. Candidats faux négatifs — ÉVALUÉS (38)

| Article | Entité | Où | Extrait |
|---|---|:---:|---|
| ASA.md | GCN | prose+table | egating the neighbors' information. **R-GCN** (Schlichtkrull et al. 2018) considers |
| BatchNS.md | GCN | prose+table | al., 2018). The problem studied by the GCN is different than the one solved by PBG |
| CAKE.md | CAKE | prose+table | Xiv:2202.13785v3 [cs.AI] 17 Apr 2022 # CAKE: A Scalable Commonsense-Aware Framework |
| dans.md | CAKE | prose+table | nerate informative negative triplets; **CAKE** [19]: a framework which leverages ext |
| dans.md | KBGAN | prose+table | ous state-of-the-art approaches such as KBGAN [3], we adopt a generative adversarial |
| DHNS.md | KBGAN | prose+table | nerate higher-quality negative triples. KBGAN [4] and IGAN [30] use Generative Advers |
| DHNS.md | OTE | prose+table | x [27], RotatE [25], PairRE [7], and GC-OTE [26]. (2) **Multimodal KGC models:** w |
| DomainNS.md | KG2E | table | 0.2</td> </tr> <tr> <td>KG2E (He et al., 2015)</td> <td>No</ |
| DomainNS.md | NTN | table | 6.7</td> </tr> <tr> <td>NTN (Socher et al., 2013)</td> <td> |
| DomainNS.md | SE | table | </thead> <tbody> <tr> <td>SE (Bordes et al., 2011)</td> <td> |
| DomainNS.md | Unstructured | table | 9.8</td> </tr> <tr> <td>Unstructured (Bordes et al., 2014)</td> <td> |
| EANS.md | KBGAN | table | 501</td> </tr> <tr> <td>KBGAN(Cai and Wang, 2017)<sup>††</sup></td> |
| ERDNS.md | KBGAN | prose+table | natural language processing (NLP) [7]. KBGAN [3], IGAN [26], and NSCaching [34] crea |
| GibbsNS.md | KBGAN | prose+table | is of static negative sampling methods, KBGAN [17] found that the majority of negativ |
| HTENS.md | KBGAN | prose+table | The GAN-based sampling methods, such as KBGAN[3] and IGAN[13], set the KGE model to b |
| IGAN.md | SE | prose+table | results show that 1. Models including SE, SME(bilinear), TransE and TransH are f |
| IGAN.md | SME | prose+table | ults show that 1. Models including SE, SME(bilinear), TransE and TransH are furthe |
| IGAN.md | Unstructured | prose+table | ages (Xie et al. 2016a) of entities. **Unstructured Model** (Bordes et al. 2012; Bordes et |
| KBGAN.md | KBGAN | prose+table | Xiv:1711.04071v3 [cs.CL] 16 Apr 2018 # KBGAN: Adversarial Learning for Knowledge Gra |
| KSGAN.md | KBGAN | prose+table | ed by an adversarial learning framework KBGAN, this paper proposes a new knowledge se |
| LAS.md | GCN | prose+table | ls, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also achieve good results for lin |
| LAS.md | KBGAN | prose+table | h outperforms GAN-based sampling method KBGAN. **INDEX TERMS** Knowledge graph, know |
| LEMON.md | KBGAN | table | 1)$</td> </tr> <tr> <td>KBGAN [6]</td> <td>$\mathcal{O}(t)$</ |
| LTS.md | LFM | table | 1.3</td> </tr> <tr> <td>LFM</td> <td>469</td> <td>4 |
| LTS.md | SME | table | 9.8</td> </tr> <tr> <td>SME</td> <td>542/526</td> < |
| M2ixKG.md | KBGAN | prose+table | tribution. IGAN [Wang et al., 2018] and KBGAN [Cai and Wang, 2018] introduce generati |
| MCNS.md | KBGAN | prose+table | ptively generate hard negative samples. KBGAN [3] employs a sampling-based adaptation |
| MDNCaching.md | KBGAN | prose+table | ative sampling strategies IGAN [12] and KBGAN [3] were introduced to generate negativ |
| NSCaching.md | KBGAN | prose+table | wo pioneered works, i.e., IGAN [39] and KBGAN [9], attempting to address these challe |
| ReasonKGE.md | ReasonKGE | prose+table | we present a novel iterative approach *ReasonKGE* that identifies dynamically via symbol |
| SANS.md | KBGAN | prose+table | egative sampling (Bordes et al., 2013), KBGAN (Cai and Wang, 2018), and NSCaching (Zh |
| SelfAdv.md | KBGAN | prose+table | en from (Cai (Cai & Wang, 2017), where KBGAN uses a ComplEx negative sample generato |
| SelfAdv.md | SE | table | </thead> <tbody> <tr> <td>SE (Bordes et al., 2011)</td> <td>$- |
| SNS.md | KBGAN | prose+table | trained to learn embeddings. IGAN [8], KBGAN [3], KSGAN [7] are three existing GAN-b |
| STC.md | TKRL | prose+table | died Knowledge Representation Learning (TKRL) to take advantages of hierarchical ent |
| TuckerDNCaching.md | KBGAN | prose+table | ributions, IGAN (Wang et al., 2018) and KBGAN (Cai et al., 2018) were introduced as n |
| Uniform.md | SE | prose+table | those of [3] (Structured Embeddings or SE) and [14]. 3 Table 1: **Numbers of pa |
| Uniform.md | SME | prose+table | 2], and the energy-based models SE [3], SME(linear)/SME(bilinear) [2] and LFM [6]. |

## C2. Candidats faux négatifs — MENTIONNÉS (11)

| Article | Entité | Où | Extrait |
|---|---|:---:|---|
| ConceptDriven.md | CAKE | prose | Commonsense-Aware Knowledge Embedding (CAKE) framework, which consists of automatic |
| DeMix.md | CAKE | prose | *CANS* [16]. The CANS is a component of CAKE [16] responsible for solving the invali |
| DeMix.md | KBGAN | prose | triples with high scores. For example, KBGAN[6] and IGAN[23] introduce a generative |
| DMNS.md | GraphSAGE | prose | conduct experiments using GAT [45] and GraphSAGE (SAGE) [14]. For GCN, we employ two lay |
| GNDN.md | GCN | prose | sists of a Convolutional Graph Network (GCN) [39] based encoder for learning repres |
| HTENS.md | TKRL | prose | <sup>1</sup>https://github.com/thunlp/TKRL SIGIR ’23, July 23–27, 2023, Taipei, T |
| Localcognitive.md | KBGAN | prose | effectively learn structured knowledge. KBGAN (Cai and Wang, 2018) uses knowledge gra |
| NSCaching.md | LINE | prose | EGATIVE ENTITIES IN CACHE ON FB13. EACH LINE DISPLAYS 5 RANDOM SAMPLED NEGATIVE ENTI |
| RAAKGC.md | KGT5 | prose | r encoding text descriptions. Moreover, KGT5-context (Kochsiek et al. 2023) and KG-S |
| RUGA.md | KBGAN | prose | herefore, Liwei Cai et al.[16] proposed KBGAN to solve the problem that negative samp |
| TypeConstraints.md | SME | prose | sup>9</sup> https://github.com/glorotxa/SME <sup>10</sup> Mainly caused by the rank |