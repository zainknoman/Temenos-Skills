*-----------------------------------------------------------------------------
* Program    : GOLDEN.JBC.PARAMETER.FIELDS
* Type       : TEMPLATE .FIELDS
* Description: Golden case
* Application: GOLDEN.JBC.PARAMETER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.JBC.PARAMETER.FIELDS
    $USING EB.Template
    $USING EB.SystemTables

    EB.Template.TableDefineid('@ID', EB.Template.T24String)
    EB.SystemTables.setIdN('20')

    EB.Template.TableAddfielddefinition('DESCRIPTION', '35', 'A', '')
    EB.Template.TableAddfield('RESERVED.3', EB.Template.T24String, EB.Template.FieldNoInput, '')
    EB.Template.TableAddfield('RESERVED.2', EB.Template.T24String, EB.Template.FieldNoInput, '')
    EB.Template.TableAddfield('RESERVED.1', EB.Template.T24String, EB.Template.FieldNoInput, '')

    EB.Template.TableSetauditposition()
RETURN
END
