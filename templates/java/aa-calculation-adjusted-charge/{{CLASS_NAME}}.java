package {{JAVA_PACKAGE}};
// Implements: Calculation from AA_CalculationHook.jar
// T24 Application: {{APP}}
// Hook type: Calculation.getAdjustedChargeAmount

import java.math.BigDecimal;
import java.math.RoundingMode;

import com.temenos.api.TDate;
import com.temenos.api.TNumber;
import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.complex.aa.calculationhook.ChargeAdjustment;
import com.temenos.t24.api.complex.aa.calculationhook.ChargeCalculationContext;
import com.temenos.t24.api.hook.arrangement.Calculation;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaprddescharge.AaPrdDesChargeRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;

public class {{CLASS_NAME}} extends Calculation {

    @Override
    public ChargeAdjustment getAdjustedChargeAmount(TDate effectiveDate, String chargeProperty,
            String chargeType, AaPrdDesChargeRecord chargePropertyRecord, TNumber chargeAmount,
            TDate periodStart, TDate periodEnd, String sourceType, String sourceBalance,
            AaAccountDetailsRecord accountDetailRecord, AaArrangementActivityRecord arrangementActivityRecord,
            ArrangementContext arrangementContext, AaArrangementRecord arrangementRecord,
            TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
            AaArrangementActivityRecord masterActivityRecord, ChargeCalculationContext chargeCalculationContext) {

        String amount = chargeAmount.toString();
        BigDecimal charge = new BigDecimal(amount.isEmpty() ? "0" : amount);
        BigDecimal waived = charge.multiply(new BigDecimal("{{WAIVE_PERCENT}}"))
                .divide(new BigDecimal("100"), 2, RoundingMode.HALF_UP);
        ChargeAdjustment adjustment = new ChargeAdjustment();
        adjustment.setAmount(chargeAmount);
        adjustment.setAdjustedAmount(new TNumber(charge.subtract(waived).toPlainString()));
        adjustment.setReason("{{REASON}}");
        return adjustment;
    }
}
