*-----------------------------------------------------------------------------
* Program    : GOLDEN.ID.RTN
* Type       : ID.RTN
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.ID.RTN
    $USING EB.SystemTables

    recordId = EB.SystemTables.getIdNew()
    IF recordId EQ '' THEN RETURN
    IF recordId[1, LEN('SMP')] NE 'SMP' THEN
        EB.SystemTables.setE('ID MUST START WITH SMP')
    END
RETURN
END
