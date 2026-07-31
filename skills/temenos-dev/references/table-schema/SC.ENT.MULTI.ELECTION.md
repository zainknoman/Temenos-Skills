# SC.ENT.MULTI.ELECTION — Table Schema

> Source: `INSERTS/I_F.SC.ENT.MULTI.ELECTION` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ENT.MULTI.OPTION.DESC` | `ScEntMultiElection_OptionDesc` |  |  |  |
| 2 | `SC.ENT.MULTI.OPTION.IND` | `ScEntMultiElection_OptionInd` |  |  |  |
| 3 | `SC.ENT.MULTI.OPTION.NUM` | `ScEntMultiElection_OptionNum` |  |  |  |
| 4 | `SC.ENT.MULTI.ELECT.DATE` | `ScEntMultiElection_ElectDate` |  |  |  |
| 5 | `SC.ENT.MULTI.ELECT.TIME` | `ScEntMultiElection_ElectTime` |  |  |  |
| 6 | `SC.ENT.MULTI.ELECT.USER` | `ScEntMultiElection_ElectUser` |  |  |  |
| 7 | `SC.ENT.MULTI.ELECT.NOM` | `ScEntMultiElection_ElectNom` |  |  |  |
| 8 | `SC.ENT.MULTI.CANCELLED.NOMINAL` | `ScEntMultiElection_CancelledNominal` |  |  |  |
| 9 | `SC.ENT.MULTI.BENE.OWN.NARR` | `ScEntMultiElection_BeneOwnNarr` |  |  |  |
| 10 | `SC.ENT.MULTI.ADDL.NARR` | `ScEntMultiElection_AddlNarr` |  |  |  |
| 11 | `SC.ENT.MULTI.SEME.REFERENCE` | `ScEntMultiElection_SemeReference` |  |  |  |
| 12 | `SC.ENT.MULTI.DELIVERY.REF` | `ScEntMultiElection_DeliveryRef` |  |  |  |
| 13 | `SC.ENT.MULTI.QUALIFY.HOLDING` | `ScEntMultiElection_QualifyHolding` | TField |  | This field will hold Qualify Holding mapped from ENTITLEMENT |
| 14 | `SC.ENT.MULTI.INST.STATUS` | `ScEntMultiElection_InstStatus` |  |  |  |
| 15 | `SC.ENT.MULTI.CANCELLED.REF` | `ScEntMultiElection_CancelledRef` |  |  |  |
| 16 | `SC.ENT.MULTI.CANC.REQ.NOM` | `ScEntMultiElection_CancReqNom` |  |  |  |
| 17 | `SC.ENT.MULTI.OPTION.NOM` | `ScEntMultiElection_OptionNom` |  |  |  |
| 18 | `SC.ENT.MULTI.567.REFERENCE` | `ScEntMultiElection_567Reference` |  |  |  |
| 19 | `SC.ENT.MULTI.ELECT.REFERENCE` | `ScEntMultiElection_ElectReference` |  |  |  |
| 20 | `SC.ENT.MULTI.ENTITLEMENT.AMT` | `ScEntMultiElection_EntitlementAmt` |  |  |  |
| 21 | `SC.ENT.MULTI.ENTITLEMENT.AMT.RECD` | `ScEntMultiElection_EntitlementAmtRecd` |  |  |  |
| 22 | `SC.ENT.MULTI.NEW.SEC.NO` | `ScEntMultiElection_NewSecNo` |  |  |  |
| 23 | `SC.ENT.MULTI.NOMINAL` | `ScEntMultiElection_Nominal` |  |  |  |
| 24 | `SC.ENT.MULTI.NOMINAL.RECD` | `ScEntMultiElection_NominalRecd` |  |  |  |
| 25 | `SC.ENT.MULTI.566.REFERENCE` | `ScEntMultiElection_566Reference` |  |  |  |
| 26 | `SC.ENT.MULTI.RECON.STATUS` | `ScEntMultiElection_ReconStatus` |  |  |  |
