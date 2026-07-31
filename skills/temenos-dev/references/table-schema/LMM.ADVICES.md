# LMM.ADVICES — Table Schema

> Source: `INSERTS/I_F.LMM.ADVICES` in `LM_Delivery.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LD23.ALL.NONE.ADVICES` | `LmmAdvices_AllNoneAdvices` | TField | No | Specifies whether advices are required for all or none of the different activities available. If N(ONE) is entered at this field then no advice or confirmation will be produced, whatever the activity. No further input is allowed. If A(LL) is entered at this field then all possible advices/confirmations will be produced. No further input is allowed and all advices will be produced on event date. Validation Rules: 1-4 alpha characters of the form A(LL) N(ONE) "blank" (Optional input; default value is blank.) Input must be valid alphabetic characters. |
| 2 | `LD23.ACTIVITY` | `LmmAdvices_Activity` |  |  |  |
| 3 | `LD23.REQUIRED.Y.N` | `LmmAdvices_RequiredYN` |  |  |  |
| 4 | `LD23.DAYS.PRIOR.POST` | `LmmAdvices_DaysPriorPost` |  |  |  |
| 5 | `LD23.FORMAT.CATEGORY` | `LmmAdvices_FormatCategory` | TField | No | Defines the category code to be used in determining the DE.FORMAT.PRINT id which defines the layout of the confirmation / advice. To determine which DE.FORMAT.PRINT record is used when producing the advice the following formulae is used: MMM.LDNNNN.1.GB Where MMM = Message type (320, 324 etc) NNNN = Category + Increment Category is the last two characters of the derived category code, see below, and the increment is derived from the first three numbers of the activity code, see the following table. ACTIVITY INCREMENT 101 0 102 200 103 400 104 0 105 2600 106 1200 107 3000 108 1400 109 2800 201 600 202 0 203 LD99 204 LD99 205 1800 206 800 301 1600 302 0 303 1000 304 LD99 305 LD99 307 2200 The category code to be used will either be that defined in this field or if left blank will default as follows: Range Default 21001 - 21039 21001 21045 - 21049 21045 21050 - 21074 21050 21075 - 21089 21075 21090 - 21094 21090 21095 - 21099 21095 Otherwise 21001 Hence, an interest payment advice for a deposit, category 21035, will use the format record 320.LD2801.1.GB. If a special advice for a particular category is required then the FORMAT.CATEGORY field could be set to 21035 for example in which case the format record used would be 320.LD2835.1.GB. Validation Rules: 5 Numeric (Optional) |
| 6 | `LD23.MATURE.MM.AT.SOD` | `LmmAdvices_MatureMmAtSod` | TField | Yes | This field is the MATURE.MM.AT.SOD, which stands for mature Money Market deals at the Start of Day. Validation Rules: 3 alphanumeric characters YES or NO. Mandatory input. Must be YES or NO. If Null then default value will be NO. |
| 7 | `LD23.FV.RATE.KEY` | `LmmAdvices_FvRateKey` | TField |  | The field is the Fair Value rate key used to provide the fair user rate on LD and MM contracts. Entering a value here provides a default for the field of same name on the LD and MM applications. Where the CATEGORY used on the MM &amp; LD contract matches the id the value here will be defaulted. It can be overridden at the contract level. This field is a link to the PERIODIC.INTEREST table and the record to use depends on the currency of the contract so if a value of 01 is entered here then a USD contract will look for a record such as 01USD20010731. Validation Rules: 1-4 numeric ID code although at present use of 2 digits is required to utilise PERIODIC.INTEREST records. |
| 8 | `LD23.FV.MARGIN.KEY` | `LmmAdvices_FvMarginKey` | TField |  | The field is the Fair Value margin rate key used to provide the fair margin rate on LD and MM contracts. Entering a value here provides a default for the field of same name on the LD and MM applications. Where the CATEGORY used on the MM &amp; LD contract matches the id the value here will be defaulted. It can be overriden at the contract level. This field is a link to the PERIODIC.INTEREST table and the record to use depends on the currency of the contract so if a value of 01 is entered here then a USD contract will look for a record such as 01USD20010731. Validation Rules: 1-4 numeric ID code although at present use of 2 digits is required to utilise PERIODIC.INTEREST records. |
| 9 | `LD23.COMPOUND.TYPE` | `LmmAdvices_CompoundType` | A (alphanumeric) | No | Frequency field which is used to determine the number of compounding periods per year. The compounding periods can be expressed as daily, weeks or Months. Validation Rules: : ------------------------------------------------------------------------------ (1) 5 type A (alphanumeric) character. Valid input is DAILY, WEEKn, Mnn, Nnn, or blank. (2) Optional field. (3) Used for money market deals. |
| 10 | `LD23.COMPOUND.YLD.MTHD` | `LmmAdvices_CompoundYldMthd` | A (alphanumeric) | No | Field which is used to determine the method of compounding. Validation Rules: : ------------------------------------------------------------------------------ (1) 8 type A (alphanumeric) character. Valid input is YIELD, or blank. (2) Can be allowed to input, if there is a value in COMPOUND.TYPE field. (3) YIELD can be set, only when the field COMPOUND.TYPE set to DAILY. (4) Optional field. (5) Used for money market deals. |
| 11 | `LD23.ALLOW.MT202` | `LmmAdvices_AllowMt202` | TField |  |  |
| 12 | `LD23.RESERVED9` | `LmmAdvices_Reserved9` | TField |  |  |
| 13 | `LD23.RESERVED8` | `LmmAdvices_Reserved8` | TField |  |  |
| 14 | `LD23.RESERVED7` | `LmmAdvices_Reserved7` | TField |  |  |
| 15 | `LD23.RESERVED6` | `LmmAdvices_Reserved6` | TField |  |  |
| 16 | `LD23.RESERVED5` | `LmmAdvices_Reserved5` | TField |  |  |
| 17 | `LD23.RESERVED4` | `LmmAdvices_Reserved4` | TField |  | Insert text here Validation Rules: Rule 1 Rule 2 |
| 18 | `LD23.RESERVED3` | `LmmAdvices_Reserved3` | TField |  | Insert text here Validation Rules: Rule 1 Rule 2 |
| 19 | `LD23.RESERVED2` | `LmmAdvices_Reserved2` | TField |  |  |
| 20 | `LD23.RESERVED1` | `LmmAdvices_Reserved1` | TField |  |  |
| 21 | `LD23.LOCAL.REF` | `LmmAdvices_LocalRef` |  |  |  |
| 22 | `LD23.RECORD.STATUS` | `LmmAdvices_RecordStatus` | String |  |  |
| 23 | `LD23.CURR.NO` | `LmmAdvices_CurrNo` | String |  |  |
| 24 | `LD23.INPUTTER` | `LmmAdvices_Inputter` |  |  |  |
| 25 | `LD23.DATE.TIME` | `LmmAdvices_DateTime` |  |  |  |
| 26 | `LD23.AUTHORISER` | `LmmAdvices_Authoriser` | String |  |  |
| 27 | `LD23.CO.CODE` | `LmmAdvices_CoCode` | String |  |  |
| 28 | `LD23.DEPT.CODE` | `LmmAdvices_DeptCode` | String |  |  |
| 29 | `LD23.AUDITOR.CODE` | `LmmAdvices_AuditorCode` | String |  |  |
| 30 | `LD23.AUDIT.DATE.TIME` | `LmmAdvices_AuditDateTime` | String |  |  |
