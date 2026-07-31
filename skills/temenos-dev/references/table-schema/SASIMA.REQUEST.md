# SASIMA.REQUEST — Table Schema

> Source: `INSERTS/I_F.SASIMA.REQUEST` in `SASIMA_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SR.WS.RUN.NO` | `SasimaRequest_RunNo` | TField |  |  |
| 2 | `SR.WS.ACTION` | `SasimaRequest_Action` | TField |  |  |
| 3 | `SR.WS.USER.ID` | `SasimaRequest_UserId` | TField |  |  |
| 4 | `SR.WS.LANGUAGE` | `SasimaRequest_Language` | TField |  |  |
| 5 | `SR.WS.ENQUIRY.TYPE` | `SasimaRequest_EnquiryType` | TField |  |  |
| 6 | `SR.WS.PRODUCT.TYPE` | `SasimaRequest_ProductType` | TField |  |  |
| 7 | `SR.WS.NO.OF.APPLICANTS` | `SasimaRequest_NoOfApplicants` | TField |  |  |
| 8 | `SR.WS.ACCOUNT.TYPE` | `SasimaRequest_AccountType` | TField |  |  |
| 9 | `SR.WS.ENQUIRY.REFERENCE` | `SasimaRequest_EnquiryReference` | TField |  |  |
| 10 | `SR.WS.PRCDPT` | `SasimaRequest_Prcdpt` | TField |  |  |
| 11 | `SR.WS.ENQRSN` | `SasimaRequest_Enqrsn` | TField |  |  |
| 12 | `SR.WS.AMOUNT` | `SasimaRequest_Amount` | TField |  |  |
| 13 | `SR.WS.CUSTOMER.CODE` | `SasimaRequest_CustomerCode` |  |  |  |
| 14 | `SR.WS.CAPL` | `SasimaRequest_Capl` |  |  |  |
| 15 | `SR.WS.CID1` | `SasimaRequest_Cid1` |  |  |  |
| 16 | `SR.WS.CID2` | `SasimaRequest_Cid2` |  |  |  |
| 17 | `SR.WS.CID3` | `SasimaRequest_Cid3` |  |  |  |
| 18 | `SR.WS.CADT` | `SasimaRequest_Cadt` |  |  |  |
| 19 | `SR.WS.CDOB` | `SasimaRequest_Cdob` |  |  |  |
| 20 | `SR.WS.CGND` | `SasimaRequest_Cgnd` |  |  |  |
| 21 | `SR.WS.CMAR` | `SasimaRequest_Cmar` |  |  |  |
| 22 | `SR.WS.CNAT` | `SasimaRequest_Cnat` |  |  |  |
| 23 | `SR.WS.CNMFA` | `SasimaRequest_Cnmfa` |  |  |  |
| 24 | `SR.WS.CNM1A` | `SasimaRequest_Cnm1a` |  |  |  |
| 25 | `SR.WS.CNM2A` | `SasimaRequest_Cnm2a` |  |  |  |
| 26 | `SR.WS.CNM3A` | `SasimaRequest_Cnm3a` |  |  |  |
| 27 | `SR.WS.CNMFE` | `SasimaRequest_Cnmfe` |  |  |  |
| 28 | `SR.WS.CNM1E` | `SasimaRequest_Cnm1e` |  |  |  |
| 29 | `SR.WS.CNM2E` | `SasimaRequest_Cnm2e` |  |  |  |
| 30 | `SR.WS.CNM3E` | `SasimaRequest_Cnm3e` |  |  |  |
| 31 | `SR.WS.CEML` | `SasimaRequest_Ceml` |  |  |  |
| 32 | `SR.WS.CAD1A` | `SasimaRequest_Cad1a` |  |  |  |
| 33 | `SR.WS.CAD2A` | `SasimaRequest_Cad2a` |  |  |  |
| 34 | `SR.WS.CAD1E` | `SasimaRequest_Cad1e` |  |  |  |
| 35 | `SR.WS.CAD2E` | `SasimaRequest_Cad2e` |  |  |  |
| 36 | `SR.WS.CAD6` | `SasimaRequest_Cad6` |  |  |  |
| 37 | `SR.WS.CAD7` | `SasimaRequest_Cad7` |  |  |  |
| 38 | `SR.WS.CAD8E` | `SasimaRequest_Cad8e` |  |  |  |
| 39 | `SR.WS.CAD8A` | `SasimaRequest_Cad8a` |  |  |  |
| 40 | `SR.WS.CAD9` | `SasimaRequest_Cad9` |  |  |  |
| 41 | `SR.WS.CCN1` | `SasimaRequest_Ccn1` |  |  |  |
| 42 | `SR.WS.CCN2` | `SasimaRequest_Ccn2` |  |  |  |
| 43 | `SR.WS.CCN3` | `SasimaRequest_Ccn3` |  |  |  |
| 44 | `SR.WS.CCN4` | `SasimaRequest_Ccn4` |  |  |  |
| 45 | `SR.WS.CCN5` | `SasimaRequest_Ccn5` |  |  |  |
| 46 | `SR.WS.ETYP` | `SasimaRequest_Etyp` |  |  |  |
| 47 | `SR.WS.EOCA` | `SasimaRequest_Eoca` |  |  |  |
| 48 | `SR.WS.EOCE` | `SasimaRequest_Eoce` |  |  |  |
| 49 | `SR.WS.EDOE` | `SasimaRequest_Edoe` |  |  |  |
| 50 | `SR.WS.ELEN` | `SasimaRequest_Elen` |  |  |  |
| 51 | `SR.WS.ECEX` | `SasimaRequest_Ecex` |  |  |  |
| 52 | `SR.WS.EMBS` | `SasimaRequest_Embs` |  |  |  |
| 53 | `SR.WS.ETMS` | `SasimaRequest_Etms` |  |  |  |
| 54 | `SR.WS.ESLF` | `SasimaRequest_Eslf` |  |  |  |
| 55 | `SR.WS.ENMA` | `SasimaRequest_Enma` |  |  |  |
| 56 | `SR.WS.ENME` | `SasimaRequest_Enme` |  |  |  |
| 57 | `SR.WS.EECO` | `SasimaRequest_Eeco` |  |  |  |
| 58 | `SR.WS.EBUS` | `SasimaRequest_Ebus` |  |  |  |
| 59 | `SR.WS.ECRN` | `SasimaRequest_Ecrn` |  |  |  |
| 60 | `SR.WS.EADT` | `SasimaRequest_Eadt` |  |  |  |
| 61 | `SR.WS.EAD1A` | `SasimaRequest_Ead1a` |  |  |  |
| 62 | `SR.WS.EAD2A` | `SasimaRequest_Ead2a` |  |  |  |
| 63 | `SR.WS.EAD1E` | `SasimaRequest_Ead1e` |  |  |  |
| 64 | `SR.WS.EAD2E` | `SasimaRequest_Ead2e` |  |  |  |
| 65 | `SR.WS.EAD6` | `SasimaRequest_Ead6` |  |  |  |
| 66 | `SR.WS.EAD7` | `SasimaRequest_Ead7` |  |  |  |
| 67 | `SR.WS.EAD8E` | `SasimaRequest_Ead8e` |  |  |  |
| 68 | `SR.WS.EAD8A` | `SasimaRequest_Ead8a` |  |  |  |
| 69 | `SR.WS.EAD9` | `SasimaRequest_Ead9` |  |  |  |
| 70 | `SR.WS.EEML` | `SasimaRequest_Eeml` |  |  |  |
| 71 | `SR.WS.WS.RESULT` | `SasimaRequest_WsResult` | TField |  |  |
| 72 | `SR.WS.REQ.XML` | `SasimaRequest_ReqXml` |  |  |  |
| 73 | `SR.WS.RESP.XML` | `SasimaRequest_RespXml` |  |  |  |
| 74 | `SR.WS.SERVICE` | `SasimaRequest_Service` | TField |  |  |
| 75 | `SR.WS.MEMBERID` | `SasimaRequest_Memberid` | TField |  |  |
| 76 | `SR.WS.WEB.CONSUME` | `SasimaRequest_WebConsume` | TField |  |  |
| 77 | `SR.WS.RESERVED.1` | `SasimaRequest_Reserved1` | TField |  |  |
| 78 | `SR.WS.RESERVED.2` | `SasimaRequest_Reserved2` | TField |  |  |
| 79 | `SR.WS.RESERVED.3` | `SasimaRequest_Reserved3` | TField |  |  |
| 80 | `SR.WS.RESERVED.4` | `SasimaRequest_Reserved4` | TField |  |  |
| 81 | `SR.WS.RESERVED.5` | `SasimaRequest_Reserved5` | TField |  |  |
| 82 | `SR.WS.RESERVED.6` | `SasimaRequest_Reserved6` | TField |  |  |
| 83 | `SR.WS.RESERVED.7` | `SasimaRequest_Reserved7` | TField |  |  |
| 84 | `SR.WS.RESERVED.8` | `SasimaRequest_Reserved8` | TField |  |  |
| 85 | `SR.WS.RESERVED.9` | `SasimaRequest_Reserved9` | TField |  |  |
| 86 | `SR.WS.RESERVED.10` | `SasimaRequest_Reserved10` | TField |  |  |
| 87 | `SR.WS.LOCAL.REF` | `SasimaRequest_LocalRef` |  |  |  |
| 88 | `SR.WS.OVERRIDE` | `SasimaRequest_Override` |  |  |  |
| 89 | `SR.WS.RECORD.STATUS` | `SasimaRequest_RecordStatus` | String |  |  |
| 90 | `SR.WS.CURR.NO` | `SasimaRequest_CurrNo` | String |  |  |
| 91 | `SR.WS.INPUTTER` | `SasimaRequest_Inputter` |  |  |  |
| 92 | `SR.WS.DATE.TIME` | `SasimaRequest_DateTime` |  |  |  |
| 93 | `SR.WS.AUTHORISER` | `SasimaRequest_Authoriser` | String |  |  |
| 94 | `SR.WS.CO.CODE` | `SasimaRequest_CoCode` | String |  |  |
| 95 | `SR.WS.DEPT.CODE` | `SasimaRequest_DeptCode` | String |  |  |
| 96 | `SR.WS.AUDITOR.CODE` | `SasimaRequest_AuditorCode` | String |  |  |
| 97 | `SR.WS.AUDIT.DATE.TIME` | `SasimaRequest_AuditDateTime` | String |  |  |
