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
$PACKAGE {{PACKAGE}}
SUBROUTINE {{TABLE_NAME}}.FIELDS
    $USING EB.Template
    $USING EB.SystemTables

    EB.Template.TableDefineid('@ID', EB.Template.T24String)
    EB.SystemTables.setIdN('{{ID_LENGTH}}')

    EB.Template.TableAddfielddefinition('{{FIELD_NAME}}', '{{FIELD_LENGTH}}', 'A', '')
    EB.Template.TableAddfield('RESERVED.3', EB.Template.T24String, EB.Template.FieldNoInput, '')
    EB.Template.TableAddfield('RESERVED.2', EB.Template.T24String, EB.Template.FieldNoInput, '')
    EB.Template.TableAddfield('RESERVED.1', EB.Template.T24String, EB.Template.FieldNoInput, '')

    EB.Template.TableSetauditposition()
RETURN
END
