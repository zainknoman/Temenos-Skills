# SY.PRODUCT.INTERFACE — Table Schema

> Source: `INSERTS/I_F.SY.PRODUCT.INTERFACE` in `SY_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.PI.USER.APPLICATION` | `SyProductInterface_UserApplication` | TField |  | A valid T24 application/EB.TABLE.DEFINITION created locally for use with SY processing. |
| 2 | `SY.PI.RESERVED.21` | `SyProductInterface_Reserved21` | TField |  |  |
| 3 | `SY.PI.PRODUCT.DEFINITION` | `SyProductInterface_ProductDefinition` | TField |  | Defines the product (SY.PRODUCT.DEFINITION) that the table defined in the key is linked to. |
| 4 | `SY.PI.RESERVED.20` | `SyProductInterface_Reserved20` | TField |  |  |
| 5 | `SY.PI.CUSTOMER.MAND` | `SyProductInterface_CustomerMand` | TField | Yes | Defines if the field defined in the CUSTOMER.FIELD is mandatory on the user created application. |
| 6 | `SY.PI.CUSTOMER.FIELD` | `SyProductInterface_CustomerField` | TField |  | Defines the name of the field from the user created application that holds the customer party to the the deal. |
| 7 | `SY.PI.RESERVED.19` | `SyProductInterface_Reserved19` | TField |  |  |
| 8 | `SY.PI.PORTFOLIO.MAND` | `SyProductInterface_PortfolioMand` | TField | Yes | Defines if the field defined in the PORTFOLIO.FIELD is mandatory on the user created application. |
| 9 | `SY.PI.PORTFOLIO.FIELD` | `SyProductInterface_PortfolioField` | TField |  | Defines the name of the field from the user created application that holds the customers portfolio. |
| 10 | `SY.PI.RESERVED.18` | `SyProductInterface_Reserved18` | TField |  |  |
| 11 | `SY.PI.COUNTERPARTY.MAND` | `SyProductInterface_CounterpartyMand` | TField | Yes | Defines if the field defined in the COUNTERPARY.FIELD is mandatory on the user created application. |
| 12 | `SY.PI.COUNTERPARTY.FIELD` | `SyProductInterface_CounterpartyField` | TField |  | Defines the name of the field from the user created application that holds the counterparty on the deal. |
| 13 | `SY.PI.RESERVED.17` | `SyProductInterface_Reserved17` | TField |  |  |
| 14 | `SY.PI.COUNTER.PTFO.MAND` | `SyProductInterface_CounterPtfoMand` | TField | Yes | Defines if the field defined in the COUNTER.PTFO.FIELD is mandatory on the user created application. |
| 15 | `SY.PI.COUNTER.PTFO.FIELD` | `SyProductInterface_CounterPtfoField` | TField |  | Defines the name of the field from the user created application that holds the Portfolio of the counterparty. |
| 16 | `SY.PI.RESERVED.16` | `SyProductInterface_Reserved16` | TField |  |  |
| 17 | `SY.PI.DEPOSIT.MAND` | `SyProductInterface_DepositMand` | TField | Yes | Defines if the field defined in the DEPOSIT.AMT.FIELD, DEPOSIT.CCY.FIELD and ACCOUNT.FIELD are mandatory on the user created application. |
| 18 | `SY.PI.DEPOSIT.AMT.FIELD` | `SyProductInterface_DepositAmtField` | TField |  | Defines the name of the field from the user created application that holds the amount of deposit to take from the customer. |
| 19 | `SY.PI.DEPOSIT.CCY.FIELD` | `SyProductInterface_DepositCcyField` | TField |  | Defines the name of the field from the user created application that holds the currency of the depoist being taken from the customer. |
| 20 | `SY.PI.RESERVED.15` | `SyProductInterface_Reserved15` | TField |  |  |
| 21 | `SY.PI.ACCOUNT.MAND` | `SyProductInterface_AccountMand` | TField | Yes | Defines if the field defined in the ACCOUNT.FIELD is mandatory on the user created application. |
| 22 | `SY.PI.ACCOUNT.FIELD` | `SyProductInterface_AccountField` | TField |  | Defines the name of the field from the user created application that holds the Account from which a deposit may be taken. |
| 23 | `SY.PI.RESERVED.13` | `SyProductInterface_Reserved13` | TField |  |  |
| 24 | `SY.PI.TRADE.DATE.MAND` | `SyProductInterface_TradeDateMand` | TField | Yes | Defines if the field defined in the TRADE.DATE.FIELD is mandatory on the user created application. |
| 25 | `SY.PI.TRADE.DATE.FIELD` | `SyProductInterface_TradeDateField` | TField |  | Defines the name of the field from the user created application that holds the trade date to be used to create underlying deals. |
| 26 | `SY.PI.RESERVED.12` | `SyProductInterface_Reserved12` | TField |  |  |
| 27 | `SY.PI.VALUE.DATE.MAND` | `SyProductInterface_ValueDateMand` | TField | Yes | Defines if the field defined in the VALUE.DATE.FIELD is mandatory on the user created application. |
| 28 | `SY.PI.VALUE.DATE.FIELD` | `SyProductInterface_ValueDateField` | TField |  | Defines the name of the field from the user created application that holds the value date to be used to create underlying deals. |
| 29 | `SY.PI.RESERVED.11` | `SyProductInterface_Reserved11` | TField |  |  |
| 30 | `SY.PI.CURRENCY.MARKET.MAND` | `SyProductInterface_CurrencyMarketMand` | TField | Yes | Defines if the field defined in the CURRENCY.MARKET.FIELD is mandatory on the user created application. |
| 31 | `SY.PI.CURRENCY.MARKET.FIELD` | `SyProductInterface_CurrencyMarketField` | TField |  | Defines the name of the field from the user created application that holds the currency market for the the deal |
| 32 | `SY.PI.RESERVED.10` | `SyProductInterface_Reserved10` | TField |  |  |
| 33 | `SY.PI.DEALER.DESK.MAND` | `SyProductInterface_DealerDeskMand` | TField | Yes | Defines if the field defined in the DEALER.DESK.FIELD is mandatory on the user created application. |
| 34 | `SY.PI.DEALER.DESK.FIELD` | `SyProductInterface_DealerDeskField` | TField |  | Defines the name of the field from the user created application that holds the dealer desk to user for the deal. |
| 35 | `SY.PI.RESERVED.9` | `SyProductInterface_Reserved9` | TField |  |  |
| 36 | `SY.PI.ACCOUNT.OFFICER.MAND` | `SyProductInterface_AccountOfficerMand` | TField | Yes | Defines if the field defined in the ACCOUNT.OFFICER.FIELD is mandatory on the user created application. |
| 37 | `SY.PI.ACCOUNT.OFFICER.FIELD` | `SyProductInterface_AccountOfficerField` | TField |  | Defines the name of the field from the user created application that holds the Account Officer for the deal. |
| 38 | `SY.PI.RESERVED.8` | `SyProductInterface_Reserved8` | TField |  |  |
| 39 | `SY.PI.RESERVED.7` | `SyProductInterface_Reserved7` | TField |  |  |
| 40 | `SY.PI.RESERVED.6` | `SyProductInterface_Reserved6` | TField |  |  |
| 41 | `SY.PI.RESERVED.5` | `SyProductInterface_Reserved5` | TField |  |  |
| 42 | `SY.PI.RESERVED.4` | `SyProductInterface_Reserved4` | TField |  |  |
| 43 | `SY.PI.RESERVED.3` | `SyProductInterface_Reserved3` | TField |  |  |
| 44 | `SY.PI.VERSION.NEW` | `SyProductInterface_VersionNew` | TField |  | Defines the version which will be used to enter new deals in the application specified in USER.APPLICATION |
| 45 | `SY.PI.VERSION.SEE` | `SyProductInterface_VersionSee` | TField |  | Defines the version which will be used to view deals in the application specified in USER.APPLICATION |
| 46 | `SY.PI.VERSION.DELETE` | `SyProductInterface_VersionDelete` | TField |  | Defines the version which will be used to delete deals in the application specified in USER.APPLICATION |
| 47 | `SY.PI.VERSION.REVERSE` | `SyProductInterface_VersionReverse` | TField |  | Defines the version which will be used to reverse deals in the application specified in USER.APPLICATION |
| 48 | `SY.PI.VERSION.EDIT` | `SyProductInterface_VersionEdit` | TField |  | Defines the version which will be used to edit deals in the application specified in USER.APPLICATION |
| 49 | `SY.PI.VERSION.AUTH` | `SyProductInterface_VersionAuth` | TField |  | Defines the version which will be used to authorise deals in the application specified in USER.APPLICATION |
| 50 | `SY.PI.MAT.DATE.MAND` | `SyProductInterface_MatDateMand` | TField | Yes | Defines if the field defined in the MAT.DATE.FIELD field are mandatory on the user created application. |
| 51 | `SY.PI.MAT.DATE.FIELD` | `SyProductInterface_MatDateField` | TField |  | Defines the name of the field from the user created application that holds the maturity date of the Structured deal. |
| 52 | `SY.PI.RESERVED.2` | `SyProductInterface_Reserved2` | TField |  |  |
| 53 | `SY.PI.RESERVED.1` | `SyProductInterface_Reserved1` | TField |  |  |
| 54 | `SY.PI.LOCAL.REF` | `SyProductInterface_LocalRef` |  |  |  |
| 55 | `SY.PI.OVERRIDE` | `SyProductInterface_Override` |  |  |  |
| 56 | `SY.PI.RECORD.STATUS` | `SyProductInterface_RecordStatus` | String |  |  |
| 57 | `SY.PI.CURR.NO` | `SyProductInterface_CurrNo` | String |  |  |
| 58 | `SY.PI.INPUTTER` | `SyProductInterface_Inputter` |  |  |  |
| 59 | `SY.PI.DATE.TIME` | `SyProductInterface_DateTime` |  |  |  |
| 60 | `SY.PI.AUTHORISER` | `SyProductInterface_Authoriser` | String |  |  |
| 61 | `SY.PI.CO.CODE` | `SyProductInterface_CoCode` | String |  |  |
| 62 | `SY.PI.DEPT.CODE` | `SyProductInterface_DeptCode` | String |  |  |
| 63 | `SY.PI.AUDITOR.CODE` | `SyProductInterface_AuditorCode` | String |  |  |
| 64 | `SY.PI.AUDIT.DATE.TIME` | `SyProductInterface_AuditDateTime` | String |  |  |
