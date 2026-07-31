# SC.CUST.EVENT.CREATE — Table Schema

> Source: `INSERTS/I_F.SC.CUST.EVENT.CREATE` in `SC_SccEventCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CEC.CUSTOMER.NO` | `ScCustEventCreate_CustomerNo` | TField |  | This field will hold the CUSTOMER ID of the initiating Client Validation Rules: Valid CUSTOMER record |
| 2 | `SC.CEC.PORTFOLIO` | `ScCustEventCreate_Portfolio` | TField |  | This field denotes the SEC.ACC.MASTER id of the customer Validation Rules: Valid SEC.ACC.MASTER record |
| 3 | `SC.CEC.ACCOUNT` | `ScCustEventCreate_Account` | TField |  | This field denotes the account in Security Currency Validation Rules: Valid ACCOUNT record |
| 4 | `SC.CEC.EVENT.SECURITY` | `ScCustEventCreate_EventSecurity` | TField |  | This field denotes the event security Validation Rules: Valid SECURITY.MASTER record |
| 5 | `SC.CEC.EVENT.TYPE` | `ScCustEventCreate_EventType` | TField |  | This field denotes the event type to be used in Diary. Defaulted from SC.CA.PARAMETER |
| 6 | `SC.CEC.DEPOSITORY` | `ScCustEventCreate_Depository` | TField |  | The field denotes the depository number to which the Diary event is related to Validation Rules: Valid CUSTOMER.SECURITY record |
| 7 | `SC.CEC.INITIATION.DATE` | `ScCustEventCreate_InitiationDate` | TField |  | This field denotes the ex date in diary record Validation Rules: Must be between CA.START.DATE and CA.END.DATE of event security record |
| 8 | `SC.CEC.EVENT.NOM` | `ScCustEventCreate_EventNom` | TField |  | This field denotes Quantity of the original security to be converted to shares |
| 9 | `SC.CEC.NEW.SEC.NO` | `ScCustEventCreate_NewSecNo` |  |  |  |
| 10 | `SC.CEC.NEW.SEC.NOM` | `ScCustEventCreate_NewSecNom` |  |  |  |
| 11 | `SC.CEC.EXERCISE.AMT` | `ScCustEventCreate_ExerciseAmt` |  |  |  |
| 12 | `SC.CEC.DIARY.ID` | `ScCustEventCreate_DiaryId` | TField |  | Holds the id of the diary record created from this application |
| 13 | `SC.CEC.TAP.REF.ID` | `ScCustEventCreate_TapRefId` | TField |  | This field is used to capture the TAP order reference in T24 This field denotes Common order reference which is maintained across Wealth Suite (T24 / TAP) |
| 14 | `SC.CEC.RESERVED.3` | `ScCustEventCreate_Reserved3` | TField |  |  |
| 15 | `SC.CEC.RESERVED.2` | `ScCustEventCreate_Reserved2` | TField |  |  |
| 16 | `SC.CEC.RESERVED.1` | `ScCustEventCreate_Reserved1` | TField |  |  |
| 17 | `SC.CEC.LOCAL.REF` | `ScCustEventCreate_LocalRef` |  |  |  |
| 18 | `SC.CEC.STMT.NOS` | `ScCustEventCreate_StmtNos` |  |  |  |
| 19 | `SC.CEC.OVERRIDE` | `ScCustEventCreate_Override` |  |  |  |
| 20 | `SC.CEC.RECORD.STATUS` | `ScCustEventCreate_RecordStatus` | String |  |  |
| 21 | `SC.CEC.CURR.NO` | `ScCustEventCreate_CurrNo` | String |  |  |
| 22 | `SC.CEC.INPUTTER` | `ScCustEventCreate_Inputter` |  |  |  |
| 23 | `SC.CEC.DATE.TIME` | `ScCustEventCreate_DateTime` |  |  |  |
| 24 | `SC.CEC.AUTHORISER` | `ScCustEventCreate_Authoriser` | String |  |  |
| 25 | `SC.CEC.CO.CODE` | `ScCustEventCreate_CoCode` | String |  |  |
| 26 | `SC.CEC.DEPT.CODE` | `ScCustEventCreate_DeptCode` | String |  |  |
| 27 | `SC.CEC.AUDITOR.CODE` | `ScCustEventCreate_AuditorCode` | String |  |  |
| 28 | `SC.CEC.AUDIT.DATE.TIME` | `ScCustEventCreate_AuditDateTime` | String |  |  |
| 29 | `SC.CEC.NEW.SEC.CCY` | `ScCustEventCreate_NewSecCcy` |  |  |  |
| 30 | `SC.CEC.SEC.CCY.EXCH.RATE` | `ScCustEventCreate_SecCcyExchRate` |  |  |  |
| 31 | `SC.CEC.TOT.EXERCISE.AMT` | `ScCustEventCreate_TotExerciseAmt` | TField |  |  |
| 32 | `SC.CEC.EVENT.CCY` | `ScCustEventCreate_EventCcy` | TField |  |  |
