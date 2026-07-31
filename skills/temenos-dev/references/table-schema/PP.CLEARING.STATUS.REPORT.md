# PP.CLEARING.STATUS.REPORT — Table Schema

> Source: `INSERTS/I_F.PP.CLEARING.STATUS.REPORT` in `PP_ClearingStatusReport.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCSR.FileReferenceIncoming` | `PpClearingStatusReport_Filereferenceincoming` | TField |  |  |
| 2 | `PPCSR.BulkReferenceIncoming` | `PpClearingStatusReport_Bulkreferenceincoming` | TField |  |  |
| 3 | `PPCSR.MessageReferenceIncoming` | `PpClearingStatusReport_Messagereferenceincoming` | TField |  |  |
| 4 | `PPCSR.StsId` | `PpClearingStatusReport_Stsid` | TField |  |  |
| 5 | `PPCSR.OrglInstrId` | `PpClearingStatusReport_Orglinstrid` | TField |  |  |
| 6 | `PPCSR.OrglEndToEndId` | `PpClearingStatusReport_Orglendtoendid` | TField |  |  |
| 7 | `PPCSR.OrglTrxId` | `PpClearingStatusReport_Orgltrxid` | TField |  |  |
| 8 | `PPCSR.TrxSts` | `PpClearingStatusReport_Trxsts` | TField |  |  |
| 9 | `PPCSR.TrxStsChgsInfAm` | `PpClearingStatusReport_Trxstschgsinfam` | TField |  |  |
| 10 | `PPCSR.TrxStsChgsInfCcy` | `PpClearingStatusReport_Trxstschgsinfccy` | TField |  |  |
| 11 | `PPCSR.TrxStsChgsInfPartyFinInstIdBIC` | `PpClearingStatusReport_Trxstschgsinfpartyfininstidbic` | TField |  |  |
| 12 | `PPCSR.StsRsnInfOrgnName` | `PpClearingStatusReport_Stsrsninforgnname` | TField |  |  |
| 13 | `PPCSR.StsRsnInfOrgnIdOrgIdBIC` | `PpClearingStatusReport_Stsrsninforgnidorgidbic` | TField |  |  |
| 14 | `PPCSR.StsRsnInfOrgnIdOrgIdOthId` | `PpClearingStatusReport_Stsrsninforgnidorgidothid` | TField |  |  |
| 15 | `PPCSR.StsRsnInfRsnCd` | `PpClearingStatusReport_Stsrsninfrsncd` | TField |  |  |
| 16 | `PPCSR.StsRsnInfRsnProp` | `PpClearingStatusReport_Stsrsninfrsnprop` | TField |  |  |
| 17 | `PPCSR.StsRsnInfAdInf` | `PpClearingStatusReport_Stsrsninfadinf` | TField |  |  |
| 18 | `PPCSR.OrglItbkSttlAm` | `PpClearingStatusReport_Orglitbksttlam` | TField |  |  |
| 19 | `PPCSR.OrglItbkSttlAmCcy` | `PpClearingStatusReport_Orglitbksttlamccy` | TField |  |  |
| 20 | `PPCSR.OrglItbkSttlDt` | `PpClearingStatusReport_Orglitbksttldt` | TField |  |  |
| 21 | `PPCSR.OrglDbtAgBICFI` | `PpClearingStatusReport_Orgldbtagbicfi` | TField |  |  |
| 22 | `PPCSR.OrglDbtAgCgSysMemIdCgSysIdCd` | `PpClearingStatusReport_Orgldbtagcgsysmemidcgsysidcd` | TField |  |  |
| 23 | `PPCSR.OrglDbtAgCgSysMemIdCgSysIdProp` | `PpClearingStatusReport_Orgldbtagcgsysmemidcgsysidprop` | TField |  |  |
| 24 | `PPCSR.OrglDbtAgCgSysMemId` | `PpClearingStatusReport_Orgldbtagcgsysmemid` | TField |  |  |
| 25 | `PPCSR.OrglCrdAgBICFI` | `PpClearingStatusReport_Orglcrdagbicfi` | TField |  |  |
| 26 | `PPCSR.OrglCrdAgCgSysMemIdCgSysIdCd` | `PpClearingStatusReport_Orglcrdagcgsysmemidcgsysidcd` | TField |  |  |
| 27 | `PPCSR.OrglCrdAgCgSysMemIdCgSysIdProp` | `PpClearingStatusReport_Orglcrdagcgsysmemidcgsysidprop` | TField |  |  |
| 28 | `PPCSR.OrglCrdAgCgSysMemId` | `PpClearingStatusReport_Orglcrdagcgsysmemid` | TField |  |  |
