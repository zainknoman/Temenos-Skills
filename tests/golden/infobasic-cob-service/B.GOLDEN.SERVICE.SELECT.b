*-----------------------------------------------------------------------------
* Program    : B.GOLDEN.SERVICE
* Type       : BATCH .SELECT
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE B.GOLDEN.SERVICE.SELECT
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_B.GOLDEN.SERVICE.COMMON

    SEL.CMD = 'SELECT ':FN.APP:' WITH SECTOR EQ ':DQUOTE('1001')
    SEL.LIST = ''
    NO.OF.REC = ''
    SEL.ERR = ''
    CALL EB.READLIST(SEL.CMD, SEL.LIST, '', NO.OF.REC, SEL.ERR)
    CALL BATCH.BUILD.LIST('', SEL.LIST)
    RETURN
END
