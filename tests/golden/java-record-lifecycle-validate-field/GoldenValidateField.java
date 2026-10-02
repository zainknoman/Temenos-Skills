package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: CUSTOMER
// Hook type: RecordLifecycle.validateField (deprecated)

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.customer.CustomerRecord;

public class GoldenValidateField extends RecordLifecycle {

    @Override
    public TValidationResponse validateField(String application, String recordId, String fieldData,
            TStructure record) {

        CustomerRecord rec = new CustomerRecord(record);
        if (fieldData == null || fieldData.isEmpty()) {
            rec.getSector().setError("SECTOR IS MANDATORY");
        }
        return rec.getValidationResponse();
    }
}
