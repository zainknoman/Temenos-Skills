*-----------------------------------------------------------------------------
* Program    : GOLDEN.PARAMETER
* Type       : TEMPLATE
* Description: Golden case
* Application: GOLDEN.PARAMETER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
    SUBROUTINE GOLDEN.PARAMETER
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_Table

    Table.name = 'GOLDEN.PARAMETER'
    Table.title = 'Golden parameter'
    Table.stereotype = 'H'
    Table.product = 'EB'
    Table.subProduct = ''
    Table.classification = 'INT'
    Table.systemClearFile = 'Y'
    Table.relatedFiles = ''
    Table.isPostClosingFile = ''
    Table.equatePrefix = 'GOLDEN.PRM'
    Table.idPrefix = ''
    Table.blockedFunctions = ''
    Table.triggerField = ''
    RETURN
END
