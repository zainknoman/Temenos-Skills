# POSTING.RESTRICT — Table Schema

> Source: `INSERTS/I_F.POSTING.RESTRICT` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.POS.DESCRIPTION` | `PostingRestrict_Description` |  |  |  |
| 2 | `AC.POS.RESTRICTION.TYPE` | `PostingRestrict_RestrictionType` | TField | Yes | Identifies the type of entries that are to be restricted, either only debits, only credits or both. This field is used to identify whether only debit, only credit or all entries are to be restricted. Validation Rules: 1-6 type SSS (uppercase alpha) characters: D(ebit) or C(redit) or A(ll) (Mandatory input) Must be ALL if Id is in the range 80-99. |
| 3 | `AC.POS.DISPO.OFFICER` | `PostingRestrict_DispoOfficer` | TField | No | The ID of the DISPO.OFFICER to be assigned to this POSTING.RESTRICT ID if they are to have authorisation to approve dispo items. Validation Rules: Must be a valid dispo officer as defined in the DISPO.OFFICER file. Optional field |
| 4 | `AC.POS.ALLOW.TXN` | `PostingRestrict_AllowTxn` | TField |  | States whether the values in the field TXN.CODE are to be allowed (set to Yes) or dis-allowed (set to No). If left blank all transactions for the restriction type will be processed. |
| 5 | `AC.POS.TXN.CODE` | `PostingRestrict_TxnCode` |  |  |  |
| 6 | `AC.POS.LOCAL.REF` | `PostingRestrict_LocalRef` |  |  |  |
| 7 | `AC.POS.ALT.OVERRIDE` | `PostingRestrict_AltOverride` | A (alphanumeric) | No | Contains the ID of the user defined OVERRIDE, assigned to this POSTING.RESTRICT ID. If user defined Override is specified in this field then it is raised instead of the core override. Validation Rules: Up to 35 type A (alphanumeric) characters. Optional field |
| 8 | `AC.POS.BLOCK.REASON.CODES` | `PostingRestrict_BlockReasonCodes` |  |  |  |
| 9 | `AC.POS.UNBLOCK.REASON.CODES` | `PostingRestrict_UnblockReasonCodes` |  |  |  |
| 10 | `AC.POS.RESERVED6` | `PostingRestrict_Reserved6` | TField |  |  |
| 11 | `AC.POS.RESERVED5` | `PostingRestrict_Reserved5` | TField |  |  |
| 12 | `AC.POS.RESERVED4` | `PostingRestrict_Reserved4` | TField |  |  |
| 13 | `AC.POS.RESERVED3` | `PostingRestrict_Reserved3` | TField |  |  |
| 14 | `AC.POS.RESERVED2` | `PostingRestrict_Reserved2` | TField |  |  |
| 15 | `AC.POS.OVERRIDE` | `PostingRestrict_Override` |  |  |  |
| 16 | `AC.POS.RECORD.STATUS` | `PostingRestrict_RecordStatus` | String |  |  |
| 17 | `AC.POS.CURR.NO` | `PostingRestrict_CurrNo` | String |  |  |
| 18 | `AC.POS.INPUTTER` | `PostingRestrict_Inputter` |  |  |  |
| 19 | `AC.POS.DATE.TIME` | `PostingRestrict_DateTime` |  |  |  |
| 20 | `AC.POS.AUTHORISER` | `PostingRestrict_Authoriser` | String |  |  |
| 21 | `AC.POS.CO.CODE` | `PostingRestrict_CoCode` | String |  |  |
| 22 | `AC.POS.DEPT.CODE` | `PostingRestrict_DeptCode` | String |  |  |
| 23 | `AC.POS.AUDITOR.CODE` | `PostingRestrict_AuditorCode` | String |  |  |
| 24 | `AC.POS.AUDIT.DATE.TIME` | `PostingRestrict_AuditDateTime` | String |  |  |
