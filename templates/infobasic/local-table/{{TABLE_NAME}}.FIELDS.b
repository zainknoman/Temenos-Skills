*-----------------------------------------------------------------------------
* Program    : {{TABLE_NAME}}.FIELDS
* Type       : TEMPLATE .FIELDS
* Description: {{DESCRIPTION}}
* Application: {{TABLE_NAME}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
    SUBROUTINE {{TABLE_NAME}}.FIELDS
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_DataTypes

    CALL Table.defineId('ID', T24_String)
    ID.N = '{{ID_LENGTH}}'

    CALL Table.addFieldDefinition('{{FIELD_NAME}}', '{{FIELD_LENGTH}}', 'A', '')
    CALL Table.addReservedField('RESERVED.3')
    CALL Table.addReservedField('RESERVED.2')
    CALL Table.addReservedField('RESERVED.1')

    CALL Table.setAuditPosition
    RETURN
END
