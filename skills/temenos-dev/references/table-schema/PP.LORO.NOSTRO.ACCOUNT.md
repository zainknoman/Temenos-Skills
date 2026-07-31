# PP.LORO.NOSTRO.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.PP.LORO.NOSTRO.ACCOUNT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.LNA.CompanyID` | `PpLoroNostroAccount_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. NoInput Field The value gets autopopulated based on the company that you login |
| 2 | `PP.LNA.BICCode` | `PpLoroNostroAccount_Biccode` | TField | Yes | Holds the BIC's/LEI's for which the account entry needs to be checked. This can be a BIC-8 or a BIC-11 field. Can be a BIC-8 or BIC-8*. For example, it can be given as a BIC-8* (eg DEUTDEFF*) or just a BIC-8 (eg DEUTDEFF). For a BIC-8* (eg DEUTDEFF*), this entry is applicable for all the defined BIC-8's and BIC-11's linked to DEUTDEFF. For example, a BIC - DEUTDEFF500,DEUTDEFF501 or DEUTDEFF will go on to select the entry for DEUTDEFF*. For a BIC-8 entry (eg DEUTDEFF), this entry is applicable only for DEUTDEFF and not for the BIC-11's linked to DEUTDEFF. Validation Rules: 1) Mandatory 2) Should be a BIC-8, BIC-8* or BIC-11. 3) Should be a valid entry in PPT.BICTABLE table. |
| 3 | `PP.LNA.AccountNumberType` | `PpLoroNostroAccount_Accountnumbertype` | TField | Yes | Specifies the type of the account number. Validation Rules: 1) Mandatory 2) Allowed values are 'V' and 'N' where V - Vostro/Loro N - Nostro |
| 4 | `PP.LNA.AccountCurrency` | `PpLoroNostroAccount_Accountcurrency` | TField | Yes | Specifies the currency of the account. Validation Rules: 1) Mandatory. 2) Dropdown field linked to PP.CURRENCY table. |
| 5 | `PP.LNA.StartDate` | `PpLoroNostroAccount_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. |
| 6 | `PP.LNA.EndDate` | `PpLoroNostroAccount_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 7 | `PP.LNA.AccountNumberCompanyID` | `PpLoroNostroAccount_Accountnumbercompanyid` |  |  |  |
| 8 | `PP.LNA.AccountNumber` | `PpLoroNostroAccount_Accountnumber` |  |  |  |
| 9 | `PP.LNA.OwningBIC` | `PpLoroNostroAccount_Owningbic` |  |  |  |
| 10 | `PP.LNA.PreferredDebitAccountNumber` | `PpLoroNostroAccount_Preferreddebitaccountnumber` |  |  |  |
| 11 | `PP.LNA.PreferredCreditAcctNumber` | `PpLoroNostroAccount_Preferredcreditacctnumber` |  |  |  |
| 12 | `PP.LNA.ChargesIndicator` | `PpLoroNostroAccount_Chargesindicator` |  |  |  |
| 13 | `PP.LNA.AccountNumberInHoldingBk` | `PpLoroNostroAccount_Accountnumberinholdingbk` |  |  |  |
| 14 | `PP.LNA.AccountShortName` | `PpLoroNostroAccount_Accountshortname` |  |  |  |
| 15 | `PP.LNA.DraftAccount` | `PpLoroNostroAccount_Draftaccount` |  |  |  |
| 16 | `PP.LNA.OutgoingMessageInterface` | `PpLoroNostroAccount_OutgoingMessageInterface` |  |  |  |
| 17 | `PP.LNA.RESERVED.3` | `PpLoroNostroAccount_Reserved3` |  |  |  |
| 18 | `PP.LNA.RESERVED.2` | `PpLoroNostroAccount_Reserved2` | TField |  |  |
| 19 | `PP.LNA.RESERVED.1` | `PpLoroNostroAccount_Reserved1` | TField |  |  |
| 20 | `PP.LNA.LOCAL.REF` | `PpLoroNostroAccount_LocalRef` |  |  |  |
| 21 | `PP.LNA.LinkID` | `PpLoroNostroAccount_Linkid` | TField |  |  |
| 22 | `PP.LNA.OVERRIDE` | `PpLoroNostroAccount_Override` |  |  |  |
| 23 | `PP.LNA.RECORD.STATUS` | `PpLoroNostroAccount_RecordStatus` | String |  |  |
| 24 | `PP.LNA.CURR.NO` | `PpLoroNostroAccount_CurrNo` | String |  |  |
| 25 | `PP.LNA.INPUTTER` | `PpLoroNostroAccount_Inputter` |  |  |  |
| 26 | `PP.LNA.DATE.TIME` | `PpLoroNostroAccount_DateTime` |  |  |  |
| 27 | `PP.LNA.AUTHORISER` | `PpLoroNostroAccount_Authoriser` | String |  |  |
| 28 | `PP.LNA.CO.CODE` | `PpLoroNostroAccount_CoCode` | String |  |  |
| 29 | `PP.LNA.DEPT.CODE` | `PpLoroNostroAccount_DeptCode` | String |  |  |
| 30 | `PP.LNA.AUDITOR.CODE` | `PpLoroNostroAccount_AuditorCode` | String |  |  |
| 31 | `PP.LNA.AUDIT.DATE.TIME` | `PpLoroNostroAccount_AuditDateTime` | String |  |  |
