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
    $USING EB.Template

    EB.Template.setTableName('{{TABLE_NAME}}')
    EB.Template.setTableTitle('{{TITLE}}')
    EB.Template.setTableStereotype('H')
    EB.Template.setTableProduct('{{PRODUCT}}')
    EB.Template.setTableSubproduct('')
    EB.Template.setTableClassification('INT')
    EB.Template.setTableSystemclearfile('Y')
    EB.Template.setTableRelatedfiles('')
    EB.Template.setTableIspostclosingfile('')
    EB.Template.setTableEquateprefix('{{EQUATE_PREFIX}}')
    EB.Template.setTableIdprefix('')
    EB.Template.setTableBlockedfunctions('')
RETURN
END
