# SC.SRD.BNK.STATIC.DTLS — Table Schema

> Source: `INSERTS/I_F.SC.SRD.BNK.STATIC.DTLS` in `SC_ScSrdEventCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SRBD.RSPND.INTERM` | `ScSrdBnkStaticDtls_RspndInterm` | TField |  | Field holds the bank�s own customer number who is responding to the shareholders identification disclosurerequest. |
| 2 | `SC.SRBD.BNK.CTCT.PRSN.TITLE` | `ScSrdBnkStaticDtls_BnkCtctPrsnTitle` | TField |  | This field holds the title of the concerned contact person from Bank Validation Rules Allowed Values defined in EbLookup - DOCT, MISS, MIST, MADM Value can be given if BNK.CTCT.PRSN.NM is given. |
| 3 | `SC.SRBD.BNK.CTCT.PRSN.FRST.NM` | `ScSrdBnkStaticDtls_BnkCtctPrsnFrstNm` | TField |  | This field holds the first name of the contact person. Validation Rules Value can be given if BNK.CTCT.PRSN.NM is given. |
| 4 | `SC.SRBD.BNK.CTCT.PRSN.NM` | `ScSrdBnkStaticDtls_BnkCtctPrsnNm` | TField |  | This field holds the name of the contact person. |
| 5 | `SC.SRBD.PHONE.NUMBER` | `ScSrdBnkStaticDtls_PhoneNumber` |  |  |  |
| 6 | `SC.SRBD.MOBILE.NUMBER` | `ScSrdBnkStaticDtls_MobileNumber` |  |  |  |
| 7 | `SC.SRBD.FAX.NUMBER` | `ScSrdBnkStaticDtls_FaxNumber` |  |  |  |
| 8 | `SC.SRBD.EMAIL` | `ScSrdBnkStaticDtls_Email` |  |  |  |
| 9 | `SC.SRBD.OUTWARD.CANC.GEN.METHOD` | `ScSrdBnkStaticDtls_OutwardCancGenMethod` | TField |  | Field to cancel last sent response and generate new response |
| 10 | `SC.SRBD.OFS.SOURCE` | `ScSrdBnkStaticDtls_OfsSource` | TField |  | Field to hold OFS.SOURCE record ID used for processing |
| 11 | `SC.SRBD.OFS.VERSION` | `ScSrdBnkStaticDtls_OfsVersion` | TField |  | Field to hold version ID used for processing |
| 12 | `SC.SRBD.RESERVED1` | `ScSrdBnkStaticDtls_Reserved1` | TField |  |  |
| 13 | `SC.SRBD.RESERVED2` | `ScSrdBnkStaticDtls_Reserved2` | TField |  |  |
| 14 | `SC.SRBD.RESERVED3` | `ScSrdBnkStaticDtls_Reserved3` | TField |  |  |
| 15 | `SC.SRBD.RESERVED4` | `ScSrdBnkStaticDtls_Reserved4` | TField |  |  |
| 16 | `SC.SRBD.RESERVED5` | `ScSrdBnkStaticDtls_Reserved5` | TField |  |  |
| 17 | `SC.SRBD.RESERVED6` | `ScSrdBnkStaticDtls_Reserved6` | TField |  |  |
| 18 | `SC.SRBD.RESERVED7` | `ScSrdBnkStaticDtls_Reserved7` | TField |  |  |
| 19 | `SC.SRBD.RESERVED8` | `ScSrdBnkStaticDtls_Reserved8` | TField |  |  |
| 20 | `SC.SRBD.RESERVED9` | `ScSrdBnkStaticDtls_Reserved9` | TField |  |  |
| 21 | `SC.SRBD.RESERVED10` | `ScSrdBnkStaticDtls_Reserved10` | TField |  |  |
| 22 | `SC.SRBD.RESERVED11` | `ScSrdBnkStaticDtls_Reserved11` | TField |  |  |
| 23 | `SC.SRBD.RESERVED12` | `ScSrdBnkStaticDtls_Reserved12` | TField |  |  |
| 24 | `SC.SRBD.RESERVED13` | `ScSrdBnkStaticDtls_Reserved13` | TField |  |  |
| 25 | `SC.SRBD.RESERVED14` | `ScSrdBnkStaticDtls_Reserved14` | TField |  |  |
| 26 | `SC.SRBD.RESERVED15` | `ScSrdBnkStaticDtls_Reserved15` | TField |  |  |
| 27 | `SC.SRBD.RESERVED16` | `ScSrdBnkStaticDtls_Reserved16` | TField |  |  |
| 28 | `SC.SRBD.RESERVED17` | `ScSrdBnkStaticDtls_Reserved17` | TField |  |  |
| 29 | `SC.SRBD.RESERVED18` | `ScSrdBnkStaticDtls_Reserved18` | TField |  |  |
| 30 | `SC.SRBD.RESERVED19` | `ScSrdBnkStaticDtls_Reserved19` | TField |  |  |
| 31 | `SC.SRBD.RESERVED20` | `ScSrdBnkStaticDtls_Reserved20` | TField |  |  |
| 32 | `SC.SRBD.RESERVED21` | `ScSrdBnkStaticDtls_Reserved21` | TField |  |  |
| 33 | `SC.SRBD.RESERVED22` | `ScSrdBnkStaticDtls_Reserved22` | TField |  |  |
| 34 | `SC.SRBD.RESERVED23` | `ScSrdBnkStaticDtls_Reserved23` | TField |  |  |
| 35 | `SC.SRBD.RESERVED24` | `ScSrdBnkStaticDtls_Reserved24` | TField |  |  |
| 36 | `SC.SRBD.RESERVED25` | `ScSrdBnkStaticDtls_Reserved25` | TField |  |  |
| 37 | `SC.SRBD.LOCAL.REF` | `ScSrdBnkStaticDtls_LocalRef` |  |  |  |
| 38 | `SC.SRBD.OVERRIDE` | `ScSrdBnkStaticDtls_Override` |  |  |  |
| 39 | `SC.SRBD.RECORD.STATUS` | `ScSrdBnkStaticDtls_RecordStatus` | String |  |  |
| 40 | `SC.SRBD.CURR.NO` | `ScSrdBnkStaticDtls_CurrNo` | String |  |  |
| 41 | `SC.SRBD.INPUTTER` | `ScSrdBnkStaticDtls_Inputter` |  |  |  |
| 42 | `SC.SRBD.DATE.TIME` | `ScSrdBnkStaticDtls_DateTime` |  |  |  |
| 43 | `SC.SRBD.AUTHORISER` | `ScSrdBnkStaticDtls_Authoriser` | String |  |  |
| 44 | `SC.SRBD.CO.CODE` | `ScSrdBnkStaticDtls_CoCode` | String |  |  |
| 45 | `SC.SRBD.DEPT.CODE` | `ScSrdBnkStaticDtls_DeptCode` | String |  |  |
| 46 | `SC.SRBD.AUDITOR.CODE` | `ScSrdBnkStaticDtls_AuditorCode` | String |  |  |
| 47 | `SC.SRBD.AUDIT.DATE.TIME` | `ScSrdBnkStaticDtls_AuditDateTime` | String |  |  |
