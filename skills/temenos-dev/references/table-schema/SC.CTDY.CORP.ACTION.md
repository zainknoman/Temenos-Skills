# SC.CTDY.CORP.ACTION — Table Schema

> Source: `INSERTS/I_F.SC.CTDY.CORP.ACTION` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CTDY.COA.PORTFOLIO` | `ScCtdyCorpAction_Portfolio` | TField |  | This field holds the portfolio number associated with the position for which the record is built |
| 2 | `SC.CTDY.COA.SECURITY.NO` | `ScCtdyCorpAction_SecurityNo` | TField |  | This field holds the Security Master ID of the event/original security Updated from the originating SC.PRE.DIARY record |
| 3 | `SC.CTDY.COA.DEPOSITORY` | `ScCtdyCorpAction_Depository` | TField |  | This field holds the depository number associated with the position |
| 4 | `SC.CTDY.COA.CUSTODY.PORT.NO` | `ScCtdyCorpAction_CustodyPortNo` | TField |  | This field holds the segregated account id of the portfolio |
| 5 | `SC.CTDY.COA.SC.PRE.DIARY.ID` | `ScCtdyCorpAction_ScPreDiaryId` | TField |  | This field holds the pre diary id |
| 6 | `SC.CTDY.COA.DIARY.ID` | `ScCtdyCorpAction_DiaryId` | TField |  | This field holds the diary id |
| 7 | `SC.CTDY.COA.ENTITLEMENT.ID` | `ScCtdyCorpAction_EntitlementId` | TField |  | This field holds the entitlement id when diary is authorised |
| 8 | `SC.CTDY.COA.CORP.REF` | `ScCtdyCorpAction_CorpRef` | TField |  | This field holds the corp reference of the incoming message |
| 9 | `SC.CTDY.COA.CAMV` | `ScCtdyCorpAction_Camv` | TField | Yes | This field is updated based on mandatory / voluntary flag in diary type |
| 10 | `SC.CTDY.COA.EX.DATE` | `ScCtdyCorpAction_ExDate` | TField |  | This field is updated with the ex-date from pre diary / diary record |
| 11 | `SC.CTDY.COA.PAY.DATE` | `ScCtdyCorpAction_PayDate` | TField |  | This field is updated with the pay-date from pre diary / diary record |
| 12 | `SC.CTDY.COA.RMDR.AUTO.DATE` | `ScCtdyCorpAction_RmdrAutoDate` |  |  |  |
| 13 | `SC.CTDY.COA.QUALIFY.HOLDING` | `ScCtdyCorpAction_QualifyHolding` | TField |  | Portfolio's holding in the original security as at EX.DATE |
| 14 | `SC.CTDY.COA.EVENT.NOMINAL` | `ScCtdyCorpAction_EventNominal` | TField |  | This is the total nominal involved in the event. If the event is a RIGHTS issue then this is the total number ofrights otherwise this will be equal to the QUALIFY.HOLDING. |
| 15 | `SC.CTDY.COA.CURRENCY` | `ScCtdyCorpAction_Currency` | TField |  | Currency in which ENTITLEMENT.AMT is calculated. If CURRENCY in Diary is a non-restricted Currency, then thecurrency will be defaulted from the CURRENCY field on the original SC.PRE.DIARY record. |
| 16 | `SC.CTDY.COA.OPTION.DESCRIPTION` | `ScCtdyCorpAction_OptionDescription` |  |  |  |
| 17 | `SC.CTDY.COA.ENTITLEMENT.AMT` | `ScCtdyCorpAction_EntitlementAmt` |  |  |  |
| 18 | `SC.CTDY.COA.RATIO` | `ScCtdyCorpAction_Ratio` |  |  |  |
| 19 | `SC.CTDY.COA.GROSS.RATE` | `ScCtdyCorpAction_GrossRate` |  |  |  |
| 20 | `SC.CTDY.COA.NET.RATE` | `ScCtdyCorpAction_NetRate` |  |  |  |
| 21 | `SC.CTDY.COA.NEW.SECURITY` | `ScCtdyCorpAction_NewSecurity` |  |  |  |
| 22 | `SC.CTDY.COA.NOMINAL` | `ScCtdyCorpAction_Nominal` |  |  |  |
| 23 | `SC.CTDY.COA.OPT.NOMINAL` | `ScCtdyCorpAction_OptNominal` |  |  |  |
| 24 | `SC.CTDY.COA.EVENT.STATUS` | `ScCtdyCorpAction_EventStatus` |  |  |  |
| 25 | `SC.CTDY.COA.MSG.TYPE` | `ScCtdyCorpAction_MsgType` |  |  |  |
| 26 | `SC.CTDY.COA.SEME.REF` | `ScCtdyCorpAction_SemeRef` |  |  |  |
| 27 | `SC.CTDY.COA.INW.SEME.REF` | `ScCtdyCorpAction_InwSemeRef` |  |  |  |
| 28 | `SC.CTDY.COA.MSG.FUNCTION` | `ScCtdyCorpAction_MsgFunction` |  |  |  |
| 29 | `SC.CTDY.COA.MSG.STATUS` | `ScCtdyCorpAction_MsgStatus` |  |  |  |
| 30 | `SC.CTDY.COA.RELA.REFERENCE` | `ScCtdyCorpAction_RelaReference` |  |  |  |
| 31 | `SC.CTDY.COA.GROSS.CASH` | `ScCtdyCorpAction_GrossCash` |  |  |  |
| 32 | `SC.CTDY.COA.PSTA.CASH` | `ScCtdyCorpAction_PstaCash` |  |  |  |
| 33 | `SC.CTDY.COA.PSTA.QTY` | `ScCtdyCorpAction_PstaQty` |  |  |  |
| 34 | `SC.CTDY.COA.NET.CASH` | `ScCtdyCorpAction_NetCash` |  |  |  |
| 35 | `SC.CTDY.COA.566.NEW.SECURITY` | `ScCtdyCorpAction_566NewSecurity` |  |  |  |
| 36 | `SC.CTDY.COA.PROC.STATUS` | `ScCtdyCorpAction_ProcStatus` |  |  |  |
| 37 | `SC.CTDY.COA.ERR.NARRATIVE` | `ScCtdyCorpAction_ErrNarrative` |  |  |  |
| 38 | `SC.CTDY.COA.INW.DELIVERY.REF` | `ScCtdyCorpAction_InwDeliveryRef` |  |  |  |
| 39 | `SC.CTDY.COA.GEN.MT567` | `ScCtdyCorpAction_GenMt567` |  |  |  |
| 40 | `SC.CTDY.COA.DELIVERY.REF` | `ScCtdyCorpAction_DeliveryRef` |  |  |  |
| 41 | `SC.CTDY.COA.ADDTL.NARR` | `ScCtdyCorpAction_AddtlNarr` |  |  |  |
| 42 | `SC.CTDY.COA.SENT.BY` | `ScCtdyCorpAction_SentBy` |  |  |  |
| 43 | `SC.CTDY.COA.SEND.MSG` | `ScCtdyCorpAction_SendMsg` |  |  |  |
| 44 | `SC.CTDY.COA.LATEST.MSG.TYPE` | `ScCtdyCorpAction_LatestMsgType` | TField |  | This field will allows the user to input the message that needs to be generated Allowed Message Types 564, 565, 567, 568 |
| 45 | `SC.CTDY.COA.LATEST.MSG.FUNCTION` | `ScCtdyCorpAction_LatestMsgFunction` | TField |  | This field will allows the user to input the function for the message that needs to be generated |
| 46 | `SC.CTDY.COA.LATEST.MSG.STATUS` | `ScCtdyCorpAction_LatestMsgStatus` | TField |  | This field will allows the user to input the status for the message that needs to be generated |
| 47 | `SC.CTDY.COA.LATEST.GROSS.CASH` | `ScCtdyCorpAction_LatestGrossCash` | TField |  | This field holds the value in the GROSS.CASH field from the option for which the latest 566 message is sent out |
| 48 | `SC.CTDY.COA.LATEST.PSTA.CASH` | `ScCtdyCorpAction_LatestPstaCash` | TField |  | This field holds the value in the PSTA.CASH field from the option for which the latest 566 message is sent out |
| 49 | `SC.CTDY.COA.LATEST.PSTA.QTY` | `ScCtdyCorpAction_LatestPstaQty` |  |  |  |
| 50 | `SC.CTDY.COA.LATEST.NET.CASH` | `ScCtdyCorpAction_LatestNetCash` | TField |  | This field holds the value in the NET.CASH field from the option for which the latest 566 message is sent out |
| 51 | `SC.CTDY.COA.LATEST.NEW.SECURITY` | `ScCtdyCorpAction_LatestNewSecurity` |  |  |  |
| 52 | `SC.CTDY.COA.LATEST.PROC.STATUS` | `ScCtdyCorpAction_LatestProcStatus` | TField |  | This field holds the value in the PROC.STATUS field from the option for which the latest 566 message is sent out |
| 53 | `SC.CTDY.COA.LATEST.ERR.NARRATIVE` | `ScCtdyCorpAction_LatestErrNarrative` |  |  |  |
| 54 | `SC.CTDY.COA.LATEST.ADDTL.NARR` | `ScCtdyCorpAction_LatestAddtlNarr` |  |  |  |
| 55 | `SC.CTDY.COA.LATEST.INW.SEME.REF` | `ScCtdyCorpAction_LatestInwSemeRef` | TField |  | This field will allow the user to input the 565 seme reference for MT567 message. Input allowed only for MT567. For MT565, this field will be mapped from INW.SEME.REF field. |
| 56 | `SC.CTDY.COA.LATEST.565.OPTION` | `ScCtdyCorpAction_Latest565Option` | TField |  | This field will allow the user to input the option number for MT567 message. Input should be a valid option number from Diary. Input allowed only for MT567. For MT565, this field will be mapped from 565.OPTION. |
| 57 | `SC.CTDY.COA.LATEST.565.NOMINAL` | `ScCtdyCorpAction_Latest565Nominal` | TField |  | This field will allow the user to input the option nominal for MT567 message. For INST,input should not be greater than QUALIFY.HOLDING minus Elected nominals. For CAST,input should not be greater than the previously elected nominal. Input allowed only for MT567. For MT565, this field will be mapped from 565.NOMINAL. |
| 58 | `SC.CTDY.COA.INW.CORP.REFERENCE` | `ScCtdyCorpAction_InwCorpReference` | TField |  | This field will store the CORP reference of incoming MT564 custodian message. No input field, updated by the system |
| 59 | `SC.CTDY.COA.RESERVED26` | `ScCtdyCorpAction_Reserved26` | TField |  |  |
| 60 | `SC.CTDY.COA.RESERVED25` | `ScCtdyCorpAction_Reserved25` | TField |  |  |
| 61 | `SC.CTDY.COA.RESERVED24` | `ScCtdyCorpAction_Reserved24` | TField |  |  |
| 62 | `SC.CTDY.COA.RESERVED23` | `ScCtdyCorpAction_Reserved23` | TField |  |  |
| 63 | `SC.CTDY.COA.RESERVED22` | `ScCtdyCorpAction_Reserved22` | TField |  |  |
| 64 | `SC.CTDY.COA.RESERVED21` | `ScCtdyCorpAction_Reserved21` | TField |  |  |
| 65 | `SC.CTDY.COA.RESERVED20` | `ScCtdyCorpAction_Reserved20` | TField |  |  |
| 66 | `SC.CTDY.COA.RESERVED19` | `ScCtdyCorpAction_Reserved19` | TField |  |  |
| 67 | `SC.CTDY.COA.RESERVED18` | `ScCtdyCorpAction_Reserved18` | TField |  |  |
| 68 | `SC.CTDY.COA.RESERVED17` | `ScCtdyCorpAction_Reserved17` | TField |  |  |
| 69 | `SC.CTDY.COA.RESERVED16` | `ScCtdyCorpAction_Reserved16` | TField |  |  |
| 70 | `SC.CTDY.COA.RESERVED15` | `ScCtdyCorpAction_Reserved15` | TField |  |  |
| 71 | `SC.CTDY.COA.RESERVED14` | `ScCtdyCorpAction_Reserved14` | TField |  |  |
| 72 | `SC.CTDY.COA.RESERVED13` | `ScCtdyCorpAction_Reserved13` | TField |  |  |
| 73 | `SC.CTDY.COA.RESERVED12` | `ScCtdyCorpAction_Reserved12` | TField |  |  |
| 74 | `SC.CTDY.COA.RESERVED11` | `ScCtdyCorpAction_Reserved11` | TField |  |  |
| 75 | `SC.CTDY.COA.RESERVED10` | `ScCtdyCorpAction_Reserved10` | TField |  |  |
| 76 | `SC.CTDY.COA.RESERVED09` | `ScCtdyCorpAction_Reserved09` | TField |  |  |
| 77 | `SC.CTDY.COA.RESERVED08` | `ScCtdyCorpAction_Reserved08` | TField |  |  |
| 78 | `SC.CTDY.COA.RESERVED07` | `ScCtdyCorpAction_Reserved07` | TField |  |  |
| 79 | `SC.CTDY.COA.RESERVED06` | `ScCtdyCorpAction_Reserved06` | TField |  |  |
| 80 | `SC.CTDY.COA.RESERVED05` | `ScCtdyCorpAction_Reserved05` | TField |  |  |
| 81 | `SC.CTDY.COA.RESERVED04` | `ScCtdyCorpAction_Reserved04` | TField |  |  |
| 82 | `SC.CTDY.COA.RESERVED03` | `ScCtdyCorpAction_Reserved03` | TField |  |  |
| 83 | `SC.CTDY.COA.RESERVED02` | `ScCtdyCorpAction_Reserved02` | TField |  |  |
| 84 | `SC.CTDY.COA.RESERVED01` | `ScCtdyCorpAction_Reserved01` | TField |  |  |
| 85 | `SC.CTDY.COA.LOCAL.REF` | `ScCtdyCorpAction_LocalRef` |  |  |  |
| 86 | `SC.CTDY.COA.OVERRIDE` | `ScCtdyCorpAction_Override` |  |  |  |
| 87 | `SC.CTDY.COA.RECORD.STATUS` | `ScCtdyCorpAction_RecordStatus` | String |  |  |
| 88 | `SC.CTDY.COA.CURR.NO` | `ScCtdyCorpAction_CurrNo` | String |  |  |
| 89 | `SC.CTDY.COA.INPUTTER` | `ScCtdyCorpAction_Inputter` |  |  |  |
| 90 | `SC.CTDY.COA.DATE.TIME` | `ScCtdyCorpAction_DateTime` |  |  |  |
| 91 | `SC.CTDY.COA.AUTHORISER` | `ScCtdyCorpAction_Authoriser` | String |  |  |
| 92 | `SC.CTDY.COA.CO.CODE` | `ScCtdyCorpAction_CoCode` | String |  |  |
| 93 | `SC.CTDY.COA.DEPT.CODE` | `ScCtdyCorpAction_DeptCode` | String |  |  |
| 94 | `SC.CTDY.COA.AUDITOR.CODE` | `ScCtdyCorpAction_AuditorCode` | String |  |  |
| 95 | `SC.CTDY.COA.AUDIT.DATE.TIME` | `ScCtdyCorpAction_AuditDateTime` | String |  |  |
| 96 | `SC.CTDY.COA.ACCOUNT.NO` | `ScCtdyCorpAction_AccountNo` | TField |  | This field holds the account number of the portfolio involved in the event |
| 97 | `SC.CTDY.COA.565.OPTION` | `ScCtdyCorpAction_565Option` |  |  |  |
| 98 | `SC.CTDY.COA.565.NOMINAL` | `ScCtdyCorpAction_565Nominal` |  |  |  |
| 99 | `SC.CTDY.SUB.ACCOUNT` | `ScCtdyCorpAction_SubAccount` | TField |  | Field to hold the SUB.ACCOUNT value. Mapped from 97A of incoming MT message to hold the SUB.ACCOUNT corresponding to SUB.ACC.EXT.ID. Any Sub account defined at CUSTOMER.SECURITY is considered OMNIBUS sub account , otherwise its a SEGREGATED sub account . Incase of Omnibus account in 97A tag, and SubAccount is defined in CUSTOMER.SECURITY, this field will hold the Omnibus Account value. Incase of Omnibus account in 97A tag and is found in DEP.EXT.ACC.ID of CUSTOMER.SECURITY, this field will hold the value 'MAIN'. Incase of Segregated account in 97A tag, this field will hold the value 'SEGREGATED' No input field |
