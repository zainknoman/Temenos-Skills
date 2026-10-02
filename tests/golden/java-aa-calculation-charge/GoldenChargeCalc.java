package com.temenos.t24.custom.golden;
// Implements: Calculation from AA_CalculationHook.jar
// T24 Application: AA.ARRANGEMENT.ACTIVITY
// Hook type: Calculation.getChargeAmount

import java.math.BigDecimal;
import java.math.RoundingMode;

import com.temenos.api.TNumber;
import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.complex.aa.calculationhook.ChargeCalculationContext;
import com.temenos.t24.api.hook.arrangement.Calculation;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;

public class GoldenChargeCalc extends Calculation {

    @Override
    public TNumber getChargeAmount(String chargePropertyId, AaPrdDesChargeRecord chargePropertyRecord,
            TNumber baseAmount, AaAccountDetailsRecord accountDetailRecord,
            AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
            AaArrangementRecord arrangementRecord, TStructure productPropertyRecord,
            AaProductCatalogRecord productRecord, TStructure record,
            AaArrangementActivityRecord masterActivityRecord, ChargeCalculationContext chargeCalculationContext) {

        BigDecimal base = new BigDecimal(baseAmount.toString().isEmpty() ? "0" : baseAmount.toString());
        BigDecimal charge = base.multiply(new BigDecimal("1.5"))
                .divide(new BigDecimal("100"), 2, RoundingMode.HALF_UP);
        BigDecimal minimum = new BigDecimal("10");
        return new TNumber(charge.max(minimum).toPlainString());
    }
}
