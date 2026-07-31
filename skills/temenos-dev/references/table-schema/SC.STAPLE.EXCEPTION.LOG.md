# SC.STAPLE.EXCEPTION.LOG — Table Schema

> Source: `INSERTS/I_F.SC.STAPLE.EXCEPTION.LOG` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SLE.PARENT.SECURITY` | `ScStapleExceptionLog_ParentSecurity` | TField |  | This field holds the parent stapled security |
| 2 | `SC.SLE.PROCESSED.PORTFOLIO` | `ScStapleExceptionLog_ProcessedPortfolio` |  |  |  |
| 3 | `SC.SLE.EXCLUDED.PORTFOLIO` | `ScStapleExceptionLog_ExcludedPortfolio` |  |  |  |
| 4 | `SC.SLE.SKIPPED.PORTFOLIO` | `ScStapleExceptionLog_SkippedPortfolio` |  |  |  |
| 5 | `SC.SLE.REASON` | `ScStapleExceptionLog_Reason` |  |  |  |
| 6 | `SC.SLE.CHILD.SECURITY` | `ScStapleExceptionLog_ChildSecurity` |  |  |  |
| 7 | `SC.SLE.NOMINAL` | `ScStapleExceptionLog_Nominal` |  |  |  |
| 8 | `SC.SLE.LOCAL.REF` | `ScStapleExceptionLog_LocalRef` |  |  |  |
| 9 | `SC.SLE.OVERRIDE` | `ScStapleExceptionLog_Override` |  |  |  |
