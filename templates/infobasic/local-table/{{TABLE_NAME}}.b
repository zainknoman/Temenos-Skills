*-----------------------------------------------------------------------------
* Program    : {{TABLE_NAME}}
* Type       : TEMPLATE
* Description: {{DESCRIPTION}}
* Application: {{TABLE_NAME}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{TABLE_NAME}}
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_Table

    Table.name = '{{TABLE_NAME}}'
    Table.title = '{{TITLE}}'
    Table.stereotype = 'H'
    Table.product = '{{PRODUCT}}'
    Table.subProduct = ''
    Table.classification = 'INT'
    Table.systemClearFile = 'Y'
    Table.relatedFiles = ''
    Table.isPostClosingFile = ''
    Table.equatePrefix = '{{EQUATE_PREFIX}}'
    Table.idPrefix = ''
    Table.blockedFunctions = ''
    Table.trigger = ''
    RETURN
END
