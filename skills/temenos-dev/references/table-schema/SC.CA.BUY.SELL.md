# SC.CA.BUY.SELL — Table Schema

> Source: `INSERTS/I_F.SC.CA.BUY.SELL` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SB.DIARY.ID` | `ScCaBuySell_DiaryId` | TField |  | Diary Id to which the ENTITLEMENT record is for. Validation Rules: This is a NOINPUT, system generated field. |
| 2 | `SC.SB.PORTFOLIO.NO` | `ScCaBuySell_PortfolioNo` | TField |  | Portfolio Number to which the ENTITLEMENT record is for. Enriched by the Account Name field from the SEC.ACC.MASTER file. Validation Rules: This is a NOINPUT, system generated field. |
| 3 | `SC.SB.DEPOSITORY` | `ScCaBuySell_Depository` | TField |  | The Depository number the ENTITLEMENT record related to. Enriched by short description from CUSTOMER.SECURITY file. Validation Rules: Updated by the system and is a NOINPUT field. |
| 4 | `SC.SB.NOMINEE` | `ScCaBuySell_Nominee` | TField |  | Unique reference which identifies the Nominee Company record. Validation Rules: This is a NOINPUT field updated by the system. |
| 5 | `SC.SB.SUB.ACCOUNT` | `ScCaBuySell_SubAccount` | TField |  | Specifies the sub account of the depository. It is defaulted from the Entitlement record. No input field |
| 6 | `SC.SB.SECURITY.NO` | `ScCaBuySell_SecurityNo` | TField |  | SEDOL number of the original security. Updated from the originating Entitlement record. Enriched by the Short description of the Security from Security Master file. Validation Rules: This is a NOINPUT field. |
| 7 | `SC.SB.EVENT.TYPE` | `ScCaBuySell_EventType` | TField |  | Specifies the Event type to which the record is associated. It is automatically defaulted from the Entitlement record. No input field |
| 8 | `SC.SB.CURRENCY` | `ScCaBuySell_Currency` | TField |  | Currency in which ENTITLEMENT.AMT is calculated.If CURRENCY in Diary is a non-restricted Currency, then Defaultedfrom the CURRENCY field on the original DIARY record.Else, from SETT.CURRENCY field in the original DIARY record. Enriched by the short description from the CURRENCY file. Validation Rules: This is a NOINPUT field, updated by the system. |
| 9 | `SC.SB.QUALIFY.HOLDING` | `ScCaBuySell_QualifyHolding` | TField |  | Portfolio's holding in the original security as at EX.DATE. Validation Rules: Field updated by the System from Entitlement |
| 10 | `SC.SB.RIGHTS.POSITION` | `ScCaBuySell_RightsPosition` | TField |  | Field automatically updated by the System from the field Event Nominal in the Entitlement Validation Rules Noinput field - Standard nominal field |
| 11 | `SC.SB.SELL.BUY.OPT.DESC` | `ScCaBuySell_SellBuyOptDesc` |  |  |  |
| 12 | `SC.SB.SELL.BUY.OPT.NO` | `ScCaBuySell_SellBuyOptNo` |  |  |  |
| 13 | `SC.SB.SELL.BUY.SEC` | `ScCaBuySell_SellBuySec` |  |  |  |
| 14 | `SC.SB.SELL.BUY.REPLY.DATE` | `ScCaBuySell_SellBuyReplyDate` |  |  |  |
| 15 | `SC.SB.TRAD.FROM.DATE` | `ScCaBuySell_TradFromDate` |  |  |  |
| 16 | `SC.SB.TRAD.TO.DATE` | `ScCaBuySell_TradToDate` |  |  |  |
| 17 | `SC.SB.QUANTITY` | `ScCaBuySell_Quantity` |  |  |  |
| 18 | `SC.SB.PRICE` | `ScCaBuySell_Price` |  |  |  |
| 19 | `SC.SB.TRADE.DATE` | `ScCaBuySell_TradeDate` |  |  |  |
| 20 | `SC.SB.VALUE.DATE` | `ScCaBuySell_ValueDate` |  |  |  |
| 21 | `SC.SB.CONSID.AMOUNT` | `ScCaBuySell_ConsidAmount` |  |  |  |
| 22 | `SC.SB.REFERENCE` | `ScCaBuySell_Reference` |  |  |  |
| 23 | `SC.SB.SB.RESERVED.05` | `ScCaBuySell_SbReserved05` |  |  |  |
| 24 | `SC.SB.SB.RESERVED.04` | `ScCaBuySell_SbReserved04` |  |  |  |
| 25 | `SC.SB.SB.RESERVED.03` | `ScCaBuySell_SbReserved03` |  |  |  |
| 26 | `SC.SB.SB.RESERVED.02` | `ScCaBuySell_SbReserved02` |  |  |  |
| 27 | `SC.SB.SB.RESERVED.01` | `ScCaBuySell_SbReserved01` |  |  |  |
| 28 | `SC.SB.NET.NOMINAL` | `ScCaBuySell_NetNominal` | TField |  | This field will the sum of QUANTITY fields. Sign of QUANITY is identified through SELL.BUY.OPTION.DESC Validation Rules Updated by the system. Noinput Field |
| 29 | `SC.SB.GENERATE.INSTRUCTION` | `ScCaBuySell_GenerateInstruction` | TField |  | YES/NO field to specify whether MT 565 has to be generated. If the field is set as YES, MT565 will be generated. If blank or NO, No MT565 will be generated Validation Rules NOINPUT for the CHILD omnibus Record type records. As MT565 instructions will be generated through parent omnibusfor all the linked Child Omnibus record Raise an error if SC-0102.EventType is not available in EB.ADVICES |
| 30 | `SC.SB.MT566.CONFIRMATION` | `ScCaBuySell_Mt566Confirmation` | TField |  | YES/NO field to specify whether the transaction status will be updated based on incoming MT 566 confirmation. If the field is set as NO, it is assumed that the processing will be manual. If YES or blank, then the processingwill be based on incoming MT 566. Validation Rules NOINPUT for the CHILD omnibus Record type records |
| 31 | `SC.SB.MT565.REF` | `ScCaBuySell_Mt565Ref` | TField |  | MT 565 delivery reference. For segregated accounts, the instruction will be generated as soon as the option iselected and record authorized. For omnibus accounts, consolidated instructions will be generated. Validation Rules Noinput field.Updated by the system |
| 32 | `SC.SB.MT566.REF` | `ScCaBuySell_Mt566Ref` | TField |  | The field has to be set to processed and record authorized for the system to automatically generate the SECTRADE. The trade will be generated in authorized status and the trade reference will be maintained for cross reference. The status will be updated automatically once confirmation (MT 566) is received and reconciled or manually (fornon-STP scenarios). In the case of omnibus accounts, the system will reconcile the aggregated quantity and update the status of allunderlying transactions. |
| 33 | `SC.SB.STATUS` | `ScCaBuySell_Status` | TField |  | The field is used to identify the Status of Election. Validation Rules Will hold either of these values: PROCESS/PROCESS.AUTO for consolidated SC.CA.BUY.SELL record. i.e for RecordType equals PARENT.OMNIBUS. Will hold PROCESSED alone for individual SC.CA.BUY.SELL record. i.e for RecordType equals OMNIBUS. If set as PROCESSED in consolidated SC.CA.BUY.SELL record, then the individual records has to be set as PROCESSED manually. If set as PROCESS.AUTO in consolidated SC.CA.BUY.SELL record, individual records will be automatically processed by the system via service. |
| 34 | `SC.SB.RECORD.TYPE` | `ScCaBuySell_RecordType` | TField |  | The field will used to identify the sub account type Validation Rules Noinput field.Updated by the system Will hold either of these values: OMNIBUS/SEGREGATED/PARENT.OMNIBUS |
| 35 | `SC.SB.TAP.REF.ID` | `ScCaBuySell_TapRefId` | TField |  |  |
| 36 | `SC.SB.TRADE.CHANNEL` | `ScCaBuySell_TradeChannel` | TField |  |  |
| 37 | `SC.SB.TGT.NEW.SHARE.QTY` | `ScCaBuySell_TgtNewShareQty` | TField |  |  |
| 38 | `SC.SB.STAND.INST.KEY` | `ScCaBuySell_StandInstKey` | TField |  |  |
| 39 | `SC.SB.OPTION.INSTR` | `ScCaBuySell_OptionInstr` | TField |  |  |
| 40 | `SC.SB.BLOCKED.NOMINAL` | `ScCaBuySell_BlockedNominal` | TField |  |  |
| 41 | `SC.SB.MULT.BUY.SELL` | `ScCaBuySell_MultBuySell` |  |  |  |
| 42 | `SC.SB.MULT.QUANTITY` | `ScCaBuySell_MultQuantity` |  |  |  |
| 43 | `SC.SB.MULT.MT565.REF` | `ScCaBuySell_MultMt565Ref` |  |  |  |
| 44 | `SC.SB.MULT.MT566.REF` | `ScCaBuySell_MultMt566Ref` |  |  |  |
| 45 | `SC.SB.MULT.PRICE` | `ScCaBuySell_MultPrice` |  |  |  |
| 46 | `SC.SB.MULT.CONSIDERATION` | `ScCaBuySell_MultConsideration` |  |  |  |
| 47 | `SC.SB.MULT.TRADE.DATE` | `ScCaBuySell_MultTradeDate` |  |  |  |
| 48 | `SC.SB.MULT.VALUE.DATE` | `ScCaBuySell_MultValueDate` |  |  |  |
| 49 | `SC.SB.MULT.STATUS` | `ScCaBuySell_MultStatus` |  |  |  |
| 50 | `SC.SB.MULT.TRADE.CHANNEL` | `ScCaBuySell_MultTradeChannel` |  |  |  |
| 51 | `SC.SB.MULT.TXN.REFERENCE` | `ScCaBuySell_MultTxnReference` |  |  |  |
| 52 | `SC.SB.MULT.SEQUENCE` | `ScCaBuySell_MultSequence` |  |  |  |
| 53 | `SC.SB.RESERVED.7` | `ScCaBuySell_Reserved7` |  |  |  |
| 54 | `SC.SB.RESERVED.6` | `ScCaBuySell_Reserved6` | TField |  |  |
| 55 | `SC.SB.RESERVED.5` | `ScCaBuySell_Reserved5` | TField |  |  |
| 56 | `SC.SB.RESERVED.4` | `ScCaBuySell_Reserved4` | TField |  |  |
| 57 | `SC.SB.RESERVED.3` | `ScCaBuySell_Reserved3` | TField |  |  |
| 58 | `SC.SB.RESERVED.2` | `ScCaBuySell_Reserved2` | TField |  |  |
| 59 | `SC.SB.RESERVED.1` | `ScCaBuySell_Reserved1` | TField |  |  |
| 60 | `SC.SB.LOCAL.REF` | `ScCaBuySell_LocalRef` |  |  |  |
| 61 | `SC.SB.OVERRIDE` | `ScCaBuySell_Override` |  |  |  |
| 62 | `SC.SB.RECORD.STATUS` | `ScCaBuySell_RecordStatus` | String |  |  |
| 63 | `SC.SB.CURR.NO` | `ScCaBuySell_CurrNo` | String |  |  |
| 64 | `SC.SB.INPUTTER` | `ScCaBuySell_Inputter` |  |  |  |
| 65 | `SC.SB.DATE.TIME` | `ScCaBuySell_DateTime` |  |  |  |
| 66 | `SC.SB.AUTHORISER` | `ScCaBuySell_Authoriser` | String |  |  |
| 67 | `SC.SB.CO.CODE` | `ScCaBuySell_CoCode` | String |  |  |
| 68 | `SC.SB.DEPT.CODE` | `ScCaBuySell_DeptCode` | String |  |  |
| 69 | `SC.SB.AUDITOR.CODE` | `ScCaBuySell_AuditorCode` | String |  |  |
| 70 | `SC.SB.AUDIT.DATE.TIME` | `ScCaBuySell_AuditDateTime` | String |  |  |
