*-----------------------------------------------------------------------------
* Program    : GOLDEN.INITIALISE
* Type       : INITIALISE
* Description: Golden case
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.INITIALISE
    $USING ST.CompanyCreation

    PUTENV('OFS_SOURCE=TEST.OFS')
    CALL JF.INITIALISE.CONNECTION
    ST.CompanyCreation.LoadCompany('GB0010001')
RETURN
END
