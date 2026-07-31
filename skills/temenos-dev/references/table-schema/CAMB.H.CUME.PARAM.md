# CAMB.H.CUME.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.H.CUME.PARAM` in `CABASE_CustomerRelation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.CUME.PER.CUS.TYPE` | `CambHCumeParam_PerCusType` | TField |  |  |
| 2 | `CAMB.CUME.BUS.CUS.TYPE` | `CambHCumeParam_BusCusType` | TField |  |  |
| 3 | `CAMB.CUME.PER.MEM.TYPE` | `CambHCumeParam_PerMemType` |  |  |  |
| 4 | `CAMB.CUME.BUS.MEM.TYPE` | `CambHCumeParam_BusMemType` |  |  |  |
| 5 | `CAMB.CUME.JUNIOR.IND` | `CambHCumeParam_JuniorInd` | TField |  |  |
| 6 | `CAMB.CUME.SENIOR.IND` | `CambHCumeParam_SeniorInd` | TField |  |  |
| 7 | `CAMB.CUME.REGULAR.IND` | `CambHCumeParam_RegularInd` | TField |  |  |
| 8 | `CAMB.CUME.CUS.CLOSE.FREQ` | `CambHCumeParam_CusCloseFreq` | TField |  |  |
| 9 | `CAMB.CUME.CUS.CLOSED.STATUS` | `CambHCumeParam_CusClosedStatus` | TField |  |  |
| 10 | `CAMB.CUME.MEM.CLOSED.STATUS` | `CambHCumeParam_MemClosedStatus` |  |  |  |
| 11 | `CAMB.CUME.BRD.REV.STATUS` | `CambHCumeParam_BrdRevStatus` | TField |  |  |
| 12 | `CAMB.CUME.DECEASED.STATUS` | `CambHCumeParam_DeceasedStatus` | TField |  |  |
| 13 | `CAMB.CUME.JUNIOR.AGE` | `CambHCumeParam_JuniorAge` | TField |  |  |
| 14 | `CAMB.CUME.JUNIOR.STATUS` | `CambHCumeParam_JuniorStatus` | TField |  |  |
| 15 | `CAMB.CUME.REGULAR.AGE` | `CambHCumeParam_RegularAge` | TField |  |  |
| 16 | `CAMB.CUME.REGULAR.STATUS` | `CambHCumeParam_RegularStatus` | TField |  |  |
| 17 | `CAMB.CUME.SENIOR.AGE` | `CambHCumeParam_SeniorAge` | TField |  |  |
| 18 | `CAMB.CUME.SENIOR.STATUS` | `CambHCumeParam_SeniorStatus` | TField |  |  |
| 19 | `CAMB.CUME.IDLE.DAYS` | `CambHCumeParam_IdleDays` | TField |  |  |
| 20 | `CAMB.CUME.OFS.VERSION` | `CambHCumeParam_OfsVersion` | TField |  |  |
| 21 | `CAMB.CUME.OFS.USER` | `CambHCumeParam_OfsUser` | TField |  |  |
| 22 | `CAMB.CUME.OFS.PASSWORD` | `CambHCumeParam_OfsPassword` | TField |  |  |
| 23 | `CAMB.CUME.OFS.SOURCE` | `CambHCumeParam_OfsSource` | TField |  |  |
| 24 | `CAMB.CUME.SOLE.SECTOR` | `CambHCumeParam_SoleSector` | TField |  |  |
| 25 | `CAMB.CUME.SOLE.INDUSTRY` | `CambHCumeParam_SoleIndustry` | TField |  |  |
| 26 | `CAMB.CUME.PER.SECTOR` | `CambHCumeParam_PerSector` |  |  |  |
| 27 | `CAMB.CUME.UNDOC.INDUSTRY` | `CambHCumeParam_UndocIndustry` | TField |  |  |
| 28 | `CAMB.CUME.NOSHARE.OWN.SECTOR` | `CambHCumeParam_NoshareOwnSector` |  |  |  |
| 29 | `CAMB.CUME.NO.TRADE.SECTOR` | `CambHCumeParam_NoTradeSector` |  |  |  |
| 30 | `CAMB.CUME.NO.TRADE.INDUSTRY` | `CambHCumeParam_NoTradeIndustry` |  |  |  |
| 31 | `CAMB.CUME.TRADE.INDUSTRY` | `CambHCumeParam_TradeIndustry` |  |  |  |
| 32 | `CAMB.CUME.DBA.SECTOR` | `CambHCumeParam_DbaSector` |  |  |  |
| 33 | `CAMB.CUME.NO.DBA.INDUSTRY` | `CambHCumeParam_NoDbaIndustry` |  |  |  |
| 34 | `CAMB.CUME.IN.TRUST.INDUSTRY` | `CambHCumeParam_InTrustIndustry` |  |  |  |
| 35 | `CAMB.CUME.SUFFIX.INDUSTRY` | `CambHCumeParam_SuffixIndustry` |  |  |  |
| 36 | `CAMB.CUME.BUS.NAME.SUFFIX` | `CambHCumeParam_BusNameSuffix` |  |  |  |
| 37 | `CAMB.CUME.DIR.INDUSTRY` | `CambHCumeParam_DirIndustry` |  |  |  |
| 38 | `CAMB.CUME.NON.GOV.IDS` | `CambHCumeParam_NonGovIds` |  |  |  |
| 39 | `CAMB.CUME.INDIAN.STATUS` | `CambHCumeParam_IndianStatus` |  |  |  |
| 40 | `CAMB.CUME.NO.HEALTH.ID.PROV` | `CambHCumeParam_NoHealthIdProv` |  |  |  |
| 41 | `CAMB.CUME.STAFF.INDUSTRY` | `CambHCumeParam_StaffIndustry` |  |  |  |
| 42 | `CAMB.CUME.START.INT.RATE` | `CambHCumeParam_StartIntRate` | TField |  |  |
| 43 | `CAMB.CUME.END.INT.RATE` | `CambHCumeParam_EndIntRate` | TField |  |  |
| 44 | `CAMB.CUME.CHK.EXCEPTION` | `CambHCumeParam_ChkException` | TField |  |  |
| 45 | `CAMB.CUME.BROKER.SECTOR` | `CambHCumeParam_BrokerSector` | TField |  |  |
| 46 | `CAMB.CUME.PER.MMBRSHIP.TYPE` | `CambHCumeParam_PerMmbrshipType` | TField |  |  |
| 47 | `CAMB.CUME.BUS.MMBRSHIP.TYPE` | `CambHCumeParam_BusMmbrshipType` | TField |  |  |
| 48 | `CAMB.CUME.PER.DISFLG.ERR.MSG` | `CambHCumeParam_PerDisflgErrMsg` | TField |  |  |
| 49 | `CAMB.CUME.BUS.DISFLG.ERR.MSG` | `CambHCumeParam_BusDisflgErrMsg` | TField |  |  |
| 50 | `CAMB.CUME.RECORD.STATUS` | `CambHCumeParam_RecordStatus` | String |  |  |
| 51 | `CAMB.CUME.CURR.NO` | `CambHCumeParam_CurrNo` | String |  |  |
| 52 | `CAMB.CUME.INPUTTER` | `CambHCumeParam_Inputter` |  |  |  |
| 53 | `CAMB.CUME.DATE.TIME` | `CambHCumeParam_DateTime` |  |  |  |
| 54 | `CAMB.CUME.AUTHORISER` | `CambHCumeParam_Authoriser` | String |  |  |
| 55 | `CAMB.CUME.CO.CODE` | `CambHCumeParam_CoCode` | String |  |  |
| 56 | `CAMB.CUME.DEPT.CODE` | `CambHCumeParam_DeptCode` | String |  |  |
| 57 | `CAMB.CUME.AUDITOR.CODE` | `CambHCumeParam_AuditorCode` | String |  |  |
| 58 | `CAMB.CUME.AUDIT.DATE.TIME` | `CambHCumeParam_AuditDateTime` | String |  |  |
