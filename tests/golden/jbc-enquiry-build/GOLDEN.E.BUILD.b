*-----------------------------------------------------------------------------
* Program    : GOLDEN.E.BUILD
* Type       : ENQUIRY BUILD.ROUTINE
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.E.BUILD(enqData)

    enqData<2,-1> = 'SECTOR'
    enqData<3,-1> = 'EQ'
    enqData<4,-1> = '1001'
RETURN
END
