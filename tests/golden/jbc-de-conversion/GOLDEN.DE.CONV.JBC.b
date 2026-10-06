*-----------------------------------------------------------------------------
* Program    : GOLDEN.DE.CONV.JBC
* Type       : DE CONVERSION
* Description: Golden case
* Application: ACCOUNT
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.DE.CONV.JBC(inValue, headerRec, mvNo, outValue, errorMsg)
    $USING AC.AccountOpening

    outValue = ''
    errorMsg = ''
    IF inValue EQ '' THEN RETURN
    readErr = ''
    record = AC.AccountOpening.Account.Read(inValue, readErr)
    IF readErr EQ '' THEN
        outValue = record<AC.AccountOpening.Account.Currency>
    END
RETURN
END
