# CAPL.H.AKCL.EXEMPT.CATEG.LIST — Table Schema

> Source: `INSERTS/I_F.CAPL.H.AKCL.EXEMPT.CATEG.LIST` in `CAAKCL_AkcelerantInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.AKCL.EXEMPT.CATEG` | `CaplHAkclExemptCategList_ExemptCateg` |  |  |  |
| 2 | `CAPL.AKCL.POST.DELIN` | `CaplHAkclExemptCategList_PostDelin` | TField |  | Field to define the No of days, post the delinquency is cleared account has to be reported.Eg. 180 days |
| 3 | `CAPL.AKCL.TRAN.FROM` | `CaplHAkclExemptCategList_TranFrom` | TField |  | Field to define the No of days, for the purpose of retrieving transactions for payments file.Eg. 180 days, Financial transaction from past 180 Days will be reported, in case LAST.EXT.DT is available, then financial transaction from LAST.EXT.DT will be reported |
| 4 | `CAPL.AKCL.AKCL.ACCT.PATH` | `CaplHAkclExemptCategList_AkclAcctPath` | TField |  | Field to define the Path for Account extract.Eg. ACCOUNT.OUTAccount extract will be placed in the directory AKC&lt;DATE&gt;&lt;TIME&gt;.TXT |
| 5 | `CAPL.AKCL.ACCT.FILE.NAME` | `CaplHAkclExemptCategList_AcctFileName` | TField |  | Field to define the File name for account extractsEg. AKC&lt;DATE&gt;&lt;TIME&gt; This field also allow to key in the basic T24 common variables as listed below,example:- if the field configured as,AKC&lt;DDMMYYYY&gt;&lt;HHMMSS &gt; DFE will REPLACE as AKC31122015210912 Conversion Action &lt;YYYYMMDD&gt; Replaces system date in YYYYMMDD format &lt;MMDDYYYY&gt; Replaces system date in MMDDYYYY format &lt;DDMMYYYY&gt; Replaces system date in DDMMYYYY format &lt;DDMMMYYYY/DDMONYYY&gt; Replaces system date in DDMMMYYYY format !MNEMONIC Replaces Company Mnemonic !TODAY Replaces Today's date in Dates record !JULIAN Replaces Today's date in JULIAN format. !LCCY Replaces by local currency from Company record. !USER Replaces by Operator. !COMPANY Replaces by company id. |
| 6 | `CAPL.AKCL.AKCL.ACCT.DELIM` | `CaplHAkclExemptCategList_AkclAcctDelim` | TField |  | Field to indicate the Delimiter/Separator for Account extract.Delimiter defined in this field will be used for as separator for each field value in account extract |
| 7 | `CAPL.AKCL.AKCL.PYMT.PATH` | `CaplHAkclExemptCategList_AkclPymtPath` | TField |  | Field to define the Path for Payment extract.Eg. PAYMENT.OUTPayment extract will be placed in the directory PAYMENT.OUT |
| 8 | `CAPL.AKCL.PYMT.FILE.NAME` | `CaplHAkclExemptCategList_PymtFileName` | TField |  | Field to define the File name for payment extractsEg. AKCHIS&lt;DATE&gt;&lt;TIME&gt; This field also allow to key in the basic T24 common variables as listed below,example:- if the field configured as,AKCHIS&lt;DDMMYYYY&gt;&lt;HHMMSS&gt; DFE will REPLACE as AKCHIS31122015210912 Conversion Action &lt;YYYYMMDD&gt; Replaces system date in YYYYMMDD format &lt;MMDDYYYY&gt; Replaces system date in MMDDYYYY format &lt;DDMMYYYY&gt; Replaces system date in DDMMYYYY format &lt;DDMMMYYYY/DDMONYYY&gt; Replaces system date in DDMMMYYYY format !TODAY Replaces Today's date in Dates record !MNEMONIC Replaces Company Mnemonic !JULIAN Replaces Today's date in JULIAN format. !LCCY Replaces by local currency from Company record. !USER Replaces by Operator User. !COMPANY Replaces by company id. |
| 9 | `CAPL.AKCL.AKCL.PYMT.DELIM` | `CaplHAkclExemptCategList_AkclPymtDelim` | TField |  | Field to indicate the Delimiter/Separator for Payment extract.Delimiter defined in this field will be used for as separator for each field value in payment extract |
| 10 | `CAPL.AKCL.AKCL.PRIORITY` | `CaplHAkclExemptCategList_AkclPriority` | TField |  |  |
| 11 | `CAPL.AKCL.PAY.ACCT.LENG` | `CaplHAkclExemptCategList_PayAcctLeng` | TField |  | This field is used to configure the length for the account number to be reported in the akcelerant payment extract.If the field is defined as 8, the length of the account number will be reported in the extract is from last 8-digit.Allowed length is 3-digit numeric value.Ex. 8, 6 |
| 12 | `CAPL.AKCL.EXC.COLL.STATUS` | `CaplHAkclExemptCategList_ExcCollStatus` |  |  |  |
| 13 | `CAPL.AKCL.ACCOUNT.INT.PROPERTY` | `CaplHAkclExemptCategList_AccountIntProperty` | TField |  | The purpose of this field is used to configure the interest property for account product line that needs to reported in the akcelerant extract.Valid record from AA.PROPERTYEx.DRINTEREST |
| 14 | `CAPL.AKCL.DEPOSIT.INT.PROPERTY` | `CaplHAkclExemptCategList_DepositIntProperty` | TField |  | The purpose of this field is used to configure the interest property for deposit products that needs to reported in the akcelerant extract.Valid record from AA.PROPERTYEx.DEPOSITINT |
| 15 | `CAPL.AKCL.RESERVED.2` | `CaplHAkclExemptCategList_Reserved2` | TField |  |  |
| 16 | `CAPL.AKCL.RESERVED.1` | `CaplHAkclExemptCategList_Reserved1` | TField |  |  |
| 17 | `CAPL.AKCL.LOCAL.REF` | `CaplHAkclExemptCategList_LocalRef` |  |  |  |
| 18 | `CAPL.AKCL.OVERRIDES` | `CaplHAkclExemptCategList_Overrides` |  |  |  |
| 19 | `CAPL.AKCL.RECORD.STATUS` | `CaplHAkclExemptCategList_RecordStatus` | String |  |  |
| 20 | `CAPL.AKCL.CURR.NO` | `CaplHAkclExemptCategList_CurrNo` | String |  |  |
| 21 | `CAPL.AKCL.INPUTTER` | `CaplHAkclExemptCategList_Inputter` |  |  |  |
| 22 | `CAPL.AKCL.DATE.TIME` | `CaplHAkclExemptCategList_DateTime` |  |  |  |
| 23 | `CAPL.AKCL.AUTHORISER` | `CaplHAkclExemptCategList_Authoriser` | String |  |  |
| 24 | `CAPL.AKCL.CO.CODE` | `CaplHAkclExemptCategList_CoCode` | String |  |  |
| 25 | `CAPL.AKCL.DEPT.CODE` | `CaplHAkclExemptCategList_DeptCode` | String |  |  |
| 26 | `CAPL.AKCL.AUDITOR.CODE` | `CaplHAkclExemptCategList_AuditorCode` | String |  |  |
| 27 | `CAPL.AKCL.AUDIT.DATE.TIME` | `CaplHAkclExemptCategList_AuditDateTime` | String |  |  |
