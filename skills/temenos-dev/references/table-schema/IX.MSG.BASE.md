# IX.MSG.BASE — Table Schema

> Source: `INSERTS/I_F.IX.MSG.BASE` in `IX_XmlStmtPrinting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IX.MSG.HDR.AC.XML.STMT.ID` | `IxMsgBase_HdrAcXmlStmtId` | TField |  |  |
| 2 | `IX.MSG.HDR.MSG.ID` | `IxMsgBase_HdrMsgId` | TField |  |  |
| 3 | `IX.MSG.HDR.CREDTIME` | `IxMsgBase_HdrCredtime` | TField |  |  |
| 4 | `IX.MSG.HDR.MSG.RCP.NM` | `IxMsgBase_HdrMsgRcpNm` | TField |  |  |
| 5 | `IX.MSG.HDR.MSG.RCPT.PSTL.ADR.TP` | `IxMsgBase_HdrMsgRcptPstlAdrTp` | TField |  |  |
| 6 | `IX.MSG.HDR.MSG.RCPT.PSTL.DEPT` | `IxMsgBase_HdrMsgRcptPstlDept` | TField |  |  |
| 7 | `IX.MSG.HDR.RCPT.PSTL.SUB.DEPT` | `IxMsgBase_HdrRcptPstlSubDept` | TField |  |  |
| 8 | `IX.MSG.HDR.MSG.RCPT.PSTL.STREET` | `IxMsgBase_HdrMsgRcptPstlStreet` | TField |  |  |
| 9 | `IX.MSG.HDR.RCPT.PSTL.BUILDING` | `IxMsgBase_HdrRcptPstlBuilding` | TField |  |  |
| 10 | `IX.MSG.HDR.RCPT.PSTL.POSTCODE` | `IxMsgBase_HdrRcptPstlPostcode` | TField |  |  |
| 11 | `IX.MSG.HDR.MSG.RCPT.PSTL.TOWN` | `IxMsgBase_HdrMsgRcptPstlTown` | TField |  |  |
| 12 | `IX.MSG.HDR.MSG.RCPT.PSTL.SUBDVSN` | `IxMsgBase_HdrMsgRcptPstlSubdvsn` | TField |  |  |
| 13 | `IX.MSG.HDR.MSG.RCPT.PSTL.COUNTRY` | `IxMsgBase_HdrMsgRcptPstlCountry` | TField |  |  |
| 14 | `IX.MSG.HDR.RCPT.PSTL.ADR.LINE` | `IxMsgBase_HdrRcptPstlAdrLine` |  |  |  |
| 15 | `IX.MSG.HDR.ORG.ID.BIC` | `IxMsgBase_HdrOrgIdBic` | TField |  |  |
| 16 | `IX.MSG.HDR.ORG.ID.OTHERID` | `IxMsgBase_HdrOrgIdOtherid` |  |  |  |
| 17 | `IX.MSG.HDR.ORG.ID.OTHERCODE` | `IxMsgBase_HdrOrgIdOthercode` |  |  |  |
| 18 | `IX.MSG.HDR.ORG.ID.OTHER.PRTRY` | `IxMsgBase_HdrOrgIdOtherPrtry` |  |  |  |
| 19 | `IX.MSG.HDR.ORG.ID.OTHER.ISSR` | `IxMsgBase_HdrOrgIdOtherIssr` |  |  |  |
| 20 | `IX.MSG.HDR.RESERVED.16` | `IxMsgBase_HdrReserved16` |  |  |  |
| 21 | `IX.MSG.HDR.RESERVED.15` | `IxMsgBase_HdrReserved15` |  |  |  |
| 22 | `IX.MSG.HDR.RESERVED.14` | `IxMsgBase_HdrReserved14` |  |  |  |
| 23 | `IX.MSG.HDR.PVT.ID.BIRTHDT` | `IxMsgBase_HdrPvtIdBirthdt` | TField |  |  |
| 24 | `IX.MSG.HDR.PVT.ID.PROVINCE` | `IxMsgBase_HdrPvtIdProvince` | TField |  |  |
| 25 | `IX.MSG.HDR.PVT.ID.BIRTHCITY` | `IxMsgBase_HdrPvtIdBirthcity` | TField |  |  |
| 26 | `IX.MSG.HDR.PVT.ID.BIRTH.COUNTRY` | `IxMsgBase_HdrPvtIdBirthCountry` | TField |  |  |
| 27 | `IX.MSG.HDR.PVT.ID.OTHERID` | `IxMsgBase_HdrPvtIdOtherid` |  |  |  |
| 28 | `IX.MSG.HDR.PVT.ID.OTHERCODE` | `IxMsgBase_HdrPvtIdOthercode` |  |  |  |
| 29 | `IX.MSG.HDR.PVT.ID.OTHER.PRTRY` | `IxMsgBase_HdrPvtIdOtherPrtry` |  |  |  |
| 30 | `IX.MSG.HDR.PVT.ID.OTHER.ISSR` | `IxMsgBase_HdrPvtIdOtherIssr` |  |  |  |
| 31 | `IX.MSG.HDR.RESERVED.13` | `IxMsgBase_HdrReserved13` |  |  |  |
| 32 | `IX.MSG.HDR.RESERVED.12` | `IxMsgBase_HdrReserved12` |  |  |  |
| 33 | `IX.MSG.HDR.RESERVED.11` | `IxMsgBase_HdrReserved11` |  |  |  |
| 34 | `IX.MSG.HDR.MSG.RCPT.COUNTRY` | `IxMsgBase_HdrMsgRcptCountry` | TField |  |  |
| 35 | `IX.MSG.HDR.CTCT.DTLS.NM.PRF` | `IxMsgBase_HdrCtctDtlsNmPrf` | TField |  |  |
| 36 | `IX.MSG.HDR.CTCT.DTLS.NM` | `IxMsgBase_HdrCtctDtlsNm` | TField |  |  |
| 37 | `IX.MSG.HDR.CTCT.DTLS.PHONE` | `IxMsgBase_HdrCtctDtlsPhone` | TField |  |  |
| 38 | `IX.MSG.HDR.CTCT.DTLSMOBILE` | `IxMsgBase_HdrCtctDtlsmobile` | TField |  |  |
| 39 | `IX.MSG.HDR.CTCT.DTLSFAX` | `IxMsgBase_HdrCtctDtlsfax` | TField |  |  |
| 40 | `IX.MSG.HDR.CTCT.DTLS.EMAIL` | `IxMsgBase_HdrCtctDtlsEmail` | TField |  |  |
| 41 | `IX.MSG.HDR.CTCT.DTLS.OTHER` | `IxMsgBase_HdrCtctDtlsOther` | TField |  |  |
| 42 | `IX.MSG.HDR.MSG.PGNPAGENO` | `IxMsgBase_HdrMsgPgnpageno` | TField |  |  |
| 43 | `IX.MSG.HDR.MSG.PGNLASTPGIND` | `IxMsgBase_HdrMsgPgnlastpgind` | TField |  |  |
| 44 | `IX.MSG.HDR.ADDTLINFO` | `IxMsgBase_HdrAddtlinfo` | TField |  |  |
| 45 | `IX.MSG.HDR.LOCAL.TAGS` | `IxMsgBase_HdrLocalTags` |  |  |  |
| 46 | `IX.MSG.HDR.LOCAL.VALUES` | `IxMsgBase_HdrLocalValues` |  |  |  |
| 47 | `IX.MSG.HDR.RESERVED.10` | `IxMsgBase_HdrReserved10` | TField |  |  |
| 48 | `IX.MSG.HDR.RESERVED.9` | `IxMsgBase_HdrReserved9` | TField |  |  |
| 49 | `IX.MSG.HDR.RESERVED.8` | `IxMsgBase_HdrReserved8` | TField |  |  |
| 50 | `IX.MSG.HDR.RESERVED.7` | `IxMsgBase_HdrReserved7` | TField |  |  |
| 51 | `IX.MSG.HDR.RESERVED.6` | `IxMsgBase_HdrReserved6` | TField |  |  |
| 52 | `IX.MSG.HDR.RESERVED.5` | `IxMsgBase_HdrReserved5` | TField |  |  |
| 53 | `IX.MSG.HDR.RESERVED.4` | `IxMsgBase_HdrReserved4` | TField |  |  |
| 54 | `IX.MSG.HDR.RESERVED.3` | `IxMsgBase_HdrReserved3` | TField |  |  |
| 55 | `IX.MSG.HDR.RESERVED.2` | `IxMsgBase_HdrReserved2` | TField |  |  |
| 56 | `IX.MSG.HDR.RESERVED.1` | `IxMsgBase_HdrReserved1` | TField |  |  |
| 57 | `IX.MSG.STMT.ID` | `IxMsgBase_StmtId` | TField |  |  |
| 58 | `IX.MSG.STMT.ELC.SEQ.NO` | `IxMsgBase_StmtElcSeqNo` | TField |  |  |
| 59 | `IX.MSG.STMT.LGL.SEQ.NO` | `IxMsgBase_StmtLglSeqNo` | TField |  |  |
| 60 | `IX.MSG.STMT.CRE.DT.TM` | `IxMsgBase_StmtCreDtTm` | TField |  |  |
| 61 | `IX.MSG.STMT.FR.DT.TM` | `IxMsgBase_StmtFrDtTm` | TField |  |  |
| 62 | `IX.MSG.STMT.TO.DT.TM` | `IxMsgBase_StmtToDtTm` | TField |  |  |
| 63 | `IX.MSG.STMT.CPY.DPLCT.IND` | `IxMsgBase_StmtCpyDplctInd` | TField |  |  |
| 64 | `IX.MSG.STMT.RPT.SRC.CODE` | `IxMsgBase_StmtRptSrcCode` | TField |  |  |
| 65 | `IX.MSG.STMT.RPT.SRC.PRTRY` | `IxMsgBase_StmtRptSrcPrtry` | TField |  |  |
| 66 | `IX.MSG.STMT.ADDITIONALINFO` | `IxMsgBase_StmtAdditionalinfo` | TField |  |  |
| 67 | `IX.MSG.STMT.LOCAL.TAGS` | `IxMsgBase_StmtLocalTags` |  |  |  |
| 68 | `IX.MSG.STMT.LOCAL.VALUES` | `IxMsgBase_StmtLocalValues` |  |  |  |
| 69 | `IX.MSG.STMT.RESERVED.10` | `IxMsgBase_StmtReserved10` | TField |  |  |
| 70 | `IX.MSG.STMT.RESERVED.9` | `IxMsgBase_StmtReserved9` | TField |  |  |
| 71 | `IX.MSG.STMT.RESERVED.8` | `IxMsgBase_StmtReserved8` | TField |  |  |
| 72 | `IX.MSG.STMT.RESERVED.7` | `IxMsgBase_StmtReserved7` | TField |  |  |
| 73 | `IX.MSG.STMT.RESERVED.6` | `IxMsgBase_StmtReserved6` | TField |  |  |
| 74 | `IX.MSG.STMT.RESERVED.5` | `IxMsgBase_StmtReserved5` | TField |  |  |
| 75 | `IX.MSG.STMT.RESERVED.4` | `IxMsgBase_StmtReserved4` | TField |  |  |
| 76 | `IX.MSG.STMT.RESERVED.3` | `IxMsgBase_StmtReserved3` | TField |  |  |
| 77 | `IX.MSG.STMT.RESERVED.2` | `IxMsgBase_StmtReserved2` | TField |  |  |
| 78 | `IX.MSG.STMT.RESERVED.1` | `IxMsgBase_StmtReserved1` | TField |  |  |
| 79 | `IX.MSG.ACCT.ID.IBAN` | `IxMsgBase_AcctIdIban` | TField |  |  |
| 80 | `IX.MSG.ACCT.ID.OTHER.ID` | `IxMsgBase_AcctIdOtherId` | TField |  |  |
| 81 | `IX.MSG.ACCT.ID.CODE` | `IxMsgBase_AcctIdCode` | TField |  |  |
| 82 | `IX.MSG.ACCT.ID.PRTRY` | `IxMsgBase_AcctIdPrtry` | TField |  |  |
| 83 | `IX.MSG.ACCT.ID.ISSR` | `IxMsgBase_AcctIdIssr` | TField |  |  |
| 84 | `IX.MSG.ACCT.TP.CODE` | `IxMsgBase_AcctTpCode` | TField |  |  |
| 85 | `IX.MSG.ACCT.TP.PRTRY` | `IxMsgBase_AcctTpPrtry` | TField |  |  |
| 86 | `IX.MSG.ACCT.CCY` | `IxMsgBase_AcctCcy` | TField |  |  |
| 87 | `IX.MSG.ACCT.NAME` | `IxMsgBase_AcctName` | TField |  |  |
| 88 | `IX.MSG.ACCT.OWNR.NAME` | `IxMsgBase_AcctOwnrName` | TField |  |  |
| 89 | `IX.MSG.ACCT.OWNR.ADR.TP` | `IxMsgBase_AcctOwnrAdrTp` | TField |  |  |
| 90 | `IX.MSG.ACCT.OWNR.DEPT` | `IxMsgBase_AcctOwnrDept` | TField |  |  |
| 91 | `IX.MSG.ACCT.OWNR.SUBDEPT` | `IxMsgBase_AcctOwnrSubdept` | TField |  |  |
| 92 | `IX.MSG.ACCT.OWNR.STREET` | `IxMsgBase_AcctOwnrStreet` | TField |  |  |
| 93 | `IX.MSG.ACCT.OWNR.BUILDING` | `IxMsgBase_AcctOwnrBuilding` | TField |  |  |
| 94 | `IX.MSG.ACCT.OWNR.POSTCODE` | `IxMsgBase_AcctOwnrPostcode` | TField |  |  |
| 95 | `IX.MSG.ACCT.OWNR.TOWN` | `IxMsgBase_AcctOwnrTown` | TField |  |  |
| 96 | `IX.MSG.ACCT.OWNR.SUBDVSN` | `IxMsgBase_AcctOwnrSubdvsn` | TField |  |  |
| 97 | `IX.MSG.ACCT.OWNR.COUNTRY` | `IxMsgBase_AcctOwnrCountry` | TField |  |  |
| 98 | `IX.MSG.ACCT.OWNR.ADR.LINE` | `IxMsgBase_AcctOwnrAdrLine` |  |  |  |
| 99 | `IX.MSG.ACCT.ORG.ID.BIC` | `IxMsgBase_AcctOrgIdBic` | TField |  |  |
| 100 | `IX.MSG.ACCT.ORG.ID.OTHERID` | `IxMsgBase_AcctOrgIdOtherid` |  |  |  |
| 101 | `IX.MSG.ACCT.ORG.ID.OTHERCODE` | `IxMsgBase_AcctOrgIdOthercode` |  |  |  |
| 102 | `IX.MSG.ACCT.ORG.ID.OTH.PTY` | `IxMsgBase_AcctOrgIdOthPty` |  |  |  |
| 103 | `IX.MSG.ACCT.ORG.ID.OTHER.ISSR` | `IxMsgBase_AcctOrgIdOtherIssr` |  |  |  |
| 104 | `IX.MSG.ACCT.RESERVED.16` | `IxMsgBase_AcctReserved16` |  |  |  |
| 105 | `IX.MSG.ACCT.RESERVED.15` | `IxMsgBase_AcctReserved15` |  |  |  |
| 106 | `IX.MSG.ACCT.RESERVED.14` | `IxMsgBase_AcctReserved14` |  |  |  |
| 107 | `IX.MSG.ACCT.PVT.ID.BIRTHDT` | `IxMsgBase_AcctPvtIdBirthdt` | TField |  |  |
| 108 | `IX.MSG.ACCT.PVT.ID.PROVINCE` | `IxMsgBase_AcctPvtIdProvince` | TField |  |  |
| 109 | `IX.MSG.ACCT.PVT.ID.BIRTHCITY` | `IxMsgBase_AcctPvtIdBirthcity` | TField |  |  |
| 110 | `IX.MSG.ACCT.PVT.ID.BIRTH.COUNTRY` | `IxMsgBase_AcctPvtIdBirthCountry` | TField |  |  |
| 111 | `IX.MSG.ACCT.PVT.ID.OTHERID` | `IxMsgBase_AcctPvtIdOtherid` |  |  |  |
| 112 | `IX.MSG.ACCT.PVT.ID.OTHERCODE` | `IxMsgBase_AcctPvtIdOthercode` |  |  |  |
| 113 | `IX.MSG.ACCT.PVT.ID.OTH.PTY` | `IxMsgBase_AcctPvtIdOthPty` |  |  |  |
| 114 | `IX.MSG.ACCT.PVT.ID.OTHER.ISSR` | `IxMsgBase_AcctPvtIdOtherIssr` |  |  |  |
| 115 | `IX.MSG.ACCT.RESERVED.13` | `IxMsgBase_AcctReserved13` |  |  |  |
| 116 | `IX.MSG.ACCT.RESERVED.12` | `IxMsgBase_AcctReserved12` |  |  |  |
| 117 | `IX.MSG.ACCT.RESERVED.11` | `IxMsgBase_AcctReserved11` |  |  |  |
| 118 | `IX.MSG.ACCT.CTRY.OF.RES` | `IxMsgBase_AcctCtryOfRes` | TField |  |  |
| 119 | `IX.MSG.ACCT.CTCT.DTLS.NM.PRF` | `IxMsgBase_AcctCtctDtlsNmPrf` | TField |  |  |
| 120 | `IX.MSG.ACCT.CTCT.DTLS.NM` | `IxMsgBase_AcctCtctDtlsNm` | TField |  |  |
| 121 | `IX.MSG.ACCT.CTCT.DTLS.PHONE` | `IxMsgBase_AcctCtctDtlsPhone` | TField |  |  |
| 122 | `IX.MSG.ACCT.CTCT.DTLSMOBILE` | `IxMsgBase_AcctCtctDtlsmobile` | TField |  |  |
| 123 | `IX.MSG.ACCT.CTCT.DTLSFAX` | `IxMsgBase_AcctCtctDtlsfax` | TField |  |  |
| 124 | `IX.MSG.ACCT.CTCT.DTLS.EMAIL` | `IxMsgBase_AcctCtctDtlsEmail` | TField |  |  |
| 125 | `IX.MSG.ACCT.CTCT.DTLS.OTHER` | `IxMsgBase_AcctCtctDtlsOther` | TField |  |  |
| 126 | `IX.MSG.ACCT.SVCR.BIC` | `IxMsgBase_AcctSvcrBic` | TField |  |  |
| 127 | `IX.MSG.ACCT.SVCR.CLR.SYS.ID.CODE` | `IxMsgBase_AcctSvcrClrSysIdCode` | TField |  |  |
| 128 | `IX.MSG.ACCT.SVCR.CLR.SYS.ID.PTY` | `IxMsgBase_AcctSvcrClrSysIdPty` | TField |  |  |
| 129 | `IX.MSG.ACCT.SVCR.MMBLD` | `IxMsgBase_AcctSvcrMmbld` | TField |  |  |
| 130 | `IX.MSG.ACCT.SVCR.NAME` | `IxMsgBase_AcctSvcrName` | TField |  |  |
| 131 | `IX.MSG.ACCT.SVCR.ADR.TP` | `IxMsgBase_AcctSvcrAdrTp` | TField |  |  |
| 132 | `IX.MSG.ACCT.SVCR.DEPT` | `IxMsgBase_AcctSvcrDept` | TField |  |  |
| 133 | `IX.MSG.ACCT.SVCR.SUBDEPT` | `IxMsgBase_AcctSvcrSubdept` | TField |  |  |
| 134 | `IX.MSG.ACCT.SVCR.STREET` | `IxMsgBase_AcctSvcrStreet` | TField |  |  |
| 135 | `IX.MSG.ACCT.SVCR.BUILDING` | `IxMsgBase_AcctSvcrBuilding` | TField |  |  |
| 136 | `IX.MSG.ACCT.SVCR.POSTCODE` | `IxMsgBase_AcctSvcrPostcode` | TField |  |  |
| 137 | `IX.MSG.ACCT.SVCR.TOWN` | `IxMsgBase_AcctSvcrTown` | TField |  |  |
| 138 | `IX.MSG.ACCT.SVCR.SUBDVSN` | `IxMsgBase_AcctSvcrSubdvsn` | TField |  |  |
| 139 | `IX.MSG.ACCT.SVCR.COUNTRY` | `IxMsgBase_AcctSvcrCountry` | TField |  |  |
| 140 | `IX.MSG.ACCT.SVCR.ADR.LINE` | `IxMsgBase_AcctSvcrAdrLine` | TField |  |  |
| 141 | `IX.MSG.ACCT.SVCR.OTHER.ID` | `IxMsgBase_AcctSvcrOtherId` | TField |  |  |
| 142 | `IX.MSG.ACCT.SVCR.OTHER.CODE` | `IxMsgBase_AcctSvcrOtherCode` | TField |  |  |
| 143 | `IX.MSG.ACCT.SVCR.OTHER.PRTRY` | `IxMsgBase_AcctSvcrOtherPrtry` | TField |  |  |
| 144 | `IX.MSG.ACCT.SVCR.OTHER.ISSR` | `IxMsgBase_AcctSvcrOtherIssr` | TField |  |  |
| 145 | `IX.MSG.ACCT.BRANCH.ID` | `IxMsgBase_AcctBranchId` | TField |  |  |
| 146 | `IX.MSG.ACCT.BRANCH.NAME` | `IxMsgBase_AcctBranchName` | TField |  |  |
| 147 | `IX.MSG.ACCT.BRANCH.ADR.TP` | `IxMsgBase_AcctBranchAdrTp` | TField |  |  |
| 148 | `IX.MSG.ACCT.BRANCH.DEPT` | `IxMsgBase_AcctBranchDept` | TField |  |  |
| 149 | `IX.MSG.ACCT.BRANCH.SUBDEPT` | `IxMsgBase_AcctBranchSubdept` | TField |  |  |
| 150 | `IX.MSG.ACCT.BRANCH.STREET` | `IxMsgBase_AcctBranchStreet` | TField |  |  |
| 151 | `IX.MSG.ACCT.BRANCH.BUILDING` | `IxMsgBase_AcctBranchBuilding` | TField |  |  |
| 152 | `IX.MSG.ACCT.BRANCH.POSTCODE` | `IxMsgBase_AcctBranchPostcode` | TField |  |  |
| 153 | `IX.MSG.ACCT.BRANCH.TOWN` | `IxMsgBase_AcctBranchTown` | TField |  |  |
| 154 | `IX.MSG.ACCT.BRANCH.SUBDVSN` | `IxMsgBase_AcctBranchSubdvsn` | TField |  |  |
| 155 | `IX.MSG.ACCT.BRANCH.COUNTRY` | `IxMsgBase_AcctBranchCountry` | TField |  |  |
| 156 | `IX.MSG.ACCT.BRANCH.ADR.LIST` | `IxMsgBase_AcctBranchAdrList` | TField |  |  |
| 157 | `IX.MSG.ACCT.RLTD.ACCT.IBAN` | `IxMsgBase_AcctRltdAcctIban` | TField |  |  |
| 158 | `IX.MSG.ACCT.RLTD.ACCT.ID` | `IxMsgBase_AcctRltdAcctId` | TField |  |  |
| 159 | `IX.MSG.ACCT.RLTD.ACCT.ID.CODE` | `IxMsgBase_AcctRltdAcctIdCode` | TField |  |  |
| 160 | `IX.MSG.ACCT.RLTD.ACCT.ID.PRTRY` | `IxMsgBase_AcctRltdAcctIdPrtry` | TField |  |  |
| 161 | `IX.MSG.ACCT.RLTD.ACCT.ID.ISSR` | `IxMsgBase_AcctRltdAcctIdIssr` | TField |  |  |
| 162 | `IX.MSG.ACCT.RLTD.ACCT.TPCODE` | `IxMsgBase_AcctRltdAcctTpcode` | TField |  |  |
| 163 | `IX.MSG.ACCT.RLTD.ACCT.TP.PRTRY` | `IxMsgBase_AcctRltdAcctTpPrtry` | TField |  |  |
| 164 | `IX.MSG.ACCT.RLTD.ACCT.CCY` | `IxMsgBase_AcctRltdAcctCcy` | TField |  |  |
| 165 | `IX.MSG.ACCT.RLTD.ACCT.NAME` | `IxMsgBase_AcctRltdAcctName` | TField |  |  |
| 166 | `IX.MSG.ACCT.INTRST.CODE` | `IxMsgBase_AcctIntrstCode` | TField |  |  |
| 167 | `IX.MSG.ACCT.INTRST.PRTRY` | `IxMsgBase_AcctIntrstPrtry` | TField |  |  |
| 168 | `IX.MSG.ACCT.INTRST.FR.DT.TM` | `IxMsgBase_AcctIntrstFrDtTm` | TField |  |  |
| 169 | `IX.MSG.ACCT.INTRST.TO.DT.TM` | `IxMsgBase_AcctIntrstToDtTm` | TField |  |  |
| 170 | `IX.MSG.ACCT.INTRST.RSN` | `IxMsgBase_AcctIntrstRsn` | TField |  |  |
| 171 | `IX.MSG.ACCT.LOCAL.TAGS` | `IxMsgBase_AcctLocalTags` |  |  |  |
| 172 | `IX.MSG.ACCT.LOCAL.VALUES` | `IxMsgBase_AcctLocalValues` |  |  |  |
| 173 | `IX.MSG.ACCT.RESERVED.10` | `IxMsgBase_AcctReserved10` | TField |  |  |
| 174 | `IX.MSG.ACCT.RESERVED.9` | `IxMsgBase_AcctReserved9` | TField |  |  |
| 175 | `IX.MSG.ACCT.RESERVED.8` | `IxMsgBase_AcctReserved8` | TField |  |  |
| 176 | `IX.MSG.ACCT.RESERVED.7` | `IxMsgBase_AcctReserved7` | TField |  |  |
| 177 | `IX.MSG.ACCT.RESERVED.6` | `IxMsgBase_AcctReserved6` | TField |  |  |
| 178 | `IX.MSG.ACCT.RESERVED.5` | `IxMsgBase_AcctReserved5` | TField |  |  |
| 179 | `IX.MSG.ACCT.RESERVED.4` | `IxMsgBase_AcctReserved4` | TField |  |  |
| 180 | `IX.MSG.ACCT.RESERVED.3` | `IxMsgBase_AcctReserved3` | TField |  |  |
| 181 | `IX.MSG.ACCT.RESERVED.2` | `IxMsgBase_AcctReserved2` | TField |  |  |
| 182 | `IX.MSG.ACCT.RESERVED.1` | `IxMsgBase_AcctReserved1` | TField |  |  |
| 183 | `IX.MSG.BAL.TP.CODE` | `IxMsgBase_BalTpCode` |  |  |  |
| 184 | `IX.MSG.BAL.TP.PRTRY` | `IxMsgBase_BalTpPrtry` |  |  |  |
| 185 | `IX.MSG.BAL.SUB.TP.CODE` | `IxMsgBase_BalSubTpCode` |  |  |  |
| 186 | `IX.MSG.BAL.SUB.TP.PRTRY` | `IxMsgBase_BalSubTpPrtry` |  |  |  |
| 187 | `IX.MSG.BAL.CDT.LINE.INCL` | `IxMsgBase_BalCdtLineIncl` |  |  |  |
| 188 | `IX.MSG.BAL.CDT.LINE.AMOUNT` | `IxMsgBase_BalCdtLineAmount` |  |  |  |
| 189 | `IX.MSG.BAL.CCY.AMOUNT` | `IxMsgBase_BalCcyAmount` |  |  |  |
| 190 | `IX.MSG.BAL.CDT.DBT.IND` | `IxMsgBase_BalCdtDbtInd` |  |  |  |
| 191 | `IX.MSG.BAL.DATE` | `IxMsgBase_BalDate` |  |  |  |
| 192 | `IX.MSG.BAL.DATE.TIME` | `IxMsgBase_BalDateTime` |  |  |  |
| 193 | `IX.MSG.BAL.AVL.DAYS` | `IxMsgBase_BalAvlDays` |  |  |  |
| 194 | `IX.MSG.BAL.AVLBTY.ACTL.DT` | `IxMsgBase_BalAvlbtyActlDt` |  |  |  |
| 195 | `IX.MSG.BAL.AVLBTY.CCY.AMT` | `IxMsgBase_BalAvlbtyCcyAmt` |  |  |  |
| 196 | `IX.MSG.BAL.AVL.CDT.DBT.IND` | `IxMsgBase_BalAvlCdtDbtInd` |  |  |  |
| 197 | `IX.MSG.BAL.LOCAL.TAGS` | `IxMsgBase_BalLocalTags` |  |  |  |
| 198 | `IX.MSG.BAL.LOCAL.VALUES` | `IxMsgBase_BalLocalValues` |  |  |  |
| 199 | `IX.MSG.BAL.RESERVED.10` | `IxMsgBase_BalReserved10` | TField |  |  |
| 200 | `IX.MSG.BAL.RESERVED.9` | `IxMsgBase_BalReserved9` | TField |  |  |
| 201 | `IX.MSG.BAL.RESERVED.8` | `IxMsgBase_BalReserved8` | TField |  |  |
| 202 | `IX.MSG.BAL.RESERVED.7` | `IxMsgBase_BalReserved7` | TField |  |  |
| 203 | `IX.MSG.BAL.RESERVED.6` | `IxMsgBase_BalReserved6` | TField |  |  |
| 204 | `IX.MSG.BAL.RESERVED.5` | `IxMsgBase_BalReserved5` | TField |  |  |
| 205 | `IX.MSG.BAL.RESERVED.4` | `IxMsgBase_BalReserved4` | TField |  |  |
| 206 | `IX.MSG.BAL.RESERVED.3` | `IxMsgBase_BalReserved3` | TField |  |  |
| 207 | `IX.MSG.BAL.RESERVED.2` | `IxMsgBase_BalReserved2` | TField |  |  |
| 208 | `IX.MSG.BAL.RESERVED.1` | `IxMsgBase_BalReserved1` | TField |  |  |
| 209 | `IX.MSG.TXN.SUMM.TOT.NB.OF.ENT` | `IxMsgBase_TxnSummTotNbOfEnt` | TField |  |  |
| 210 | `IX.MSG.TXN.SUMM.TOL.ENT.SUM` | `IxMsgBase_TxnSummTolEntSum` | TField |  |  |
| 211 | `IX.MSG.TXN.SUMM.TOT.ENT.NET.AMT` | `IxMsgBase_TxnSummTotEntNetAmt` | TField |  |  |
| 212 | `IX.MSG.TXN.SUMM.TOT.CDT.DBT.IND` | `IxMsgBase_TxnSummTotCdtDbtInd` | TField |  |  |
| 213 | `IX.MSG.TXN.SUMM.CDT.NB.OF.NTRIES` | `IxMsgBase_TxnSummCdtNbOfNtries` | TField |  |  |
| 214 | `IX.MSG.TXN.SUMM.CDT.SUM` | `IxMsgBase_TxnSummCdtSum` | TField |  |  |
| 215 | `IX.MSG.TXN.SUMM.DBT.NB.OF.NTRIES` | `IxMsgBase_TxnSummDbtNbOfNtries` | TField |  |  |
| 216 | `IX.MSG.TXN.SUMM.DBT.SUM` | `IxMsgBase_TxnSummDbtSum` | TField |  |  |
| 217 | `IX.MSG.TXN.SUMM.LOCAL.TAGS` | `IxMsgBase_TxnSummLocalTags` |  |  |  |
| 218 | `IX.MSG.TXN.SUMM.LOCAL.VALUES` | `IxMsgBase_TxnSummLocalValues` |  |  |  |
| 219 | `IX.MSG.TXN.SUMM.RESERVED.10` | `IxMsgBase_TxnSummReserved10` | TField |  |  |
| 220 | `IX.MSG.TXN.SUMM.RESERVED.9` | `IxMsgBase_TxnSummReserved9` | TField |  |  |
| 221 | `IX.MSG.TXN.SUMM.RESERVED.8` | `IxMsgBase_TxnSummReserved8` | TField |  |  |
| 222 | `IX.MSG.TXN.SUMM.RESERVED.7` | `IxMsgBase_TxnSummReserved7` | TField |  |  |
| 223 | `IX.MSG.TXN.SUMM.RESERVED.6` | `IxMsgBase_TxnSummReserved6` | TField |  |  |
| 224 | `IX.MSG.TXN.SUMM.RESERVED.5` | `IxMsgBase_TxnSummReserved5` | TField |  |  |
| 225 | `IX.MSG.TXN.SUMM.RESERVED.4` | `IxMsgBase_TxnSummReserved4` | TField |  |  |
| 226 | `IX.MSG.TXN.SUMM.RESERVED.3` | `IxMsgBase_TxnSummReserved3` | TField |  |  |
| 227 | `IX.MSG.TXN.SUMM.RESERVED.2` | `IxMsgBase_TxnSummReserved2` | TField |  |  |
| 228 | `IX.MSG.TXN.SUMM.RESERVED.1` | `IxMsgBase_TxnSummReserved1` | TField |  |  |
| 229 | `IX.MSG.ENT.PER.NB.OF.NTRIES` | `IxMsgBase_EntPerNbOfNtries` |  |  |  |
| 230 | `IX.MSG.ENT.PER.SUM` | `IxMsgBase_EntPerSum` |  |  |  |
| 231 | `IX.MSG.ENT.PER.NET.AMT` | `IxMsgBase_EntPerNetAmt` |  |  |  |
| 232 | `IX.MSG.ENT.PER.CDT.DBT.IND` | `IxMsgBase_EntPerCdtDbtInd` |  |  |  |
| 233 | `IX.MSG.ENT.PER.FCST.INT` | `IxMsgBase_EntPerFcstInt` |  |  |  |
| 234 | `IX.MSG.ENT.PER.DOMN.CODE` | `IxMsgBase_EntPerDomnCode` |  |  |  |
| 235 | `IX.MSG.ENT.PER.DOMN.FMLY.CODE` | `IxMsgBase_EntPerDomnFmlyCode` |  |  |  |
| 236 | `IX.MSG.ENT.PER.DOM.SUBFMLY.CD` | `IxMsgBase_EntPerDomSubfmlyCd` |  |  |  |
| 237 | `IX.MSG.ENT.PER.PRTRY.CODE` | `IxMsgBase_EntPerPrtryCode` |  |  |  |
| 238 | `IX.MSG.ENT.PER.PRTRY.ISSR` | `IxMsgBase_EntPerPrtryIssr` |  |  |  |
| 239 | `IX.MSG.ENT.PER.AVL.DAYS` | `IxMsgBase_EntPerAvlDays` |  |  |  |
| 240 | `IX.MSG.ENT.PER.AVL.ACTL.DT` | `IxMsgBase_EntPerAvlActlDt` |  |  |  |
| 241 | `IX.MSG.ENT.PER.AVL.CCY.AMT` | `IxMsgBase_EntPerAvlCcyAmt` |  |  |  |
| 242 | `IX.MSG.ENT.PER.AVCD.DB.IND` | `IxMsgBase_EntPerAvcdDbInd` |  |  |  |
| 243 | `IX.MSG.ENT.PER.RESERVED.10` | `IxMsgBase_EntPerReserved10` | TField |  |  |
| 244 | `IX.MSG.ENT.PER.RESERVED.9` | `IxMsgBase_EntPerReserved9` | TField |  |  |
| 245 | `IX.MSG.ENT.PER.RESERVED.8` | `IxMsgBase_EntPerReserved8` | TField |  |  |
| 246 | `IX.MSG.ENT.PER.RESERVED.7` | `IxMsgBase_EntPerReserved7` | TField |  |  |
| 247 | `IX.MSG.ENT.PER.RESERVED.6` | `IxMsgBase_EntPerReserved6` | TField |  |  |
| 248 | `IX.MSG.ENT.PER.RESERVED.5` | `IxMsgBase_EntPerReserved5` | TField |  |  |
| 249 | `IX.MSG.ENT.PER.RESERVED.4` | `IxMsgBase_EntPerReserved4` | TField |  |  |
| 250 | `IX.MSG.ENT.PER.RESERVED.3` | `IxMsgBase_EntPerReserved3` | TField |  |  |
| 251 | `IX.MSG.ENT.PER.RESERVED.2` | `IxMsgBase_EntPerReserved2` | TField |  |  |
| 252 | `IX.MSG.ENT.PER.RESERVED.1` | `IxMsgBase_EntPerReserved1` | TField |  |  |
| 253 | `IX.MSG.ENTRY.REF` | `IxMsgBase_EntryRef` |  |  |  |
| 254 | `IX.MSG.ENT.CCY.AMOUNT` | `IxMsgBase_EntCcyAmount` |  |  |  |
| 255 | `IX.MSG.ENT.CDT.DBT.IND` | `IxMsgBase_EntCdtDbtInd` |  |  |  |
| 256 | `IX.MSG.ENT.REV.IND` | `IxMsgBase_EntRevInd` |  |  |  |
| 257 | `IX.MSG.ENT.STATUS` | `IxMsgBase_EntStatus` |  |  |  |
| 258 | `IX.MSG.ENT.BOOK.DATE` | `IxMsgBase_EntBookDate` |  |  |  |
| 259 | `IX.MSG.ENT.BOOKING.DATE.TIME` | `IxMsgBase_EntBookingDateTime` |  |  |  |
| 260 | `IX.MSG.ENT.VALUE.DATE` | `IxMsgBase_EntValueDate` |  |  |  |
| 261 | `IX.MSG.ENT.VALUE.DATE.TIME` | `IxMsgBase_EntValueDateTime` |  |  |  |
| 262 | `IX.MSG.ENT.SVCR.REF` | `IxMsgBase_EntSvcrRef` |  |  |  |
| 263 | `IX.MSG.ENT.AVLBTY.NBOFDAYS` | `IxMsgBase_EntAvlbtyNbofdays` |  |  |  |
| 264 | `IX.MSG.ENT.AVLBTY.ACTL.DT` | `IxMsgBase_EntAvlbtyActlDt` |  |  |  |
| 265 | `IX.MSG.ENT.AVLBTY.CCY.AMT` | `IxMsgBase_EntAvlbtyCcyAmt` |  |  |  |
| 266 | `IX.MSG.ENT.AVL.CDT.DBT.IND` | `IxMsgBase_EntAvlCdtDbtInd` |  |  |  |
| 267 | `IX.MSG.ENT.BK.TX.DOMNCODE` | `IxMsgBase_EntBkTxDomncode` |  |  |  |
| 268 | `IX.MSG.ENT.BK.TX.FMLYCODE` | `IxMsgBase_EntBkTxFmlycode` |  |  |  |
| 269 | `IX.MSG.ENT.BK.TX.SUB.FMLYCODE` | `IxMsgBase_EntBkTxSubFmlycode` |  |  |  |
| 270 | `IX.MSG.ENT.BK.TX.PRTRYCODE` | `IxMsgBase_EntBkTxPrtrycode` |  |  |  |
| 271 | `IX.MSG.ENT.BK.TX.PRTRY.ISSUER` | `IxMsgBase_EntBkTxPrtryIssuer` |  |  |  |
| 272 | `IX.MSG.ENT.COMSSN.WVR.IND` | `IxMsgBase_EntComssnWvrInd` |  |  |  |
| 273 | `IX.MSG.ENT.ADDINFO.MSG.NM.ID` | `IxMsgBase_EntAddinfoMsgNmId` |  |  |  |
| 274 | `IX.MSG.ENT.ADDINFO.MSG.ID` | `IxMsgBase_EntAddinfoMsgId` |  |  |  |
| 275 | `IX.MSG.ENT.INSTD.AMT.CCY.AMT` | `IxMsgBase_EntInstdAmtCcyAmt` |  |  |  |
| 276 | `IX.MSG.ENT.INSTD.AMT.SRC.CCY` | `IxMsgBase_EntInstdAmtSrcCcy` |  |  |  |
| 277 | `IX.MSG.ENT.INSTD.AMT.TRGT.CCY` | `IxMsgBase_EntInstdAmtTrgtCcy` |  |  |  |
| 278 | `IX.MSG.ENT.INSTD.AMT.UNIT.CCY` | `IxMsgBase_EntInstdAmtUnitCcy` |  |  |  |
| 279 | `IX.MSG.ENT.INS.AMT.XCH.RATE` | `IxMsgBase_EntInsAmtXchRate` |  |  |  |
| 280 | `IX.MSG.ENT.INSTD.AMT.CTRCT.ID` | `IxMsgBase_EntInstdAmtCtrctId` |  |  |  |
| 281 | `IX.MSG.ENT.INSTD.AMT.QTN.DT` | `IxMsgBase_EntInstdAmtQtnDt` |  |  |  |
| 282 | `IX.MSG.ENT.TX.AMT.CCY.AMT` | `IxMsgBase_EntTxAmtCcyAmt` |  |  |  |
| 283 | `IX.MSG.ENT.TX.AMT.SRC.CCY` | `IxMsgBase_EntTxAmtSrcCcy` |  |  |  |
| 284 | `IX.MSG.ENT.TX.AMT.TRGT.CCY` | `IxMsgBase_EntTxAmtTrgtCcy` |  |  |  |
| 285 | `IX.MSG.ENT.TX.AMT.UNIT.CCY` | `IxMsgBase_EntTxAmtUnitCcy` |  |  |  |
| 286 | `IX.MSG.ENT.TX.AMT.XCHG.RATE` | `IxMsgBase_EntTxAmtXchgRate` |  |  |  |
| 287 | `IX.MSG.ENT.TX.AMT.CTRCT.ID` | `IxMsgBase_EntTxAmtCtrctId` |  |  |  |
| 288 | `IX.MSG.ENT.TX.AMT.QTN.DT` | `IxMsgBase_EntTxAmtQtnDt` |  |  |  |
| 289 | `IX.MSG.ENT.CTRL.VAL.CCY.AMT` | `IxMsgBase_EntCtrlValCcyAmt` |  |  |  |
| 290 | `IX.MSG.ENT.CTRL.VAL.AMT.SRC` | `IxMsgBase_EntCtrlValAmtSrc` |  |  |  |
| 291 | `IX.MSG.ENT.CTRL.VAL.AMT.TRGT` | `IxMsgBase_EntCtrlValAmtTrgt` |  |  |  |
| 292 | `IX.MSG.ENT.CTRL.VAL.AMT.UNIT` | `IxMsgBase_EntCtrlValAmtUnit` |  |  |  |
| 293 | `IX.MSG.ENT.CTRL.VAL.AMT.XCHRT` | `IxMsgBase_EntCtrlValAmtXchrt` |  |  |  |
| 294 | `IX.MSG.ENT.CTRL.VAL.AMT.CTID` | `IxMsgBase_EntCtrlValAmtCtid` |  |  |  |
| 295 | `IX.MSG.ENT.CTRL.VAL.AMT.QTNDT` | `IxMsgBase_EntCtrlValAmtQtndt` |  |  |  |
| 296 | `IX.MSG.ENT.ANCD.PST.AMT.CCY` | `IxMsgBase_EntAncdPstAmtCcy` |  |  |  |
| 297 | `IX.MSG.ENT.ANCD.PST.AMT.SRC` | `IxMsgBase_EntAncdPstAmtSrc` |  |  |  |
| 298 | `IX.MSG.ENT.ANCD.PST.AMT.TRGT` | `IxMsgBase_EntAncdPstAmtTrgt` |  |  |  |
| 299 | `IX.MSG.ENT.ANCD.PST.AMT.UNIT` | `IxMsgBase_EntAncdPstAmtUnit` |  |  |  |
| 300 | `IX.MSG.ENT.ANCD.PST.AMT.XCHRT` | `IxMsgBase_EntAncdPstAmtXchrt` |  |  |  |
| 301 | `IX.MSG.ENT.ANNCD.PST.AMT.CTID` | `IxMsgBase_EntAnncdPstAmtCtid` |  |  |  |
| 302 | `IX.MSG.ENT.ANCD.PST.AMT.QTNDT` | `IxMsgBase_EntAncdPstAmtQtndt` |  |  |  |
| 303 | `IX.MSG.ENT.PRTRY.TP` | `IxMsgBase_EntPrtryTp` |  |  |  |
| 304 | `IX.MSG.ENT.PRTRY.AMT.CCY.AMT` | `IxMsgBase_EntPrtryAmtCcyAmt` |  |  |  |
| 305 | `IX.MSG.ENT.PRTRY.AMT.SRC.CCY` | `IxMsgBase_EntPrtryAmtSrcCcy` |  |  |  |
| 306 | `IX.MSG.ENT.PRTRY.AMT.TRGT.CCY` | `IxMsgBase_EntPrtryAmtTrgtCcy` |  |  |  |
| 307 | `IX.MSG.ENT.PRTRY.AMT.UNIT.CCY` | `IxMsgBase_EntPrtryAmtUnitCcy` |  |  |  |
| 308 | `IX.MSG.ENT.PRTRY.AMT.XCHRT` | `IxMsgBase_EntPrtryAmtXchrt` |  |  |  |
| 309 | `IX.MSG.ENT.PRTRY.AMT.CTRCT.ID` | `IxMsgBase_EntPrtryAmtCtrctId` |  |  |  |
| 310 | `IX.MSG.ENT.PRTRY.AMT.QTN.DT` | `IxMsgBase_EntPrtryAmtQtnDt` |  |  |  |
| 311 | `IX.MSG.ENT.CH.CCY.TOT.CHG.TAX` | `IxMsgBase_EntChCcyTotChgTax` |  |  |  |
| 312 | `IX.MSG.ENT.CHG.CCY.AMT` | `IxMsgBase_EntChgCcyAmt` |  |  |  |
| 313 | `IX.MSG.ENT.CHG.CDT.DBT.IND` | `IxMsgBase_EntChgCdtDbtInd` |  |  |  |
| 314 | `IX.MSG.ENT.CHG.TP.CODE` | `IxMsgBase_EntChgTpCode` |  |  |  |
| 315 | `IX.MSG.ENT.CHG.PRTRY.ID` | `IxMsgBase_EntChgPrtryId` |  |  |  |
| 316 | `IX.MSG.ENT.CHG.PRTRY.ISSR` | `IxMsgBase_EntChgPrtryIssr` |  |  |  |
| 317 | `IX.MSG.ENT.CHG.RATE` | `IxMsgBase_EntChgRate` |  |  |  |
| 318 | `IX.MSG.ENT.CHG.BR` | `IxMsgBase_EntChgBr` |  |  |  |
| 319 | `IX.MSG.ENT.CHG.PTY.BIC` | `IxMsgBase_EntChgPtyBic` |  |  |  |
| 320 | `IX.MSG.ENT.CH.PTY.CL.SYSID.CD` | `IxMsgBase_EntChPtyClSysidCd` |  |  |  |
| 321 | `IX.MSG.ENT.CH.PTY.CL.SYSID.PY` | `IxMsgBase_EntChPtyClSysidPy` |  |  |  |
| 322 | `IX.MSG.ENT.CHG.PTY.MMBLD` | `IxMsgBase_EntChgPtyMmbld` |  |  |  |
| 323 | `IX.MSG.ENT.CHG.PTY.NAME` | `IxMsgBase_EntChgPtyName` |  |  |  |
| 324 | `IX.MSG.ENT.CHG.PTY.ADR.TP` | `IxMsgBase_EntChgPtyAdrTp` |  |  |  |
| 325 | `IX.MSG.ENT.CHG.PTY.DEPT` | `IxMsgBase_EntChgPtyDept` |  |  |  |
| 326 | `IX.MSG.ENT.CHG.PTY.SUBDEPT` | `IxMsgBase_EntChgPtySubdept` |  |  |  |
| 327 | `IX.MSG.ENT.CHG.PTY.STREET` | `IxMsgBase_EntChgPtyStreet` |  |  |  |
| 328 | `IX.MSG.ENT.CHG.PTY.BUILDING` | `IxMsgBase_EntChgPtyBuilding` |  |  |  |
| 329 | `IX.MSG.ENT.CHG.PTY.POSTCODE` | `IxMsgBase_EntChgPtyPostcode` |  |  |  |
| 330 | `IX.MSG.ENT.CHG.PTY.TOWN` | `IxMsgBase_EntChgPtyTown` |  |  |  |
| 331 | `IX.MSG.ENT.CHG.PTY.SUBDVSN` | `IxMsgBase_EntChgPtySubdvsn` |  |  |  |
| 332 | `IX.MSG.ENT.CHG.PTY.COUNTRY` | `IxMsgBase_EntChgPtyCountry` |  |  |  |
| 333 | `IX.MSG.ENT.CH.PTY.ADR.LIST` | `IxMsgBase_EntChPtyAdrList` |  |  |  |
| 334 | `IX.MSG.ENT.CHG.PTY.OTHER.ID` | `IxMsgBase_EntChgPtyOtherId` |  |  |  |
| 335 | `IX.MSG.ENT.CHG.PTY.OTHER.CODE` | `IxMsgBase_EntChgPtyOtherCode` |  |  |  |
| 336 | `IX.MSG.ENT.CH.PTY.OTH.PTY` | `IxMsgBase_EntChPtyOthPty` |  |  |  |
| 337 | `IX.MSG.ENT.CHG.PTY.OTHER.ISSR` | `IxMsgBase_EntChgPtyOtherIssr` |  |  |  |
| 338 | `IX.MSG.ENT.CHG.PTY.BRANCH.ID` | `IxMsgBase_EntChgPtyBranchId` |  |  |  |
| 339 | `IX.MSG.ENT.CH.PTY.BR.NAME` | `IxMsgBase_EntChPtyBrName` |  |  |  |
| 340 | `IX.MSG.ENT.CH.PTY.BR.ADR.TP` | `IxMsgBase_EntChPtyBrAdrTp` |  |  |  |
| 341 | `IX.MSG.ENT.CH.PTY.BR.DEPT` | `IxMsgBase_EntChPtyBrDept` |  |  |  |
| 342 | `IX.MSG.ENT.CH.PTY.BR.SUBDEPT` | `IxMsgBase_EntChPtyBrSubdept` |  |  |  |
| 343 | `IX.MSG.ENT.CH.PTY.BR.STREET` | `IxMsgBase_EntChPtyBrStreet` |  |  |  |
| 344 | `IX.MSG.ENT.CH.PTY.BR.BUILDING` | `IxMsgBase_EntChPtyBrBuilding` |  |  |  |
| 345 | `IX.MSG.ENT.CH.PTY.BR.POSTCODE` | `IxMsgBase_EntChPtyBrPostcode` |  |  |  |
| 346 | `IX.MSG.ENT.CH.PTY.BR.TOWN` | `IxMsgBase_EntChPtyBrTown` |  |  |  |
| 347 | `IX.MSG.ENT.CH.PTY.BR.SUBDVSN` | `IxMsgBase_EntChPtyBrSubdvsn` |  |  |  |
| 348 | `IX.MSG.ENT.CH.PTY.BR.COUNTRY` | `IxMsgBase_EntChPtyBrCountry` |  |  |  |
| 349 | `IX.MSG.ENT.CH.PTY.BR.ADRLT` | `IxMsgBase_EntChPtyBrAdrlt` |  |  |  |
| 350 | `IX.MSG.ENT.CHG.TAX.ID` | `IxMsgBase_EntChgTaxId` |  |  |  |
| 351 | `IX.MSG.ENT.CHG.TAX.RATE` | `IxMsgBase_EntChgTaxRate` |  |  |  |
| 352 | `IX.MSG.ENT.CHG.TAX.CCY.AMT` | `IxMsgBase_EntChgTaxCcyAmt` |  |  |  |
| 353 | `IX.MSG.ENT.TECH.INPT.CODE` | `IxMsgBase_EntTechInptCode` |  |  |  |
| 354 | `IX.MSG.ENT.TECH.INPT.PRTRY` | `IxMsgBase_EntTechInptPrtry` |  |  |  |
| 355 | `IX.MSG.ENT.INT.CCY.AMT` | `IxMsgBase_EntIntCcyAmt` |  |  |  |
| 356 | `IX.MSG.ENT.INT.CDT.DBT.IND` | `IxMsgBase_EntIntCdtDbtInd` |  |  |  |
| 357 | `IX.MSG.ENT.INT.TP.CODE` | `IxMsgBase_EntIntTpCode` |  |  |  |
| 358 | `IX.MSG.ENT.INT.TP.PRTRY` | `IxMsgBase_EntIntTpPrtry` |  |  |  |
| 359 | `IX.MSG.ENT.INT.RATE.PCTG` | `IxMsgBase_EntIntRatePctg` |  |  |  |
| 360 | `IX.MSG.ENT.INT.RATE.OTHER` | `IxMsgBase_EntIntRateOther` |  |  |  |
| 361 | `IX.MSG.ENT.INT.RT.FR.BDRY.AMT` | `IxMsgBase_EntIntRtFrBdryAmt` |  |  |  |
| 362 | `IX.MSG.ENT.INT.RATE.FR.INCL` | `IxMsgBase_EntIntRateFrIncl` |  |  |  |
| 363 | `IX.MSG.ENT.INT.RT.TO.BDRY.AMT` | `IxMsgBase_EntIntRtToBdryAmt` |  |  |  |
| 364 | `IX.MSG.ENT.INT.RATE.TO.INCL` | `IxMsgBase_EntIntRateToIncl` |  |  |  |
| 365 | `IX.MSG.ENT.INT.RT.FT.BDRY.AMT` | `IxMsgBase_EntIntRtFtBdryAmt` |  |  |  |
| 366 | `IX.MSG.ENT.INT.RT.FTF.INCL` | `IxMsgBase_EntIntRtFtfIncl` |  |  |  |
| 367 | `IX.MSG.ENT.INT.RT.FTT.BDR.AMT` | `IxMsgBase_EntIntRtFttBdrAmt` |  |  |  |
| 368 | `IX.MSG.ENT.INT.RT.FTT.INCL` | `IxMsgBase_EntIntRtFttIncl` |  |  |  |
| 369 | `IX.MSG.ENT.INT.RATE.EQ.AMT` | `IxMsgBase_EntIntRateEqAmt` |  |  |  |
| 370 | `IX.MSG.ENT.INT.RATE.NEQ.AMT` | `IxMsgBase_EntIntRateNeqAmt` |  |  |  |
| 371 | `IX.MSG.ENT.INT.RT.CDT.DB.IND` | `IxMsgBase_EntIntRtCdtDbInd` |  |  |  |
| 372 | `IX.MSG.ENT.INT.RATE.CCY` | `IxMsgBase_EntIntRateCcy` |  |  |  |
| 373 | `IX.MSG.ENT.INT.FR.DT.TM` | `IxMsgBase_EntIntFrDtTm` |  |  |  |
| 374 | `IX.MSG.ENT.INT.TO.DT.TM` | `IxMsgBase_EntIntToDtTm` |  |  |  |
| 375 | `IX.MSG.ENT.INT.RSN` | `IxMsgBase_EntIntRsn` |  |  |  |
| 376 | `IX.MSG.ENT.ADD.ENTRY.INFO` | `IxMsgBase_EntAddEntryInfo` |  |  |  |
| 377 | `IX.MSG.ENTRY.LOCAL.TAGS` | `IxMsgBase_EntryLocalTags` |  |  |  |
| 378 | `IX.MSG.ENTRY.LOCAL.VALUES` | `IxMsgBase_EntryLocalValues` |  |  |  |
| 379 | `IX.MSG.BTCH.MSG.ID` | `IxMsgBase_BtchMsgId` |  |  |  |
| 380 | `IX.MSG.BTCH.PMT.INF.IND` | `IxMsgBase_BtchPmtInfInd` |  |  |  |
| 381 | `IX.MSG.BTCH.NB.OF.TXS` | `IxMsgBase_BtchNbOfTxs` |  |  |  |
| 382 | `IX.MSG.BTCH.CCY.AMT` | `IxMsgBase_BtchCcyAmt` |  |  |  |
| 383 | `IX.MSG.BTCH.CDT.DBT.IND` | `IxMsgBase_BtchCdtDbtInd` |  |  |  |
| 384 | `IX.MSG.BTCH.LOCAL.TAGS` | `IxMsgBase_BtchLocalTags` |  |  |  |
| 385 | `IX.MSG.BTCH.LOCAL.VALUES` | `IxMsgBase_BtchLocalValues` |  |  |  |
| 386 | `IX.MSG.TXN.DET.ALL.INFO` | `IxMsgBase_TxnDetAllInfo` |  |  |  |
| 387 | `IX.MSG.ENT.RESERVED.10` | `IxMsgBase_EntReserved10` | TField |  |  |
| 388 | `IX.MSG.ENT.RESERVED.9` | `IxMsgBase_EntReserved9` | TField |  |  |
| 389 | `IX.MSG.ENT.RESERVED.8` | `IxMsgBase_EntReserved8` | TField |  |  |
| 390 | `IX.MSG.ENT.RESERVED.7` | `IxMsgBase_EntReserved7` | TField |  |  |
| 391 | `IX.MSG.ENT.RESERVED.6` | `IxMsgBase_EntReserved6` | TField |  |  |
| 392 | `IX.MSG.ENT.RESERVED.5` | `IxMsgBase_EntReserved5` | TField |  |  |
| 393 | `IX.MSG.ENT.RESERVED.4` | `IxMsgBase_EntReserved4` | TField |  |  |
| 394 | `IX.MSG.ENT.RESERVED.3` | `IxMsgBase_EntReserved3` | TField |  |  |
| 395 | `IX.MSG.ENT.RESERVED.2` | `IxMsgBase_EntReserved2` | TField |  |  |
| 396 | `IX.MSG.ENT.RESERVED.1` | `IxMsgBase_EntReserved1` | TField |  |  |
| 397 | `IX.MSG.HDR.SEG.ACCOUNT.ID` | `IxMsgBase_HdrSegAccountId` | TField |  |  |
| 398 | `IX.MSG.HDR.SEG.MESSAGE.TYPE` | `IxMsgBase_HdrSegMessageType` | TField |  |  |
| 399 | `IX.MSG.HDR.SEG.STMT.DATE` | `IxMsgBase_HdrSegStmtDate` | TField |  |  |
| 400 | `IX.MSG.HDR.SEG.COMPANY.ID` | `IxMsgBase_HdrSegCompanyId` | TField |  |  |
| 401 | `IX.MSG.SEGMENT.COUNT` | `IxMsgBase_SegmentCount` | TField |  |  |
| 402 | `IX.MSG.SEGMENT.ID` | `IxMsgBase_SegmentId` | TField |  |  |
| 403 | `IX.MSG.NO.MVMT.STMT` | `IxMsgBase_NoMvmtStmt` | TField |  |  |
| 404 | `IX.MSG.RESERVED.9` | `IxMsgBase_Reserved9` | TField |  |  |
| 405 | `IX.MSG.RESERVED.8` | `IxMsgBase_Reserved8` | TField |  |  |
| 406 | `IX.MSG.RESERVED.7` | `IxMsgBase_Reserved7` | TField |  |  |
| 407 | `IX.MSG.RESERVED.6` | `IxMsgBase_Reserved6` | TField |  |  |
| 408 | `IX.MSG.RESERVED.5` | `IxMsgBase_Reserved5` | TField |  |  |
| 409 | `IX.MSG.RESERVED.4` | `IxMsgBase_Reserved4` | TField |  |  |
| 410 | `IX.MSG.RESERVED.3` | `IxMsgBase_Reserved3` | TField |  |  |
| 411 | `IX.MSG.RESERVED.2` | `IxMsgBase_Reserved2` | TField |  |  |
| 412 | `IX.MSG.RESERVED.1` | `IxMsgBase_Reserved1` | TField |  |  |
| 413 | `IX.MSG.LOCAL.REF` | `IxMsgBase_LocalRef` |  |  |  |
