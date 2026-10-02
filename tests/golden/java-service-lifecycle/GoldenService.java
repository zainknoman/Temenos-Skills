package com.temenos.t24.custom.golden;
// Implements: ServiceLifecycle from EB_ServiceHook.jar
// T24 Application: CUSTOMER
// Hook type: ServiceLifecycle

import java.util.List;

import com.temenos.t24.api.complex.eb.servicehook.ServiceData;
import com.temenos.t24.api.hook.system.ServiceLifecycle;
import com.temenos.t24.api.records.customer.CustomerRecord;
import com.temenos.t24.api.system.DataAccess;

public class GoldenService extends ServiceLifecycle {

    @Override
    public List<String> getIds(ServiceData serviceData, List<String> controlList) {
        DataAccess da = new DataAccess(this);
        return da.selectRecords("", "CUSTOMER", "", "WITH SECTOR EQ '1001'");
    }

    @Override
    public void process(String id, ServiceData serviceData, String controlItem) {
        DataAccess da = new DataAccess(this);
        CustomerRecord rec = new CustomerRecord(da.getRecord("CUSTOMER", id));
        String value = rec.getSector().getValue();
        if (!"1001".equals(value)) {
            return; // changed since getIds ran
        }
        // Process the record here; raise updates through updateRecord or postUpdateRequest.
    }
}
