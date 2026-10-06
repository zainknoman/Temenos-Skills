*-----------------------------------------------------------------------------
* Program    : V.GOLDEN.CHECK.REC
* Type       : CHECK.REC.RTN
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE V.GOLDEN.CHECK.REC
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.CUSTOMER

    IF R.NEW(EB.CUS.SECTOR) EQ '' THEN
        R.NEW(EB.CUS.SECTOR) = '1001'
    END
    RETURN
END
