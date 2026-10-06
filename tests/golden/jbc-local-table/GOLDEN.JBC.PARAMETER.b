*-----------------------------------------------------------------------------
* Program    : GOLDEN.JBC.PARAMETER
* Type       : TEMPLATE
* Description: Golden case
* Application: GOLDEN.JBC.PARAMETER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.JBC.PARAMETER
    $USING EB.Template

    EB.Template.setTableName('GOLDEN.JBC.PARAMETER')
    EB.Template.setTableTitle('Golden parameter')
    EB.Template.setTableStereotype('H')
    EB.Template.setTableProduct('EB')
    EB.Template.setTableSubproduct('')
    EB.Template.setTableClassification('INT')
    EB.Template.setTableSystemclearfile('Y')
    EB.Template.setTableRelatedfiles('')
    EB.Template.setTableIspostclosingfile('')
    EB.Template.setTableEquateprefix('GOLDEN.JPRM')
    EB.Template.setTableIdprefix('')
    EB.Template.setTableBlockedfunctions('')
RETURN
END
