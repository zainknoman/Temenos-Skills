# SC.AUTO.GROUP.ORDERS — Table Schema

> Source: `INSERTS/I_F.SC.AUTO.GROUP.ORDERS` in `SC_SctOrderGrouping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.AUTO.GRP.CUT.OFF.DATE` | `ScAutoGroupOrders_CutOffDate` | TField | Conditional | If &amp;#8216;Automatic&amp;#8217; grouping is adopted, this field will carry the date when the Sec.Open.orderswould get grouped. On the specified date, at the specified time in CUT.OFF.TIME field, a phantom job will generateOFS messages to authorize the SC.GROUP.ORDERS whose Ids are available in field GROUP.ORDER.NO. On authorization ofSC.GROUP.ORDERS, the following additional OFS messages are generated. a) OFS messages for reversal of the basic ordersb) OFS message for input of a grouped SEC.OPEN.ORDER.All the above messages are placed in the in-directory defined in the related OFS.SOURCE records linked inSC.STD.SEC.TRADE. If a cut off frequency is defined then based on the frequency, the date will get automatically reset at the timeof grouping. However, the primary check would be on CUT.OFF.EXPIRY.DATE and that date should be greater than thecurrent date. Otherwise the whole record becomes irrelevant for auto-grouping. Validation Rules: 1-11 date field(optional) Mandatory field A valid date is allowed. Cut off Date can be today or in future, but cannot be less than today. Cut off Date cannot be set for a holiday(for the local country). Cut off Date cannot be greater than Cut off Expiry Date |
| 2 | `SC.AUTO.GRP.CUT.OFF.TIME` | `ScAutoGroupOrders_CutOffTime` | TField | Yes | Field carrying valid time. Automatic groping of Sec.open.orders will be done based on the time set in this field.Relevant only for the CUTOFF.DATE specified in the record. If the CUT.OFF.TIME is reached then OFS message would begenerated and placed in a specific in-directory(OFS.SOURCE record linked in SC.STD.SEC.TRADE) for authorizing thoseSC.GROUP.ORDERS which appear in GROUP.ORDER.NO field. Validation Rules: 1-11 mandatory field Mandatory field. A valid time is allowed as input. |
| 3 | `SC.AUTO.GRP.ORDER.NUMBER` | `ScAutoGroupOrders_OrderNumber` |  |  |  |
| 4 | `SC.AUTO.GRP.GROUP.ORDER.NO` | `ScAutoGroupOrders_GroupOrderNo` |  |  |  |
| 5 | `SC.AUTO.GRP.CUT.OFF.FREQ` | `ScAutoGroupOrders_CutOffFreq` | TField |  | A valid frequency is allowed to be entered. Frequency will be allowed to be input only if Cut off date isdefined. After grouping is complete and a grouped SEC.OPEN.ORDER is created, the cut off date will be reset basedon the cut off frequency. E.g. M0101 - Monthly Frequency DAILY - Daily Frequency BSNSS - BUSINESS DAY WEEK1 - Weekly Frequency (WEEK2) TWMTH - Twice a month on 15th and Last day of the Month Validation Rules: 1-19 alphanumeric field Standard T24 frequency field. |
| 6 | `SC.AUTO.GRP.CUT.OFF.EXPRY.DATE` | `ScAutoGroupOrders_CutOffExpryDate` | TField |  | This field will control the EXPIRY DATE of the record. When this date is reached then grouping will not beprocessed under this record. A date greater than or equal to the CUT.OFF.DATE can be input. If a date equal to CUT.OFF.DATE is input, then on that date no grouping will take place since the record becomesirrelevant for processing. This will facilitate stoppage of grouping through a particular SC.AUTO.GROUP.ORDER id,in case such stoppage is desired. Validation Rules: 1-11 date feild Valid date field Noinput allowed if order number &amp; group order number exists i.e if any SC.GROUP.ORDERS record exists in INAUstatus, waiting for grouping. Cannot be less than cut off date No-input field if the id of SC.AUTO.GROUP.ORDERS is 'ALL' |
| 7 | `SC.AUTO.GRP.DAY.CONVENTION` | `ScAutoGroupOrders_DayConvention` | TField |  | Allowed value is FOLLOWING_PRECEDING If the computed CUT.OFF.DATE is a holiday then if this field is set, the corresponding working day will becomputed based on PRECEDING or FOLLOWING as previous working day or next working day respectively |
| 8 | `SC.AUTO.GRP.ACT.CUT.OFF.DATE` | `ScAutoGroupOrders_ActCutOffDate` | TField |  | This will be a Noinput field The value will be populated with the actual cut-off date before applying the day convention and will be used indetermining of future cut off dates |
| 9 | `SC.AUTO.GRP.PREV.CUT.OFF.DATE` | `ScAutoGroupOrders_PrevCutOffDate` | TField |  | This will be a Noinput field The value will be populated with the previous actual cut-off date when the date is recycled |
| 10 | `SC.AUTO.GRP.PARENT.CHILD` | `ScAutoGroupOrders_ParentChild` | TField |  | Allowed value is YES This is the flag to indicate whether the group order be created as parent child order or single order |
| 11 | `SC.AUTO.GRP.EXTD.CUT.OFF.TIME` | `ScAutoGroupOrders_ExtdCutOffTime` | TField |  | When the order is placed between the cut off time and extended cut off time, then the order will be transmittedinstantly without waiting for grouping Validation Rules Valid time |
| 12 | `SC.AUTO.GRP.DAYS.OFFSET` | `ScAutoGroupOrders_DaysOffset` | TField |  |  |
| 13 | `SC.AUTO.GRP.RESERVED.18` | `ScAutoGroupOrders_Reserved18` | TField |  |  |
| 14 | `SC.AUTO.GRP.RESERVED.17` | `ScAutoGroupOrders_Reserved17` | TField |  |  |
| 15 | `SC.AUTO.GRP.RESERVED.16` | `ScAutoGroupOrders_Reserved16` | TField |  |  |
| 16 | `SC.AUTO.GRP.RESERVED.15` | `ScAutoGroupOrders_Reserved15` | TField |  |  |
| 17 | `SC.AUTO.GRP.RESERVED.14` | `ScAutoGroupOrders_Reserved14` | TField |  |  |
| 18 | `SC.AUTO.GRP.RESERVED.13` | `ScAutoGroupOrders_Reserved13` | TField |  |  |
| 19 | `SC.AUTO.GRP.RESERVED.12` | `ScAutoGroupOrders_Reserved12` | TField |  |  |
| 20 | `SC.AUTO.GRP.RESERVED.11` | `ScAutoGroupOrders_Reserved11` | TField |  |  |
| 21 | `SC.AUTO.GRP.RESERVED.10` | `ScAutoGroupOrders_Reserved10` | TField |  |  |
| 22 | `SC.AUTO.GRP.RESERVED.09` | `ScAutoGroupOrders_Reserved09` | TField |  |  |
| 23 | `SC.AUTO.GRP.RESERVED.08` | `ScAutoGroupOrders_Reserved08` | TField |  |  |
| 24 | `SC.AUTO.GRP.RESERVED.07` | `ScAutoGroupOrders_Reserved07` | TField |  |  |
| 25 | `SC.AUTO.GRP.RESERVED.06` | `ScAutoGroupOrders_Reserved06` | TField |  |  |
| 26 | `SC.AUTO.GRP.RESERVED.05` | `ScAutoGroupOrders_Reserved05` | TField |  |  |
| 27 | `SC.AUTO.GRP.RESERVED.04` | `ScAutoGroupOrders_Reserved04` | TField |  |  |
| 28 | `SC.AUTO.GRP.RESERVED.03` | `ScAutoGroupOrders_Reserved03` | TField |  |  |
| 29 | `SC.AUTO.GRP.RESERVED.02` | `ScAutoGroupOrders_Reserved02` | TField |  |  |
| 30 | `SC.AUTO.GRP.RESERVED.01` | `ScAutoGroupOrders_Reserved01` | TField |  |  |
| 31 | `SC.AUTO.GRP.LOCAL.REF` | `ScAutoGroupOrders_LocalRef` |  |  |  |
| 32 | `SC.AUTO.GRP.OVERRIDE` | `ScAutoGroupOrders_Override` |  |  |  |
| 33 | `SC.AUTO.GRP.RECORD.STATUS` | `ScAutoGroupOrders_RecordStatus` | String |  |  |
| 34 | `SC.AUTO.GRP.CURR.NO` | `ScAutoGroupOrders_CurrNo` | String |  |  |
| 35 | `SC.AUTO.GRP.INPUTTER` | `ScAutoGroupOrders_Inputter` |  |  |  |
| 36 | `SC.AUTO.GRP.DATE.TIME` | `ScAutoGroupOrders_DateTime` |  |  |  |
| 37 | `SC.AUTO.GRP.AUTHORISER` | `ScAutoGroupOrders_Authoriser` | String |  |  |
| 38 | `SC.AUTO.GRP.CO.CODE` | `ScAutoGroupOrders_CoCode` | String |  |  |
| 39 | `SC.AUTO.GRP.DEPT.CODE` | `ScAutoGroupOrders_DeptCode` | String |  |  |
| 40 | `SC.AUTO.GRP.AUDITOR.CODE` | `ScAutoGroupOrders_AuditorCode` | String |  |  |
| 41 | `SC.AUTO.GRP.AUDIT.DATE.TIME` | `ScAutoGroupOrders_AuditDateTime` | String |  |  |
