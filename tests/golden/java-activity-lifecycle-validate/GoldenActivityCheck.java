package com.temenos.t24.custom.golden;
// Implements: ActivityLifecycle from AA_ActivityHook.jar
// T24 Application: AA.ARRANGEMENT.ACTIVITY
// Hook type: ActivityLifecycle.validateRecord

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.hook.arrangement.ActivityLifecycle;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;

public class GoldenActivityCheck extends ActivityLifecycle {

    @Override
    public TValidationResponse validateRecord(AaAccountDetailsRecord accountDetailRecord,
            AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
            AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
            TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record) {

        String value = arrangementActivityRecord.getEffectiveDate().getValue();
        if (value == null || value.isEmpty()) {
            arrangementActivityRecord.getEffectiveDate().setError("EFFECTIVE DATE IS MANDATORY");
        }
        return arrangementActivityRecord.getValidationResponse();
    }
}
