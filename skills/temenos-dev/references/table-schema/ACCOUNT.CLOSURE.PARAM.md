# ACCOUNT.CLOSURE.PARAM — Table Schema

> Source: `INSERTS/I_F.ACCOUNT.CLOSURE.PARAM` in `AC_AccountClosure.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.ACL.PR.DESCRIPTION` | `AccountClosureParam_Description` |  |  |  |
| 2 | `AC.ACL.PR.APPLICATION` | `AccountClosureParam_Application` |  |  |  |
| 3 | `AC.ACL.PR.LOCAL.APPLICATION` | `AccountClosureParam_LocalApplication` |  |  |  |
| 4 | `AC.ACL.PR.LOCAL.APPLICATION.API` | `AccountClosureParam_LocalApplicationApi` |  |  |  |
| 5 | `AC.ACL.PR.LOCAL.RESERVED.20` | `AccountClosureParam_LocalReserved20` |  |  |  |
| 6 | `AC.ACL.PR.LOCAL.RESERVED.19` | `AccountClosureParam_LocalReserved19` |  |  |  |
| 7 | `AC.ACL.PR.LOCAL.RESERVED.18` | `AccountClosureParam_LocalReserved18` |  |  |  |
| 8 | `AC.ACL.PR.LOCAL.RESERVED.17` | `AccountClosureParam_LocalReserved17` |  |  |  |
| 9 | `AC.ACL.PR.LOCAL.RESERVED.16` | `AccountClosureParam_LocalReserved16` |  |  |  |
| 10 | `AC.ACL.PR.LOCAL.RESERVED.15` | `AccountClosureParam_LocalReserved15` |  |  |  |
| 11 | `AC.ACL.PR.LOCAL.RESERVED.14` | `AccountClosureParam_LocalReserved14` |  |  |  |
| 12 | `AC.ACL.PR.LOCAL.RESERVED.13` | `AccountClosureParam_LocalReserved13` |  |  |  |
| 13 | `AC.ACL.PR.LOCAL.RESERVED.12` | `AccountClosureParam_LocalReserved12` |  |  |  |
| 14 | `AC.ACL.PR.LOCAL.RESERVED.11` | `AccountClosureParam_LocalReserved11` |  |  |  |
| 15 | `AC.ACL.PR.LOCAL.RESERVED.10` | `AccountClosureParam_LocalReserved10` |  |  |  |
| 16 | `AC.ACL.PR.LOCAL.RESERVED.9` | `AccountClosureParam_LocalReserved9` |  |  |  |
| 17 | `AC.ACL.PR.LOCAL.RESERVED.8` | `AccountClosureParam_LocalReserved8` |  |  |  |
| 18 | `AC.ACL.PR.LOCAL.RESERVED.7` | `AccountClosureParam_LocalReserved7` |  |  |  |
| 19 | `AC.ACL.PR.LOCAL.RESERVED.6` | `AccountClosureParam_LocalReserved6` |  |  |  |
| 20 | `AC.ACL.PR.LOCAL.RESERVED.5` | `AccountClosureParam_LocalReserved5` |  |  |  |
| 21 | `AC.ACL.PR.LOCAL.RESERVED.4` | `AccountClosureParam_LocalReserved4` |  |  |  |
| 22 | `AC.ACL.PR.LOCAL.RESERVED.3` | `AccountClosureParam_LocalReserved3` |  |  |  |
| 23 | `AC.ACL.PR.LOCAL.RESERVED.2` | `AccountClosureParam_LocalReserved2` |  |  |  |
| 24 | `AC.ACL.PR.LOCAL.RESERVED.1` | `AccountClosureParam_LocalReserved1` |  |  |  |
| 25 | `AC.ACL.PR.LOCAL.REF` | `AccountClosureParam_LocalRef` |  |  |  |
| 26 | `AC.ACL.PR.PO.PRODUCT.TYPE.AC` | `AccountClosureParam_PoProductTypeAc` | TField |  | Payment Order Product which needs to be specified for Account closures using PAYMENT as the close mode, for account transfers.Should be a valid record in payment order product System will pick the parameters maintained in this PO product while raising the PO transaction. Validation Rules: Should be allowed for input only if PI module is installed PO product specifed here needs to be Account Transfer type - The field "Pay through Beneficiary" in the Payment Order Product application should be set to NO |
| 27 | `AC.ACL.PR.PO.PRODUCT.TYPE.BC` | `AccountClosureParam_PoProductTypeBc` | TField |  | Payment Order Product which needs to be specified for Account closures using PAYMENT as the close mode, for beneficiary transfers.Should be a valid record in payment order product System will pick the paramters maintained in this PO product while raising the PO transaction. Validation Rules: Should be allowed for input only if PI module is installed PO product specifed here needs to be Account Transfer type - The field "Pay through Beneficiary" in the Payment Order Product application should be set to YES |
| 28 | `AC.ACL.PR.RESERVED.18` | `AccountClosureParam_Reserved18` | TField |  |  |
| 29 | `AC.ACL.PR.RESERVED.17` | `AccountClosureParam_Reserved17` | TField |  |  |
| 30 | `AC.ACL.PR.RESERVED.16` | `AccountClosureParam_Reserved16` | TField |  |  |
| 31 | `AC.ACL.PR.RESERVED.15` | `AccountClosureParam_Reserved15` | TField |  |  |
| 32 | `AC.ACL.PR.RESERVED.14` | `AccountClosureParam_Reserved14` | TField |  |  |
| 33 | `AC.ACL.PR.RESERVED.13` | `AccountClosureParam_Reserved13` | TField |  |  |
| 34 | `AC.ACL.PR.RESERVED.12` | `AccountClosureParam_Reserved12` | TField |  |  |
| 35 | `AC.ACL.PR.RESERVED.11` | `AccountClosureParam_Reserved11` | TField |  |  |
| 36 | `AC.ACL.PR.RESERVED.10` | `AccountClosureParam_Reserved10` | TField |  |  |
| 37 | `AC.ACL.PR.RESERVED.9` | `AccountClosureParam_Reserved9` | TField |  |  |
| 38 | `AC.ACL.PR.RESERVED.8` | `AccountClosureParam_Reserved8` | TField |  |  |
| 39 | `AC.ACL.PR.RESERVED.7` | `AccountClosureParam_Reserved7` | TField |  |  |
| 40 | `AC.ACL.PR.RESERVED.6` | `AccountClosureParam_Reserved6` | TField |  |  |
| 41 | `AC.ACL.PR.RESERVED.5` | `AccountClosureParam_Reserved5` | TField |  |  |
| 42 | `AC.ACL.PR.RESERVED.4` | `AccountClosureParam_Reserved4` | TField |  |  |
| 43 | `AC.ACL.PR.RESERVED.3` | `AccountClosureParam_Reserved3` | TField |  |  |
| 44 | `AC.ACL.PR.RESERVED.2` | `AccountClosureParam_Reserved2` | TField |  |  |
| 45 | `AC.ACL.PR.RESERVED.1` | `AccountClosureParam_Reserved1` | TField |  |  |
| 46 | `AC.ACL.PR.OVERRIDE` | `AccountClosureParam_Override` |  |  |  |
| 47 | `AC.ACL.PR.RECORD.STATUS` | `AccountClosureParam_RecordStatus` | String |  |  |
| 48 | `AC.ACL.PR.CURR.NO` | `AccountClosureParam_CurrNo` | String |  |  |
| 49 | `AC.ACL.PR.INPUTTER` | `AccountClosureParam_Inputter` |  |  |  |
| 50 | `AC.ACL.PR.DATE.TIME` | `AccountClosureParam_DateTime` |  |  |  |
| 51 | `AC.ACL.PR.AUTHORISER` | `AccountClosureParam_Authoriser` | String |  |  |
| 52 | `AC.ACL.PR.CO.CODE` | `AccountClosureParam_CoCode` | String |  |  |
| 53 | `AC.ACL.PR.DEPT.CODE` | `AccountClosureParam_DeptCode` | String |  |  |
| 54 | `AC.ACL.PR.AUDITOR.CODE` | `AccountClosureParam_AuditorCode` | String |  |  |
| 55 | `AC.ACL.PR.AUDIT.DATE.TIME` | `AccountClosureParam_AuditDateTime` | String |  |  |
