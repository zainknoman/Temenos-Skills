# ESB / Non-ESB Integration Package Reference

Source: `bnk/ESBProjects/`, `bnk/NonESBProjects/`, verified 2026-07-31 against a
real R25 install. Each package directory contains an `ESB_SOURCE/` subfolder
with the actual integration source — this file lists which packages exist, not
their internal contents (not yet surveyed).

## `bnk/ESBProjects/` — 72 packages

```
AC        BU        CGSWMX    DD        DE        DEMXTR    ESIBER    MXSECU
PI        PP        PPAACH    PPADEB    PPAUBD    PPAUBP    PPAUDE    PPAURX
PPBACS    PPBECS    PPC2BM    PPCHSI    PPCLIT    PPEPCP    PPESIC    PPESII
PPEWSP    PPHIG2    PPHINS    PPHKCQ    PPHKCX    PPHKFB    PPIC2B    PPICEF
PPIEBA    PPIHCT    PPINCT    PPINIP    PPINNP    PPINRX    PPINST    PPIPCL
PPISIP    PPITIP    PPLCIT    PPLNCL    PPMASV    PPNPCT    PPRPCL    PPRPCQ
PPSARI    PPSGMX    PPSICH    PPSWCL    PPSWCQ    PPSWCR    PPSWEI    PPSWMX
PPSYTC    PPTGMX    PPTGTC    PPTNCL    PPUFPS    PPUKCX    PPUSFI    PPUSFX
RF        RFPYEU    RFPYSA    RFUSFI    SC        SFRD25    SP        USRTGS
```

Naming pattern observed: the large `PP*` cluster (58 of the 72 packages) is
clearly a **payment-scheme integration family** — `PP` prefix, then a
scheme/country code. A few are confidently decodable by standard industry
acronym (`USRTGS` = US Real-Time Gross Settlement; `PPBACS` almost certainly
UK BACS; `PPBECS` almost certainly Australia's BECS). Most others (`PPHIG2`,
`PPSWMX`, `PPINRX`, etc.) are **not decoded here** — don't guess a scheme name
from the code; open the package's `ESB_SOURCE/` to confirm before telling a
developer what a given package integrates with.

Non-`PP` packages: `AC`, `BU`, `CGSWMX`, `DD`, `DE`, `DEMXTR`, `ESIBER`,
`MXSECU`, `PI`, `RF`, `RFPYEU`, `RFPYSA`, `RFUSFI`, `SC`, `SFRD25`, `SP` —
also not semantically decoded here.

## `bnk/NonESBProjects/` — 11 packages

```
CAHINS    CAHKRX    CAUSFI    PI        PP        PPAUBD
PPAUDE    PPAUNC    PPCAIC    PPHKCX    PPSICH
```

Note the overlap with the ESB tree (`PI`, `PP`, `PPAUBD`, `PPAUDE`, `PPHKCX`,
`PPSICH` appear in both) — these are **separate implementations**, not
shared code. See the "Two integration project trees" note in `SKILL.md`.

## Next step for a deeper survey

This file captures package *existence*, not package *purpose or dependency
graph*. If a task requires knowing exactly what a specific package does,
open its `ESB_SOURCE/` directory directly rather than relying on the name —
this reference has not been extended to that depth yet.
