# SZ.CUSTOMER.ENT.SUPP.INFO — Table Schema

> Source: `INSERTS/I_F.SZ.CUSTOMER.ENT.SUPP.INFO` in `SZ_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SZ.CSI.NATIONAL.IDENTIFIER` | `SzCustomerEntSuppInfo_NationalIdentifier` |  |  |  |
| 2 | `SZ.CSI.NATIONAL.IDENTIFIER.TYPE` | `SzCustomerEntSuppInfo_NationalIdentifierType` |  |  |  |
| 3 | `SZ.CSI.NI.RESERVED.05` | `SzCustomerEntSuppInfo_NiReserved05` |  |  |  |
| 4 | `SZ.CSI.NI.RESERVED.04` | `SzCustomerEntSuppInfo_NiReserved04` |  |  |  |
| 5 | `SZ.CSI.NI.RESERVED.03` | `SzCustomerEntSuppInfo_NiReserved03` |  |  |  |
| 6 | `SZ.CSI.NI.RESERVED.02` | `SzCustomerEntSuppInfo_NiReserved02` |  |  |  |
| 7 | `SZ.CSI.NI.RESERVED.01` | `SzCustomerEntSuppInfo_NiReserved01` |  |  |  |
| 8 | `SZ.CSI.VAT.ID` | `SzCustomerEntSuppInfo_VatId` | TField |  | It stores the Value Added Tax Id for corporate customers and banks |
| 9 | `SZ.CSI.LEGAL.FORM` | `SzCustomerEntSuppInfo_LegalForm` | TField |  | It stores the legal form of a company for corporate customers and banks |
| 10 | `SZ.CSI.IND.ECO.ACT.SCHEME` | `SzCustomerEntSuppInfo_IndEcoActScheme` |  |  |  |
| 11 | `SZ.CSI.IND.ECO.ACT.CODE` | `SzCustomerEntSuppInfo_IndEcoActCode` |  |  |  |
| 12 | `SZ.CSI.ECO.ACT.RESERVED.05` | `SzCustomerEntSuppInfo_EcoActReserved05` |  |  |  |
| 13 | `SZ.CSI.ECO.ACT.RESERVED.04` | `SzCustomerEntSuppInfo_EcoActReserved04` |  |  |  |
| 14 | `SZ.CSI.ECO.ACT.RESERVED.03` | `SzCustomerEntSuppInfo_EcoActReserved03` |  |  |  |
| 15 | `SZ.CSI.ECO.ACT.RESERVED.02` | `SzCustomerEntSuppInfo_EcoActReserved02` |  |  |  |
| 16 | `SZ.CSI.ECO.ACT.RESERVED.01` | `SzCustomerEntSuppInfo_EcoActReserved01` |  |  |  |
| 17 | `SZ.CSI.INST.SECTOR.CODE` | `SzCustomerEntSuppInfo_InstSectorCode` | TField |  | It is to capture Institutional sector code of the customer |
| 18 | `SZ.CSI.LEG.STAT.PROC` | `SzCustomerEntSuppInfo_LegStatProc` |  |  |  |
| 19 | `SZ.CSI.INIT.LEG.PROC.DATE` | `SzCustomerEntSuppInfo_InitLegProcDate` |  |  |  |
| 20 | `SZ.CSI.STAT.PROC.RESERVED.05` | `SzCustomerEntSuppInfo_StatProcReserved05` |  |  |  |
| 21 | `SZ.CSI.STAT.PROC.RESERVED.04` | `SzCustomerEntSuppInfo_StatProcReserved04` |  |  |  |
| 22 | `SZ.CSI.STAT.PROC.RESERVED.03` | `SzCustomerEntSuppInfo_StatProcReserved03` |  |  |  |
| 23 | `SZ.CSI.STAT.PROC.RESERVED.02` | `SzCustomerEntSuppInfo_StatProcReserved02` |  |  |  |
| 24 | `SZ.CSI.STAT.PROC.RESERVED.01` | `SzCustomerEntSuppInfo_StatProcReserved01` |  |  |  |
| 25 | `SZ.CSI.ENTERPRISE.SIZE` | `SzCustomerEntSuppInfo_EnterpriseSize` |  |  |  |
| 26 | `SZ.CSI.DATE.OF.ENTERPRISE.SIZE` | `SzCustomerEntSuppInfo_DateOfEnterpriseSize` |  |  |  |
| 27 | `SZ.CSI.NO.OF.EMPLOYEES` | `SzCustomerEntSuppInfo_NoOfEmployees` |  |  |  |
| 28 | `SZ.CSI.BAL.SHEET.TOT.CCY` | `SzCustomerEntSuppInfo_BalSheetTotCcy` |  |  |  |
| 29 | `SZ.CSI.BAL.SHEET.TOT` | `SzCustomerEntSuppInfo_BalSheetTot` |  |  |  |
| 30 | `SZ.CSI.ANN.TURNOVR.CCY` | `SzCustomerEntSuppInfo_AnnTurnovrCcy` |  |  |  |
| 31 | `SZ.CSI.ANN.TURNOVR` | `SzCustomerEntSuppInfo_AnnTurnovr` |  |  |  |
| 32 | `SZ.CSI.ES.RESERVED.05` | `SzCustomerEntSuppInfo_EsReserved05` |  |  |  |
| 33 | `SZ.CSI.ES.RESERVED.04` | `SzCustomerEntSuppInfo_EsReserved04` |  |  |  |
| 34 | `SZ.CSI.ES.RESERVED.03` | `SzCustomerEntSuppInfo_EsReserved03` |  |  |  |
| 35 | `SZ.CSI.ES.RESERVED.02` | `SzCustomerEntSuppInfo_EsReserved02` |  |  |  |
| 36 | `SZ.CSI.ES.RESERVED.01` | `SzCustomerEntSuppInfo_EsReserved01` |  |  |  |
| 37 | `SZ.CSI.RESERVED.71` | `SzCustomerEntSuppInfo_Reserved71` | TField |  |  |
| 38 | `SZ.CSI.RESERVED.70` | `SzCustomerEntSuppInfo_Reserved70` | TField |  |  |
| 39 | `SZ.CSI.RESERVED.69` | `SzCustomerEntSuppInfo_Reserved69` | TField |  |  |
| 40 | `SZ.CSI.RESERVED.68` | `SzCustomerEntSuppInfo_Reserved68` | TField |  |  |
| 41 | `SZ.CSI.RESERVED.67` | `SzCustomerEntSuppInfo_Reserved67` | TField |  |  |
| 42 | `SZ.CSI.RESERVED.66` | `SzCustomerEntSuppInfo_Reserved66` | TField |  |  |
| 43 | `SZ.CSI.RESERVED.65` | `SzCustomerEntSuppInfo_Reserved65` | TField |  |  |
| 44 | `SZ.CSI.RESERVED.64` | `SzCustomerEntSuppInfo_Reserved64` | TField |  |  |
| 45 | `SZ.CSI.RESERVED.63` | `SzCustomerEntSuppInfo_Reserved63` | TField |  |  |
| 46 | `SZ.CSI.RESERVED.62` | `SzCustomerEntSuppInfo_Reserved62` | TField |  |  |
| 47 | `SZ.CSI.RESERVED.61` | `SzCustomerEntSuppInfo_Reserved61` | TField |  |  |
| 48 | `SZ.CSI.RESERVED.60` | `SzCustomerEntSuppInfo_Reserved60` | TField |  |  |
| 49 | `SZ.CSI.RESERVED.59` | `SzCustomerEntSuppInfo_Reserved59` | TField |  |  |
| 50 | `SZ.CSI.RESERVED.58` | `SzCustomerEntSuppInfo_Reserved58` | TField |  |  |
| 51 | `SZ.CSI.RESERVED.57` | `SzCustomerEntSuppInfo_Reserved57` | TField |  |  |
| 52 | `SZ.CSI.RESERVED.56` | `SzCustomerEntSuppInfo_Reserved56` | TField |  |  |
| 53 | `SZ.CSI.RESERVED.55` | `SzCustomerEntSuppInfo_Reserved55` | TField |  |  |
| 54 | `SZ.CSI.RESERVED.54` | `SzCustomerEntSuppInfo_Reserved54` | TField |  |  |
| 55 | `SZ.CSI.RESERVED.53` | `SzCustomerEntSuppInfo_Reserved53` | TField |  |  |
| 56 | `SZ.CSI.RESERVED.52` | `SzCustomerEntSuppInfo_Reserved52` | TField |  |  |
| 57 | `SZ.CSI.RESERVED.51` | `SzCustomerEntSuppInfo_Reserved51` | TField |  |  |
| 58 | `SZ.CSI.RESERVED.50` | `SzCustomerEntSuppInfo_Reserved50` | TField |  |  |
| 59 | `SZ.CSI.RESERVED.49` | `SzCustomerEntSuppInfo_Reserved49` | TField |  |  |
| 60 | `SZ.CSI.RESERVED.48` | `SzCustomerEntSuppInfo_Reserved48` | TField |  |  |
| 61 | `SZ.CSI.RESERVED.47` | `SzCustomerEntSuppInfo_Reserved47` | TField |  |  |
| 62 | `SZ.CSI.RESERVED.46` | `SzCustomerEntSuppInfo_Reserved46` | TField |  |  |
| 63 | `SZ.CSI.RESERVED.45` | `SzCustomerEntSuppInfo_Reserved45` | TField |  |  |
| 64 | `SZ.CSI.RESERVED.44` | `SzCustomerEntSuppInfo_Reserved44` | TField |  |  |
| 65 | `SZ.CSI.RESERVED.43` | `SzCustomerEntSuppInfo_Reserved43` | TField |  |  |
| 66 | `SZ.CSI.RESERVED.42` | `SzCustomerEntSuppInfo_Reserved42` | TField |  |  |
| 67 | `SZ.CSI.RESERVED.41` | `SzCustomerEntSuppInfo_Reserved41` | TField |  |  |
| 68 | `SZ.CSI.RESERVED.40` | `SzCustomerEntSuppInfo_Reserved40` | TField |  |  |
| 69 | `SZ.CSI.RESERVED.39` | `SzCustomerEntSuppInfo_Reserved39` | TField |  |  |
| 70 | `SZ.CSI.RESERVED.38` | `SzCustomerEntSuppInfo_Reserved38` | TField |  |  |
| 71 | `SZ.CSI.RESERVED.37` | `SzCustomerEntSuppInfo_Reserved37` | TField |  |  |
| 72 | `SZ.CSI.RESERVED.36` | `SzCustomerEntSuppInfo_Reserved36` | TField |  |  |
| 73 | `SZ.CSI.RESERVED.35` | `SzCustomerEntSuppInfo_Reserved35` | TField |  |  |
| 74 | `SZ.CSI.RESERVED.34` | `SzCustomerEntSuppInfo_Reserved34` | TField |  |  |
| 75 | `SZ.CSI.RESERVED.33` | `SzCustomerEntSuppInfo_Reserved33` | TField |  |  |
| 76 | `SZ.CSI.RESERVED.32` | `SzCustomerEntSuppInfo_Reserved32` | TField |  |  |
| 77 | `SZ.CSI.RESERVED.31` | `SzCustomerEntSuppInfo_Reserved31` | TField |  |  |
| 78 | `SZ.CSI.RESERVED.30` | `SzCustomerEntSuppInfo_Reserved30` | TField |  |  |
| 79 | `SZ.CSI.RESERVED.29` | `SzCustomerEntSuppInfo_Reserved29` | TField |  |  |
| 80 | `SZ.CSI.RESERVED.28` | `SzCustomerEntSuppInfo_Reserved28` | TField |  |  |
| 81 | `SZ.CSI.RESERVED.27` | `SzCustomerEntSuppInfo_Reserved27` | TField |  |  |
| 82 | `SZ.CSI.RESERVED.26` | `SzCustomerEntSuppInfo_Reserved26` | TField |  |  |
| 83 | `SZ.CSI.RESERVED.25` | `SzCustomerEntSuppInfo_Reserved25` | TField |  |  |
| 84 | `SZ.CSI.RESERVED.24` | `SzCustomerEntSuppInfo_Reserved24` | TField |  |  |
| 85 | `SZ.CSI.RESERVED.23` | `SzCustomerEntSuppInfo_Reserved23` | TField |  |  |
| 86 | `SZ.CSI.RESERVED.22` | `SzCustomerEntSuppInfo_Reserved22` | TField |  |  |
| 87 | `SZ.CSI.RESERVED.21` | `SzCustomerEntSuppInfo_Reserved21` | TField |  |  |
| 88 | `SZ.CSI.RESERVED.20` | `SzCustomerEntSuppInfo_Reserved20` | TField |  |  |
| 89 | `SZ.CSI.RESERVED.19` | `SzCustomerEntSuppInfo_Reserved19` | TField |  |  |
| 90 | `SZ.CSI.RESERVED.18` | `SzCustomerEntSuppInfo_Reserved18` | TField |  |  |
| 91 | `SZ.CSI.RESERVED.17` | `SzCustomerEntSuppInfo_Reserved17` | TField |  |  |
| 92 | `SZ.CSI.RESERVED.16` | `SzCustomerEntSuppInfo_Reserved16` | TField |  |  |
| 93 | `SZ.CSI.RESERVED.15` | `SzCustomerEntSuppInfo_Reserved15` | TField |  |  |
| 94 | `SZ.CSI.RESERVED.14` | `SzCustomerEntSuppInfo_Reserved14` | TField |  |  |
| 95 | `SZ.CSI.RESERVED.13` | `SzCustomerEntSuppInfo_Reserved13` | TField |  |  |
| 96 | `SZ.CSI.RESERVED.12` | `SzCustomerEntSuppInfo_Reserved12` | TField |  |  |
| 97 | `SZ.CSI.RESERVED.11` | `SzCustomerEntSuppInfo_Reserved11` | TField |  |  |
| 98 | `SZ.CSI.RESERVED.10` | `SzCustomerEntSuppInfo_Reserved10` | TField |  |  |
| 99 | `SZ.CSI.RESERVED.09` | `SzCustomerEntSuppInfo_Reserved09` | TField |  |  |
| 100 | `SZ.CSI.RESERVED.08` | `SzCustomerEntSuppInfo_Reserved08` | TField |  |  |
| 101 | `SZ.CSI.RESERVED.07` | `SzCustomerEntSuppInfo_Reserved07` | TField |  |  |
| 102 | `SZ.CSI.RESERVED.06` | `SzCustomerEntSuppInfo_Reserved06` | TField |  |  |
| 103 | `SZ.CSI.RESERVED.05` | `SzCustomerEntSuppInfo_Reserved05` | TField |  |  |
| 104 | `SZ.CSI.RESERVED.04` | `SzCustomerEntSuppInfo_Reserved04` | TField |  |  |
| 105 | `SZ.CSI.RESERVED.03` | `SzCustomerEntSuppInfo_Reserved03` | TField |  |  |
| 106 | `SZ.CSI.RESERVED.02` | `SzCustomerEntSuppInfo_Reserved02` | TField |  |  |
| 107 | `SZ.CSI.RESERVED.01` | `SzCustomerEntSuppInfo_Reserved01` | TField |  |  |
| 108 | `SZ.CSI.LOCAL.REF` | `SzCustomerEntSuppInfo_LocalRef` |  |  |  |
| 109 | `SZ.CSI.OVERRIDE` | `SzCustomerEntSuppInfo_Override` |  |  |  |
| 110 | `SZ.CSI.RECORD.STATUS` | `SzCustomerEntSuppInfo_RecordStatus` | String |  |  |
| 111 | `SZ.CSI.CURR.NO` | `SzCustomerEntSuppInfo_CurrNo` | String |  |  |
| 112 | `SZ.CSI.INPUTTER` | `SzCustomerEntSuppInfo_Inputter` |  |  |  |
| 113 | `SZ.CSI.DATE.TIME` | `SzCustomerEntSuppInfo_DateTime` |  |  |  |
| 114 | `SZ.CSI.AUTHORISER` | `SzCustomerEntSuppInfo_Authoriser` | String |  |  |
| 115 | `SZ.CSI.CO.CODE` | `SzCustomerEntSuppInfo_CoCode` | String |  |  |
| 116 | `SZ.CSI.DEPT.CODE` | `SzCustomerEntSuppInfo_DeptCode` | String |  |  |
| 117 | `SZ.CSI.AUDITOR.CODE` | `SzCustomerEntSuppInfo_AuditorCode` | String |  |  |
| 118 | `SZ.CSI.AUDIT.DATE.TIME` | `SzCustomerEntSuppInfo_AuditDateTime` | String |  |  |
