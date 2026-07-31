# SASIMA.ENQUIRY.RESPONSE — Table Schema

> Source: `INSERTS/I_F.SASIMA.ENQUIRY.RESPONSE` in `SASIMA_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.SI.ENQUIRY.REFERENCE` | `SasimaEnquiryResponse_EnquiryReference` | TField |  |  |
| 2 | `SA.SI.ENQUIRY.TYPE` | `SasimaEnquiryResponse_EnquiryType` | TField |  |  |
| 3 | `SA.SI.REPORT.DATE` | `SasimaEnquiryResponse_ReportDate` | TField |  |  |
| 4 | `SA.SI.ENQUIRY.NO` | `SasimaEnquiryResponse_EnquiryNo` | TField |  |  |
| 5 | `SA.SI.PRODUCT.TYPE` | `SasimaEnquiryResponse_ProductType` | TField |  |  |
| 6 | `SA.SI.NO.OF.APPLICANTS` | `SasimaEnquiryResponse_NoOfApplicants` | TField |  |  |
| 7 | `SA.SI.ACCOUNT.TYPE` | `SasimaEnquiryResponse_AccountType` | TField |  |  |
| 8 | `SA.SI.AMOUNT` | `SasimaEnquiryResponse_Amount` | TField |  |  |
| 9 | `SA.SI.MBR.TYPE` | `SasimaEnquiryResponse_MbrType` | TField |  |  |
| 10 | `SA.SI.MBR.STS` | `SasimaEnquiryResponse_MbrSts` | TField |  |  |
| 11 | `SA.SI.CAPL` | `SasimaEnquiryResponse_Capl` |  |  |  |
| 12 | `SA.SI.CID1` | `SasimaEnquiryResponse_Cid1` |  |  |  |
| 13 | `SA.SI.CID2` | `SasimaEnquiryResponse_Cid2` |  |  |  |
| 14 | `SA.SI.CID3` | `SasimaEnquiryResponse_Cid3` |  |  |  |
| 15 | `SA.SI.CVIP` | `SasimaEnquiryResponse_Cvip` |  |  |  |
| 16 | `SA.SI.PCNMFA` | `SasimaEnquiryResponse_Pcnmfa` |  |  |  |
| 17 | `SA.SI.PCNM1A` | `SasimaEnquiryResponse_Pcnm1a` |  |  |  |
| 18 | `SA.SI.PCNM2A` | `SasimaEnquiryResponse_Pcnm2a` |  |  |  |
| 19 | `SA.SI.PCNM3A` | `SasimaEnquiryResponse_Pcnm3a` |  |  |  |
| 20 | `SA.SI.PCNMFE` | `SasimaEnquiryResponse_Pcnmfe` |  |  |  |
| 21 | `SA.SI.PCNM1E` | `SasimaEnquiryResponse_Pcnm1e` |  |  |  |
| 22 | `SA.SI.PCNM2E` | `SasimaEnquiryResponse_Pcnm2e` |  |  |  |
| 23 | `SA.SI.PCNM3E` | `SasimaEnquiryResponse_Pcnm3e` |  |  |  |
| 24 | `SA.SI.PCDOB` | `SasimaEnquiryResponse_Pcdob` |  |  |  |
| 25 | `SA.SI.PCGND` | `SasimaEnquiryResponse_Pcgnd` |  |  |  |
| 26 | `SA.SI.PCMAR` | `SasimaEnquiryResponse_Pcmar` |  |  |  |
| 27 | `SA.SI.PCNAT` | `SasimaEnquiryResponse_Pcnat` |  |  |  |
| 28 | `SA.SI.PCEML` | `SasimaEnquiryResponse_Pceml` |  |  |  |
| 29 | `SA.SI.ACNMFA` | `SasimaEnquiryResponse_Acnmfa` |  |  |  |
| 30 | `SA.SI.ACNM1A` | `SasimaEnquiryResponse_Acnm1a` |  |  |  |
| 31 | `SA.SI.ACNM2A` | `SasimaEnquiryResponse_Acnm2a` |  |  |  |
| 32 | `SA.SI.ACNM3A` | `SasimaEnquiryResponse_Acnm3a` |  |  |  |
| 33 | `SA.SI.ACNM7A` | `SasimaEnquiryResponse_Acnm7a` |  |  |  |
| 34 | `SA.SI.ACNMFE` | `SasimaEnquiryResponse_Acnmfe` |  |  |  |
| 35 | `SA.SI.ACNM1E` | `SasimaEnquiryResponse_Acnm1e` |  |  |  |
| 36 | `SA.SI.ACNM2E` | `SasimaEnquiryResponse_Acnm2e` |  |  |  |
| 37 | `SA.SI.ACNM3E` | `SasimaEnquiryResponse_Acnm3e` |  |  |  |
| 38 | `SA.SI.ACNM7E` | `SasimaEnquiryResponse_Acnm7e` |  |  |  |
| 39 | `SA.SI.ACDOB` | `SasimaEnquiryResponse_Acdob` |  |  |  |
| 40 | `SA.SI.ACGND` | `SasimaEnquiryResponse_Acgnd` |  |  |  |
| 41 | `SA.SI.ACMAR` | `SasimaEnquiryResponse_Acmar` |  |  |  |
| 42 | `SA.SI.ACNAT` | `SasimaEnquiryResponse_Acnat` |  |  |  |
| 43 | `SA.SI.ACEML` | `SasimaEnquiryResponse_Aceml` |  |  |  |
| 44 | `SA.SI.PE.DATE` | `SasimaEnquiryResponse_PeDate` |  |  |  |
| 45 | `SA.SI.PE.INQR` | `SasimaEnquiryResponse_PeInqr` |  |  |  |
| 46 | `SA.SI.PE.TYPE` | `SasimaEnquiryResponse_PeType` |  |  |  |
| 47 | `SA.SI.PE.MEMB.REF` | `SasimaEnquiryResponse_PeMembRef` |  |  |  |
| 48 | `SA.SI.PE.PRD` | `SasimaEnquiryResponse_PePrd` |  |  |  |
| 49 | `SA.SI.PE.AMOUNT` | `SasimaEnquiryResponse_PeAmount` |  |  |  |
| 50 | `SA.SI.PE.NMFA` | `SasimaEnquiryResponse_PeNmfa` |  |  |  |
| 51 | `SA.SI.PE.NM1A` | `SasimaEnquiryResponse_PeNm1a` |  |  |  |
| 52 | `SA.SI.PE.NM2A` | `SasimaEnquiryResponse_PeNm2a` |  |  |  |
| 53 | `SA.SI.PE.NM3A` | `SasimaEnquiryResponse_PeNm3a` |  |  |  |
| 54 | `SA.SI.PE.NMFE` | `SasimaEnquiryResponse_PeNmfe` |  |  |  |
| 55 | `SA.SI.PE.NM1E` | `SasimaEnquiryResponse_PeNm1e` |  |  |  |
| 56 | `SA.SI.PE.NM2E` | `SasimaEnquiryResponse_PeNm2e` |  |  |  |
| 57 | `SA.SI.PE.NM3E` | `SasimaEnquiryResponse_PeNm3e` |  |  |  |
| 58 | `SA.SI.PE.RSN` | `SasimaEnquiryResponse_PeRsn` |  |  |  |
| 59 | `SA.SI.RESERVED.25` | `SasimaEnquiryResponse_Reserved25` |  |  |  |
| 60 | `SA.SI.CI.CRDTR` | `SasimaEnquiryResponse_CiCrdtr` |  |  |  |
| 61 | `SA.SI.CI.PRD` | `SasimaEnquiryResponse_CiPrd` |  |  |  |
| 62 | `SA.SI.CI.ACC.NO` | `SasimaEnquiryResponse_CiAccNo` |  |  |  |
| 63 | `SA.SI.CI.LIMIT` | `SasimaEnquiryResponse_CiLimit` |  |  |  |
| 64 | `SA.SI.CI.ISSU.DT` | `SasimaEnquiryResponse_CiIssuDt` |  |  |  |
| 65 | `SA.SI.CI.PROD.EXP.DT` | `SasimaEnquiryResponse_CiProdExpDt` |  |  |  |
| 66 | `SA.SI.CI.STATUS` | `SasimaEnquiryResponse_CiStatus` |  |  |  |
| 67 | `SA.SI.CI.CLSD.DT` | `SasimaEnquiryResponse_CiClsdDt` |  |  |  |
| 68 | `SA.SI.CI.TNR` | `SasimaEnquiryResponse_CiTnr` |  |  |  |
| 69 | `SA.SI.CI.FRQ` | `SasimaEnquiryResponse_CiFrq` |  |  |  |
| 70 | `SA.SI.CI.INSTL` | `SasimaEnquiryResponse_CiInstl` |  |  |  |
| 71 | `SA.SI.CI.SAL` | `SasimaEnquiryResponse_CiSal` |  |  |  |
| 72 | `SA.SI.CI.SEC` | `SasimaEnquiryResponse_CiSec` |  |  |  |
| 73 | `SA.SI.CI.CUB` | `SasimaEnquiryResponse_CiCub` |  |  |  |
| 74 | `SA.SI.CI.ODB` | `SasimaEnquiryResponse_CiOdb` |  |  |  |
| 75 | `SA.SI.CI.LAST.AMT.PD` | `SasimaEnquiryResponse_CiLastAmtPd` |  |  |  |
| 76 | `SA.SI.CI.LAST.PAY.DT` | `SasimaEnquiryResponse_CiLastPayDt` |  |  |  |
| 77 | `SA.SI.CI.AS.OF.DT` | `SasimaEnquiryResponse_CiAsOfDt` |  |  |  |
| 78 | `SA.SI.CI.NXT.DU.DT` | `SasimaEnquiryResponse_CiNxtDuDt` |  |  |  |
| 79 | `SA.SI.CI.SUMMRY` | `SasimaEnquiryResponse_CiSummry` |  |  |  |
| 80 | `SA.SI.DF.PRD` | `SasimaEnquiryResponse_DfPrd` |  |  |  |
| 81 | `SA.SI.DF.CAPL` | `SasimaEnquiryResponse_DfCapl` |  |  |  |
| 82 | `SA.SI.DF.ACC.NO` | `SasimaEnquiryResponse_DfAccNo` |  |  |  |
| 83 | `SA.SI.DF.CRDTR` | `SasimaEnquiryResponse_DfCrdtr` |  |  |  |
| 84 | `SA.SI.DF.LOAD.DT` | `SasimaEnquiryResponse_DfLoadDt` |  |  |  |
| 85 | `SA.SI.DF.ORIG.AMT` | `SasimaEnquiryResponse_DfOrigAmt` |  |  |  |
| 86 | `SA.SI.DF.CUB` | `SasimaEnquiryResponse_DfCub` |  |  |  |
| 87 | `SA.SI.DF.STAT` | `SasimaEnquiryResponse_DfStat` |  |  |  |
| 88 | `SA.SI.DF.SETTLD.DATE` | `SasimaEnquiryResponse_DfSettldDate` |  |  |  |
| 89 | `SA.SI.BC.PRD` | `SasimaEnquiryResponse_BcPrd` |  |  |  |
| 90 | `SA.SI.BC.CRDTR` | `SasimaEnquiryResponse_BcCrdtr` |  |  |  |
| 91 | `SA.SI.BC.CHECK.NO` | `SasimaEnquiryResponse_BcCheckNo` |  |  |  |
| 92 | `SA.SI.BC.LOAD.DT` | `SasimaEnquiryResponse_BcLoadDt` |  |  |  |
| 93 | `SA.SI.BC.ORIG.AMT` | `SasimaEnquiryResponse_BcOrigAmt` |  |  |  |
| 94 | `SA.SI.BC.CUB` | `SasimaEnquiryResponse_BcCub` |  |  |  |
| 95 | `SA.SI.BC.STAT` | `SasimaEnquiryResponse_BcStat` |  |  |  |
| 96 | `SA.SI.BC.SETTLD.DATE` | `SasimaEnquiryResponse_BcSettldDate` |  |  |  |
| 97 | `SA.SI.EJ.ENFORCE.DATE` | `SasimaEnquiryResponse_EjEnforceDate` |  |  |  |
| 98 | `SA.SI.EJ.RES.NUMBER` | `SasimaEnquiryResponse_EjResNumber` |  |  |  |
| 99 | `SA.SI.EJ.EXEC.TYPE` | `SasimaEnquiryResponse_EjExecType` |  |  |  |
| 100 | `SA.SI.EJ.CITY` | `SasimaEnquiryResponse_EjCity` |  |  |  |
| 101 | `SA.SI.EJ.COURT.CODE` | `SasimaEnquiryResponse_EjCourtCode` |  |  |  |
| 102 | `SA.SI.EJ.CASE.NUMBER` | `SasimaEnquiryResponse_EjCaseNumber` |  |  |  |
| 103 | `SA.SI.EJ.DATE.LOADED` | `SasimaEnquiryResponse_EjDateLoaded` |  |  |  |
| 104 | `SA.SI.EJ.ORIG.CLAIM.AMT` | `SasimaEnquiryResponse_EjOrigClaimAmt` |  |  |  |
| 105 | `SA.SI.EJ.CLAIM.AMT` | `SasimaEnquiryResponse_EjClaimAmt` |  |  |  |
| 106 | `SA.SI.EJ.STATUS` | `SasimaEnquiryResponse_EjStatus` |  |  |  |
| 107 | `SA.SI.EJ.SETTLE.DATE` | `SasimaEnquiryResponse_EjSettleDate` |  |  |  |
| 108 | `SA.SI.PN.LOAD.DT` | `SasimaEnquiryResponse_PnLoadDt` |  |  |  |
| 109 | `SA.SI.PN.TYPE` | `SasimaEnquiryResponse_PnType` |  |  |  |
| 110 | `SA.SI.PN.PUBLICATION` | `SasimaEnquiryResponse_PnPublication` |  |  |  |
| 111 | `SA.SI.PN.COMMENT` | `SasimaEnquiryResponse_PnComment` |  |  |  |
| 112 | `SA.SI.PN.PUBLICATION.AR` | `SasimaEnquiryResponse_PnPublicationAr` |  |  |  |
| 113 | `SA.SI.PN.COMMENT.AR` | `SasimaEnquiryResponse_PnCommentAr` |  |  |  |
| 114 | `SA.SI.RESERVED.26` | `SasimaEnquiryResponse_Reserved26` |  |  |  |
| 115 | `SA.SI.NA.LOAD.DT` | `SasimaEnquiryResponse_NaLoadDt` |  |  |  |
| 116 | `SA.SI.NA.LOADED.BY` | `SasimaEnquiryResponse_NaLoadedBy` |  |  |  |
| 117 | `SA.SI.NA.TYPE` | `SasimaEnquiryResponse_NaType` |  |  |  |
| 118 | `SA.SI.NA.TEXT` | `SasimaEnquiryResponse_NaText` |  |  |  |
| 119 | `SA.SI.NA.TEXT.AR` | `SasimaEnquiryResponse_NaTextAr` |  |  |  |
| 120 | `SA.SI.CA.LOAD.DT` | `SasimaEnquiryResponse_CaLoadDt` |  |  |  |
| 121 | `SA.SI.CA.CADT` | `SasimaEnquiryResponse_CaCadt` |  |  |  |
| 122 | `SA.SI.CA.CAD1A` | `SasimaEnquiryResponse_CaCad1a` |  |  |  |
| 123 | `SA.SI.CA.CAD2A` | `SasimaEnquiryResponse_CaCad2a` |  |  |  |
| 124 | `SA.SI.CA.CAD1E` | `SasimaEnquiryResponse_CaCad1e` |  |  |  |
| 125 | `SA.SI.CA.CAD2E` | `SasimaEnquiryResponse_CaCad2e` |  |  |  |
| 126 | `SA.SI.CA.CAD6` | `SasimaEnquiryResponse_CaCad6` |  |  |  |
| 127 | `SA.SI.CA.CAD7` | `SasimaEnquiryResponse_CaCad7` |  |  |  |
| 128 | `SA.SI.CA.CAD8A` | `SasimaEnquiryResponse_CaCad8a` |  |  |  |
| 129 | `SA.SI.CA.CAD8E` | `SasimaEnquiryResponse_CaCad8e` |  |  |  |
| 130 | `SA.SI.CA.CAD9` | `SasimaEnquiryResponse_CaCad9` |  |  |  |
| 131 | `SA.SI.RESERVED.27` | `SasimaEnquiryResponse_Reserved27` |  |  |  |
| 132 | `SA.SI.CCN1` | `SasimaEnquiryResponse_Ccn1` |  |  |  |
| 133 | `SA.SI.CCN2` | `SasimaEnquiryResponse_Ccn2` |  |  |  |
| 134 | `SA.SI.CCN3` | `SasimaEnquiryResponse_Ccn3` |  |  |  |
| 135 | `SA.SI.CCN4` | `SasimaEnquiryResponse_Ccn4` |  |  |  |
| 136 | `SA.SI.CCN5` | `SasimaEnquiryResponse_Ccn5` |  |  |  |
| 137 | `SA.SI.ETYP` | `SasimaEnquiryResponse_Etyp` |  |  |  |
| 138 | `SA.SI.ENME` | `SasimaEnquiryResponse_Enme` |  |  |  |
| 139 | `SA.SI.ENMA` | `SasimaEnquiryResponse_Enma` |  |  |  |
| 140 | `SA.SI.EADT` | `SasimaEnquiryResponse_Eadt` |  |  |  |
| 141 | `SA.SI.EAD1A` | `SasimaEnquiryResponse_Ead1a` |  |  |  |
| 142 | `SA.SI.EAD2A` | `SasimaEnquiryResponse_Ead2a` |  |  |  |
| 143 | `SA.SI.EAD1E` | `SasimaEnquiryResponse_Ead1e` |  |  |  |
| 144 | `SA.SI.EAD2E` | `SasimaEnquiryResponse_Ead2e` |  |  |  |
| 145 | `SA.SI.EAD6` | `SasimaEnquiryResponse_Ead6` |  |  |  |
| 146 | `SA.SI.EAD7` | `SasimaEnquiryResponse_Ead7` |  |  |  |
| 147 | `SA.SI.EAD8A` | `SasimaEnquiryResponse_Ead8a` |  |  |  |
| 148 | `SA.SI.EAD8E` | `SasimaEnquiryResponse_Ead8e` |  |  |  |
| 149 | `SA.SI.EAD9` | `SasimaEnquiryResponse_Ead9` |  |  |  |
| 150 | `SA.SI.EOCA` | `SasimaEnquiryResponse_Eoca` |  |  |  |
| 151 | `SA.SI.EOCE` | `SasimaEnquiryResponse_Eoce` |  |  |  |
| 152 | `SA.SI.EDOE` | `SasimaEnquiryResponse_Edoe` |  |  |  |
| 153 | `SA.SI.ELEN` | `SasimaEnquiryResponse_Elen` |  |  |  |
| 154 | `SA.SI.ECEX` | `SasimaEnquiryResponse_Ecex` |  |  |  |
| 155 | `SA.SI.EDLD` | `SasimaEnquiryResponse_Edld` |  |  |  |
| 156 | `SA.SI.EMBS` | `SasimaEnquiryResponse_Embs` |  |  |  |
| 157 | `SA.SI.ETMS` | `SasimaEnquiryResponse_Etms` |  |  |  |
| 158 | `SA.SI.CNT.PE` | `SasimaEnquiryResponse_CntPe` |  |  |  |
| 159 | `SA.SI.CNT.MTDE` | `SasimaEnquiryResponse_CntMtde` |  |  |  |
| 160 | `SA.SI.CNT.CI` | `SasimaEnquiryResponse_CntCi` |  |  |  |
| 161 | `SA.SI.CNT.GCI` | `SasimaEnquiryResponse_CntGci` |  |  |  |
| 162 | `SA.SI.CNT.DEF` | `SasimaEnquiryResponse_CntDef` |  |  |  |
| 163 | `SA.SI.EIID` | `SasimaEnquiryResponse_Eiid` |  |  |  |
| 164 | `SA.SI.TOT.LIM` | `SasimaEnquiryResponse_TotLim` |  |  |  |
| 165 | `SA.SI.TOT.GLIM` | `SasimaEnquiryResponse_TotGlim` |  |  |  |
| 166 | `SA.SI.TOT.LIAB` | `SasimaEnquiryResponse_TotLiab` |  |  |  |
| 167 | `SA.SI.TOT.GLIAB` | `SasimaEnquiryResponse_TotGliab` |  |  |  |
| 168 | `SA.SI.TOT.DEF` | `SasimaEnquiryResponse_TotDef` |  |  |  |
| 169 | `SA.SI.CUR.DB` | `SasimaEnquiryResponse_CurDb` |  |  |  |
| 170 | `SA.SI.SC.SCORE` | `SasimaEnquiryResponse_ScScore` |  |  |  |
| 171 | `SA.SI.SC.REASON.CODE` | `SasimaEnquiryResponse_ScReasonCode` |  |  |  |
| 172 | `SA.SI.SC.SCORECARD` | `SasimaEnquiryResponse_ScScorecard` |  |  |  |
| 173 | `SA.SI.SC.SCOREINDEX` | `SasimaEnquiryResponse_ScScoreindex` |  |  |  |
| 174 | `SA.SI.SC.MINIMUM` | `SasimaEnquiryResponse_ScMinimum` |  |  |  |
| 175 | `SA.SI.SC.MAXIMUM` | `SasimaEnquiryResponse_ScMaximum` |  |  |  |
| 176 | `SA.SI.DI.TEXT` | `SasimaEnquiryResponse_DiText` |  |  |  |
| 177 | `SA.SI.DI.TEXT.AR` | `SasimaEnquiryResponse_DiTextAr` |  |  |  |
| 178 | `SA.SI.CUSTOMER.CODE` | `SasimaEnquiryResponse_CustomerCode` | TField |  |  |
| 179 | `SA.SI.RESERVED.1` | `SasimaEnquiryResponse_Reserved1` | TField |  |  |
| 180 | `SA.SI.RESERVED.2` | `SasimaEnquiryResponse_Reserved2` | TField |  |  |
| 181 | `SA.SI.RESERVED.3` | `SasimaEnquiryResponse_Reserved3` | TField |  |  |
| 182 | `SA.SI.RESERVED.4` | `SasimaEnquiryResponse_Reserved4` | TField |  |  |
| 183 | `SA.SI.RESERVED.5` | `SasimaEnquiryResponse_Reserved5` | TField |  |  |
| 184 | `SA.SI.RESERVED.6` | `SasimaEnquiryResponse_Reserved6` | TField |  |  |
| 185 | `SA.SI.RESERVED.7` | `SasimaEnquiryResponse_Reserved7` | TField |  |  |
| 186 | `SA.SI.RESERVED.8` | `SasimaEnquiryResponse_Reserved8` | TField |  |  |
| 187 | `SA.SI.RESERVED.9` | `SasimaEnquiryResponse_Reserved9` | TField |  |  |
| 188 | `SA.SI.RESERVED.10` | `SasimaEnquiryResponse_Reserved10` | TField |  |  |
