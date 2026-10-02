package {{JAVA_PACKAGE}};
// Implements: ServiceLifecycle from EB_ServiceHook.jar
// T24 Application: {{APP}}
// Hook type: ServiceLifecycle

import java.util.List;

import com.temenos.t24.api.complex.eb.servicehook.ServiceData;
import com.temenos.t24.api.hook.system.ServiceLifecycle;
import com.temenos.t24.api.records.{{RECORD_PACKAGE}}.{{RECORD_CLASS}}Record;
import com.temenos.t24.api.system.DataAccess;

public class {{CLASS_NAME}} extends ServiceLifecycle {

    @Override
    public List<String> getIds(ServiceData serviceData, List<String> controlList) {
        DataAccess da = new DataAccess(this);
        return da.selectRecords("", "{{APP}}", "", "WITH {{FIELD_NAME}} EQ '{{SELECT_VALUE}}'");
    }

    @Override
    public void process(String id, ServiceData serviceData, String controlItem) {
        DataAccess da = new DataAccess(this);
        {{RECORD_CLASS}}Record rec = new {{RECORD_CLASS}}Record(da.getRecord("{{APP}}", id));
        String value = rec.get{{FIELD}}().getValue();
        if (!"{{SELECT_VALUE}}".equals(value)) {
            return; // changed since getIds ran
        }
        // Process the record here; raise updates through updateRecord or postUpdateRequest.
    }
}
