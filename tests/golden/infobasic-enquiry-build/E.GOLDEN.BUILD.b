*-----------------------------------------------------------------------------
* Program    : E.GOLDEN.BUILD
* Type       : ENQUIRY BUILD.ROUTINE
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE E.GOLDEN.BUILD(ENQ.DATA)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_ENQUIRY.COMMON

    ENQ.DATA<2,-1> = 'SECTOR'
    ENQ.DATA<3,-1> = 'EQ'
    ENQ.DATA<4,-1> = '1001'
    RETURN
END
