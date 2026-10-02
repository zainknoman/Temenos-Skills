package {{JAVA_PACKAGE}};
// Implements: Enquiry from EB_EnquiryHook.jar
// T24 Application: {{APP}}
// Hook type: Enquiry.setIds (NOFILE)

import java.util.ArrayList;
import java.util.List;

import com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext;
import com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria;
import com.temenos.t24.api.hook.system.Enquiry;
import com.temenos.t24.api.system.DataAccess;

public class {{CLASS_NAME}} extends Enquiry {

    @Override
    public List<String> setIds(List<FilterCriteria> filterCriteria, EnquiryContext enquiryContext) {
        String selectValue = "";
        for (FilterCriteria criteria : filterCriteria) {
            if ("{{FIELD_NAME}}".equals(criteria.getFieldname())) {
                selectValue = criteria.getValue();
            }
        }
        if (selectValue == null || selectValue.isEmpty()) {
            return new ArrayList<>();
        }
        DataAccess da = new DataAccess(this);
        return da.selectRecords("", "{{APP}}", "", "WITH {{FIELD_NAME}} EQ '" + selectValue + "'");
    }
}
