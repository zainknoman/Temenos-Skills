*-----------------------------------------------------------------------------
* Program    : V.GOLDEN.ID.RTN
* Type       : ID.RTN
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE V.GOLDEN.ID.RTN
    $INSERT I_COMMON
    $INSERT I_EQUATE

    Y.ID = ID.NEW
    IF Y.ID EQ '' THEN RETURN
    IF Y.ID[1, LEN('SMP')] NE 'SMP' THEN
        E = 'ID MUST START WITH SMP'
    END
    RETURN
END
