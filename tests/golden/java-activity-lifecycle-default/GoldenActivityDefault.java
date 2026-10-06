package com.temenos.t24.custom.golden;
// Implements: ActivityLifecycle from AA_ActivityHook.jar
// T24 Application: AA.ARRANGEMENT.ACTIVITY
// Hook type: ActivityLifecycle.defaultFieldValues

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.hook.arrangement.ActivityLifecycle;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;

public class GoldenActivityDefault extends ActivityLifecycle {

    @Override
    public void defaultFieldValues(AaAccountDetailsRecord accountDetailRecord,
            AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
            AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
            TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record) {

        String value = arrangementActivityRecord.getActivity().getValue();
        if (value == null || value.isEmpty()) {
            arrangementActivityRecord.setActivity("SAMPLE");
        }
    }
}
