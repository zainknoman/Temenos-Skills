# SC.PRE.DIARY — Table Schema

> Source: `INSERTS/I_F.SC.PRE.DIARY` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PRD.SECURITY.NO` | `ScPreDiary_SecurityNo` | TField |  | The Security number of the security that the Diary record relates to. Must exist on the SECURITY.MASTER record. If it doesn't exist in SECURITY.MASTER file, at authorisation stage : - the field is set to blank, - a message is set to the HOLD.REASON field - the record stay in hld status. Validation Rules: |
| 2 | `SC.PRD.EVENT.TYPE` | `ScPreDiary_EventType` | TField |  | Event type that the incoming swift message refers to. It must be a valid DIARY.TYPE record. If it doesn't exist in DIARAY.TYPE file, at authorisation stage : - a message is set to the HOLD.REASON field - the record stay in hld status. Validation Rules: |
| 3 | `SC.PRD.EX.DATE` | `ScPreDiary_ExDate` | TField | Yes | The Ex.Div date of the DIARY. All holders in the Security specified as of this date are entitled to the event. Validation Rules: Mandatory input of Standard T24 Date format. |
| 4 | `SC.PRD.PAY.DATE` | `ScPreDiary_PayDate` | TField | Yes | Date of the Event is paid/issued. Validation Rules: Mandatory input of Standard T24 Date format. |
| 5 | `SC.PRD.REPLY.BY.DATE` | `ScPreDiary_ReplyByDate` | TField | No | Advises the date that instructions must be with the registrar or custodian. Validation Rules: Optional input of Standard T24 Date format. |
| 6 | `SC.PRD.CURRENCY` | `ScPreDiary_Currency` | TField |  | Indicates the Currency of the Event which is being defined. Validation Rules: |
| 7 | `SC.PRD.RATE.TYPE` | `ScPreDiary_RateType` | TField |  | This field will indicate whether the Rate is quoted as a net or gross figure - with respect to tax. The CorporateActions suite of programs allows rates to be entered before tax &amp; or charges (Gross) or after tax &amp; orcharges (Net). Validation Rules: Only input of 'GROSS' or 'NET' allowed. |
| 8 | `SC.PRD.OPTION.DESC` | `ScPreDiary_OptionDesc` |  |  |  |
| 9 | `SC.PRD.CASH.CCY` | `ScPreDiary_CashCcy` |  |  |  |
| 10 | `SC.PRD.OPTION.IND` | `ScPreDiary_OptionInd` |  |  |  |
| 11 | `SC.PRD.OPTION.NUM` | `ScPreDiary_OptionNum` |  |  |  |
| 12 | `SC.PRD.DEFAULT.OPTION` | `ScPreDiary_DefaultOption` |  |  |  |
| 13 | `SC.PRD.OPT.CCY.DIV.RATE` | `ScPreDiary_OptCcyDivRate` |  |  |  |
| 14 | `SC.PRD.OPT.CCY.EXCH.RATE` | `ScPreDiary_OptCcyExchRate` |  |  |  |
| 15 | `SC.PRD.OPT.REPLY.BY.DATE` | `ScPreDiary_OptReplyByDate` |  |  |  |
| 16 | `SC.PRD.OPT.REPLY.BY.TIME` | `ScPreDiary_OptReplyByTime` |  |  |  |
| 17 | `SC.PRD.OPT.PAY.DATE` | `ScPreDiary_OptPayDate` |  |  |  |
| 18 | `SC.PRD.EXPIRY.DATE` | `ScPreDiary_ExpiryDate` |  |  |  |
| 19 | `SC.PRD.PERIOD.FROM` | `ScPreDiary_PeriodFrom` |  |  |  |
| 20 | `SC.PRD.PERIOD.TO` | `ScPreDiary_PeriodTo` |  |  |  |
| 21 | `SC.PRD.MIN.EXC.QTY` | `ScPreDiary_MinExcQty` |  |  |  |
| 22 | `SC.PRD.MAX.EXC.QTY` | `ScPreDiary_MaxExcQty` |  |  |  |
| 23 | `SC.PRD.OPT.TRAD.PRD.FROM` | `ScPreDiary_OptTradPrdFrom` |  |  |  |
| 24 | `SC.PRD.OPT.TRAD.PRD.TO` | `ScPreDiary_OptTradPrdTo` |  |  |  |
| 25 | `SC.PRD.OPT.ACT.PRD.FROM` | `ScPreDiary_OptActPrdFrom` |  |  |  |
| 26 | `SC.PRD.OPT.ACT.PRD.TO` | `ScPreDiary_OptActPrdTo` |  |  |  |
| 27 | `SC.PRD.OPT.REVOC.PRD.FROM` | `ScPreDiary_OptRevocPrdFrom` |  |  |  |
| 28 | `SC.PRD.OPT.REVOC.PRD.TO` | `ScPreDiary_OptRevocPrdTo` |  |  |  |
| 29 | `SC.PRD.OPT.VALUE.DATE` | `ScPreDiary_OptValueDate` |  |  |  |
| 30 | `SC.PRD.RESERVED20` | `ScPreDiary_Reserved20` |  |  |  |
| 31 | `SC.PRD.RATE` | `ScPreDiary_Rate` |  |  |  |
| 32 | `SC.PRD.OLD.FACTOR` | `ScPreDiary_OldFactor` |  |  |  |
| 33 | `SC.PRD.NEW.FACTOR` | `ScPreDiary_NewFactor` |  |  |  |
| 34 | `SC.PRD.PERCENTAGE` | `ScPreDiary_Percentage` |  |  |  |
| 35 | `SC.PRD.NEW.SEC.NO` | `ScPreDiary_NewSecNo` |  |  |  |
| 36 | `SC.PRD.NEW.PRICE` | `ScPreDiary_NewPrice` |  |  |  |
| 37 | `SC.PRD.OLD.RATIO` | `ScPreDiary_OldRatio` |  |  |  |
| 38 | `SC.PRD.NEW.RATIO` | `ScPreDiary_NewRatio` |  |  |  |
| 39 | `SC.PRD.RIGHTS.NO` | `ScPreDiary_RightsNo` |  |  |  |
| 40 | `SC.PRD.OLD.TO.RIGHT` | `ScPreDiary_OldToRight` |  |  |  |
| 41 | `SC.PRD.RIGHT.TO.NEW` | `ScPreDiary_RightToNew` |  |  |  |
| 42 | `SC.PRD.FRACTION.DISP` | `ScPreDiary_FractionDisp` |  |  |  |
| 43 | `SC.PRD.CASH.IN.LIEU.PRICE` | `ScPreDiary_CashInLieuPrice` |  |  |  |
| 44 | `SC.PRD.ROUND.NOMINAL` | `ScPreDiary_RoundNominal` |  |  |  |
| 45 | `SC.PRD.AVAILABLE.DATE` | `ScPreDiary_AvailableDate` |  |  |  |
| 46 | `SC.PRD.TAX.PRICE` | `ScPreDiary_TaxPrice` |  |  |  |
| 47 | `SC.PRD.SEC.RESERVED.02` | `ScPreDiary_SecReserved02` |  |  |  |
| 48 | `SC.PRD.SEC.RESERVED.01` | `ScPreDiary_SecReserved01` |  |  |  |
| 49 | `SC.PRD.ARCH.DATE` | `ScPreDiary_ArchDate` | TField | Yes | Archive date of the SC.PRE.DIARY record. This date is defaulted to the date derived from the DIARY.REMAIN field of the SC.PARAMETER file that contains the number of days the diaries should remains before archiving. The date can be amended manually. Validation Rules: Mandatory input of Standard T24 Date format. |
| 50 | `SC.PRD.DELIVERY.INREF` | `ScPreDiary_DeliveryInref` |  |  |  |
| 51 | `SC.PRD.NARRATIVE` | `ScPreDiary_Narrative` |  |  |  |
| 52 | `SC.PRD.ISIN.NR` | `ScPreDiary_IsinNr` | TField |  | ISIN nr of the concerned security. Can be useful (if security number does not exist) to open a new SECURITY.MASTER record. Validation Rules: |
| 53 | `SC.PRD.HLD.REASON` | `ScPreDiary_HldReason` | TField |  | Reason of the HLD status of the record. If the DIARY cannot be generated, the reason is indicated here. Validation Rules: Automatic reason (at authorisation stage) : - SECURITY.NO UNKNOWN - SC.PRE.DIARY (OR $HIS OR $NAU) ALLREADY EXISTS - DIARY (OR $HIS OR $NAU) ALLREADY EXISTS - EVENT.TYPE MISSING - EX.DATE MISSING - NO POSITION - EVENT UNKNOWN IN DIARY.TYPE any manual entry |
| 54 | `SC.PRD.DEPOSITORY` | `ScPreDiary_Depository` | TField |  | The depository from whom this notice originated. Extracted from the inward delivery message. |
| 55 | `SC.PRD.QTY.SECURITY` | `ScPreDiary_QtySecurity` | TField |  | The quantity of security concerned by the event populated from the QTY.SECURITY field of the incoming swift message. Validation Rules: |
| 56 | `SC.PRD.QTY.DERIVED` | `ScPreDiary_QtyDerived` | TField |  | The quantity derived from the original security concerned by the event populated from the QTY.DERIVED field ofthe incoming swift message. Validation Rules: |
| 57 | `SC.PRD.GROSS.AMOUNT` | `ScPreDiary_GrossAmount` | TField |  | The gross amount generated by the event populated from the GROSS.AMOUNT field of the incoming swift message. Validation Rules: |
| 58 | `SC.PRD.MESSAGE.TYPE` | `ScPreDiary_MessageType` | TField |  | Message type of the incoming swift message (MTxxx) Validation Rules: |
| 59 | `SC.PRD.FEED.SOURCE` | `ScPreDiary_FeedSource` | TField |  | User defined field indicating the transaction source. |
| 60 | `SC.PRD.SOURCE.REF` | `ScPreDiary_SourceRef` | TField |  | Extracted from the inward delivery message senders reference (prefix SEME) |
| 61 | `SC.PRD.ACTION.STATUS` | `ScPreDiary_ActionStatus` | TField |  | Extracted from the inward delivery message to indicate status, for SWIFT this can be NEWM or CANC etc. |
| 62 | `SC.PRD.DIARY.ID` | `ScPreDiary_DiaryId` | TField |  | This field is a system maintained field that stores the reference to the DIARY record created when theSC.PRE.DIARY record was authorised. Validation Rules: An EXTERNAL field. Maintained by the system. |
| 63 | `SC.PRD.RECORD.DATE` | `ScPreDiary_RecordDate` | TField | No | The RECORD.DATE of the DIARY.Optional date field that can be before, after or equal to EX.DATE. The Record Dateof a Corporate Event does not affect the beneficial entitlement to the event, but does affect the way the event isprocessed with regard to who will receive the outcome of an event directly and where the outcome is due to/from. Validation Rules: Optional input of Standard T24 Date format. |
| 64 | `SC.PRD.LINK.REF` | `ScPreDiary_LinkRef` | TField |  | Extracted from the inward delivery message senders reference (prefix CORP) |
| 65 | `SC.PRD.ADDL.NARRATIVE` | `ScPreDiary_AddlNarrative` |  |  |  |
| 66 | `SC.PRD.EARLY.DEADLINE` | `ScPreDiary_EarlyDeadline` | TField |  | This field will be updated from inward message MT564 and will hold the early deadline date of the event. |
| 67 | `SC.PRD.AUTO.AUTH.DATE` | `ScPreDiary_AutoAuthDate` | TField |  | Date on which the Start of Day process will automatically authorise the SC.PRE.DIARY record. This field is automatically populated from the parameters entered in the related DIARY.TYPE record (fields PRE.DIA.DAYS, PRE.DIA.PRI.AFT, PRE.DIA.SEL.DATE) This field can be amended. The user will be prompted to bypass the date when authorising the SC.PRE.DIARY record manually. Validation Rules: Standard T24 Date format The date must be at least the next working day |
| 68 | `SC.PRD.SOURCE.COMPANY` | `ScPreDiary_SourceCompany` | TField |  | Denotes the company in which SC.PRE.DIARY record is created The field will be defaulted with ID.COMPANY Validation Rules: Accepts a valid company code. |
| 69 | `SC.PRD.STP` | `ScPreDiary_Stp` | TField |  | Holds value YES - This field is only for informatory purpose and will determine whether Diary caters to Full STP. |
| 70 | `SC.PRD.LOAN` | `ScPreDiary_Loan` | TField |  | Holds value YES - This field is only for informatory purpose and will determine whether Diary caters to lentposition of the security. |
| 71 | `SC.PRD.REDEM.PERCENT` | `ScPreDiary_RedemPercent` | TField |  | This field will hold the redemption percentage, up to which the nominal will be redeemed based on trading units. Validation Rules: |
| 72 | `SC.PRD.SETT.CURRENCY` | `ScPreDiary_SettCurrency` | TField |  | If CURRENCY is a restricted Curreny, then this field contains the Settlement Currency. Validation Rules: Must exist in CURRENCY file. |
| 73 | `SC.PRD.EXCH.RATE` | `ScPreDiary_ExchRate` | TField |  | If CURRENCY is a restricted Curreny,then this field contains contains the Exchange Rate between CURRENCY andSETT.CURRENCY. |
| 74 | `SC.PRD.TRD.PERIOD.START` | `ScPreDiary_TrdPeriodStart` | TField |  | To record Start Trading Period.Mapped from 564 identifier, 69B::TRDP. |
| 75 | `SC.PRD.TRD.PERIOD.END` | `ScPreDiary_TrdPeriodEnd` | TField |  | To record End Trading Period.Mapped from 564 identifier, 69B::TRDP. |
| 76 | `SC.PRD.MAND.VOLU.FLAG` | `ScPreDiary_MandVoluFlag` | TField | Yes | Mandatory or voluntary indicator for the Event. Mapped from 564 identifier, 22F::CAMV. Validation Rules: Allowed values: MAND,VOLU,CHOS |
| 77 | `SC.PRD.OVER.OPTION.DESC` | `ScPreDiary_OverOptionDesc` | TField |  | Option indicator for oversubscription. Mapped from 564 identifier,22F::CAOP if option in CAOP tag contains OVER.If manually input, this should be specified as OVER. |
| 78 | `SC.PRD.OVER.OPTION.NUM` | `ScPreDiary_OverOptionNum` | TField |  | Option number pertaining to Oversubscription.Mapped from 564 identifier, 13A::CAON. |
| 79 | `SC.PRD.OVER.SUBS.PRICE` | `ScPreDiary_OverSubsPrice` | TField |  | This holds the price at which Over subscribed quantity is to be sold. Mapped from 564 identifier, 95a::PRPP. |
| 80 | `SC.PRD.MEETING.DATE` | `ScPreDiary_MeetingDate` | TField |  | This field specifies the date of meeting and so updated from 98A tag of CA option details of MT564 with qualifierMEET. Validation Rules Standard T24 Date field |
| 81 | `SC.PRD.MEETING.TIME` | `ScPreDiary_MeetingTime` | TField |  | This field specifies the time of meeting and so updated from 98C tag of CA option details of MT564 with qualifierMEET. Validation Rules Standard T24 time field |
| 82 | `SC.PRD.MEET.VENUE` | `ScPreDiary_MeetVenue` |  |  |  |
| 83 | `SC.PRD.NEW.INCORP.PLACE` | `ScPreDiary_NewIncorpPlace` | TField |  | This field specifies the New Company's place of Incorporation. System will update this field from 94E tag of MT564 when the qualifier is NPLI For e.g. if 94E tag contains the value,:94E::NPLI//11 Eunos Rd 8,Lvl 1 Event Hall, system updates this field as"11 Eunos Rd 8,Lvl 1 Event Hall" Validation Rules Standard T24 Time field |
| 84 | `SC.PRD.OTH.DATE.TYPE` | `ScPreDiary_OthDateType` |  |  |  |
| 85 | `SC.PRD.OTH.DATE` | `ScPreDiary_OthDate` |  |  |  |
| 86 | `SC.PRD.OTH.DATE.TIME` | `ScPreDiary_OthDateTime` |  |  |  |
| 87 | `SC.PRD.CERTIFICATION.TYPE` | `ScPreDiary_CertificationType` |  |  |  |
| 88 | `SC.PRD.CERT.PLACE` | `ScPreDiary_CertPlace` |  |  |  |
| 89 | `SC.PRD.CURR.FUNC` | `ScPreDiary_CurrFunc` | TField |  | The field to capture the function of the latest message (MT564 - Corporate Action Notification). Validation Rules The valid functions are defined in EB.LOOKUP table - MSG.FUNC*(ADDB,CANC,NEWM,REPE,REPL,RMDR,WITH) |
| 90 | `SC.PRD.CURR.STATUS.CODE` | `ScPreDiary_CurrStatusCode` | TField |  | The field to capture the processing status (Field 25D - Processing Status)from the latest MT 564 Validation Rules The valid statuses are defined in EB.LOOKUP table - MSG.STATUS*(COMP,COMU,ENTL,PREU,PREC) |
| 91 | `SC.PRD.RERUN` | `ScPreDiary_Rerun` | TField |  | Field to trigger rerun of eligible holding calculation. It will be automatically set to Y on receipt of MT 564forwhich notification has to be generated. This field also enable to trigger the rerun to generate the MT564 outward for eligible holders Validation Rules Cannot be set once the DIARY is created. Allowed Values : Y, MT564, BOTH Y - To trigger rerun of eligible holding calculation to send the pre advice notification. MT564 - To generate NEWM for new eligible holders and REPE if there is change in holdings (Where we have alreadysent NEWM for this holder) BOTH - Handle both MT564 outward and pre advice notification Rerun to generate the MT564 outward for new eligible holders cannot be set a) when it is succeeded by another custodian SC.PRE.DIARY b) For source other than NON.CUSTODIAN c) When DIARY has been generated Rerun to generate the MT564 for new eligible holders will happen only when GEN.MT564 is set to YES or STP, elseerror will be raised |
| 92 | `SC.PRD.PRE.ADVICE.REQ` | `ScPreDiary_PreAdviceReq` | TField | No | Determines whether pre confirmation advices are generated when SC.PRE.DIARY is created. The value will be defaulted from the relevant DIARY.TYPE record. The actual message types are determined via the relevant EB.ADVICES records, which will be eitherSC-0100-EVENT.TYPE. Validation Rules Optional Input can be set to YES or NO |
| 93 | `SC.PRD.INIT.ADVICE.SENT` | `ScPreDiary_InitAdviceSent` | TField |  | Flag to indicate whether initial advice is sent from pre diary Validation Rules Noinput Field |
| 94 | `SC.PRD.CAEV.TYPE` | `ScPreDiary_CaevType` | TField |  | Denotes the Corporate action Event Indicator in SWIFT terms. Validation Rules Valid Swift indicator |
| 95 | `SC.PRD.INT.DIST.TYPE` | `ScPreDiary_IntDistType` | TField |  | This field denotes whether the rights distribution event is for reinvestment, exchange or subscription of rights. Mapped from 564 identifier, 22F::RHDI from D sequence. Validation Rules: Allowed values: EXRI,EXOF,DRIP |
| 96 | `SC.PRD.PERCENT.SOUGHT` | `ScPreDiary_PercentSought` | TField |  | This field is an information field to denote the percentage of shares sought. Mapped from 564 identifier, 92A::PTSC from D sequence. |
| 97 | `SC.PRD.SOURCE.TAX.PERC` | `ScPreDiary_SourceTaxPerc` | TField |  | Rate of Source Tax levied. This field will only be updated if the TAXABLE field on the DIARY.TYPE record that defines this corporate actionis set to NO. Mapped from 564 identifier, 92A::TAXR from E2 sequence. This field will be mapped to DIARY to ENTITLEMENT record. |
| 98 | `SC.PRD.LOCAL.TAX.PERC` | `ScPreDiary_LocalTaxPerc` |  |  |  |
| 99 | `SC.PRD.SELL.BUY.OPT.DESC` | `ScPreDiary_SellBuyOptDesc` |  |  |  |
| 100 | `SC.PRD.SELL.BUY.OPT.NO` | `ScPreDiary_SellBuyOptNo` |  |  |  |
| 101 | `SC.PRD.SELL.BUY.SEC` | `ScPreDiary_SellBuySec` |  |  |  |
| 102 | `SC.PRD.SELL.BUY.REPLY.DATE` | `ScPreDiary_SellBuyReplyDate` |  |  |  |
| 103 | `SC.PRD.SELL.BUY.TRAD.FROM.DATE` | `ScPreDiary_SellBuyTradFromDate` |  |  |  |
| 104 | `SC.PRD.SELL.BUY.TRAD.TO.DATE` | `ScPreDiary_SellBuyTradToDate` |  |  |  |
| 105 | `SC.PRD.RIGHTS.CREDIT.DATE` | `ScPreDiary_RightsCreditDate` | TField |  | This field will specify the date on which rights will be credited to the account. Mapped from 98A/Post in Sequence C of MT564 Validation Rules Must be valid T24 Date Format |
| 106 | `SC.PRD.RIGHTS.EXP.DATE` | `ScPreDiary_RightsExpDate` | TField |  | Denotes the expiry date of the rights. Mapped from 98A/EXPI in Sequence C of MT564. Validation Rules Must be valid T24 Date Format |
| 107 | `SC.PRD.TAXABLE.RATE` | `ScPreDiary_TaxableRate` | TField |  | Denotes the Taxable rate of Dividend or coupon This field is used to store the taxable rate of income(e.g PID component in UK) Only this portion of the dividend is taxable Validation Rules Input allowed only when Rate field has value Negative rates are not allowed |
| 108 | `SC.PRD.TAX.EXEMPT.RATE` | `ScPreDiary_TaxExemptRate` | TField |  | Denotes the tax-exempt rate of Dividend or coupon This field is used to store the tax exempt rate of income(e.g non PID component in UK) This portion of the Dividend is non-taxable Validation Rules Input allowed only when Rate field has value Negative rates are not allowed |
| 109 | `SC.PRD.FRANKED.CREDIT.RATE` | `ScPreDiary_FrankedCreditRate` | TField |  | This field will hold the Franking Credit rate that will be used for computing franking credits This will be a Rate or a Percentage of face value, based on whether field PERCENTAGE is set as No or Yes Validation Rules Field can be inputted only when 1. CASH field for the record in DIARY.TYPE table is set to yes 2. BOND.OR.SHARE set as 'S' in SECURITY.MASTER record 3. FRANKING.CR.ALLOWED field should be set as YES at Parameter level Negative rates are not allowed. Sum of franked credit rate and unfranked rate should be equal to the rate field. |
| 110 | `SC.PRD.UNFRANKED.RATE` | `ScPreDiary_UnfrankedRate` | TField |  | This field will hold the Unfranked rate This will be a Rate or a Percentage of face value, based on whether field PERCENTAGE is set as No or Yes If not available, this will default to the dividend rate minus FRANKED.CREDIT.RATE Validation Rules Field can be inputted only when 1. CASH field for the record in DIARY.TYPE table is set to yes 2. BOND.OR.SHARE set as 'S' in SECURITY.MASTER record 3. FRANKING.CR.ALLOWED field should be set as YES at Parameter level Negative rates are not allowed. Sum of franked credit rate and unfranked rate should be equal to the rate field. |
| 111 | `SC.PRD.UNFRANKED.CFI.RATE` | `ScPreDiary_UnfrankedCfiRate` | TField |  | This field will hold Conduit Foreign Income rate and should not exceed the unfranked rate. This will be a Rate or a Percentage of face value, based on whether field PERCENTAGE is set as No or Yes Validation Rules Field can be inputted only when 1. CASH field for the record in DIARY.TYPE table is set to yes 2. BOND.OR.SHARE set as 'S' in SECURITY.MASTER record 3. FRANKING.CR.ALLOWED field should be set as YES at Parameter level 4. Only when Unfranked rate is inputted Negative rates are not allowed. |
| 112 | `SC.PRD.GEN.MT564` | `ScPreDiary_GenMt564` | TField |  | This field will be defaulted to STP or NO from GEN.MT564.METHOD in diary type. For manual generation of outward 564/568 message, this field needs to be set to yes |
| 113 | `SC.PRD.GEN.MT568` | `ScPreDiary_GenMt568` | TField |  | This field needs to be manually set to YES, to generate outward 568 message Validation Rules Field can be inputted only when ADDL.NARRATIVE is given |
| 114 | `SC.PRD.BLOCK.POSITION` | `ScPreDiary_BlockPosition` | TField | No | Specifies whether the Security Position is to be blocked by execution of a corporate action of this type. If a position is to be blocked it can be blocked either at authorisation of the DIARY record, i.e. when theunauthorised entitlements are created, or when the ENTITLEMENT is authorised. Position can also be blocked during the election of option in ENTITLEMENT record. This is possible whenBLOCK.POSITION is set as OPTION Validation Rules: Optional input Possible values OPTION, DIARY, ENTITLEMENT or NONE |
| 115 | `SC.PRD.BLOCK.FROM` | `ScPreDiary_BlockFrom` | TField |  | Specifies the date from which the security position will be effectively be blocked Validation Rules: Allowed Values : EX.DATE or RECORD.DATE Input allowed only when BLOCK.POSITION is set as Diary |
| 116 | `SC.PRD.SOURCE` | `ScPreDiary_Source` | TField |  | Denote the source of SC.PRE.DIARY created either from MT564 from the Custodian or Non Custodian Validation Rules: Allowed Values : MANUAL, NON.CUSTODIAN or Blank value Input allowed only when NON.DEPO.MSG is set in Diary Type Default option is blank indicating the pre-diary is created based on an MT564 from the Custodian. If the SC.PRE.DIARY is created as a result of MT564-like message from a non-custodian, this field will beauto-populated as Non-custodian. Where the SC.PRE.DIARY is created or amended manually, user has to mark it manual. By default if the field DELIVERY.INREF is empty, then this field will be automatically populated as Manual. |
| 117 | `SC.PRD.LINK.RECORD.REF` | `ScPreDiary_LinkRecordRef` |  |  |  |
| 118 | `SC.PRD.COMMISSION.CODE` | `ScPreDiary_CommissionCode` | TField |  | Default Commission Code to be used in calculation of commission for the entitlements generated by this event ifthe portfolio has not had a charging structure set-up for this type of Corporate Action. This field will defaults to the Commission Type setup in CUSTOMER.SECURITY file for the DIARY.TYPE. If this isblank it will defaults to the Commission Type defined in the DIARY.TYPE record. This code is validated against the FT.COMMISSION.TYPE file. Validation Rules: Must exist in FT.COMMISSION.TYPE file. 11 characters alphanumeric input. NOCHANGE field. |
| 119 | `SC.PRD.LOCAL.REF` | `ScPreDiary_LocalRef` |  |  |  |
| 120 | `SC.PRD.STATEMENT.NOS` | `ScPreDiary_StatementNos` |  |  |  |
| 121 | `SC.PRD.OVERRIDE` | `ScPreDiary_Override` |  |  |  |
| 122 | `SC.PRD.RECORD.STATUS` | `ScPreDiary_RecordStatus` | String |  |  |
| 123 | `SC.PRD.CURR.NO` | `ScPreDiary_CurrNo` | String |  |  |
| 124 | `SC.PRD.INPUTTER` | `ScPreDiary_Inputter` |  |  |  |
| 125 | `SC.PRD.DATE.TIME` | `ScPreDiary_DateTime` |  |  |  |
| 126 | `SC.PRD.AUTHORISER` | `ScPreDiary_Authoriser` | String |  |  |
| 127 | `SC.PRD.CO.CODE` | `ScPreDiary_CoCode` | String |  |  |
| 128 | `SC.PRD.DEPT.CODE` | `ScPreDiary_DeptCode` | String |  |  |
| 129 | `SC.PRD.AUDITOR.CODE` | `ScPreDiary_AuditorCode` | String |  |  |
| 130 | `SC.PRD.AUDIT.DATE.TIME` | `ScPreDiary_AuditDateTime` | String |  |  |
| 131 | `SC.PRD.SOURCE.TAX.CODE` | `ScPreDiary_SourceTaxCode` | TField |  | Source Tax Code used for Source Tax. Automatically updated by the system from COUPON.TAX.CODE file. The field contains either the key of a TAX record or the key of TAX.TYPE.CONDITION record prefixed by an *. Validation Rules: This is an INPUT field. 2 numeric characters allowed for a TAX code. |
| 132 | `SC.PRD.LOCAL.TAX.CODE` | `ScPreDiary_LocalTaxCode` |  |  |  |
| 133 | `SC.PRD.CONFIRM.REQ` | `ScPreDiary_ConfirmReq` | TField | No | Determines whether confirmation advices are generated when entitlements are created via this Diary record. The value will be defaulted from the relevant DIARY.TYPE record. Validation Rules: Optional Input can be set to YES or NO |
| 134 | `SC.PRD.PORTFOLIO.NO` | `ScPreDiary_PortfolioNo` |  |  |  |
| 135 | `SC.PRD.ODD.LOT.SEC` | `ScPreDiary_OddLotSec` | TField | No | Optional field containing the security number of the Odd Lot Security. Must exist on the SECURITY.MASTERapplication. This field can be the same or it can be different that the main security on which the transaction takes place. Validation Rules: Valid Security Number must exist in SECURITY.MASTER file. |
| 136 | `SC.PRD.DEF.INSTR.DATE` | `ScPreDiary_DefInstrDate` | TField |  | Date on which the Start of Day process will apply default instructions to the ENTITLEMENT records generated from the current DIARY. This field is automatically populated from the parameters entered in the related DIARY.TYPE record (fields DEF.INSTR.APPLY, DEF.NB.OF.DAYS, DEF.PRI.AFT and DEF.INSTR.SEL.DATE). This field can be amended. Validation Rules: Standard T24 Date format |
| 137 | `SC.PRD.DEF.INS.OPTION` | `ScPreDiary_DefInsOption` | TField |  | Specify the option to be choosed by default if not standing instruction have been found or no instructions have been given by the customer. Validation Rules: Option number (multi-value number of the OPTION.DESC field) Input allowed only if the DEF.INSTR.DATE is present. |
| 138 | `SC.PRD.SRC.TAX.DEDUCTED` | `ScPreDiary_SrcTaxDeducted` | TField | No | This Field should be used to specify whether the Depository account should be debited with the Gross amount orthe Gross amount less Source Tax. In the former case, the Source Tax will be shown as a separate accounting entryin the Depositoty account. Validation Rules: Optional Input. Input can be YES, No or left Blank. |
| 139 | `SC.PRD.SC.TAX.CODE` | `ScPreDiary_ScTaxCode` |  |  |  |
| 140 | `SC.PRD.SC.TAX.TYPE` | `ScPreDiary_ScTaxType` |  |  |  |
| 141 | `SC.PRD.SOURCE.OR.LOCAL` | `ScPreDiary_SourceOrLocal` |  |  |  |
| 142 | `SC.PRD.REC.DATE.TRFR` | `ScPreDiary_RecDateTrfr` | TField |  | This field is to switch on Record date processing at individual DIARY level.The value set at this level willdeterminewhether the record dated processing is applicable for the eventIt overrides the setting at SC PARAMETER/DIARY TYPElevel. Validation Rules Input can be YES, No or left Blank. RECORD.DATE should Contain value |
| 143 | `SC.PRD.REC.DATE.TRD` | `ScPreDiary_RecDateTrd` | TField |  | This field is to switch on Record date processing for SEC.TRADEs at individual DIARY level.The value set at thislevelwill determine whether the record dated processing is applicable for the eventIt overrides the setting at SCPARAMETER/ DIARY TYPE level. Validation Rules Input can be YES, No or left Blank. RECORD.DATE should Contain value |
| 144 | `SC.PRD.REC.DT.TXN.CODE` | `ScPreDiary_RecDtTxnCode` |  |  |  |
| 145 | `SC.PRD.UNSETT.TRF.PRE.EX` | `ScPreDiary_UnsettTrfPreEx` | TField |  | This field controls whether transactions done prior to ex-date but not settled by record date will be includedfor eligible holding calculations at individual DIARY level. This will take the highest priority.By default (if thefield is blank), transaction will be included for eligible holding calculations under CAprocessing. Validation Rules Allowed value - NO RECORD.DATE should Contain value |
| 146 | `SC.PRD.EFF.DATE.PROCESSING` | `ScPreDiary_EffDateProcessing` | TField |  | This field at individual event(DIARY) level controls the calculation of the qualified or Eligible holdings basedon settled positions (of both Trades and transfers) as of Effective Date based on the set up to this field.This isfor events like Stock Split and Rev Stock Split event which is based on Effective Date (where Ex.Date and Pay Dateare all the same).Any transactions settling on Effective Date, irrespective of whether it settles SOD, EOD oranytime during the day,will not be considered if the effective date processing flag is set to yes Validation Rules Input allowed are YES, NOValue Yes indicates the effective date processing is enabledValue No indicates thateffective date processing is not applicable for the event RECORD.DATE should Contain value |
| 147 | `SC.PRD.CASH.ENT.CHECK` | `ScPreDiary_CashEntCheck` | TField |  | This field at event level controls whether nostro entries to be raised when the sum of cash and stockentitlementis equal to number of entitlementscreated Defaulted from SC.PARAMATER. Can be changed at event level Validation Rules Input allowed - YES, NO |
| 148 | `SC.PRD.VALUE.DATE` | `ScPreDiary_ValueDate` | TField |  | Date the portfolios (SEC.ACC.MASTER and related cash accounts) are to be updated by the event. This is the value date of the corporate action event in respect of updating the ACCOUNT and SECURITY.POSITIONfiles as a result of the corporate action. In some cases, it may be found necessary to delay the value date forwhich customers accounts receive value. Such instances may, for example, include those cases where the dividend isreceived by cheque and, should this be in a foreign currency, will require sending for collection. If no date is entered then this field will default to the same date as that entered into the PAY.DATE field. Validation Rules: Standard T24 Date format. |
| 149 | `SC.PRD.INT.REPLY.BY.DATE` | `ScPreDiary_IntReplyByDate` | TField |  | This field will be defaulted with REPLY.BY.DATE if not specified and will be mapped in advices. |
| 150 | `SC.PRD.INCOME.CODE` | `ScPreDiary_IncomeCode` |  |  |  |
| 151 | `SC.PRD.INCOME.RATE` | `ScPreDiary_IncomeRate` |  |  |  |
| 152 | `SC.PRD.INCOME.PERCENTAGE` | `ScPreDiary_IncomePercentage` |  |  |  |
| 153 | `SC.PRD.TAXABLE` | `ScPreDiary_Taxable` |  |  |  |
| 154 | `SC.PRD.REPORTABLE` | `ScPreDiary_Reportable` |  |  |  |
| 155 | `SC.PRD.MRGR.TAX.TREATMENT` | `ScPreDiary_MrgrTaxTreatment` | TField |  | This field indicates whether the event is subject to S302 regulation of US IRS Allowed Values : S302 , Blank |
| 156 | `SC.PRD.PERIODIC.RATE` | `ScPreDiary_PeriodicRate` | TField |  |  |
| 157 | `SC.PRD.ACCRUAL.START.DATE` | `ScPreDiary_AccrualStartDate` | TField |  |  |
| 158 | `SC.PRD.ACCRUAL.END.DATE` | `ScPreDiary_AccrualEndDate` | TField |  |  |
| 159 | `SC.PRD.DEF.INS.RIGHTS` | `ScPreDiary_DefInsRights` | TField |  |  |
| 160 | `SC.PRD.SUB.ACCOUNT` | `ScPreDiary_SubAccount` | TField |  | Field to hold the SUB.ACCOUNT value. Mapped from 97A of incoming MT message to hold the SUB.ACCOUNT corresponding to SUB.ACC.EXT.ID. This field can also be inputted manually. Any Sub account defined at CUSTOMER.SECURITY is considered OMNIBUS sub account , otherwise its a SEGREGATED subaccount . Incase of Omnibus account in 97A tag, and SubAccount is defined in CUSTOMER.SECURITY, this field will hold theOmnibus Account value. Incase of Omnibus account in 97A tag and is found in DEP.EXT.ACC.ID of CUSTOMER.SECURITY, this field will holdthe value 'MAIN'. Incase of Segregated account in 97A tag, this field will hold the value 'SEGREGATED' Validation Rules: Allowed values : SEGREGATED, MAIN, Omnibus Accounts |
| 161 | `SC.PRD.PROVIDER.ID` | `ScPreDiary_ProviderId` | TField | Yes | This field will hold the market providerId. When the system is configured for reconciliation of Golden Source and when the pre-diary is created for anon-custodian this field is mandatory as the system needs to update the common reference(golden source reference)in the pre-diary for further reconciliation process. When the pre-diary is created for a custodian if this field is not inputted, then the system will not considerthis pre-diary for golden source reconciliation process. Validation Rules: Value should be record of SC.CA.MKT.PROVIDER. |
| 162 | `SC.PRD.IS.GOLDEN.SOURCE` | `ScPreDiary_IsGoldenSource` | TField |  | This field denotes that the pre-diary is a Golden Source of CA notification for a given event among thepre-diaries with the same EVENT.TYPE, SECURITY.NO and within the allowed range of EX.DATE and PAY.DATE. There can be only one Golden Source for an event. Validation Rules: Noinput Field. |
| 163 | `SC.PRD.GOLDEN.SOURCE.REFERENCE` | `ScPreDiary_GoldenSourceReference` | TField |  | This field holds the common reference between the pre-diaries that enables the Golden Source reconciliation. Itis updated with the the record id of Golden Source pre-diary. Validation Rules: Input not allowed to this field. |
| 164 | `SC.PRD.SYS.MASTER` | `ScPreDiary_SysMaster` | TField |  | This field holds the master pre-diary ID that is used as a source of updating the Golden source pre-diary. This pre-diary is the master of this event until the Manual Master is updated with any value. Validation Rules: Value should be updated only for the Golden Source Pre-diary. |
| 165 | `SC.PRD.MANUAL.MASTER` | `ScPreDiary_ManualMaster` | TField |  | This field holds the pre diary id of same event whose details used to override golden source pre diary wascreated/updated. When this field holds some value, this will be treated as a master of this event and overrides the Sys Masterpre-diary. Validation Rules: The user is allowed to input any pre-diary of the same event with the same common reference(Golden SourceReference) updated. Value should be updated only for the Golden Source Pre-diary(Is Golden Source set to YES). |
| 166 | `SC.PRD.RECON.STATUS` | `ScPreDiary_ReconStatus` | TField |  | This field holds the reconciliation status of the given corporate action event. This can be updated only for thepre-diary with IS.GOLDEN.SOURCE set to YES. Validation Rules: Possible values SYSTEM.UPDATED- This status denotes that the golden source pre-diary is created or updated based on the Masterconfiguration at system level. Applicable only for Golden Source Pre-diary UPDATE.MASTER- This option should be enabled if the user wants to update the Master Pre-diary record manually.The field MANUAL.MASTER should allow input only if the status is set to this option UDPATE.GOLDEN.SOURCE- When this option is set, the user can manually update the attributes of Golden SourcePre-diary. COMPLETE- This status denotes that the user has reviewed the pre-diaries from various sources and reconciliationis complete NOTIFY.CLIENTS- This status denotes that the user can set GEN.MT564 and PRE.ADVICE flags to generate respectivenotification/advice |
