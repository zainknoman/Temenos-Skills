*-----------------------------------------------------------------------------
* Program    : GOLDEN.PARAMETER.FIELDS
* Type       : TEMPLATE .FIELDS
* Description: Golden case
* Application: GOLDEN.PARAMETER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE GOLDEN.PARAMETER.FIELDS
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_DataTypes

    CALL Table.defineId('ID', T24_String)
    ID.N = '20'

    CALL Table.addFieldDefinition('DESCRIPTION', '35', 'A', '')
    CALL Table.addReservedField('RESERVED.3')
    CALL Table.addReservedField('RESERVED.2')
    CALL Table.addReservedField('RESERVED.1')

    CALL Table.setAuditPosition
    RETURN
END
