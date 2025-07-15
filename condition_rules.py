condition_rules = [
    # Starting Issues
     {
    "conditions": ["engine won't crank", "cold", "slow cranking"],
    "bullets": [
        "- Condition: engine won't crank + cold + slow cranking",
        "- Likely Issue: reduced battery performance due to cold weather",
        "- Related Issue: battery issues / starting system",
        "- Suggestion: check battery voltage and terminals; use winter-grade oil; inspect belts for wear or slipping"
    ]
},
{
    "conditions": ["auto start stop not working", "traffic", "battery okay"],
    "bullets": [
        "- Condition: auto start-stop not working + in traffic + battery healthy",
        "- Likely Issue: brake switch, temperature sensor, or ECU logic preventing start-stop",
        "- Related Issue: Start-Stop System Malfunction",
        "- Suggestion: scan BCM faults; test brake sensor and ambient temperature inputs"
    ]
},
{
    "conditions": ["slow acceleration", "low rpm", "turbo engine"],
    "bullets": [
        "- Condition: slow acceleration + low rpm + turbo engine",
        "- Likely Issue: turbo lag or boost leak",
        "- Related Issue: Turbocharger Lag or Hesitation",
        "- Suggestion: inspect boost hoses, turbo actuator, and MAF sensor"
    ]
},
{
    "conditions": ["boost loss", "check engine light", "whistling noise", "cel"],
    "bullets": [
        "- Condition: boost loss + check engine light + whistling noise",
        "- Likely Issue: turbo leak or wastegate malfunction",
        "- Related Issue: Turbocharger Lag or Hesitation",
        "- Suggestion: inspect turbo piping; run OBD scan for boost-related codes (e.g., P0299)"
    ]
},
{
    "conditions": ["rattling", "cold start", "timing codes"],
    "bullets": [
        "- Condition: rattling noise on cold start + timing codes present",
        "- Likely Issue: stuck VVT actuator or solenoid",
        "- Related Issue: VVT System Failure",
        "- Suggestion: check oil condition; inspect VVT solenoid; scan for camshaft timing errors"
    ]
},
{
    "conditions": ["engine won't crank", "no crank"],
    "bullets": [
        "- Condition: engine won't crank + no crank",
        "- Likely Issue: dead or faulty battery or starter motor issue",
        "- Related Issue: battery and starting system",
        "- Suggestion: test battery and starter motor; check battery connections"
    ]
},
{
    "conditions": ["oil level rising", "fuel smell", "short trips"],
    "bullets": [
        "- Condition: oil level increasing + fuel smell in oil + frequent short trips",
        "- Likely Issue: oil dilution due to unburned fuel",
        "- Related Issue: Oil Dilution in Turbocharged Engines",
        "- Suggestion: change oil frequently; avoid short trips; scan for rich mixture codes"
    ]
},
{
    "conditions": ["shakes", "in drive", "no warning light", "no cel"],
    "bullets": [
        "- Condition: engine shakes + in drive + no warning light",
        "- Likely Issue: worn engine mounts",
        "- Related Issue: engine shakes at idle",
        "- Suggestion: inspect engine and transmission mounts"
    ]
},
{
    "conditions": ["shakes", "check engine light", "rough idle", "cel"],
    "bullets": [
        "- Condition: engine shakes + check engine light + rough idle",
        "- Likely Issue: ignition misfire or fuel injector problems",
        "- Related Issue: ignition system maintenance",
        "- Suggestion: inspect spark plugs, ignition coils, and fuel injectors"
    ]
},
{
    "conditions": ["rough idle", "gdi engine", "misfires"],
    "bullets": [
        "- Condition: rough idle + GDI engine + misfires",
        "- Likely Issue: carbon buildup on intake valves",
        "- Related Issue: GDI Carbon Buildup",
        "- Suggestion: inspect intake valves with borescope; clean using walnut blasting"
    ]
},
{
    "conditions": ["engine overheats", "hot weather", "ac on"],
    "bullets": [
        "- Condition: engine overheats + hot weather + A/C on",
        "- Likely Issue: cooling system overloaded or faulty fan",
        "- Related Issue: engine overheating",
        "- Suggestion: check coolant level; verify fan operation; test thermostat"
    ]
},
{
    "conditions": ["engine overheats", "coolant full", "fan not working"],
    "bullets": [
        "- Condition: engine overheats + coolant full + fan not working",
        "- Likely Issue: fan motor or relay failure",
        "- Related Issue: engine overheating",
        "- Suggestion: test and repair fan motor and relays"
    ]
},
{
    "conditions": ["hybrid", "fan noise", "battery warning"],
    "bullets": [
        "- Condition: hybrid vehicle + loud battery cooling fan + battery warning light",
        "- Likely Issue: clogged or faulty hybrid battery cooling fan",
        "- Related Issue: Hybrid Battery Cooling Fan Blocked",
        "- Suggestion: clean intake duct; inspect fan and temperature sensors; scan for cooling system DTCs"
    ]
},
{
    "conditions": ["rainy", "brakes squeak", "rust"],
    "bullets": [
        "- Condition: rainy weather + brakes squeak + visible rust",
        "- Likely Issue: surface rust on brake discs",
        "- Related Issue: disc brakes",
        "- Suggestion: drive normally to clean rust; inspect brake pads if noise persists"
    ]
},
{
    "conditions": ["brake pedal goes to floor", "low fluid"],
    "bullets": [
        "- Condition: brake pedal goes to floor + low fluid",
        "- Likely Issue: brake fluid leak or air in lines",
        "- Related Issue: braking system",
        "- Suggestion: inspect for leaks; bleed brake lines"
    ]
},
{
    "conditions": ["hybrid", "regen braking not working", "brake warning"],
    "bullets": [
        "- Condition: hybrid vehicle + regen braking not working + brake warning light",
        "- Likely Issue: brake booster sensor or ABS module fault affecting regen",
        "- Related Issue: Hybrid Brake Regeneration Fault",
        "- Suggestion: check ABS and hybrid system codes; inspect brake sensors and fluid condition"
    ]
},
{
    "conditions": ["power steering hard", "noisy steering"],
    "bullets": [
        "- Condition: hard or noisy steering",
        "- Likely Issue: low power steering fluid or leak",
        "- Related Issue: power steering fluid",
        "- Suggestion: check power steering fluid reservoir and inspect for leaks"
    ]
},
{
    "conditions": ["wheel noise", "rough rotation"],
    "bullets": [
        "- Condition: wheel noise or rough rotation",
        "- Likely Issue: deteriorated wheel bearing grease",
        "- Related Issue: wheel bearing grease",
        "- Suggestion: re-grease or replace bearings as needed"
    ]
},
{
    "conditions": ["knocking", "suspension", "turning"],
    "bullets": [
        "- Condition: knocking noise while turning",
        "- Likely Issue: worn ball joints or bushings",
        "- Related Issue: suspension and shock absorbers",
        "- Suggestion: inspect and replace worn suspension components"
    ]
},
{
    "conditions": ["squeaking", "start", "engine"],
    "bullets": [
        "- Condition: squeaking noise when starting engine",
        "- Likely Issue: worn or loose serpentine belt, faulty belt tensioner, or starter motor noise",
        "- Related Issue: belt wear, starting system, accessory components",
        "- Suggestion: inspect serpentine belt and tensioner for wear and alignment; check starter motor operation; clean belts if contaminated",
        "- Temporary Fix: apply belt dressing spray; avoid high RPM cranking until fixed"
    ]
},

{
    "conditions": ["P0171", "system too lean bank 1", "vacuum leak", "maf sensor"],
    "bullets": [
        "- Code: P0171",
        "- Description: System Too Lean (Bank 1)",
        "- Symptoms: Check engine light, rough idle, poor acceleration",
        "- Possible Causes: vacuum leaks, faulty fuel injectors, dirty MAF sensor",
        "- Suggested Fixes: inspect and repair vacuum leaks; clean or replace MAF sensor; check fuel injectors"
    ]
},

{
    "conditions": ["P0174", "system too lean bank 2", "vacuum leak", "oxygen sensor"],
    "bullets": [
        "- Code: P0174",
        "- Description: System Too Lean (Bank 2)",
        "- Symptoms: Check engine light, rough idle, poor engine performance",
        "- Possible Causes: vacuum leaks, faulty oxygen sensor, clogged fuel filter",
        "- Suggested Fixes: check and repair vacuum leaks; replace faulty O2 sensor; replace fuel filter"
    ]
},

{
    "conditions": ["P0420", "catalytic converter efficiency", "oxygen sensor"],
    "bullets": [
        "- Code: P0420",
        "- Description: Catalyst System Efficiency Below Threshold (Bank 1)",
        "- Symptoms: Check engine light, poor fuel economy, increased emissions",
        "- Possible Causes: faulty catalytic converter, damaged oxygen sensors",
        "- Suggested Fixes: inspect catalytic converter; replace oxygen sensors if needed"
    ]
},

{
    "conditions": ["P0430", "catalytic converter efficiency", "oxygen sensor"],
    "bullets": [
        "- Code: P0430",
        "- Description: Catalyst System Efficiency Below Threshold (Bank 2)",
        "- Symptoms: Check engine light, failed emissions test",
        "- Possible Causes: failing catalytic converter, bad oxygen sensor",
        "- Suggested Fixes: replace catalytic converter or oxygen sensor as necessary"
    ]
},

{
    "conditions": ["P0133", "oxygen sensor slow response", "bank 1 sensor 1"],
    "bullets": [
        "- Code: P0133",
        "- Description: O2 Sensor Circuit Slow Response (Bank 1 Sensor 1)",
        "- Symptoms: Poor engine performance, increased fuel consumption",
        "- Possible Causes: faulty oxygen sensor, wiring issues",
        "- Suggested Fixes: replace oxygen sensor; check wiring and connectors"
    ]
},

{
    "conditions": ["P0135", "oxygen sensor heater", "bank 1 sensor 1"],
    "bullets": [
        "- Code: P0135",
        "- Description: O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)",
        "- Symptoms: Check engine light, rough idle",
        "- Possible Causes: faulty heater element in O2 sensor, blown fuse",
        "- Suggested Fixes: replace O2 sensor; check related fuses and wiring"
    ]
},

{
    "conditions": ["P0141", "oxygen sensor heater", "bank 1 sensor 2"],
    "bullets": [
        "- Code: P0141",
        "- Description: O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 2)",
        "- Symptoms: Check engine light, poor engine performance",
        "- Possible Causes: failed heater in oxygen sensor, wiring problems",
        "- Suggested Fixes: replace oxygen sensor; inspect wiring harness"
    ]
},

{
    "conditions": ["P0455", "evaporative emission large leak", "fuel odor"],
    "bullets": [
        "- Code: P0455",
        "- Description: Evaporative Emission System Leak Detected (Large Leak)",
        "- Symptoms: Check engine light, fuel odor near vehicle",
        "- Possible Causes: loose or damaged gas cap, cracked EVAP hose",
        "- Suggested Fixes: tighten or replace gas cap; inspect and repair EVAP system hoses"
    ]
},

{
    "conditions": ["P0442", "evaporative emission small leak", "check engine light"],
    "bullets": [
        "- Code: P0442",
        "- Description: Evaporative Emission System Leak Detected (Small Leak)",
        "- Symptoms: Check engine light",
        "- Possible Causes: faulty gas cap, small crack in EVAP system",
        "- Suggested Fixes: replace gas cap; inspect and fix EVAP system leaks"
    ]
},

{
    "conditions": ["P0113", "intake air temperature sensor", "circuit high input"],
    "bullets": [
        "- Code: P0113",
        "- Description: Intake Air Temperature Sensor 1 Circuit High Input",
        "- Symptoms: Poor engine performance, rough idle",
        "- Possible Causes: faulty intake air temperature sensor, wiring issues",
        "- Suggested Fixes: replace sensor; check wiring and connectors"
    ]
},

{
    "conditions": ["P0117", "engine coolant temperature sensor", "circuit low input"],
    "bullets": [
        "- Code: P0117",
        "- Description: Engine Coolant Temperature Sensor Circuit Low Input",
        "- Symptoms: Engine overheating, poor fuel economy",
        "- Possible Causes: faulty coolant temperature sensor, wiring fault",
        "- Suggested Fixes: replace coolant temp sensor; inspect wiring"
    ]
},
{
    "conditions": ["P0118", "engine coolant temperature sensor", "high input"],
    "bullets": [
        "- Code: P0118",
        "- Description: Engine Coolant Temperature Sensor Circuit High Input",
        "- Symptoms: Engine overheating, poor heater performance",
        "- Possible Causes: Faulty coolant temperature sensor, wiring issues or shorts",
        "- Suggested Fixes: Replace coolant temperature sensor; inspect and repair wiring"
    ]
},
{
    "conditions": ["P0128", "coolant thermostat", "temperature below regulating"],
    "bullets": [
        "- Code: P0128",
        "- Description: Coolant Thermostat (Coolant Temperature Below Thermostat Regulating Temperature)",
        "- Symptoms: Engine takes longer to warm up, heater not working well",
        "- Possible Causes: Stuck open thermostat",
        "- Suggested Fixes: Replace thermostat"
    ]
},
{
    "conditions": ["P0120", "throttle position sensor malfunction", "TPS circuit"],
    "bullets": [
        "- Code: P0120",
        "- Description: Throttle/Pedal Position Sensor/Switch 'A' Circuit Malfunction",
        "- Symptoms: Reduced power, poor acceleration",
        "- Possible Causes: Faulty throttle position sensor, wiring faults or connectors",
        "- Suggested Fixes: Replace throttle position sensor; check wiring and connectors"
    ]
},
{
    "conditions": ["P0121", "throttle position sensor performance", "TPS range problem"],
    "bullets": [
        "- Code: P0121",
        "- Description: Throttle/Pedal Position Sensor/Switch 'A' Circuit Range/Performance Problem",
        "- Symptoms: Engine hesitation, rough idle",
        "- Possible Causes: Faulty sensor or connector, dirty throttle body",
        "- Suggested Fixes: Clean throttle body; replace sensor if needed"
    ]
},
{
    "conditions": ["P0122", "throttle position sensor low input", "TPS circuit low"],
    "bullets": [
        "- Code: P0122",
        "- Description: Throttle/Pedal Position Sensor/Switch 'A' Circuit Low Input",
        "- Symptoms: Reduced power, engine stalling",
        "- Possible Causes: Faulty sensor, wiring short or damaged connector",
        "- Suggested Fixes: Replace sensor; inspect wiring harness"
    ]
},
{
    "conditions": ["P0123", "throttle position sensor high input", "TPS circuit high"],
    "bullets": [
        "- Code: P0123",
        "- Description: Throttle/Pedal Position Sensor/Switch 'A' Circuit High Input",
        "- Symptoms: Poor throttle response",
        "- Possible Causes: Faulty sensor, wiring open circuit or connector issues",
        "- Suggested Fixes: Replace sensor; check wiring and connectors"
    ]
},
{
    "conditions": ["P0130", "oxygen sensor malfunction", "bank 1 sensor 1"],
    "bullets": [
        "- Code: P0130",
        "- Description: O2 Sensor Circuit Malfunction (Bank 1 Sensor 1)",
        "- Symptoms: Check engine light, poor fuel economy",
        "- Possible Causes: Faulty oxygen sensor, wiring faults",
        "- Suggested Fixes: Replace oxygen sensor; inspect wiring harness"
    ]
},
{
    "conditions": ["P0146", "oxygen sensor malfunction", "bank 1 sensor 3"],
    "bullets": [
        "- Code: P0146",
        "- Description: O2 Sensor Circuit Malfunction (Bank 1 Sensor 3)",
        "- Symptoms: Poor engine performance, increased emissions",
        "- Possible Causes: Faulty oxygen sensor, wiring damage",
        "- Suggested Fixes: Replace sensor; inspect wiring harness"
    ]
},
{
    "conditions": ["P0138", "oxygen sensor high voltage", "bank 1 sensor 2"],
    "bullets": [
        "- Code: P0138",
        "- Description: O2 Sensor Circuit High Voltage (Bank 1 Sensor 2)",
        "- Symptoms: Rough idle, poor fuel economy",
        "- Possible Causes: Faulty oxygen sensor, wiring shorts",
        "- Suggested Fixes: Replace sensor; inspect wiring"
    ]
},
{
    "conditions": ["P0139", "oxygen sensor slow response", "bank 1 sensor 2"],
    "bullets": [
        "- Code: P0139",
        "- Description: O2 Sensor Circuit Slow Response (Bank 1 Sensor 2)",
        "- Symptoms: Check engine light, poor fuel economy, rough idle",
        "- Possible Causes: Faulty oxygen sensor, wiring issues, exhaust leaks",
        "- Suggested Fixes: Inspect and replace oxygen sensor if faulty; check wiring and connectors"
    ]
},
{
    "conditions": ["P0401", "EGR flow insufficient", "exhaust gas recirculation"],
    "bullets": [
        "- Code: P0401",
        "- Description: Exhaust Gas Recirculation (EGR) Flow Insufficient Detected",
        "- Symptoms: Check engine light, rough idle, increased emissions",
        "- Possible Causes: Clogged or faulty EGR valve, vacuum leaks",
        "- Suggested Fixes: Clean or replace EGR valve; inspect vacuum lines"
    ]
},
{
    "conditions": ["P0402", "EGR flow excessive", "exhaust gas recirculation"],
    "bullets": [
        "- Code: P0402",
        "- Description: Exhaust Gas Recirculation (EGR) Flow Excessive Detected",
        "- Symptoms: Rough idle, engine knocking, check engine light",
        "- Possible Causes: Stuck open or faulty EGR valve",
        "- Suggested Fixes: Inspect and replace EGR valve as necessary"
    ]
},
{
    "conditions": ["P0410", "secondary air injection malfunction"],
    "bullets": [
        "- Code: P0410",
        "- Description: Secondary Air Injection System Malfunction",
        "- Symptoms: Check engine light, failed emissions test, engine hesitation",
        "- Possible Causes: Faulty air pump, blocked injection passages, defective check valves",
        "- Suggested Fixes: Inspect and repair or replace faulty components"
    ]
},
{
    "conditions": ["P0440", "evaporative emission control malfunction", "EVAP system"],
    "bullets": [
        "- Code: P0440",
        "- Description: Evaporative Emission Control System Malfunction",
        "- Symptoms: Check engine light, fuel odor, failed emissions test",
        "- Possible Causes: Loose or damaged gas cap, faulty purge valve, leaks in EVAP system",
        "- Suggested Fixes: Tighten or replace gas cap; inspect and repair EVAP system leaks"
    ]
},
{
    "conditions": ["P0446", "EVAP vent control circuit malfunction"],
    "bullets": [
        "- Code: P0446",
        "- Description: Evaporative Emission Control System Vent Control Circuit Malfunction",
        "- Symptoms: Check engine light, failed emissions test",
        "- Possible Causes: Faulty vent valve or solenoid, wiring problems",
        "- Suggested Fixes: Inspect and replace vent valve or solenoid; repair wiring"
    ]
},
{
    "conditions": ["P0507", "idle control system high rpm", "idle air control valve"],
    "bullets": [
        "- Code: P0507",
        "- Description: Idle Control System RPM Higher Than Expected",
        "- Symptoms: High idle speed, rough idle",
        "- Possible Causes: Vacuum leaks, faulty idle air control valve, throttle body issues",
        "- Suggested Fixes: Check for vacuum leaks; clean or replace idle air control valve"
    ]
},
{
    "conditions": ["P0505", "idle control system malfunction"],
    "bullets": [
        "- Code: P0505",
        "- Description: Idle Control System Malfunction",
        "- Symptoms: Erratic idle, stalling, check engine light",
        "- Possible Causes: Faulty idle air control valve, wiring issues",
        "- Suggested Fixes: Inspect and replace idle air control valve; check wiring"
    ]
},
{
    "conditions": ["P0606", "ECM PCM processor fault"],
    "bullets": [
        "- Code: P0606",
        "- Description: ECM/PCM Processor Fault",
        "- Symptoms: Check engine light, poor engine performance, starting issues",
        "- Possible Causes: Faulty ECM/PCM, software issues, wiring problems",
        "- Suggested Fixes: Perform diagnostic scan; reprogram or replace ECM/PCM"
    ]
},
{
    "conditions": ["P0172", "system too rich bank 1", "fuel system"],
    "bullets": [
        "- Code: P0172",
        "- Description: System Too Rich (Bank 1)",
        "- Symptoms: Poor fuel economy, black smoke from exhaust, rough idle",
        "- Possible Causes: Faulty fuel injectors, leaking fuel pressure regulator, bad oxygen sensor",
        "- Suggested Fixes: Inspect fuel system components; replace faulty parts"
    ]
},
{
    "conditions": ["P0175", "system too rich bank 2", "fuel system"],
    "bullets": [
        "- Code: P0175",
        "- Description: System Too Rich (Bank 2)",
        "- Symptoms: Poor fuel economy, black smoke from exhaust, rough idle",
        "- Possible Causes: Faulty fuel injectors, leaking fuel pressure regulator, bad oxygen sensor",
        "- Suggested Fixes: Inspect fuel system and sensors; repair or replace as needed"
    ]
},
{
    "conditions": ["P0219", "transmission over temperature"],
    "bullets": [
        "- Code: P0219",
        "- Description: Transmission Over Temperature Condition",
        "- Symptoms: Transmission slipping, delayed shifts, warning light",
        "- Possible Causes: Low transmission fluid, faulty transmission cooler, heavy load or towing",
        "- Suggested Fixes: Check transmission fluid level and quality; repair cooling system"
    ]
},
{
    "conditions": ["P0700", "transmission control system malfunction"],
    "bullets": [
        "- Code: P0700",
        "- Description: Transmission Control System Malfunction",
        "- Symptoms: Check engine light, transmission failsafe mode",
        "- Possible Causes: Transmission control module fault, wiring issues",
        "- Suggested Fixes: Perform diagnostic scan; repair or replace transmission control module"
    ]
},
{
    "conditions": ["P0730", "incorrect gear ratio"],
    "bullets": [
        "- Code: P0730",
        "- Description: Incorrect Gear Ratio",
        "- Symptoms: Check engine light, harsh shifting, transmission slips",
        "- Possible Causes: Worn transmission gears, faulty sensors, incorrect fluid",
        "- Suggested Fixes: Inspect transmission components and sensors"
    ]
},
{
    "conditions": ["P0740", "torque converter clutch circuit malfunction"],
    "bullets": [
        "- Code: P0740",
        "- Description: Torque Converter Clutch Circuit Malfunction",
        "- Symptoms: Transmission slipping, poor fuel economy, check engine light",
        "- Possible Causes: Faulty torque converter clutch solenoid, wiring issues",
        "- Suggested Fixes: Replace solenoid; inspect wiring"
    ]
},
{
    "conditions": ["P0750", "shift solenoid A malfunction"],
    "bullets": [
        "- Code: P0750",
        "- Description: Shift Solenoid A Malfunction",
        "- Symptoms: Harsh or delayed shifting, check engine light",
        "- Possible Causes: Faulty shift solenoid, wiring problems",
        "- Suggested Fixes: Replace solenoid; check wiring"
    ]
},
{
    "conditions": ["P0755", "shift solenoid B malfunction"],
    "bullets": [
        "- Code: P0755",
        "- Description: Shift Solenoid B Malfunction",
        "- Symptoms: Transmission slipping, delayed shifts",
        "- Possible Causes: Faulty solenoid, wiring issues",
        "- Suggested Fixes: Inspect and replace solenoid"
    ]
},
{
    "conditions": ["P0760", "shift solenoid C malfunction"],
    "bullets": [
        "- Code: P0760",
        "- Description: Shift Solenoid C Malfunction",
        "- Symptoms: Transmission slips, rough shifting",
        "- Possible Causes: Solenoid failure, wiring issues",
        "- Suggested Fixes: Replace solenoid; repair wiring"
    ]
},
{
    "conditions": ["P0770", "shift solenoid D malfunction"],
    "bullets": [
        "- Code: P0770",
        "- Description: Shift Solenoid D Malfunction",
        "- Symptoms: Delayed or harsh shifting",
        "- Possible Causes: Solenoid or wiring fault",
        "- Suggested Fixes: Replace or repair as needed"
    ]
},
{
    "conditions": ["P0780", "shift incorrect"],
    "bullets": [
        "- Code: P0780",
        "- Description: Shift Incorrect",
        "- Symptoms: Harsh shifting, transmission warning light",
        "- Possible Causes: Transmission control issues, solenoid problems",
        "- Suggested Fixes: Perform diagnostic scan; repair components"
    ]
},
{
    "conditions": ["P0101", "mass air flow circuit range performance", "MAF sensor issue"],
    "bullets": [
        "- Code: P0101",
        "- Description: Mass Air Flow (MAF) Circuit Range/Performance Problem",
        "- Symptoms: Poor acceleration, rough idle, check engine light",
        "- Possible Causes: Dirty or faulty MAF sensor, wiring problems",
        "- Suggested Fixes: Clean or replace MAF sensor; inspect wiring"
    ]
},
{
    "conditions": ["P0102", "mass air flow circuit low input", "MAF sensor low input"],
    "bullets": [
        "- Code: P0102",
        "- Description: Mass Air Flow (MAF) Circuit Low Input",
        "- Symptoms: Engine hesitation, poor fuel economy",
        "- Possible Causes: Faulty MAF sensor, wiring issues",
        "- Suggested Fixes: Inspect and replace sensor or repair wiring"
    ]
},
{
    "conditions": ["P0103", "mass air flow circuit high input", "MAF sensor high input"],
    "bullets": [
        "- Code: P0103",
        "- Description: Mass Air Flow (MAF) Circuit High Input",
        "- Symptoms: High idle, rough running",
        "- Possible Causes: Shorted MAF sensor wiring, faulty sensor",
        "- Suggested Fixes: Check wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["P0110", "intake air temperature sensor circuit malfunction", "IAT sensor fault"],
    "bullets": [
        "- Code: P0110",
        "- Description: Intake Air Temperature Sensor Circuit Malfunction",
        "- Symptoms: Poor engine performance, check engine light",
        "- Possible Causes: Faulty sensor, wiring issues",
        "- Suggested Fixes: Inspect and replace sensor or repair wiring"
    ]
},
{
    "conditions": ["P0112", "intake air temperature sensor circuit low input", "IAT sensor low input"],
    "bullets": [
        "- Code: P0112",
        "- Description: Intake Air Temperature Sensor Circuit Low Input",
        "- Symptoms: Engine runs rich, rough idle",
        "- Possible Causes: Faulty sensor, wiring problems",
        "- Suggested Fixes: Replace sensor; check wiring"
    ]
},
{
    "conditions": ["P0134", "oxygen sensor circuit no activity detected", "bank 1 sensor 1 O2 sensor"],
    "bullets": [
        "- Code: P0134",
        "- Description: O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 1)",
        "- Symptoms: Check engine light, poor fuel economy",
        "- Possible Causes: Faulty O2 sensor, wiring problems",
        "- Suggested Fixes: Replace sensor; check wiring and connectors"
    ]
},
{
    "conditions": ["P0170", "fuel trim malfunction bank 1", "fuel trim issue"],
    "bullets": [
        "- Code: P0170",
        "- Description: Fuel Trim Malfunction (Bank 1)",
        "- Symptoms: Poor engine performance, check engine light",
        "- Possible Causes: Vacuum leaks, faulty sensors",
        "- Suggested Fixes: Inspect vacuum system and sensors"
    ]
},
{
    "conditions": ["P0173", "fuel trim malfunction bank 2", "fuel trim issue"],
    "bullets": [
        "- Code: P0173",
        "- Description: Fuel Trim Malfunction (Bank 2)",
        "- Symptoms: Rough running, check engine light",
        "- Possible Causes: Vacuum leaks, faulty sensors",
        "- Suggested Fixes: Inspect and repair vacuum leaks or sensors"
    ]
},
{
    "conditions": ["P0506", "idle control rpm lower than expected", "idle air control valve low rpm"],
    "bullets": [
        "- Code: P0506",
        "- Description: Idle Control System RPM Lower Than Expected",
        "- Symptoms: Low idle, stalling",
        "- Possible Causes: Faulty idle air control valve, vacuum leaks",
        "- Suggested Fixes: Clean or replace idle air control valve; check vacuum lines"
    ]
},
{
    "conditions": ["P0309", "cylinder 9 misfire detected", "engine misfire cylinder 9"],
    "bullets": [
        "- Code: P0309",
        "- Description: Cylinder 9 Misfire Detected",
        "- Symptoms: Engine hesitation, rough idle, misfire codes",
        "- Possible Causes: Faulty spark plug or coil, fuel injector issues",
        "- Suggested Fixes: Replace spark plug; check ignition coil and injector"
    ]
},
{
    "conditions": ["P0315", "crankshaft position sensor malfunction", "CKP sensor fault"],
    "bullets": [
        "- Code: P0315",
        "- Description: Crankshaft Position Sensor Circuit Malfunction",
        "- Symptoms: Engine misfires, hard starting, stalling",
        "- Possible Causes: Faulty sensor, wiring issues, damaged reluctor ring",
        "- Suggested Fixes: Inspect and replace sensor; repair wiring"
    ]
},
{
    "conditions": ["P0325", "knock sensor malfunction bank 1", "knock sensor fault"],
    "bullets": [
        "- Code: P0325",
        "- Description: Knock Sensor Circuit Malfunction (Bank 1 or Single Sensor)",
        "- Symptoms: Engine knocking, poor performance, check engine light",
        "- Possible Causes: Faulty knock sensor, wiring problems",
        "- Suggested Fixes: Replace knock sensor; inspect wiring"
    ]
},
{
    "conditions": ["P0335", "crankshaft position sensor A malfunction", "CKP sensor A fault"],
    "bullets": [
        "- Code: P0335",
        "- Description: Crankshaft Position Sensor A Circuit Malfunction",
        "- Symptoms: Engine stalls, no start, misfires",
        "- Possible Causes: Faulty sensor, wiring or connector issues",
        "- Suggested Fixes: Replace sensor; check wiring and connectors"
    ]
},
{
    "conditions": ["P0340", "camshaft position sensor malfunction", "CMP sensor fault"],
    "bullets": [
        "- Code: P0340",
        "- Description: Camshaft Position Sensor Circuit Malfunction",
        "- Symptoms: Engine misfire, poor acceleration, stalling",
        "- Possible Causes: Faulty sensor, wiring issues",
        "- Suggested Fixes: Replace camshaft sensor; inspect wiring"
    ]
},
{
    "conditions": ["P0345", "camshaft position sensor malfunction bank 2", "CMP sensor bank 2 fault"],
    "bullets": [
        "- Code: P0345",
        "- Description: Camshaft Position Sensor Circuit Malfunction (Bank 2)",
        "- Symptoms: Rough running, misfires, check engine light",
        "- Possible Causes: Faulty sensor, wiring faults",
        "- Suggested Fixes: Replace sensor; check wiring"
    ]
},
{
    "conditions": ["P0411", "secondary air injection incorrect flow"],
    "bullets": [
        "- Code: P0411",
        "- Description: Secondary Air Injection System Incorrect Flow Detected",
        "- Symptoms: Failed emissions test, check engine light",
        "- Possible Causes: Faulty air injection pump or valves",
        "- Suggested Fixes: Inspect and repair or replace components"
    ]
},
{
    "conditions": ["P0421", "catalyst efficiency below threshold bank 1", "catalytic converter efficiency"],
    "bullets": [
        "- Code: P0421",
        "- Description: Catalyst System Efficiency Below Threshold (Bank 1)",
        "- Symptoms: Reduced engine performance, check engine light",
        "- Possible Causes: Failed catalytic converter, exhaust leaks, faulty O2 sensors",
        "- Suggested Fixes: Inspect and replace catalytic converter or sensors"
    ]
},
{
    "conditions": ["P0441", "evaporative emission control incorrect purge flow", "EVAP purge valve issue"],
    "bullets": [
        "- Code: P0441",
        "- Description: Evaporative Emission Control System Incorrect Purge Flow",
        "- Symptoms: Check engine light, fuel odor",
        "- Possible Causes: Faulty purge valve, leaks in EVAP system",
        "- Suggested Fixes: Inspect and repair EVAP components"
    ]
},
{
    "conditions": ["P0456", "evaporative emission leak very small", "EVAP small leak"],
    "bullets": [
        "- Code: P0456",
        "- Description: Evaporative Emission System Leak Detected (Very Small Leak)",
        "- Symptoms: Check engine light, fuel smell",
        "- Possible Causes: Loose gas cap, small EVAP leaks",
        "- Suggested Fixes: Tighten or replace gas cap; inspect EVAP system"
    ]
},
{
    "conditions": ["P0500", "vehicle speed sensor malfunction", "speedometer fault"],
    "bullets": [
        "- Code: P0500",
        "- Description: Vehicle Speed Sensor Malfunction",
        "- Symptoms: Speedometer malfunction, transmission shifting issues",
        "- Possible Causes: Faulty sensor, wiring problems",
        "- Suggested Fixes: Replace sensor; check wiring"
    ]
},
{
    "conditions": ["P0550", "auxiliary vacuum pump control circuit malfunction", "vacuum pump fault"],
    "bullets": [
        "- Code: P0550",
        "- Description: Auxiliary Vacuum Pump Control Circuit Malfunction",
        "- Symptoms: Brake assist problems, check engine light",
        "- Possible Causes: Faulty vacuum pump, wiring issues",
        "- Suggested Fixes: Inspect and replace vacuum pump or wiring"
    ]
},
{
    "conditions": ["P0601", "internal control module memory checksum error", "ECM memory error"],
    "bullets": [
        "- Code: P0601",
        "- Description: Internal Control Module Memory Check Sum Error",
        "- Symptoms: Engine performance issues, check engine light",
        "- Possible Causes: Faulty ECM/PCM, corrupted software",
        "- Suggested Fixes: Reprogram or replace control module"
    ]
},
{
    "conditions": ["P0602", "control module programming error", "ECM programming error"],
    "bullets": [
        "- Code: P0602",
        "- Description: Control Module Programming Error",
        "- Symptoms: Check engine light, drivability problems",
        "- Possible Causes: Corrupted ECM software",
        "- Suggested Fixes: Reprogram or replace ECM/PCM"
    ]
},
{
    "conditions": ["P0603", "internal control module keep alive memory error", "ECM KAM error"],
    "bullets": [
        "- Code: P0603",
        "- Description: Internal Control Module Keep Alive Memory (KAM) Error",
        "- Symptoms: Engine stalling, poor performance",
        "- Possible Causes: Faulty ECM/PCM, wiring issues",
        "- Suggested Fixes: Repair or replace control module"
    ]
},
{
    "conditions": ["P0705", "transmission range sensor malfunction", "PRNDL input fault"],
    "bullets": [
        "- Code: P0705",
        "- Description: Transmission Range Sensor Circuit Malfunction (PRNDL Input)",
        "- Symptoms: Incorrect gear indication, transmission won’t shift properly",
        "- Possible Causes: Faulty sensor or wiring",
        "- Suggested Fixes: Replace sensor; check wiring"
    ]
},
{
    "conditions": ["P0715", "input turbine speed sensor malfunction", "input speed sensor fault"],
    "bullets": [
        "- Code: P0715",
        "- Description: Input/Turbine Speed Sensor Circuit Malfunction",
        "- Symptoms: Transmission shifting problems, check engine light",
        "- Possible Causes: Faulty speed sensor, wiring issues",
        "- Suggested Fixes: Inspect and replace sensor"
    ]
},
{
    "conditions": ["P0720", "output speed sensor malfunction", "output speed sensor fault"],
    "bullets": [
        "- Code: P0720",
        "- Description: Output Speed Sensor Circuit Malfunction",
        "- Symptoms: Transmission shifting problems, check engine light",
        "- Possible Causes: Faulty sensor, wiring problems",
        "- Suggested Fixes: Replace sensor; repair wiring"
    ]
},
{
    "conditions": ["P0731", "gear 1 incorrect ratio", "gear 1 ratio fault"],
    "bullets": [
        "- Code: P0731",
        "- Description: Gear 1 Incorrect Ratio",
        "- Symptoms: Harsh shifting, check engine light",
        "- Possible Causes: Transmission mechanical faults, sensor errors",
        "- Suggested Fixes: Inspect transmission and sensors"
    ]
},
{
    "conditions": ["P0732", "gear 2 incorrect ratio", "gear 2 ratio fault"],
    "bullets": [
        "- Code: P0732",
        "- Description: Gear 2 Incorrect Ratio",
        "- Symptoms: Transmission slip, rough shifting",
        "- Possible Causes: Transmission wear or sensor failure",
        "- Suggested Fixes: Inspect and repair transmission"
    ]
},
{
    "conditions": ["P0733", "gear 3 incorrect ratio", "gear 3 ratio fault"],
    "bullets": [
        "- Code: P0733",
        "- Description: Gear 3 Incorrect Ratio",
        "- Symptoms: Harsh shifting, poor acceleration",
        "- Possible Causes: Mechanical or sensor problems",
        "- Suggested Fixes: Inspect transmission"
    ]
},
{
    "conditions": ["P0734", "gear 4 incorrect ratio", "gear 4 ratio fault"],
    "bullets": [
        "- Code: P0734",
        "- Description: Gear 4 Incorrect Ratio",
        "- Symptoms: Transmission issues, check engine light",
        "- Possible Causes: Mechanical faults or sensor errors",
        "- Suggested Fixes: Repair transmission"
    ]
},
{
    "conditions": ["P0735", "gear 5 incorrect ratio", "gear 5 ratio fault"],
    "bullets": [
        "- Code: P0735",
        "- Description: Gear 5 Incorrect Ratio",
        "- Symptoms: Poor shifting, check engine light",
        "- Possible Causes: Transmission wear or sensor issues",
        "- Suggested Fixes: Inspect and repair"
    ]
},
{
    "conditions": ["P0736", "reverse gear incorrect ratio", "reverse gear ratio fault"],
    "bullets": [
        "- Code: P0736",
        "- Description: Reverse Gear Incorrect Ratio",
        "- Symptoms: Transmission slipping in reverse",
        "- Possible Causes: Transmission mechanical faults",
        "- Suggested Fixes: Repair transmission"
    ]
},
{
    "conditions": ["P0756", "shift solenoid B performance or stuck off", "shift solenoid B fault"],
    "bullets": [
        "- Code: P0756",
        "- Description: Shift Solenoid B Performance or Stuck Off",
        "- Symptoms: Transmission slipping or rough shifting",
        "- Possible Causes: Faulty solenoid, wiring issues",
        "- Suggested Fixes: Replace solenoid; check wiring"
    ]
},
{
    "conditions": ["P0775", "shift solenoid D performance or stuck off", "shift solenoid D fault"],
    "bullets": [
        "- Code: P0775",
        "- Description: Shift Solenoid D Performance or Stuck Off",
        "- Symptoms: Transmission shifting problems",
        "- Possible Causes: Faulty solenoid or wiring",
        "- Suggested Fixes: Replace or repair solenoid"
    ]
},
{
    "conditions": ["P0785", "shift to reverse or park inhibited", "reverse or park shift fault"],
    "bullets": [
        "- Code: P0785",
        "- Description: Shift to Reverse or Park Inhibited",
        "- Symptoms: Transmission won’t shift into reverse or park",
        "- Possible Causes: Transmission range sensor or wiring fault",
        "- Suggested Fixes: Repair sensor or wiring"
    ]
},
{
    "conditions": ["P0795", "pressure control solenoid malfunction", "pressure control solenoid fault"],
    "bullets": [
        "- Code: P0795",
        "- Description: Pressure Control Solenoid Malfunction",
        "- Symptoms: Transmission slipping, poor shifting",
        "- Possible Causes: Faulty solenoid or wiring",
        "- Suggested Fixes: Replace solenoid"
    ]
},
{
    "conditions": ["P0801", "reverse inhibit control circuit malfunction", "reverse inhibit fault"],
    "bullets": [
        "- Code: P0801",
        "- Description: Reverse Inhibit Control Circuit Malfunction",
        "- Symptoms: Transmission won’t shift to reverse",
        "- Possible Causes: Wiring or control module issues",
        "- Suggested Fixes: Repair wiring or control module"
    ]
},
{
    "conditions": ["P0805", "clutch position sensor circuit malfunction", "clutch position sensor fault"],
    "bullets": [
        "- Code: P0805",
        "- Description: Clutch Position Sensor Circuit Malfunction",
        "- Symptoms: Difficulty shifting gears",
        "- Possible Causes: Faulty sensor, wiring problems",
        "- Suggested Fixes: Replace sensor; repair wiring"
    ]
},
{
    "conditions": ["P0830", "clutch pedal position sensor circuit malfunction", "clutch pedal position sensor fault"],
    "bullets": [
        "- Code: P0830",
        "- Description: Clutch Pedal Position Sensor Circuit Malfunction",
        "- Symptoms: Check engine light, clutch engagement issues",
        "- Possible Causes: Sensor or wiring fault",
        "- Suggested Fixes: Replace sensor; inspect wiring"
    ]
},
{
    "conditions": ["P0841", "transmission fluid pressure sensor circuit range performance", "TFP sensor range/performance"],
    "bullets": [
        "- Code: P0841",
        "- Description: Transmission Fluid Pressure Sensor Circuit Range/Performance",
        "- Symptoms: Transmission shifting issues",
        "- Possible Causes: Faulty pressure sensor, wiring problems",
        "- Suggested Fixes: Replace sensor; check wiring"
    ]
},
{
    "conditions": ["P0850", "transmission fluid pressure sensor circuit malfunction", "TFP sensor malfunction"],
    "bullets": [
        "- Code: P0850",
        "- Description: Transmission Fluid Pressure Sensor Circuit Malfunction",
        "- Symptoms: Transmission slipping, harsh shifting",
        "- Possible Causes: Faulty sensor or wiring",
        "- Suggested Fixes: Repair or replace sensor"
    ]
},
{
    "conditions": ["P0868", "transmission fluid pressure low", "TFP low pressure"],
    "bullets": [
        "- Code: P0868",
        "- Description: Transmission Fluid Pressure Low",
        "- Symptoms: Slipping, delayed shifting",
        "- Possible Causes: Low fluid, faulty sensor",
        "- Suggested Fixes: Check fluid level; replace sensor"
    ]
},
{
    "conditions": ["P0870", "transmission fluid pressure high", "TFP high pressure"],
    "bullets": [
        "- Code: P0870",
        "- Description: Transmission Fluid Pressure High",
        "- Symptoms: Harsh shifting",
        "- Possible Causes: Faulty sensor or high fluid pressure",
        "- Suggested Fixes: Inspect system; replace sensor"
    ]
},
{
    "conditions": ["P0986", "EGR valve position sensor circuit malfunction", "EGR valve position sensor fault"],
    "bullets": [
        "- Code: P0986",
        "- Description: EGR Valve Position Sensor Circuit Malfunction",
        "- Symptoms: Rough idle, check engine light",
        "- Possible Causes: Faulty sensor or wiring",
        "- Suggested Fixes: Replace sensor; repair wiring"
    ]
},
{
    "conditions": ["P1000", "OBD systems readiness test not complete"],
    "bullets": [
        "- Code: P1000",
        "- Description: OBD Systems Readiness Test Not Complete",
        "- Symptoms: Check engine light",
        "- Possible Causes: Drive cycle not completed, recent battery disconnect",
        "- Suggested Fixes: Complete drive cycle; clear codes"
    ]
},
{
    "conditions": ["P1101", "mass air flow sensor out of self test range", "MAF sensor self-test fault"],
    "bullets": [
        "- Code: P1101",
        "- Description: Mass Air Flow Sensor Out of Self-Test Range",
        "- Symptoms: Check engine light, poor performance",
        "- Possible Causes: Faulty MAF sensor, wiring issues",
        "- Suggested Fixes: Replace or clean sensor; check wiring"
    ]
},
{
    "conditions": ["P1121", "throttle position sensor circuit range performance", "TPS range/performance fault"],
    "bullets": [
        "- Code: P1121",
        "- Description: Throttle Position Sensor Circuit Range/Performance",
        "- Symptoms: Poor throttle response, check engine light",
        "- Possible Causes: Faulty sensor or wiring",
        "- Suggested Fixes: Replace sensor; check wiring"
    ]
},
{
    "conditions": ["P1151", "oxygen sensor heater resistance high bank 1 sensor 1", "O2 sensor heater fault"],
    "bullets": [
        "- Code: P1151",
        "- Description: Oxygen Sensor Heater Resistance High (Bank 1 Sensor 1)",
        "- Symptoms: Check engine light, poor fuel economy",
        "- Possible Causes: Faulty oxygen sensor heater circuit",
        "- Suggested Fixes: Replace oxygen sensor"
    ]
},
{
    "conditions": ["P1259", "injector circuit malfunction", "fuel injector fault"],
    "bullets": [
        "- Code: P1259",
        "- Description: Injector Circuit Malfunction",
        "- Symptoms: Rough running, misfires",
        "- Possible Causes: Faulty injector wiring or injector",
        "- Suggested Fixes: Inspect and repair injector circuit; replace injector if needed"
    ]
},
{
    "conditions": ["evap vent valve malfunction", "check engine light", "evap system fault"],
    "bullets": [
        "- Condition: Evaporative Emission System Vent Valve/Solenoid Circuit Malfunction",
        "- Description: Faulty vent valve or solenoid in EVAP system",
        "- Symptoms: Fuel vapor leak or EVAP emission system fault",
        "- Suggested Fixes: Inspect EVAP vent valve and wiring; test solenoid operation"
    ]
},
{
    "conditions": ["evap pressure sensor low input", "evap system fault", "check engine light"],
    "bullets": [
        "- Condition: Evaporative Emission Control System Pressure Sensor Low Input",
        "- Description: Faulty or low input from EVAP pressure sensor",
        "- Symptoms: EVAP system monitoring issues",
        "- Suggested Fixes: Check sensor wiring and connections; replace faulty sensor"
    ]
},
{
    "conditions": ["evap pressure sensor high input", "evap system fault", "check engine light"],
    "bullets": [
        "- Condition: Evaporative Emission Control System Pressure Sensor High Input",
        "- Description: EVAP pressure sensor sending abnormally high voltage",
        "- Symptoms: EVAP system monitoring issues",
        "- Suggested Fixes: Test sensor output; inspect for wiring shorts"
    ]
},
    {
    "conditions": ["fuel level sensor high input", "fuel gauge error", "fuel system warning"],
    "bullets": [
        "- Condition: Fuel Level Sensor Circuit High Input",
        "- Likely Issue: Faulty fuel level sensor or wiring",
        "- Related Issue: Fuel gauge and fuel system monitoring",
        "- Suggestion: Test sensor and wiring; replace sensor if faulty"
    ]
},
{
    "conditions": ["evap flow during non-purge", "evap system fault", "check engine light"],
    "bullets": [
        "- Condition: EVAP Flow Detected During Non-Purge Condition",
        "- Likely Issue: Leak or malfunction in EVAP system valves or lines",
        "- Related Issue: EVAP system integrity",
        "- Suggestion: Inspect EVAP valves and lines for leaks or damage"
    ]
},
{
    "conditions": ["engine oil pressure sensor malfunction", "oil pressure warning light", "engine warning light"],
    "bullets": [
        "- Condition: Engine Oil Pressure Sensor/Switch Circuit Malfunction",
        "- Likely Issue: Faulty oil pressure sensor or wiring",
        "- Related Issue: Engine lubrication monitoring",
        "- Suggestion: Check oil pressure sensor operation; inspect wiring and connectors"
    ]
},
{
    "conditions": ["engine oil pressure sensor low voltage", "oil pressure warning light"],
    "bullets": [
        "- Condition: Engine Oil Pressure Sensor/Switch Low Voltage",
        "- Likely Issue: Low voltage signal from oil pressure sensor",
        "- Related Issue: Engine oil monitoring system",
        "- Suggestion: Inspect wiring and sensor; verify oil pressure mechanically"
    ]
},
{
    "conditions": ["system voltage low", "battery warning", "electrical issues"],
    "bullets": [
        "- Condition: System Voltage Low",
        "- Likely Issue: Weak battery or charging system fault",
        "- Related Issue: Electrical system health",
        "- Suggestion: Test battery and alternator output; inspect wiring"
    ]
},
{
    "conditions": ["system voltage high", "battery warning", "electrical issues"],
    "bullets": [
        "- Condition: System Voltage High",
        "- Likely Issue: Overcharging by alternator or voltage regulator issue",
        "- Related Issue: Electrical charging system",
        "- Suggestion: Test alternator voltage output and regulator function"
    ]
},
{
    "conditions": ["thermostat heater circuit open", "engine temperature warning", "cooling system fault"],
    "bullets": [
        "- Condition: Thermostat Heater Control Circuit Open",
        "- Likely Issue: Open circuit in thermostat heater control wiring",
        "- Related Issue: Engine temperature regulation",
        "- Suggestion: Inspect wiring and thermostat heater; replace defective components"
    ]
},
{
    "conditions": ["serial communication link malfunction", "multiple system errors", "check engine light"],
    "bullets": [
        "- Condition: Serial Communication Link Malfunction",
        "- Likely Issue: Communication failure between control modules",
        "- Related Issue: Vehicle data bus or network",
        "- Suggestion: Inspect wiring, connectors, and module communication lines"
    ]
},
{
    "conditions": ["internal control module ram error", "check engine light", "performance issues"],
    "bullets": [
        "- Condition: Internal Control Module RAM Error",
        "- Likely Issue: Faulty module memory or software corruption",
        "- Related Issue: Engine or transmission control module",
        "- Suggestion: Reprogram or replace affected control module"
    ]
},
{
    "conditions": ["control module performance fault", "engine running issues", "check engine light"],
    "bullets": [
        "- Condition: Control Module Performance Fault",
        "- Likely Issue: Internal control module error affecting vehicle operation",
        "- Related Issue: Engine or transmission control",
        "- Suggestion: Diagnostic scan and module reprogram or replacement"
    ]
},
{
    "conditions": ["control module vehicle options error", "check engine light"],
    "bullets": [
        "- Condition: Control Module Vehicle Options Error",
        "- Likely Issue: Mismatch or corruption in vehicle configuration data",
        "- Related Issue: Control module settings",
        "- Suggestion: Reprogram control module with correct vehicle options"
    ]
},
{
    "conditions": ["starter relay circuit fault", "engine won't start", "no crank"],
    "bullets": [
        "- Condition: Starter Relay Circuit Malfunction",
        "- Likely Issue: Faulty starter relay or wiring",
        "- Related Issue: Starting system",
        "- Suggestion: Test and replace starter relay; check wiring"
    ]
},
{
    "conditions": ["generator control circuit malfunction", "charging system warning", "battery warning light"],
    "bullets": [
        "- Condition: Generator Control Circuit Malfunction",
        "- Likely Issue: Fault in alternator control or wiring",
        "- Related Issue: Charging system",
        "- Suggestion: Test alternator and regulator; inspect wiring"
    ]
},
{
    "conditions": ["fuel pump control circuit open", "engine stall", "no fuel pressure"],
    "bullets": [
        "- Condition: Fuel Pump A Control Circuit/Open",
        "- Likely Issue: Open circuit or failure in fuel pump control wiring",
        "- Related Issue: Fuel delivery system",
        "- Suggestion: Inspect wiring and connectors; test/replace fuel pump relay or pump"
    ]
},
{
    "conditions": ["mil control circuit malfunction", "check engine light won't turn off"],
    "bullets": [
        "- Condition: Malfunction Indicator Lamp (MIL) Control Circuit Malfunction",
        "- Likely Issue: Fault in MIL circuit or wiring",
        "- Related Issue: Dashboard warning system",
        "- Suggestion: Inspect wiring and bulb; repair or replace MIL circuit components"
    ]
},
{
    "conditions": ["ecm power relay circuit open", "engine won't start", "no power to ECM"],
    "bullets": [
        "- Condition: ECM/PCM Power Relay Control Circuit/Open",
        "- Likely Issue: Open power relay circuit to engine control module",
        "- Related Issue: Engine control power supply",
        "- Suggestion: Check power relay and wiring; replace relay if needed"
    ]
},
{
    "conditions": ["transmission range sensor circuit range performance", "gear shifting problems", "check engine light"],
    "bullets": [
        "- Condition: Transmission Range Sensor Circuit Range/Performance",
        "- Likely Issue: Faulty transmission range sensor or wiring",
        "- Related Issue: Transmission gear selection",
        "- Suggestion: Test transmission range sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor malfunction", "check engine light", "transmission overheating"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty or disconnected transmission fluid temperature sensor",
        "- Related Issue: Transmission overheating or improper shifting",
        "- Suggestion: Inspect sensor wiring and connections; replace sensor if faulty"
    ]
},
{
    "conditions": ["input turbine speed sensor no signal", "no speed signal", "transmission shifting problems"],
    "bullets": [
        "- Condition: Input/Turbine Speed Sensor No Signal",
        "- Likely Issue: Faulty input speed sensor or wiring issue",
        "- Related Issue: Transmission speed monitoring",
        "- Suggestion: Check sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["engine speed input circuit malfunction", "rpm signal error", "check engine light"],
    "bullets": [
        "- Condition: Engine Speed Input Circuit Malfunction",
        "- Likely Issue: Faulty engine speed sensor or circuit problem",
        "- Related Issue: Engine rpm monitoring",
        "- Suggestion: Test sensor and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["torque converter clutch circuit performance stuck off", "slipping transmission", "check engine light"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Performance/Stuck Off",
        "- Likely Issue: TCC solenoid stuck off or faulty",
        "- Related Issue: Transmission locking and fuel efficiency",
        "- Suggestion: Test TCC solenoid and circuit; clean or replace solenoid"
    ]
},
{
    "conditions": ["torque converter clutch circuit stuck on", "harsh shifting", "engine stall risk"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Stuck On",
        "- Likely Issue: TCC solenoid stuck engaged",
        "- Related Issue: Transmission and engine stalling",
        "- Suggestion: Inspect solenoid and control circuit; repair or replace"
    ]
},
{
    "conditions": ["shift solenoid a performance stuck off", "transmission shifting issues", "check engine light"],
    "bullets": [
        "- Condition: Shift Solenoid A Performance or Stuck Off",
        "- Likely Issue: Faulty or stuck shift solenoid A",
        "- Related Issue: Gear shifting",
        "- Suggestion: Test shift solenoid; clean or replace if faulty"
    ]
},
{
    "conditions": ["shift solenoid a electrical malfunction", "transmission shifting problems"],
    "bullets": [
        "- Condition: Shift Solenoid A Electrical Malfunction",
        "- Likely Issue: Electrical problem in shift solenoid A circuit",
        "- Related Issue: Transmission gear shifting",
        "- Suggestion: Check wiring and connectors; repair circuit or replace solenoid"
    ]
},
{
    "conditions": ["shift solenoid c performance stuck off", "transmission shifting problems"],
    "bullets": [
        "- Condition: Shift Solenoid C Performance or Stuck Off",
        "- Likely Issue: Shift solenoid C malfunction or stuck",
        "- Related Issue: Gear shifting issues",
        "- Suggestion: Test and replace solenoid if necessary"
    ]
},
{
    "conditions": ["shift solenoid d performance stuck off", "transmission shifting issues"],
    "bullets": [
        "- Condition: Shift Solenoid D Performance or Stuck Off",
        "- Likely Issue: Shift solenoid D faulty or stuck",
        "- Related Issue: Gear shifting problems",
        "- Suggestion: Diagnose solenoid; repair or replace"
    ]
},
{
    "conditions": ["pressure control solenoid b performance stuck off", "transmission pressure control fault"],
    "bullets": [
        "- Condition: Pressure Control Solenoid B Performance/Stuck Off",
        "- Likely Issue: Pressure control solenoid B malfunction",
        "- Related Issue: Transmission pressure regulation",
        "- Suggestion: Test solenoid and control circuit; repair or replace"
    ]
},
    {

    "conditions": ["clutch position sensor circuit range performance", "clutch engagement issues"],
    "bullets": [
        "- Condition: Clutch Position Sensor Circuit Range/Performance",
        "- Likely Issue: Faulty clutch position sensor or wiring",
        "- Related Issue: Clutch operation and transmission shifting",
        "- Suggestion: Inspect sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["clutch pedal switch b circuit fault", "clutch pedal issues"],
    "bullets": [
        "- Condition: Clutch Pedal Switch “B” Circuit Malfunction",
        "- Likely Issue: Faulty clutch pedal switch or wiring",
        "- Related Issue: Clutch pedal signal to transmission",
        "- Suggestion: Test switch and wiring; replace switch if defective"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor switch b circuit malfunction", "transmission pressure warning"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor/Switch B Circuit Malfunction",
        "- Likely Issue: Faulty transmission fluid pressure sensor or wiring",
        "- Related Issue: Transmission fluid pressure monitoring",
        "- Suggestion: Test sensor and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor switch b range performance", "transmission pressure sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor/Switch B Range/Performance",
        "- Likely Issue: Sensor output out of range or degraded performance",
        "- Related Issue: Transmission fluid pressure regulation",
        "- Suggestion: Inspect sensor operation; replace if needed"
    ]
},
{
    "conditions": ["tcm communication circuit malfunction", "transmission control module error"],
    "bullets": [
        "- Condition: Transmission Control Module (TCM) Communication Circuit Malfunction",
        "- Likely Issue: Communication failure with transmission control module",
        "- Related Issue: Transmission electronic control",
        "- Suggestion: Check wiring, connectors, and TCM for faults"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor switch c range performance", "transmission pressure sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor/Switch C Range/Performance",
        "- Likely Issue: Sensor output outside expected range",
        "- Related Issue: Transmission pressure monitoring",
        "- Suggestion: Test sensor function; replace if necessary"
    ]
},
{
    "conditions": ["transmission component slipping", "gear slipping", "transmission warning"],
    "bullets": [
        "- Condition: Transmission Component Slipping",
        "- Likely Issue: Internal transmission wear or clutch slipping",
        "- Related Issue: Transmission mechanical issues",
        "- Suggestion: Inspect transmission internals; repair or rebuild as needed"
    ]
},
{
    "conditions": ["clutch actuator circuit open", "clutch won't engage", "transmission shifting problems"],
    "bullets": [
        "- Condition: Clutch Actuator Circuit Open",
        "- Likely Issue: Open circuit in clutch actuator control wiring",
        "- Related Issue: Clutch control and engagement",
        "- Suggestion: Check wiring and connectors; repair or replace actuator"
    ]
},
{
    "conditions": ["hydraulic pressure sensor circuit high", "hydraulic pressure warning", "transmission problems"],
    "bullets": [
        "- Condition: Hydraulic Pressure Sensor Circuit High",
        "- Likely Issue: High voltage signal or sensor fault",
        "- Related Issue: Transmission hydraulic system",
        "- Suggestion: Inspect sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["pressure control solenoid a control circuit open", "transmission pressure control fault"],
    "bullets": [
        "- Condition: Pressure Control Solenoid “A” Control Circuit Open",
        "- Likely Issue: Open circuit or failure in solenoid control wiring",
        "- Related Issue: Transmission pressure control",
        "- Suggestion: Check wiring and solenoid; repair or replace as needed"
    ]
},
{
    "conditions": ["pressure control solenoid a control circuit low", "transmission pressure control low signal"],
    "bullets": [
        "- Condition: Pressure Control Solenoid “A” Control Circuit Low",
        "- Likely Issue: Low voltage or weak signal in solenoid control",
        "- Related Issue: Transmission pressure regulation",
        "- Suggestion: Inspect wiring and solenoid; repair or replace"
    ]
},
{
    "conditions": ["pressure control solenoid b control circuit open", "transmission pressure control fault"],
    "bullets": [
        "- Condition: Pressure Control Solenoid “B” Control Circuit Open",
        "- Likely Issue: Open control circuit for solenoid B",
        "- Related Issue: Transmission pressure control",
        "- Suggestion: Check wiring and solenoid; repair or replace"
    ]
},
{
    "conditions": ["shift solenoid c control circuit open", "transmission shifting fault"],
    "bullets": [
        "- Condition: Shift Solenoid “C” Control Circuit Open",
        "- Likely Issue: Open or broken circuit for solenoid C",
        "- Related Issue: Gear shifting control",
        "- Suggestion: Test wiring and solenoid; repair or replace"
    ]
},
{
    "conditions": ["shift solenoid a control circuit low", "transmission shifting problem"],
    "bullets": [
        "- Condition: Shift Solenoid “A” Control Circuit Low",
        "- Likely Issue: Weak signal or voltage to solenoid A",
        "- Related Issue: Gear shifting",
        "- Suggestion: Inspect wiring and connectors; repair or replace"
    ]
},
{
    "conditions": ["shift solenoid b control circuit high", "transmission shifting fault"],
    "bullets": [
        "- Condition: Shift Solenoid “B” Control Circuit High",
        "- Likely Issue: High voltage or signal above normal",
        "- Related Issue: Gear shifting control",
        "- Suggestion: Inspect wiring and solenoid circuit; repair as necessary"
    ]
},
{
    "conditions": ["shift solenoid c control circuit high", "transmission shifting fault"],
    "bullets": [
        "- Condition: Shift Solenoid “C” Control Circuit High",
        "- Likely Issue: High voltage signal to solenoid C",
        "- Related Issue: Gear shifting problems",
        "- Suggestion: Check wiring and solenoid; repair or replace"
    ]
},
{
    "conditions": ["manufacturer controlled auxiliary emission controls", "emission control error"],
    "bullets": [
        "- Condition: Manufacturer Controlled Auxiliary Emission Controls",
        "- Likely Issue: Malfunction in auxiliary emission control devices",
        "- Related Issue: Emission control systems",
        "- Suggestion: Diagnose emission control devices; repair or replace faulty parts"
    ]
},
{
    "conditions": ["short runner valve control performance", "engine performance issue", "emission fault"],
    "bullets": [
        "- Condition: Short Runner Valve Control Performance",
        "- Likely Issue: Malfunction in intake short runner valve",
        "- Related Issue: Intake manifold airflow control",
        "- Suggestion: Inspect valve operation and control wiring; repair as needed"
    ]
},
{
    "conditions": ["heated o2 sensor control circuit fault", "oxygen sensor heater malfunction", "check engine light"],
    "bullets": [
        "- Condition: Heated O2 Sensor Control Circuit (Bank 1 Sensor 1) Fault",
        "- Likely Issue: Faulty heater circuit in oxygen sensor",
        "- Related Issue: Emission control and fuel mixture regulation",
        "- Suggestion: Check sensor heater circuit; replace oxygen sensor if faulty"
    ]
},
{
    "conditions": ["map sensor range performance fault", "manifold absolute pressure sensor error", "engine performance issues"],
    "bullets": [
        "- Condition: Manifold Absolute Pressure (MAP) Sensor Range/Performance Fault",
        "- Likely Issue: Faulty or out-of-range MAP sensor readings",
        "- Related Issue: Engine load and fuel control",
        "- Suggestion: Test MAP sensor and wiring; clean or replace sensor"
    ]
},
{
    "conditions": ["intake air temperature sensor intermittent high voltage", "engine temperature sensor fault", "check engine light"],
    "bullets": [
        "- Condition: Intake Air Temperature Sensor Intermittent High Voltage",
        "- Likely Issue: Intermittent high voltage signal from intake air temperature sensor",
        "- Related Issue: Engine air temperature monitoring",
        "- Suggestion: Inspect sensor and wiring for intermittent faults; repair or replace"
    ]
},
{
    "conditions": ["throttle position sensor intermittent fault", "throttle sensor signal unstable", "check engine light"],
    "bullets": [
        "- Condition: Throttle Position Sensor Intermittent Fault",
        "- Likely Issue: Unstable or intermittent throttle position sensor signal",
        "- Related Issue: Throttle control and engine response",
        "- Suggestion: Inspect wiring and sensor connector; replace sensor if needed"
    ]
},
{
    "conditions": ["lack of HO2S switch sensor indicates lean bank 1 sensor 1", "P1131", "HO2S lean sensor fault"],
    "bullets": [
        "- Condition: Lack of Heated Oxygen Sensor (HO2S) Switch – Sensor Indicates Lean (Bank 1 Sensor 1)",
        "- Likely Issue: Faulty oxygen sensor indicating lean air-fuel mixture",
        "- Related Issue: Poor fuel economy, engine hesitation",
        "- Suggestion: Check sensor wiring and connections; replace oxygen sensor if faulty"
    ]
},
{
    "conditions": ["lack of HO2S switch sensor indicates lean bank 1 sensor 2", "P1137", "HO2S lean sensor fault"],
    "bullets": [
        "- Condition: Lack of HO2S Switch – Sensor Indicates Lean (Bank 1 Sensor 2)",
        "- Likely Issue: Oxygen sensor after catalytic converter showing lean condition",
        "- Related Issue: Emission control inefficiency",
        "- Suggestion: Inspect sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["HO2S insufficient switching bank 2 sensor 1", "P1153", "oxygen sensor switching fault"],
    "bullets": [
        "- Condition: Heated Oxygen Sensor Insufficient Switching (Bank 2 Sensor 1)",
        "- Likely Issue: Oxygen sensor heater or sensor not switching properly",
        "- Related Issue: Poor emission control and fuel mixture",
        "- Suggestion: Test sensor operation; replace sensor or wiring if faulty"
    ]
},
{
    "conditions": ["HO2S bank 1 sensor 1 trim adaptation", "P1166", "oxygen sensor fuel trim issue"],
    "bullets": [
        "- Condition: HO2S Bank 1 Sensor 1 – Trim Adaptation",
        "- Likely Issue: Fuel trim adaptation issue due to oxygen sensor readings",
        "- Related Issue: Air-fuel ratio imbalances",
        "- Suggestion: Check sensor and fuel system; clean or replace sensor"
    ]
},
{
    "conditions": ["fuel system lean during acceleration bank 1", "P1171", "lean fuel mixture acceleration"],
    "bullets": [
        "- Condition: Fuel System Lean During Acceleration (Bank 1)",
        "- Likely Issue: Insufficient fuel delivery or vacuum leak",
        "- Related Issue: Engine hesitation and power loss during acceleration",
        "- Suggestion: Inspect fuel injectors, fuel pump, and vacuum lines"
    ]
},
{
    "conditions": ["injector control circuit", "P1200", "fuel injector fault"],
    "bullets": [
        "- Condition: Injector Control Circuit",
        "- Likely Issue: Faulty fuel injector or wiring problem",
        "- Related Issue: Misfire or poor engine performance",
        "- Suggestion: Test injector and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["injector control pressure too high", "P1211", "high fuel pressure"],
    "bullets": [
        "- Condition: Injector Control Pressure Too High",
        "- Likely Issue: Fuel pressure regulator malfunction",
        "- Related Issue: Rich running condition, possible fuel leaks",
        "- Suggestion: Check fuel pressure regulator and fuel lines"
    ]
},
{
    "conditions": ["fuel pump feedback circuit", "P1225", "fuel pump feedback fault"],
    "bullets": [
        "- Condition: Fuel Pump Feedback Circuit",
        "- Likely Issue: Feedback circuit malfunction causing fuel pump control issues",
        "- Related Issue: Engine stalling or no-start conditions",
        "- Suggestion: Inspect fuel pump wiring and control module"
    ]
},
{
    "conditions": ["fuel pump driver module disabled", "P1233", "fuel pump driver fault"],
    "bullets": [
        "- Condition: Fuel Pump Driver Module Disabled",
        "- Likely Issue: Fuel pump driver module malfunction or disabled",
        "- Related Issue: Fuel delivery failure",
        "- Suggestion: Diagnose driver module; repair or replace as necessary"
    ]
},
{
    "conditions": ["turbo boost pressure low", "P1247", "low boost pressure"],
    "bullets": [
        "- Condition: Turbo Boost Pressure Low",
        "- Likely Issue: Boost leak, wastegate stuck open, or faulty sensor",
        "- Related Issue: Reduced engine power and performance",
        "- Suggestion: Inspect boost hoses, turbo system, and sensors"
    ]
},
{
    "conditions": ["pressure regulator control solenoid circuit", "P1250", "fuel pressure regulator solenoid fault"],
    "bullets": [
        "- Condition: Pressure Regulator Control Solenoid Circuit",
        "- Likely Issue: Faulty solenoid controlling fuel pressure regulator",
        "- Related Issue: Fuel pressure irregularities",
        "- Suggestion: Check solenoid operation and wiring; replace if faulty"
    ]
},
{
    "conditions": ["theft detected engine disabled", "P1260", "anti-theft system activated"],
    "bullets": [
        "- Condition: Theft Detected – Engine Disabled",
        "- Likely Issue: Anti-theft immobilizer activated",
        "- Related Issue: Engine will not start",
        "- Suggestion: Reset or reprogram anti-theft system; consult dealer"
    ]
},
{
    "conditions": ["cylinder head temperature sensor out of range", "P1288", "overtemperature sensor fault"],
    "bullets": [
        "- Condition: Cylinder Head Temperature Sensor Out of Range",
        "- Likely Issue: Faulty temperature sensor or wiring",
        "- Related Issue: Engine overheating or false temperature readings",
        "- Suggestion: Check sensor and wiring; replace if necessary"
    ]
},
    {
    "conditions": ["cylinder head overtemperature protection active", "P1299", "engine overheating protection"],
    "bullets": [
        "- Condition: Cylinder Head Overtemperature Protection Active",
        "- Likely Issue: Engine temperature exceeding safe limits",
        "- Related Issue: Possible engine damage prevention mode",
        "- Suggestion: Inspect cooling system and sensors immediately"
    ]
},
{
    "conditions": ["ignition signal primary", "P1320", "ignition system fault"],
    "bullets": [
        "- Condition: Ignition Signal Primary Fault",
        "- Likely Issue: Faulty ignition coil or wiring",
        "- Related Issue: Misfire and engine starting problems",
        "- Suggestion: Test ignition coil and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["crankshaft position sensor ref signal", "P1335", "crankshaft sensor fault"],
    "bullets": [
        "- Condition: Crankshaft Position Sensor REF Signal Fault",
        "- Likely Issue: Faulty or intermittent crankshaft position sensor signal",
        "- Related Issue: Engine stalling or no-start",
        "- Suggestion: Inspect sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["camshaft position sensor crankshaft position sensor correlation", "P1345", "sensor correlation fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor / Crankshaft Position Sensor Correlation Fault",
        "- Likely Issue: Timing misalignment or sensor synchronization problem",
        "- Related Issue: Poor engine performance, misfires",
        "- Suggestion: Check timing chain/belt and sensor signals"
    ]
},
{
    "conditions": ["differential pressure feedback sensor circuit high voltage", "P1401", "DPF sensor voltage high"],
    "bullets": [
        "- Condition: Differential Pressure Feedback Sensor Circuit High Voltage",
        "- Likely Issue: Faulty sensor or wiring causing high voltage reading",
        "- Related Issue: Exhaust backpressure monitoring problems",
        "- Suggestion: Inspect sensor wiring and sensor; replace if faulty"
    ]
},
{
    "conditions": ["egr valve pintle position circuit", "P1406", "EGR valve sensor fault"],
    "bullets": [
        "- Condition: EGR Valve Pintle Position Circuit Fault",
        "- Likely Issue: Faulty EGR valve position sensor or wiring",
        "- Related Issue: Emission control and engine performance",
        "- Suggestion: Test valve and sensor; repair or replace as needed"
    ]
},
{
    "conditions": ["secondary air injection system switching valve circuit", "P1410", "secondary air injection valve fault"],
    "bullets": [
        "- Condition: Secondary Air Injection System Switching Valve Circuit Fault",
        "- Likely Issue: Faulty switching valve or wiring",
        "- Related Issue: Emission control inefficiency",
        "- Suggestion: Check valve operation and wiring; repair or replace"
    ]
},
{
    "conditions": ["evap system flow during non-purge condition", "P1441", "evap flow fault"],
    "bullets": [
        "- Condition: EVAP System Flow During Non-Purge Condition",
        "- Likely Issue: Leak or malfunction in EVAP system",
        "- Related Issue: Fuel vapor leak and emission issues",
        "- Suggestion: Inspect EVAP valves and hoses for leaks or faults"
    ]
},
{
    "conditions": ["evap emission control system leak detected", "P1447", "evap system leak"],
    "bullets": [
        "- Condition: EVAP Emission Control System Leak Detected",
        "- Likely Issue: Leak in EVAP system",
        "- Related Issue: Emission failure and fuel odor",
        "- Suggestion: Perform smoke test to locate leaks; repair leaks"
    ]
},
{
    "conditions": ["evap control system leak fuel tank system", "P1456", "fuel tank evap leak"],
    "bullets": [
        "- Condition: EVAP Control System Leak (Fuel Tank System)",
        "- Likely Issue: Leak or faulty component in fuel tank EVAP system",
        "- Related Issue: Fuel vapor leakage",
        "- Suggestion: Inspect fuel tank and hoses; repair or replace faulty parts"
    ]
},
{
    "conditions": ["ldp switch function", "P1470", "load detection switch fault"],
    "bullets": [
        "- Condition: Load Detection (LDP) Switch Function Fault",
        "- Likely Issue: Faulty load detection switch or wiring",
        "- Related Issue: Transmission shifting and load sensing",
        "- Suggestion: Test switch and wiring; replace if necessary"
    ]
},
{
    "conditions": ["idle air control circuit malfunction", "P1504", "idle control fault"],
    "bullets": [
        "- Condition: Idle Air Control Circuit Malfunction",
        "- Likely Issue: Faulty idle air control valve or circuit",
        "- Related Issue: Irregular idle speed",
        "- Suggestion: Check valve operation and wiring; repair or replace"
    ]
},
{
    "conditions": ["throttle actuator control module", "P1516", "throttle control module fault"],
    "bullets": [
        "- Condition: Throttle Actuator Control Module Fault",
        "- Likely Issue: Malfunction in throttle actuator control module",
        "- Related Issue: Throttle response issues",
        "- Suggestion: Diagnose module and wiring; replace if defective"
    ]
},
{
    "conditions": ["variable camshaft timing oil control valve", "P1524", "camshaft timing valve fault"],
    "bullets": [
        "- Condition: Variable Camshaft Timing Oil Control Valve Fault",
        "- Likely Issue: Faulty camshaft timing valve or wiring",
        "- Related Issue: Engine timing and performance issues",
        "- Suggestion: Inspect valve and wiring; clean or replace as needed"
    ]
},
{
    "conditions": ["a/c clutch relay circuit", "P1530", "a/c clutch relay fault"],
    "bullets": [
        "- Condition: A/C Clutch Relay Circuit Fault",
        "- Likely Issue: Faulty relay or wiring for A/C clutch",
        "- Related Issue: Air conditioning system failure",
        "- Suggestion: Test relay and wiring; replace if faulty"
    ]
},
{
    "conditions": ["power steering pressure sensor circuit malfunction", "P1550", "power steering pressure sensor fault"],
    "bullets": [
        "- Condition: Power Steering Pressure Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Power steering assistance issues",
        "- Suggestion: Check sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["battery voltage too low", "P1602", "low battery voltage"],
    "bullets": [
        "- Condition: Battery Voltage Too Low",
        "- Likely Issue: Weak or discharged battery",
        "- Related Issue: Starting and electrical issues",
        "- Suggestion: Test battery and charging system; recharge or replace battery"
    ]
},
{
    "conditions": ["ecm backup circuit", "P1603", "ecm backup power fault"],
    "bullets": [
        "- Condition: ECM Backup Circuit Fault",
        "- Likely Issue: Fault in ECM backup power supply",
        "- Related Issue: Engine control module stability",
        "- Suggestion: Inspect ECM power and ground connections"
    ]
},
{
    "conditions": ["theft deterrent fuel enable signal not received", "P1626", "anti-theft fuel enable fault"],
    "bullets": [
        "- Condition: Theft Deterrent Fuel Enable Signal Not Received",
        "- Likely Issue: Anti-theft system communication fault",
        "- Related Issue: Engine fuel disable",
        "- Suggestion: Reset or repair anti-theft system"
    ]
},
{
    "conditions": ["theft deterrent start enable signal not correct", "P1631", "anti-theft start enable fault"],
    "bullets": [
        "- Condition: Theft Deterrent Start Enable Signal Not Correct",
        "- Likely Issue: Anti-theft system start enable signal fault",
        "- Related Issue: Engine start disable",
        "- Suggestion: Diagnose anti-theft system and repair"
    ]
},
{
    "conditions": ["ignition 1 switch circuit 2 fault", "P1682", "ignition switch fault"],
    "bullets": [
        "- Condition: Ignition 1 Switch Circuit 2 Fault",
        "- Likely Issue: Fault in ignition switch circuit",
        "- Related Issue: Starting or ignition issues",
        "- Suggestion: Check ignition switch wiring and contacts"
    ]
},
{
    "conditions": ["battery disconnected last 50 starts", "P1684", "battery disconnect history"],
    "bullets": [
        "- Condition: Battery Disconnected (Last 50 Starts)",
        "- Likely Issue: Battery was disconnected recently",
        "- Related Issue: Possible resetting of ECU data",
        "- Suggestion: Verify battery connections"
    ]
},
{
    "conditions": ["throttle position sensor circuit malfunction transmission related", "P1705", "transmission throttle sensor fault"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit Malfunction (Transmission Related)",
        "- Likely Issue: Faulty throttle position sensor circuit affecting transmission",
        "- Related Issue: Transmission shift problems",
        "- Suggestion: Check throttle sensor wiring and connections"
    ]
},
{
    "conditions": ["torque converter clutch or overdrive solenoid performance", "P1740", "TCC solenoid fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch or Overdrive Solenoid Performance Fault",
        "- Likely Issue: Faulty torque converter clutch solenoid or overdrive solenoid",
        "- Related Issue: Transmission slipping, harsh shifting",
        "- Suggestion: Test solenoid operation and wiring; replace if faulty"
    ]
},
{
    "conditions": ["shift solenoid malfunction", "P1751", "shift solenoid fault"],
    "bullets": [
        "- Condition: Shift Solenoid Malfunction",
        "- Likely Issue: Faulty shift solenoid or wiring",
        "- Related Issue: Improper gear shifting",
        "- Suggestion: Diagnose and replace defective solenoid or repair wiring"
    ]
},
{
    "conditions": ["overrun clutch solenoid circuit malfunction", "P1760", "overrun clutch solenoid fault"],
    "bullets": [
        "- Condition: Overrun Clutch Solenoid Circuit Malfunction",
        "- Likely Issue: Faulty solenoid or circuit controlling overrun clutch",
        "- Related Issue: Transmission slipping or failure to shift properly",
        "- Suggestion: Check solenoid and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["solenoid switch valve latched in LR position", "P1776", "solenoid valve latch fault"],
    "bullets": [
        "- Condition: Solenoid Switch Valve Latched in Low/Reverse Position",
        "- Likely Issue: Solenoid valve stuck in low/reverse position",
        "- Related Issue: Transmission stuck in low gear or reverse",
        "- Suggestion: Inspect solenoid valve and control circuitry; clean or replace"
    ]
},
{
    "conditions": ["park neutral position switch malfunction", "P1780", "PNP switch fault"],
    "bullets": [
        "- Condition: Park/Neutral Position Switch Malfunction",
        "- Likely Issue: Faulty PNP switch or wiring",
        "- Related Issue: Transmission starting or shift issues",
        "- Suggestion: Test and replace PNP switch or repair wiring"
    ]
},
{
    "conditions": ["fault immediately after shift", "P1790", "post-shift fault"],
    "bullets": [
        "- Condition: Fault Immediately After Shift",
        "- Likely Issue: Transmission fault detected just after gear change",
        "- Related Issue: Harsh or delayed shifting",
        "- Suggestion: Diagnose transmission control module and solenoids"
    ]
},
{
    "conditions": ["transmission fluid pressure switch assembly", "P1810", "fluid pressure switch fault"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Switch Assembly Fault",
        "- Likely Issue: Faulty pressure switch or circuit",
        "- Related Issue: Transmission shifting or pressure regulation problems",
        "- Suggestion: Test pressure switch and replace if faulty"
    ]
},
{
    "conditions": ["TCC PWM solenoid circuit electrical", "P1860", "torque converter clutch PWM solenoid electrical fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch PWM Solenoid Circuit Electrical Fault",
        "- Likely Issue: Electrical fault in torque converter clutch PWM solenoid circuit",
        "- Related Issue: Torque converter clutch not engaging properly",
        "- Suggestion: Check wiring, connectors, and solenoid; repair or replace"
    ]
},
    {
    "conditions": ["transmission component slipping", "P1870", "transmission slipping"],
    "bullets": [
        "- Condition: Transmission Component Slipping",
        "- Likely Issue: Worn or damaged transmission components causing slipping",
        "- Related Issue: Loss of power and irregular gear engagement",
        "- Suggestion: Inspect transmission internals and check fluid level and quality"
    ]
},
{
    "conditions": ["transmission performance degraded", "P1890", "degraded transmission performance"],
    "bullets": [
        "- Condition: Transmission Performance Degraded",
        "- Likely Issue: General transmission malfunction or wear",
        "- Related Issue: Reduced drivability and responsiveness",
        "- Suggestion: Perform comprehensive transmission diagnostics"
    ]
},
{
    "conditions": ["throttle actuator control motor circuit range performance", "P2101", "throttle actuator motor fault"],
    "bullets": [
        "- Condition: Throttle Actuator Control Motor Circuit Range/Performance Fault",
        "- Likely Issue: Fault in throttle actuator motor circuit causing limited throttle control",
        "- Related Issue: Reduced engine power or hesitation",
        "- Suggestion: Inspect throttle actuator and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["throttle actuator control system forced limited power", "P2106", "throttle control system limp mode"],
    "bullets": [
        "- Condition: Throttle Actuator Control System Forced Limited Power",
        "- Likely Issue: System detected critical fault, forcing engine into limp mode",
        "- Related Issue: Severely limited engine power for safety",
        "- Suggestion: Scan for related faults; repair throttle system components"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit", "P0711", "transmission fluid temp sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty temperature sensor or wiring in transmission fluid sensor circuit",
        "- Related Issue: Incorrect transmission fluid temperature readings affecting shifting",
        "- Suggestion: Test sensor and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["transmission input speed sensor circuit", "P0715", "input speed sensor fault"],
    "bullets": [
        "- Condition: Transmission Input Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty input speed sensor or wiring",
        "- Related Issue: Incorrect speed data affecting gear shifts",
        "- Suggestion: Inspect sensor and wiring; replace faulty components"
    ]
},
{
    "conditions": ["transmission output speed sensor circuit", "P0720", "output speed sensor fault"],
    "bullets": [
        "- Condition: Transmission Output Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty output speed sensor or wiring",
        "- Related Issue: Transmission shifting irregularities and speedometer issues",
        "- Suggestion: Test sensor and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["torque converter clutch solenoid stuck open", "torque converter clutch slipping", "transmission slip"],
    "bullets": [
        "- Condition: Torque Converter Clutch Solenoid Stuck Open",
        "- Likely Issue: TCC solenoid failing to engage properly",
        "- Related Issue: Transmission slipping, poor fuel efficiency",
        "- Suggestion: Test TCC solenoid; clean or replace if faulty"
    ]
},
{
    "conditions": ["pressure control solenoid malfunction", "P0746", "pressure control solenoid performance"],
    "bullets": [
        "- Condition: Pressure Control Solenoid Malfunction",
        "- Likely Issue: Faulty pressure control solenoid or wiring",
        "- Related Issue: Transmission pressure irregularities causing shifting issues",
        "- Suggestion: Inspect solenoid and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit", "P0711", "transmission fluid temp sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty transmission fluid temperature sensor or wiring",
        "- Related Issue: Incorrect transmission fluid temperature readings causing shift timing errors",
        "- Suggestion: Test sensor and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["transmission input speed sensor circuit", "P0715", "input speed sensor fault"],
    "bullets": [
        "- Condition: Transmission Input Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty input speed sensor or wiring",
        "- Related Issue: Erratic or incorrect gear shifts due to inaccurate speed data",
        "- Suggestion: Inspect sensor and wiring; replace faulty components"
    ]
},
{
    "conditions": ["transmission output speed sensor circuit", "P0720", "output speed sensor fault"],
    "bullets": [
        "- Condition: Transmission Output Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty output speed sensor or wiring",
        "- Related Issue: Transmission slipping, inaccurate speedometer readings",
        "- Suggestion: Test sensor and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["torque converter clutch solenoid stuck open", "torque converter clutch slipping", "transmission slip"],
    "bullets": [
        "- Condition: Torque Converter Clutch Solenoid Stuck Open",
        "- Likely Issue: Torque converter clutch solenoid failing to engage properly",
        "- Related Issue: Transmission slipping, decreased fuel economy, poor acceleration",
        "- Suggestion: Test TCC solenoid; clean or replace if faulty"
    ]
},
{
    "conditions": ["pressure control solenoid malfunction", "P0746", "pressure control solenoid performance"],
    "bullets": [
        "- Condition: Pressure Control Solenoid Malfunction",
        "- Likely Issue: Faulty pressure control solenoid or wiring",
        "- Related Issue: Erratic transmission pressure leading to shifting problems",
        "- Suggestion: Inspect solenoid and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["shift solenoid b stuck open", "transmission shifting fault"],
    "bullets": [
        "- Condition: Shift Solenoid B Stuck Open",
        "- Likely Issue: Shift solenoid B is malfunctioning or stuck open",
        "- Related Issue: Harsh or delayed gear shifting",
        "- Suggestion: Diagnose solenoid operation; clean or replace as necessary"
    ]
},
{
    "conditions": ["transmission range sensor malfunction", "P0705", "transmission range sensor fault"],
    "bullets": [
        "- Condition: Transmission Range Sensor Circuit Malfunction",
        "- Likely Issue: Faulty transmission range sensor or wiring",
        "- Related Issue: Incorrect gear selection, no start or no shift conditions",
        "- Suggestion: Test sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["clutch pressure control valve malfunction", "clutch slipping", "transmission issues"],
    "bullets": [
        "- Condition: Clutch Pressure Control Valve Malfunction",
        "- Likely Issue: Faulty valve causing insufficient clutch pressure",
        "- Related Issue: Clutch slipping, delayed or rough shifting",
        "- Suggestion: Inspect valve; repair or replace if faulty"
    ]
},
{
    "conditions": ["hydraulic control unit malfunction", "transmission hydraulic fault"],
    "bullets": [
        "- Condition: Hydraulic Control Unit Malfunction",
        "- Likely Issue: Faulty hydraulic control unit or solenoids",
        "- Related Issue: Transmission shifting irregularities, failure to engage gears",
        "- Suggestion: Diagnose hydraulic control unit; repair or replace as needed"
    ]
},
{
    "conditions": ["transmission fluid level low", "transmission overheating", "slipping gears"],
    "bullets": [
        "- Condition: Transmission Fluid Level Low",
        "- Likely Issue: Insufficient transmission fluid causing overheating and slipping",
        "- Related Issue: Gear slipping, harsh shifting, potential transmission damage",
        "- Suggestion: Check and top up transmission fluid; inspect for leaks"
    ]
},
{
    "conditions": ["transmission fluid contamination", "dirty transmission fluid", "slipping transmission"],
    "bullets": [
        "- Condition: Transmission Fluid Contamination",
        "- Likely Issue: Dirty or degraded transmission fluid reducing lubrication",
        "- Related Issue: Gear slipping, overheating, increased wear",
        "- Suggestion: Flush transmission fluid; replace filter and refill"
    ]
},
{
    "conditions": ["transmission control module (TCM) failure", "P1893", "transmission control module fault"],
    "bullets": [
        "- Condition: Transmission Control Module Failure",
        "- Likely Issue: TCM malfunction or communication failure",
        "- Related Issue: Erratic shifting, limp mode, transmission warning light",
        "- Suggestion: Scan and diagnose TCM; repair or replace module"
    ]
},
{
    "conditions": ["shift solenoid c stuck closed", "gear shifting failure"],
    "bullets": [
        "- Condition: Shift Solenoid C Stuck Closed",
        "- Likely Issue: Shift solenoid C stuck closed preventing proper gear changes",
        "- Related Issue: Transmission stuck in gear, harsh shifting",
        "- Suggestion: Test solenoid operation; repair or replace as necessary"
    ]
},
{
    "conditions": ["transmission oil pump failure", "loss of hydraulic pressure", "gear slipping"],
    "bullets": [
        "- Condition: Transmission Oil Pump Failure",
        "- Likely Issue: Oil pump malfunction causing loss of hydraulic pressure",
        "- Related Issue: Gear slipping, failure to shift, transmission overheating",
        "- Suggestion: Inspect and repair or replace oil pump"
    ]
},
{
    "conditions": ["clutch actuator failure", "clutch won't engage", "transmission shifting issues"],
    "bullets": [
        "- Condition: Clutch Actuator Failure",
        "- Likely Issue: Faulty clutch actuator or control circuit",
        "- Related Issue: Clutch disengagement failure, gear shifting problems",
        "- Suggestion: Diagnose actuator and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["solenoid valve stuck in low gear", "P1776", "solenoid valve latch fault"],
    "bullets": [
        "- Condition: Solenoid Valve Latched in Low/Reverse Position",
        "- Likely Issue: Solenoid valve stuck preventing shifting out of low gear",
        "- Related Issue: Transmission stuck in low gear or reverse",
        "- Suggestion: Inspect solenoid and control wiring; clean or replace"
    ]
},
{
    "conditions": ["transmission clutch pack wear", "slipping transmission", "gear engagement failure"],
    "bullets": [
        "- Condition: Transmission Clutch Pack Wear",
        "- Likely Issue: Worn clutch packs causing slipping and poor gear engagement",
        "- Related Issue: Loss of power, harsh shifting",
        "- Suggestion: Inspect clutch packs; rebuild or replace transmission components"
    ]
},
{
    "conditions": ["throttle position sensor signal out of range", "P0122", "TPS low voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Signal Low",
        "- Likely Issue: Faulty TPS or wiring causing low voltage signal",
        "- Related Issue: Poor throttle response, engine hesitation",
        "- Suggestion: Test TPS and wiring; repair or replace sensor"
    ]
},
{
    "conditions": ["throttle position sensor signal high", "P0123", "TPS high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Signal High",
        "- Likely Issue: Faulty TPS or wiring causing high voltage signal",
        "- Related Issue: Erratic throttle response, possible limp mode",
        "- Suggestion: Inspect TPS and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["vehicle speed sensor malfunction", "P0500", "speed sensor fault"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Malfunction",
        "- Likely Issue: Faulty speed sensor or wiring",
        "- Related Issue: Speedometer inaccuracies, transmission shifting issues",
        "- Suggestion: Test speed sensor and wiring; repair or replace sensor"
    ]
},
{
    "conditions": ["transmission input speed sensor intermittent", "P0716", "input speed sensor intermittent fault"],
    "bullets": [
        "- Condition: Transmission Input Speed Sensor Intermittent",
        "- Likely Issue: Intermittent fault or wiring issue with input speed sensor",
        "- Related Issue: Erratic shifting, transmission hesitation",
        "- Suggestion: Inspect sensor wiring and connector; replace sensor if necessary"
    ]
},
{
    "conditions": ["transmission output speed sensor intermittent", "P0725", "output speed sensor intermittent fault"],
    "bullets": [
        "- Condition: Transmission Output Speed Sensor Intermittent",
        "- Likely Issue: Intermittent wiring or sensor failure",
        "- Related Issue: Transmission shift irregularities, speedometer errors",
        "- Suggestion: Test wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor circuit low", "P0795", "pressure sensor low voltage"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor Circuit Low Voltage",
        "- Likely Issue: Sensor output below expected range or wiring issue",
        "- Related Issue: Improper pressure regulation affecting shifting",
        "- Suggestion: Inspect sensor and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["shift solenoid e stuck off", "transmission shifting failure"],
    "bullets": [
        "- Condition: Shift Solenoid E Stuck Off",
        "- Likely Issue: Faulty or stuck solenoid E",
        "- Related Issue: Transmission fails to shift properly",
        "- Suggestion: Test solenoid; clean or replace if faulty"
    ]
},
{
    "conditions": ["transmission control module power supply fault", "P1601", "TCM power issue"],
    "bullets": [
        "- Condition: Transmission Control Module Power Supply Fault",
        "- Likely Issue: Power supply problem to TCM",
        "- Related Issue: Transmission control failure, shifting issues",
        "- Suggestion: Check TCM power and ground circuits; repair wiring"
    ]
},
{
    "conditions": ["transmission range sensor circuit low", "P0706", "range sensor low voltage"],
    "bullets": [
        "- Condition: Transmission Range Sensor Circuit Low Voltage",
        "- Likely Issue: Low voltage or wiring fault in transmission range sensor",
        "- Related Issue: Incorrect gear detection, shifting issues",
        "- Suggestion: Inspect sensor wiring; repair or replace sensor"
    ]
},
{
    "conditions": ["clutch pedal position sensor malfunction", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Pedal Position Sensor Malfunction",
        "- Likely Issue: Faulty sensor or wiring affecting clutch engagement signals",
        "- Related Issue: Transmission unable to detect clutch position properly",
        "- Suggestion: Test sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["hydraulic pressure sensor circuit low", "transmission hydraulic fault"],
    "bullets": [
        "- Condition: Hydraulic Pressure Sensor Circuit Low",
        "- Likely Issue: Low signal or wiring issue from hydraulic pressure sensor",
        "- Related Issue: Poor hydraulic pressure monitoring affecting shifting",
        "- Suggestion: Check sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["torque converter clutch solenoid circuit open", "P0741", "TCC solenoid circuit open"],
    "bullets": [
        "- Condition: Torque Converter Clutch Solenoid Circuit Open",
        "- Likely Issue: Open or broken circuit in TCC solenoid wiring",
        "- Related Issue: TCC fails to engage, causing slipping and poor fuel economy",
        "- Suggestion: Inspect wiring; repair or replace circuit and solenoid"
    ]
},
{
    "conditions": ["shift solenoid a control circuit open", "P0751", "solenoid A circuit open"],
    "bullets": [
        "- Condition: Shift Solenoid A Control Circuit Open",
        "- Likely Issue: Open circuit or wiring break in solenoid A control",
        "- Related Issue: Gear shifting failures",
        "- Suggestion: Diagnose wiring; repair or replace solenoid and connectors"
    ]
},
{
    "conditions": ["shift solenoid b control circuit low", "P0756", "solenoid B low voltage"],
    "bullets": [
        "- Condition: Shift Solenoid B Control Circuit Low",
        "- Likely Issue: Weak voltage or wiring problem in solenoid B control circuit",
        "- Related Issue: Transmission fails to shift properly",
        "- Suggestion: Inspect wiring and connectors; repair or replace as needed"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit intermittent", "P0712", "transmission fluid temp sensor intermittent"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Intermittent",
        "- Likely Issue: Intermittent sensor signal or wiring problem",
        "- Related Issue: Transmission shift timing issues and overheating risk",
        "- Suggestion: Check sensor and wiring; repair or replace faulty parts"
    ]
},
{
    "conditions": ["transmission pressure control solenoid malfunction", "P0746", "pressure control solenoid fault"],
    "bullets": [
        "- Condition: Transmission Pressure Control Solenoid Malfunction",
        "- Likely Issue: Faulty solenoid or wiring causing pressure control problems",
        "- Related Issue: Harsh shifting and slipping",
        "- Suggestion: Test solenoid and wiring; clean or replace"
    ]
},
{
    "conditions": ["clutch position sensor circuit intermittent", "clutch engagement irregular"],
    "bullets": [
        "- Condition: Clutch Position Sensor Circuit Intermittent",
        "- Likely Issue: Intermittent sensor or wiring fault affecting clutch operation",
        "- Related Issue: Erratic clutch engagement",
        "- Suggestion: Inspect sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["shift solenoid d control circuit open", "P0766", "solenoid D circuit open"],
    "bullets": [
        "- Condition: Shift Solenoid D Control Circuit Open",
        "- Likely Issue: Open or broken wiring in solenoid D control circuit",
        "- Related Issue: Transmission shifting problems",
        "- Suggestion: Check wiring; repair or replace solenoid and connectors"
    ]
},
{
    "conditions": ["transmission torque converter clutch stuck on", "engine stall risk", "harsh shifting"],
    "bullets": [
        "- Condition: Torque Converter Clutch Stuck On",
        "- Likely Issue: Solenoid stuck engaged causing clutch lockup",
        "- Related Issue: Engine stalls at stop, harsh or abrupt shifting",
        "- Suggestion: Inspect and test solenoid and control circuit; repair or replace"
    ]
},
{
    "conditions": ["transmission fluid pump pressure low", "P1811", "fluid pump low pressure"],
    "bullets": [
        "- Condition: Transmission Fluid Pump Pressure Low",
        "- Likely Issue: Failing fluid pump or obstruction causing low pressure",
        "- Related Issue: Slipping gears, transmission overheating",
        "- Suggestion: Diagnose fluid pump and hydraulic system; repair or replace"
    ]
},
{
    "conditions": ["park neutral position switch circuit low", "P1785", "PNP switch low voltage"],
    "bullets": [
        "- Condition: Park/Neutral Position Switch Circuit Low Voltage",
        "- Likely Issue: Low voltage or wiring issue in PNP switch circuit",
        "- Related Issue: Transmission starting or shifting issues",
        "- Suggestion: Inspect wiring and switch; repair or replace"
    ]
},
{
    "conditions": ["clutch pedal switch circuit open", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Pedal Switch Circuit Open",
        "- Likely Issue: Open circuit in clutch pedal switch wiring",
        "- Related Issue: Transmission control unable to detect clutch pedal position",
        "- Suggestion: Test wiring and switch; repair or replace"
    ]
},
{
    "conditions": ["pressure control solenoid c control circuit low", "transmission pressure control low signal"],
    "bullets": [
        "- Condition: Pressure Control Solenoid C Control Circuit Low",
        "- Likely Issue: Low voltage or weak signal in solenoid C control circuit",
        "- Related Issue: Transmission pressure regulation failure",
        "- Suggestion: Inspect wiring and solenoid; repair or replace"
    ]
},
{
    "conditions": ["clutch actuator circuit short to ground", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Actuator Circuit Short to Ground",
        "- Likely Issue: Short circuit in clutch actuator wiring",
        "- Related Issue: Clutch actuator malfunction causing engagement problems",
        "- Suggestion: Inspect wiring harness for shorts; repair or replace damaged wiring"
    ]
},
{
    "conditions": ["torque converter clutch relay circuit fault", "P0747", "TCC relay fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch Relay Circuit Fault",
        "- Likely Issue: Faulty relay or wiring in TCC relay circuit",
        "- Related Issue: Torque converter clutch engagement failure",
        "- Suggestion: Test relay and circuit; replace relay or repair wiring"
    ]
},
{
    "conditions": ["shift solenoid f performance stuck off", "transmission shifting issues"],
    "bullets": [
        "- Condition: Shift Solenoid F Performance/Stuck Off",
        "- Likely Issue: Malfunction or stuck shift solenoid F",
        "- Related Issue: Gear shifting problems and delayed engagement",
        "- Suggestion: Test solenoid; clean or replace if necessary"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit high", "P0713", "transmission fluid temperature sensor high voltage"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit High Voltage",
        "- Likely Issue: High voltage signal from fluid temperature sensor circuit",
        "- Related Issue: Transmission overheating warning or improper shifting",
        "- Suggestion: Inspect sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["pressure control solenoid d control circuit intermittent", "transmission pressure control fault"],
    "bullets": [
        "- Condition: Pressure Control Solenoid D Control Circuit Intermittent",
        "- Likely Issue: Intermittent wiring fault in solenoid D control circuit",
        "- Related Issue: Erratic transmission pressure control causing shifting issues",
        "- Suggestion: Check wiring and connectors; repair or replace"
    ]
},
{
    "conditions": ["transmission input speed sensor circuit no signal", "P0715", "input speed sensor no signal"],
    "bullets": [
        "- Condition: Transmission Input Speed Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring open circuit",
        "- Related Issue: Transmission shifting malfunction and limp mode",
        "- Suggestion: Test sensor and wiring; replace sensor or repair wiring"
    ]
},
{
    "conditions": ["shift solenoid g control circuit high", "transmission shifting fault"],
    "bullets": [
        "- Condition: Shift Solenoid G Control Circuit High Voltage",
        "- Likely Issue: Excessive voltage signal to solenoid G",
        "- Related Issue: Gear shifting problems",
        "- Suggestion: Inspect wiring and solenoid; repair or replace as necessary"
    ]
},
{
    "conditions": ["clutch pressure sensor circuit range/performance", "clutch engagement inconsistency"],
    "bullets": [
        "- Condition: Clutch Pressure Sensor Circuit Range/Performance",
        "- Likely Issue: Sensor output out of expected range or degraded performance",
        "- Related Issue: Erratic clutch engagement and shifting issues",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor switch a range/performance", "transmission pressure sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor/Switch A Range/Performance",
        "- Likely Issue: Sensor output outside normal range",
        "- Related Issue: Transmission pressure monitoring and control faults",
        "- Suggestion: Inspect sensor function; replace if needed"
    ]
},
{
    "conditions": ["transmission control module internal failure", "P1600", "TCM internal fault"],
    "bullets": [
        "- Condition: Transmission Control Module Internal Failure",
        "- Likely Issue: Internal malfunction of TCM",
        "- Related Issue: Transmission shifting irregularities or failure",
        "- Suggestion: Scan and replace TCM if confirmed faulty"
    ]
},
{
    "conditions": ["pressure control solenoid e performance stuck off", "transmission pressure control fault"],
    "bullets": [
        "- Condition: Pressure Control Solenoid E Performance/Stuck Off",
        "- Likely Issue: Faulty pressure control solenoid E",
        "- Related Issue: Pressure control failure causing shifting issues",
        "- Suggestion: Test and replace solenoid as needed"
    ]
},
{
    "conditions": ["torque converter clutch solenoid stuck on", "P0740", "TCC solenoid stuck engaged"],
    "bullets": [
        "- Condition: Torque Converter Clutch Solenoid Stuck On",
        "- Likely Issue: Solenoid stuck in engaged position",
        "- Related Issue: Harsh shifting, engine stalling at idle",
        "- Suggestion: Diagnose solenoid and wiring; clean or replace"
    ]
},
{
    "conditions": ["transmission fluid pump circuit open", "transmission fluid pump fault"],
    "bullets": [
        "- Condition: Transmission Fluid Pump Circuit Open",
        "- Likely Issue: Open wiring or circuit fault in transmission fluid pump control",
        "- Related Issue: Low fluid pressure, slipping, overheating",
        "- Suggestion: Inspect wiring and pump; repair or replace as needed"
    ]
},
{
    "conditions": ["clutch pedal position sensor circuit low voltage", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Pedal Position Sensor Circuit Low Voltage",
        "- Likely Issue: Low voltage signal or wiring fault",
        "- Related Issue: Incorrect clutch position readings causing shifting problems",
        "- Suggestion: Test sensor wiring; repair or replace sensor"
    ]
},
{
    "conditions": ["shift solenoid h control circuit open", "transmission shifting fault"],
    "bullets": [
        "- Condition: Shift Solenoid H Control Circuit Open",
        "- Likely Issue: Open or broken circuit in solenoid H wiring",
        "- Related Issue: Transmission shifting failures",
        "- Suggestion: Test wiring and solenoid; repair or replace"
    ]
},
{
    "conditions": ["clutch pedal position sensor circuit intermittent", "clutch engagement inconsistent"],
    "bullets": [
        "- Condition: Clutch Pedal Position Sensor Circuit Intermittent",
        "- Likely Issue: Intermittent wiring fault or sensor malfunction",
        "- Related Issue: Unpredictable clutch operation affecting shifting",
        "- Suggestion: Inspect wiring and sensor; repair or replace as necessary"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit low", "P0714", "transmission fluid temperature sensor low voltage"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Low Voltage",
        "- Likely Issue: Low voltage or short in sensor circuit",
        "- Related Issue: Incorrect transmission fluid temperature readings",
        "- Suggestion: Test sensor wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["shift solenoid b control circuit intermittent", "transmission shifting problem"],
    "bullets": [
        "- Condition: Shift Solenoid B Control Circuit Intermittent",
        "- Likely Issue: Intermittent wiring fault affecting solenoid B",
        "- Related Issue: Erratic gear shifting and transmission issues",
        "- Suggestion: Inspect and repair wiring; replace solenoid if faulty"
    ]
},
{
    "conditions": ["torque converter clutch circuit stuck on", "P0741", "TCC circuit stuck engaged"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Stuck On",
        "- Likely Issue: Solenoid or circuit stuck in engaged position",
        "- Related Issue: Transmission harsh shifting, engine stall risk",
        "- Suggestion: Check solenoid operation and wiring; clean or replace"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor switch d range performance", "transmission pressure sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor/Switch D Range/Performance",
        "- Likely Issue: Sensor output outside normal parameters",
        "- Related Issue: Transmission pressure regulation problems",
        "- Suggestion: Test sensor function; replace if necessary"
    ]
},
{
    "conditions": ["clutch actuator circuit short to battery", "clutch actuator malfunction"],
    "bullets": [
        "- Condition: Clutch Actuator Circuit Short to Battery",
        "- Likely Issue: Short circuit in clutch actuator wiring to positive voltage",
        "- Related Issue: Clutch actuator failure or damage",
        "- Suggestion: Inspect wiring for shorts; repair or replace damaged harness"
    ]
},
{
    "conditions": ["shift solenoid e performance stuck on", "transmission shifting issues"],
    "bullets": [
        "- Condition: Shift Solenoid E Performance/Stuck On",
        "- Likely Issue: Solenoid stuck in energized position",
        "- Related Issue: Delayed or harsh shifting",
        "- Suggestion: Test solenoid and wiring; clean or replace"
    ]
},
{
    "conditions": ["torque converter clutch circuit stuck off", "P0746", "TCC circuit stuck disengaged"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Stuck Off",
        "- Likely Issue: Solenoid stuck off or circuit failure",
        "- Related Issue: Reduced fuel efficiency and transmission slippage",
        "- Suggestion: Diagnose solenoid and circuit; repair or replace"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor switch e circuit malfunction", "transmission pressure sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor/Switch E Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring causing incorrect readings",
        "- Related Issue: Transmission pressure monitoring errors",
        "- Suggestion: Inspect sensor and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["shift solenoid d control circuit low", "transmission shifting fault"],
    "bullets": [
        "- Condition: Shift Solenoid D Control Circuit Low Voltage",
        "- Likely Issue: Weak voltage signal to solenoid D",
        "- Related Issue: Gear shifting problems",
        "- Suggestion: Check wiring and connectors; repair or replace faulty components"
    ]
},
{
    "conditions": ["clutch position sensor circuit open", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Position Sensor Circuit Open",
        "- Likely Issue: Open circuit or broken wiring in clutch position sensor",
        "- Related Issue: Clutch operation and shifting irregularities",
        "- Suggestion: Inspect wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["transmission control module power relay fault", "P1604", "TCM power relay fault"],
    "bullets": [
        "- Condition: Transmission Control Module Power Relay Fault",
        "- Likely Issue: Faulty power relay supplying the TCM",
        "- Related Issue: Transmission control failures or no start conditions",
        "- Suggestion: Test relay and circuit; replace relay if defective"
    ]
},
{
    "conditions": ["shift solenoid h performance stuck off", "transmission shifting issues"],
    "bullets": [
        "- Condition: Shift Solenoid H Performance/Stuck Off",
        "- Likely Issue: Malfunction or stuck solenoid H",
        "- Related Issue: Gear shifting delays or failure",
        "- Suggestion: Test solenoid; clean or replace if needed"
    ]
},
{
    "conditions": ["hydraulic pressure sensor circuit low", "hydraulic pressure warning"],
    "bullets": [
        "- Condition: Hydraulic Pressure Sensor Circuit Low Voltage",
        "- Likely Issue: Low voltage or sensor failure",
        "- Related Issue: Transmission hydraulic system malfunction",
        "- Suggestion: Inspect sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["transmission fluid level sensor circuit malfunction", "transmission fluid monitoring fault"],
    "bullets": [
        "- Condition: Transmission Fluid Level Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring causing incorrect fluid level readings",
        "- Related Issue: Transmission overheating or slipping",
        "- Suggestion: Test sensor and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["clutch pedal switch a circuit fault", "clutch pedal malfunction"],
    "bullets": [
        "- Condition: Clutch Pedal Switch “A” Circuit Fault",
        "- Likely Issue: Faulty switch or wiring affecting clutch pedal signals",
        "- Related Issue: Transmission shifting or starting issues",
        "- Suggestion: Test switch and wiring; replace switch if defective"
    ]
},
{
    "conditions": ["transmission range sensor circuit malfunction", "P0705", "transmission range sensor fault"],
    "bullets": [
        "- Condition: Transmission Range Sensor Circuit Malfunction",
        "- Likely Issue: Faulty transmission range sensor or wiring",
        "- Related Issue: Gear selection issues, shifting faults",
        "- Suggestion: Inspect sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["throttle position sensor circuit low input", "P0122", "throttle position sensor low voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit Low Input",
        "- Likely Issue: Sensor voltage below expected range",
        "- Related Issue: Poor throttle response, stalling",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["manifold absolute pressure sensor circuit intermittent", "P0106", "MAP sensor intermittent fault"],
    "bullets": [
        "- Condition: Manifold Absolute Pressure Sensor Circuit Intermittent",
        "- Likely Issue: Intermittent wiring or sensor failure",
        "- Related Issue: Engine performance issues, fluctuating idle",
        "- Suggestion: Inspect wiring and sensor; replace as necessary"
    ]
},
{
    "conditions": ["oxygen sensor heater circuit malfunction bank 1 sensor 2", "P0141", "O2 sensor heater fault"],
    "bullets": [
        "- Condition: Oxygen Sensor Heater Circuit Malfunction (Bank 1 Sensor 2)",
        "- Likely Issue: Faulty heater element or wiring",
        "- Related Issue: Poor fuel economy, emission issues",
        "- Suggestion: Check sensor heater circuit; replace sensor if faulty"
    ]
},
{
    "conditions": ["evaporative emission control system leak detected large leak", "P0456", "EVAP system small leak"],
    "bullets": [
        "- Condition: EVAP System Leak Detected (Small Leak)",
        "- Likely Issue: Leak in EVAP hoses, purge valve, or fuel cap",
        "- Related Issue: Fuel vapor leak, emission failure",
        "- Suggestion: Inspect EVAP components; tighten or replace faulty parts"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit malfunction", "P0500", "speed sensor fault"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty speed sensor or wiring",
        "- Related Issue: Speedometer issues, transmission shifting faults",
        "- Suggestion: Test sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["intake air temperature sensor circuit high voltage", "P0111", "intake air temp sensor high voltage"],
    "bullets": [
        "- Condition: Intake Air Temperature Sensor Circuit High Voltage",
        "- Likely Issue: Short or wiring fault causing high voltage",
        "- Related Issue: Incorrect air temperature readings affecting fuel mixture",
        "- Suggestion: Inspect sensor wiring; repair or replace sensor"
    ]
},
{
    "conditions": ["mass air flow sensor circuit low voltage", "P0102", "MAF sensor low voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Low Voltage",
        "- Likely Issue: Sensor or wiring fault causing low signal",
        "- Related Issue: Engine performance issues, poor fuel economy",
        "- Suggestion: Test MAF sensor and wiring; clean or replace as needed"
    ]
},
{
    "conditions": ["fuel pressure regulator control circuit", "P1250", "fuel pressure regulator solenoid fault"],
    "bullets": [
        "- Condition: Fuel Pressure Regulator Control Circuit Fault",
        "- Likely Issue: Faulty solenoid or wiring",
        "- Related Issue: Fuel pressure inconsistencies",
        "- Suggestion: Test solenoid and wiring; repair or replace faulty parts"
    ]
},
{
    "conditions": ["exhaust gas recirculation sensor circuit high", "P1401", "EGR sensor circuit high voltage"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Sensor Circuit High Voltage",
        "- Likely Issue: Sensor or wiring failure causing high voltage signal",
        "- Related Issue: Emission control issues, rough idle",
        "- Suggestion: Inspect wiring and sensor; repair or replace as necessary"
    ]
},
{
    "conditions": ["knock sensor circuit malfunction", "P0325", "knock sensor fault"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Malfunction",
        "- Likely Issue: Faulty knock sensor or wiring",
        "- Related Issue: Engine knocking, poor performance",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["camshaft position sensor circuit low input", "P0340", "camshaft sensor low voltage"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit Low Input",
        "- Likely Issue: Sensor voltage below expected range",
        "- Related Issue: Poor engine timing, stalling",
        "- Suggestion: Inspect wiring and sensor; repair or replace as needed"
    ]
},
{
    "conditions": ["crankshaft position sensor circuit intermittent", "P0335", "crankshaft sensor intermittent fault"],
    "bullets": [
        "- Condition: Crankshaft Position Sensor Circuit Intermittent",
        "- Likely Issue: Wiring or sensor failure causing intermittent signal",
        "- Related Issue: Engine stalling or no start",
        "- Suggestion: Test wiring and sensor; replace if necessary"
    ]
},
{
    "conditions": ["fuel injector circuit malfunction bank 1", "P0201", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Circuit Malfunction (Bank 1)",
        "- Likely Issue: Faulty injector or wiring",
        "- Related Issue: Engine misfire or poor performance",
        "- Suggestion: Test injector and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["camshaft position actuator circuit malfunction", "P0011", "camshaft actuator fault"],
    "bullets": [
        "- Condition: Camshaft Position Actuator Circuit Malfunction",
        "- Likely Issue: Faulty actuator or wiring",
        "- Related Issue: Engine timing and performance issues",
        "- Suggestion: Inspect actuator and wiring; repair or replace"
    ]
},
{
    "conditions": ["throttle actuator control module circuit malfunction", "P2102", "throttle actuator control fault"],
    "bullets": [
        "- Condition: Throttle Actuator Control Module Circuit Malfunction",
        "- Likely Issue: Wiring or module fault",
        "- Related Issue: Throttle response issues",
        "- Suggestion: Diagnose wiring and module; replace if defective"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor switch a circuit malfunction", "P0749", "transmission pressure sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor/Switch A Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Transmission pressure irregularities",
        "- Suggestion: Test sensor and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["anti-lock brake system (ABS) sensor circuit malfunction", "P0500", "ABS sensor fault"],
    "bullets": [
        "- Condition: ABS Sensor Circuit Malfunction",
        "- Likely Issue: Faulty ABS sensor or wiring",
        "- Related Issue: ABS warning light, braking issues",
        "- Suggestion: Inspect sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["battery temperature sensor circuit malfunction", "battery overheating risk"],
    "bullets": [
        "- Condition: Battery Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Battery management issues, overheating risk",
        "- Suggestion: Inspect sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit no signal", "P0500", "speed sensor no signal"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit No Signal",
        "- Likely Issue: Broken sensor or wiring",
        "- Related Issue: Speedometer failure, transmission shift problems",
        "- Suggestion: Check sensor and wiring; replace as necessary"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit malfunction", "P0711", "transmission fluid temp sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty temperature sensor or wiring",
        "- Related Issue: Incorrect transmission fluid temperature readings affecting shifting",
        "- Suggestion: Inspect sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["torque converter clutch circuit electrical", "P0740", "torque converter clutch solenoid fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Electrical Fault",
        "- Likely Issue: Faulty TCC solenoid or wiring",
        "- Related Issue: Transmission slipping, harsh shifting, fuel economy",
        "- Suggestion: Test solenoid and circuit; repair or replace as needed"
    ]
},
{
    "conditions": ["clutch pedal position sensor malfunction", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Pedal Position Sensor Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Clutch engagement irregularities, shifting problems",
        "- Suggestion: Check sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["vehicle speed sensor intermittent signal", "transmission shifting erratic"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Intermittent Signal",
        "- Likely Issue: Loose wiring or failing sensor",
        "- Related Issue: Erratic speedometer and transmission shifting",
        "- Suggestion: Inspect wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["throttle position sensor circuit high input", "P0123", "throttle position sensor high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit High Input",
        "- Likely Issue: Short or wiring fault causing high voltage",
        "- Related Issue: Poor throttle control and engine response",
        "- Suggestion: Test sensor wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["mass air flow sensor circuit intermittent", "engine stalling", "check engine light"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Intermittent Fault",
        "- Likely Issue: Wiring or sensor failure causing unstable signal",
        "- Related Issue: Engine hesitation, stalling, poor fuel economy",
        "- Suggestion: Inspect wiring and sensor; clean or replace as needed"
    ]
},
{
    "conditions": ["fuel rail pressure sensor circuit malfunction", "P0190", "fuel pressure sensor fault"],
    "bullets": [
        "- Condition: Fuel Rail Pressure Sensor Circuit Malfunction",
        "- Likely Issue: Sensor or wiring fault",
        "- Related Issue: Fuel delivery problems, poor engine performance",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["camshaft position sensor circuit no signal", "P0341", "camshaft sensor signal fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring open circuit",
        "- Related Issue: Engine misfire, poor performance",
        "- Suggestion: Inspect wiring and sensor; replace as needed"
    ]
},
{
    "conditions": ["crankshaft position sensor circuit no signal", "P0336", "crankshaft sensor no signal"],
    "bullets": [
        "- Condition: Crankshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Engine stalls or fails to start",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["engine coolant temperature sensor circuit low input", "P0117", "coolant temp sensor low voltage"],
    "bullets": [
        "- Condition: Engine Coolant Temperature Sensor Circuit Low Input",
        "- Likely Issue: Sensor voltage below threshold or wiring fault",
        "- Related Issue: Incorrect engine temp readings, cold start issues",
        "- Suggestion: Check sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["intake manifold runner control stuck closed", "P2004", "intake manifold runner fault"],
    "bullets": [
        "- Condition: Intake Manifold Runner Control Stuck Closed",
        "- Likely Issue: Faulty runner control valve or wiring",
        "- Related Issue: Reduced engine power and efficiency",
        "- Suggestion: Inspect valve operation; repair or replace"
    ]
},
{
    "conditions": ["evaporative emission control system purge control valve stuck open", "P0443", "EVAP purge valve fault"],
    "bullets": [
        "- Condition: EVAP System Purge Control Valve Stuck Open",
        "- Likely Issue: Purge valve failure or wiring issue",
        "- Related Issue: Fuel vapor leak, failed emissions test",
        "- Suggestion: Test valve operation; repair or replace"
    ]
},
{
    "conditions": ["exhaust gas recirculation flow insufficient", "P0401", "EGR flow insufficient"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Flow Insufficient",
        "- Likely Issue: Blocked EGR valve or faulty sensor",
        "- Related Issue: Emission increase, engine rough idle",
        "- Suggestion: Clean or replace EGR valve and sensor"
    ]
},
{
    "conditions": ["knock sensor circuit low input", "P0326", "knock sensor low voltage"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Low Input",
        "- Likely Issue: Faulty knock sensor or wiring",
        "- Related Issue: Engine knocking, poor fuel economy",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["battery voltage too high", "P0562", "high battery voltage"],
    "bullets": [
        "- Condition: Battery Voltage Too High",
        "- Likely Issue: Overcharging by alternator or wiring fault",
        "- Related Issue: Battery damage, electrical system faults",
        "- Suggestion: Inspect alternator and voltage regulator"
    ]
},
{
    "conditions": ["evap system leak detected large leak", "P0455", "EVAP system large leak"],
    "bullets": [
        "- Condition: EVAP System Leak Detected (Large Leak)",
        "- Likely Issue: Broken EVAP hose or faulty fuel cap",
        "- Related Issue: Emission failure and fuel odor",
        "- Suggestion: Perform smoke test; repair leaks and replace cap"
    ]
},
{
    "conditions": ["oxygen sensor circuit low voltage bank 2 sensor 1", "P0136", "O2 sensor low voltage"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit Low Voltage (Bank 2 Sensor 1)",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Poor emission control and fuel economy",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["mass air flow sensor circuit high voltage", "P0103", "MAF sensor high voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit High Voltage",
        "- Likely Issue: Short or wiring fault",
        "- Related Issue: Rich running condition, engine performance issues",
        "- Suggestion: Inspect wiring; clean or replace sensor"
    ]
},
{
    "conditions": ["fuel injector circuit malfunction bank 2", "P0202", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Circuit Malfunction (Bank 2)",
        "- Likely Issue: Faulty injector or wiring",
        "- Related Issue: Misfire, rough running",
        "- Suggestion: Test injector and wiring; repair or replace"
    ]
},
{
    "conditions": ["idle control system malfunction", "P0505", "idle control fault"],
    "bullets": [
        "- Condition: Idle Control System Malfunction",
        "- Likely Issue: Faulty idle air control valve or wiring",
        "- Related Issue: Irregular idle speed",
        "- Suggestion: Test valve and wiring; repair or replace"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit intermittent", "P0500", "speed sensor intermittent signal"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Intermittent",
        "- Likely Issue: Loose or damaged wiring",
        "- Related Issue: Erratic speedometer, transmission shifting issues",
        "- Suggestion: Inspect wiring; secure or replace sensor"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit malfunction", "P0711", "transmission fluid temp sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty temperature sensor or wiring",
        "- Related Issue: Incorrect transmission fluid temperature readings affecting shifting",
        "- Suggestion: Inspect sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["torque converter clutch circuit electrical", "P0740", "torque converter clutch solenoid fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Electrical Fault",
        "- Likely Issue: Faulty TCC solenoid or wiring",
        "- Related Issue: Transmission slipping, harsh shifting, fuel economy",
        "- Suggestion: Test solenoid and circuit; repair or replace as needed"
    ]
},
{
    "conditions": ["clutch pedal position sensor malfunction", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Pedal Position Sensor Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Clutch engagement irregularities, shifting problems",
        "- Suggestion: Check sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["vehicle speed sensor intermittent signal", "transmission shifting erratic"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Intermittent Signal",
        "- Likely Issue: Loose wiring or failing sensor",
        "- Related Issue: Erratic speedometer and transmission shifting",
        "- Suggestion: Inspect wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["throttle position sensor circuit high input", "P0123", "throttle position sensor high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit High Input",
        "- Likely Issue: Short or wiring fault causing high voltage",
        "- Related Issue: Poor throttle control and engine response",
        "- Suggestion: Test sensor wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["mass air flow sensor circuit intermittent", "engine stalling", "check engine light"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Intermittent Fault",
        "- Likely Issue: Wiring or sensor failure causing unstable signal",
        "- Related Issue: Engine hesitation, stalling, poor fuel economy",
        "- Suggestion: Inspect wiring and sensor; clean or replace as needed"
    ]
},
{
    "conditions": ["fuel rail pressure sensor circuit malfunction", "P0190", "fuel pressure sensor fault"],
    "bullets": [
        "- Condition: Fuel Rail Pressure Sensor Circuit Malfunction",
        "- Likely Issue: Sensor or wiring fault",
        "- Related Issue: Fuel delivery problems, poor engine performance",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["camshaft position sensor circuit no signal", "P0341", "camshaft sensor signal fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring open circuit",
        "- Related Issue: Engine misfire, poor performance",
        "- Suggestion: Inspect wiring and sensor; replace as needed"
    ]
},
{
    "conditions": ["crankshaft position sensor circuit no signal", "P0336", "crankshaft sensor no signal"],
    "bullets": [
        "- Condition: Crankshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Engine stalls or fails to start",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["engine coolant temperature sensor circuit low input", "P0117", "coolant temp sensor low voltage"],
    "bullets": [
        "- Condition: Engine Coolant Temperature Sensor Circuit Low Input",
        "- Likely Issue: Sensor voltage below threshold or wiring fault",
        "- Related Issue: Incorrect engine temp readings, cold start issues",
        "- Suggestion: Check sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["intake manifold runner control stuck closed", "P2004", "intake manifold runner fault"],
    "bullets": [
        "- Condition: Intake Manifold Runner Control Stuck Closed",
        "- Likely Issue: Faulty runner control valve or wiring",
        "- Related Issue: Reduced engine power and efficiency",
        "- Suggestion: Inspect valve operation; repair or replace"
    ]
},
{
    "conditions": ["evaporative emission control system purge control valve stuck open", "P0443", "EVAP purge valve fault"],
    "bullets": [
        "- Condition: EVAP System Purge Control Valve Stuck Open",
        "- Likely Issue: Purge valve failure or wiring issue",
        "- Related Issue: Fuel vapor leak, failed emissions test",
        "- Suggestion: Test valve operation; repair or replace"
    ]
},
{
    "conditions": ["exhaust gas recirculation flow insufficient", "P0401", "EGR flow insufficient"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Flow Insufficient",
        "- Likely Issue: Blocked EGR valve or faulty sensor",
        "- Related Issue: Emission increase, engine rough idle",
        "- Suggestion: Clean or replace EGR valve and sensor"
    ]
},
{
    "conditions": ["knock sensor circuit low input", "P0326", "knock sensor low voltage"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Low Input",
        "- Likely Issue: Faulty knock sensor or wiring",
        "- Related Issue: Engine knocking, poor fuel economy",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["battery voltage too high", "P0562", "high battery voltage"],
    "bullets": [
        "- Condition: Battery Voltage Too High",
        "- Likely Issue: Overcharging by alternator or wiring fault",
        "- Related Issue: Battery damage, electrical system faults",
        "- Suggestion: Inspect alternator and voltage regulator"
    ]
},
{
    "conditions": ["evap system leak detected large leak", "P0455", "EVAP system large leak"],
    "bullets": [
        "- Condition: EVAP System Leak Detected (Large Leak)",
        "- Likely Issue: Broken EVAP hose or faulty fuel cap",
        "- Related Issue: Emission failure and fuel odor",
        "- Suggestion: Perform smoke test; repair leaks and replace cap"
    ]
},
{
    "conditions": ["oxygen sensor circuit low voltage bank 2 sensor 1", "P0136", "O2 sensor low voltage"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit Low Voltage (Bank 2 Sensor 1)",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Poor emission control and fuel economy",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["mass air flow sensor circuit high voltage", "P0103", "MAF sensor high voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit High Voltage",
        "- Likely Issue: Short or wiring fault",
        "- Related Issue: Rich running condition, engine performance issues",
        "- Suggestion: Inspect wiring; clean or replace sensor"
    ]
},
{
    "conditions": ["fuel injector circuit malfunction bank 2", "P0202", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Circuit Malfunction (Bank 2)",
        "- Likely Issue: Faulty injector or wiring",
        "- Related Issue: Misfire, rough running",
        "- Suggestion: Test injector and wiring; repair or replace"
    ]
},
{
    "conditions": ["idle control system malfunction", "P0505", "idle control fault"],
    "bullets": [
        "- Condition: Idle Control System Malfunction",
        "- Likely Issue: Faulty idle air control valve or wiring",
        "- Related Issue: Irregular idle speed",
        "- Suggestion: Test valve and wiring; repair or replace"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit intermittent", "P0500", "speed sensor intermittent signal"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Intermittent",
        "- Likely Issue: Loose or damaged wiring",
        "- Related Issue: Erratic speedometer, transmission shifting issues",
        "- Suggestion: Inspect wiring; secure or replace sensor"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit malfunction", "P0711", "transmission fluid temp sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty temperature sensor or wiring",
        "- Related Issue: Incorrect transmission fluid temperature readings affecting shifting",
        "- Suggestion: Inspect sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["torque converter clutch circuit electrical", "P0740", "torque converter clutch solenoid fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Electrical Fault",
        "- Likely Issue: Faulty TCC solenoid or wiring",
        "- Related Issue: Transmission slipping, harsh shifting, fuel economy",
        "- Suggestion: Test solenoid and circuit; repair or replace as needed"
    ]
},
{
    "conditions": ["clutch pedal position sensor malfunction", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Pedal Position Sensor Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Clutch engagement irregularities, shifting problems",
        "- Suggestion: Check sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["vehicle speed sensor intermittent signal", "transmission shifting erratic"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Intermittent Signal",
        "- Likely Issue: Loose wiring or failing sensor",
        "- Related Issue: Erratic speedometer and transmission shifting",
        "- Suggestion: Inspect wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["throttle position sensor circuit high input", "P0123", "throttle position sensor high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit High Input",
        "- Likely Issue: Short or wiring fault causing high voltage",
        "- Related Issue: Poor throttle control and engine response",
        "- Suggestion: Test sensor wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["mass air flow sensor circuit intermittent", "engine stalling", "check engine light"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Intermittent Fault",
        "- Likely Issue: Wiring or sensor failure causing unstable signal",
        "- Related Issue: Engine hesitation, stalling, poor fuel economy",
        "- Suggestion: Inspect wiring and sensor; clean or replace as needed"
    ]
},
{
    "conditions": ["fuel rail pressure sensor circuit malfunction", "P0190", "fuel pressure sensor fault"],
    "bullets": [
        "- Condition: Fuel Rail Pressure Sensor Circuit Malfunction",
        "- Likely Issue: Sensor or wiring fault",
        "- Related Issue: Fuel delivery problems, poor engine performance",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["camshaft position sensor circuit no signal", "P0341", "camshaft sensor signal fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring open circuit",
        "- Related Issue: Engine misfire, poor performance",
        "- Suggestion: Inspect wiring and sensor; replace as needed"
    ]
},
{
    "conditions": ["crankshaft position sensor circuit no signal", "P0336", "crankshaft sensor no signal"],
    "bullets": [
        "- Condition: Crankshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Engine stalls or fails to start",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["engine coolant temperature sensor circuit low input", "P0117", "coolant temp sensor low voltage"],
    "bullets": [
        "- Condition: Engine Coolant Temperature Sensor Circuit Low Input",
        "- Likely Issue: Sensor voltage below threshold or wiring fault",
        "- Related Issue: Incorrect engine temp readings, cold start issues",
        "- Suggestion: Check sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["intake manifold runner control stuck closed", "P2004", "intake manifold runner fault"],
    "bullets": [
        "- Condition: Intake Manifold Runner Control Stuck Closed",
        "- Likely Issue: Faulty runner control valve or wiring",
        "- Related Issue: Reduced engine power and efficiency",
        "- Suggestion: Inspect valve operation; repair or replace"
    ]
},
{
    "conditions": ["evaporative emission control system purge control valve stuck open", "P0443", "EVAP purge valve fault"],
    "bullets": [
        "- Condition: EVAP System Purge Control Valve Stuck Open",
        "- Likely Issue: Purge valve failure or wiring issue",
        "- Related Issue: Fuel vapor leak, failed emissions test",
        "- Suggestion: Test valve operation; repair or replace"
    ]
},
{
    "conditions": ["exhaust gas recirculation flow insufficient", "P0401", "EGR flow insufficient"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Flow Insufficient",
        "- Likely Issue: Blocked EGR valve or faulty sensor",
        "- Related Issue: Emission increase, engine rough idle",
        "- Suggestion: Clean or replace EGR valve and sensor"
    ]
},
{
    "conditions": ["knock sensor circuit low input", "P0326", "knock sensor low voltage"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Low Input",
        "- Likely Issue: Faulty knock sensor or wiring",
        "- Related Issue: Engine knocking, poor fuel economy",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["battery voltage too high", "P0562", "high battery voltage"],
    "bullets": [
        "- Condition: Battery Voltage Too High",
        "- Likely Issue: Overcharging by alternator or wiring fault",
        "- Related Issue: Battery damage, electrical system faults",
        "- Suggestion: Inspect alternator and voltage regulator"
    ]
},
{
    "conditions": ["evap system leak detected large leak", "P0455", "EVAP system large leak"],
    "bullets": [
        "- Condition: EVAP System Leak Detected (Large Leak)",
        "- Likely Issue: Broken EVAP hose or faulty fuel cap",
        "- Related Issue: Emission failure and fuel odor",
        "- Suggestion: Perform smoke test; repair leaks and replace cap"
    ]
},
{
    "conditions": ["oxygen sensor circuit low voltage bank 2 sensor 1", "P0136", "O2 sensor low voltage"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit Low Voltage (Bank 2 Sensor 1)",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Poor emission control and fuel economy",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["mass air flow sensor circuit high voltage", "P0103", "MAF sensor high voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit High Voltage",
        "- Likely Issue: Short or wiring fault",
        "- Related Issue: Rich running condition, engine performance issues",
        "- Suggestion: Inspect wiring; clean or replace sensor"
    ]
},
{
    "conditions": ["fuel injector circuit malfunction bank 2", "P0202", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Circuit Malfunction (Bank 2)",
        "- Likely Issue: Faulty injector or wiring",
        "- Related Issue: Misfire, rough running",
        "- Suggestion: Test injector and wiring; repair or replace"
    ]
},
{
    "conditions": ["idle control system malfunction", "P0505", "idle control fault"],
    "bullets": [
        "- Condition: Idle Control System Malfunction",
        "- Likely Issue: Faulty idle air control valve or wiring",
        "- Related Issue: Irregular idle speed",
        "- Suggestion: Test valve and wiring; repair or replace"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit intermittent", "P0500", "speed sensor intermittent signal"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Intermittent",
        "- Likely Issue: Loose or damaged wiring",
        "- Related Issue: Erratic speedometer, transmission shifting issues",
        "- Suggestion: Inspect wiring; secure or replace sensor"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit malfunction", "P0711", "transmission fluid temp sensor fault"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty temperature sensor or wiring",
        "- Related Issue: Incorrect transmission fluid temperature readings affecting shifting",
        "- Suggestion: Inspect sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["torque converter clutch circuit electrical", "P0740", "torque converter clutch solenoid fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Electrical Fault",
        "- Likely Issue: Faulty TCC solenoid or wiring",
        "- Related Issue: Transmission slipping, harsh shifting, fuel economy",
        "- Suggestion: Test solenoid and circuit; repair or replace as needed"
    ]
},
{
    "conditions": ["clutch pedal position sensor malfunction", "clutch engagement failure"],
    "bullets": [
        "- Condition: Clutch Pedal Position Sensor Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Clutch engagement irregularities, shifting problems",
        "- Suggestion: Check sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["vehicle speed sensor intermittent signal", "transmission shifting erratic"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Intermittent Signal",
        "- Likely Issue: Loose wiring or failing sensor",
        "- Related Issue: Erratic speedometer and transmission shifting",
        "- Suggestion: Inspect wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["throttle position sensor circuit high input", "P0123", "throttle position sensor high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit High Input",
        "- Likely Issue: Short or wiring fault causing high voltage",
        "- Related Issue: Poor throttle control and engine response",
        "- Suggestion: Test sensor wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["mass air flow sensor circuit intermittent", "engine stalling", "check engine light"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Intermittent Fault",
        "- Likely Issue: Wiring or sensor failure causing unstable signal",
        "- Related Issue: Engine hesitation, stalling, poor fuel economy",
        "- Suggestion: Inspect wiring and sensor; clean or replace as needed"
    ]
},
{
    "conditions": ["fuel rail pressure sensor circuit malfunction", "P0190", "fuel pressure sensor fault"],
    "bullets": [
        "- Condition: Fuel Rail Pressure Sensor Circuit Malfunction",
        "- Likely Issue: Sensor or wiring fault",
        "- Related Issue: Fuel delivery problems, poor engine performance",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["camshaft position sensor circuit no signal", "P0341", "camshaft sensor signal fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring open circuit",
        "- Related Issue: Engine misfire, poor performance",
        "- Suggestion: Inspect wiring and sensor; replace as needed"
    ]
},
{
    "conditions": ["crankshaft position sensor circuit no signal", "P0336", "crankshaft sensor no signal"],
    "bullets": [
        "- Condition: Crankshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Engine stalls or fails to start",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["engine coolant temperature sensor circuit low input", "P0117", "coolant temp sensor low voltage"],
    "bullets": [
        "- Condition: Engine Coolant Temperature Sensor Circuit Low Input",
        "- Likely Issue: Sensor voltage below threshold or wiring fault",
        "- Related Issue: Incorrect engine temp readings, cold start issues",
        "- Suggestion: Check sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["intake manifold runner control stuck closed", "P2004", "intake manifold runner fault"],
    "bullets": [
        "- Condition: Intake Manifold Runner Control Stuck Closed",
        "- Likely Issue: Faulty runner control valve or wiring",
        "- Related Issue: Reduced engine power and efficiency",
        "- Suggestion: Inspect valve operation; repair or replace"
    ]
},
{
    "conditions": ["evaporative emission control system purge control valve stuck open", "P0443", "EVAP purge valve fault"],
    "bullets": [
        "- Condition: EVAP System Purge Control Valve Stuck Open",
        "- Likely Issue: Purge valve failure or wiring issue",
        "- Related Issue: Fuel vapor leak, failed emissions test",
        "- Suggestion: Test valve operation; repair or replace"
    ]
},
{
    "conditions": ["exhaust gas recirculation flow insufficient", "P0401", "EGR flow insufficient"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Flow Insufficient",
        "- Likely Issue: Blocked EGR valve or faulty sensor",
        "- Related Issue: Emission increase, engine rough idle",
        "- Suggestion: Clean or replace EGR valve and sensor"
    ]
},
{
    "conditions": ["knock sensor circuit low input", "P0326", "knock sensor low voltage"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Low Input",
        "- Likely Issue: Faulty knock sensor or wiring",
        "- Related Issue: Engine knocking, poor fuel economy",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["battery voltage too high", "P0562", "high battery voltage"],
    "bullets": [
        "- Condition: Battery Voltage Too High",
        "- Likely Issue: Overcharging by alternator or wiring fault",
        "- Related Issue: Battery damage, electrical system faults",
        "- Suggestion: Inspect alternator and voltage regulator"
    ]
},
{
    "conditions": ["evap system leak detected large leak", "P0455", "EVAP system large leak"],
    "bullets": [
        "- Condition: EVAP System Leak Detected (Large Leak)",
        "- Likely Issue: Broken EVAP hose or faulty fuel cap",
        "- Related Issue: Emission failure and fuel odor",
        "- Suggestion: Perform smoke test; repair leaks and replace cap"
    ]
},
{
    "conditions": ["oxygen sensor circuit low voltage bank 2 sensor 1", "P0136", "O2 sensor low voltage"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit Low Voltage (Bank 2 Sensor 1)",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Poor emission control and fuel economy",
        "- Suggestion: Test sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["mass air flow sensor circuit high voltage", "P0103", "MAF sensor high voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit High Voltage",
        "- Likely Issue: Short or wiring fault",
        "- Related Issue: Rich running condition, engine performance issues",
        "- Suggestion: Inspect wiring; clean or replace sensor"
    ]
},
{
    "conditions": ["fuel injector circuit malfunction bank 2", "P0202", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Circuit Malfunction (Bank 2)",
        "- Likely Issue: Faulty injector or wiring",
        "- Related Issue: Misfire, rough running",
        "- Suggestion: Test injector and wiring; repair or replace"
    ]
},
{
    "conditions": ["idle control system malfunction", "P0505", "idle control fault"],
    "bullets": [
        "- Condition: Idle Control System Malfunction",
        "- Likely Issue: Faulty idle air control valve or wiring",
        "- Related Issue: Irregular idle speed",
        "- Suggestion: Test valve and wiring; repair or replace"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit intermittent", "P0500", "speed sensor intermittent signal"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Intermittent",
        "- Likely Issue: Loose or damaged wiring",
        "- Related Issue: Erratic speedometer, transmission shifting issues",
        "- Suggestion: Inspect wiring; secure or replace sensor"
    ]
},
{
    "conditions": ["transmission input speed sensor circuit malfunction", "P0715", "input speed sensor fault"],
    "bullets": [
        "- Condition: Transmission Input Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty input speed sensor or wiring",
        "- Related Issue: Transmission shifting problems and erratic speed readings",
        "- Suggestion: Test sensor and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["transmission output speed sensor circuit malfunction", "P0720", "output speed sensor fault"],
    "bullets": [
        "- Condition: Transmission Output Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty output speed sensor or wiring",
        "- Related Issue: Gear shifting issues and speedometer malfunction",
        "- Suggestion: Inspect sensor wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["fuel pressure regulator control circuit malfunction", "P1256", "fuel pressure regulator fault"],
    "bullets": [
        "- Condition: Fuel Pressure Regulator Control Circuit Malfunction",
        "- Likely Issue: Faulty fuel pressure regulator or wiring",
        "- Related Issue: Fuel delivery irregularities, engine performance issues",
        "- Suggestion: Test regulator and wiring; repair or replace"
    ]
},
{
    "conditions": ["camshaft timing over-advanced or system performance", "P0011", "camshaft timing fault"],
    "bullets": [
        "- Condition: Camshaft Timing Over-Advanced or System Performance",
        "- Likely Issue: Variable Valve Timing (VVT) malfunction or oil flow issue",
        "- Related Issue: Poor engine performance, rough idle",
        "- Suggestion: Inspect VVT components; clean or replace as needed"
    ]
},
{
    "conditions": ["camshaft timing retard or system performance", "P0012", "camshaft timing retard fault"],
    "bullets": [
        "- Condition: Camshaft Timing Retard or System Performance",
        "- Likely Issue: VVT system malfunction or low oil pressure",
        "- Related Issue: Engine hesitation, reduced power",
        "- Suggestion: Check oil condition and VVT solenoids; repair or replace"
    ]
},
{
    "conditions": ["knock sensor 2 circuit malfunction bank 1", "P0331", "knock sensor fault"],
    "bullets": [
        "- Condition: Knock Sensor 2 Circuit Malfunction (Bank 1)",
        "- Likely Issue: Faulty knock sensor or wiring",
        "- Related Issue: Engine knocking, poor fuel economy",
        "- Suggestion: Test sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["evaporative emission system leak detected small leak", "P0456", "EVAP small leak"],
    "bullets": [
        "- Condition: EVAP System Leak Detected (Small Leak)",
        "- Likely Issue: Loose or damaged fuel cap, minor leak",
        "- Related Issue: Emission failure, fuel vapor smell",
        "- Suggestion: Check and tighten fuel cap; repair leaks if present"
    ]
},
{
    "conditions": ["oxygen sensor heater circuit malfunction bank 1 sensor 2", "P0141", "O2 sensor heater fault"],
    "bullets": [
        "- Condition: Oxygen Sensor Heater Circuit Malfunction (Bank 1 Sensor 2)",
        "- Likely Issue: Faulty heater element or wiring",
        "- Related Issue: Delayed sensor operation, increased emissions",
        "- Suggestion: Inspect heater circuit and wiring; replace sensor if faulty"
    ]
},
{
    "conditions": ["catalyst system efficiency below threshold bank 1", "P0420", "catalytic converter inefficiency"],
    "bullets": [
        "- Condition: Catalyst System Efficiency Below Threshold (Bank 1)",
        "- Likely Issue: Catalytic converter degradation or sensor fault",
        "- Related Issue: Increased emissions, poor fuel economy",
        "- Suggestion: Check catalytic converter and O2 sensors; replace as needed"
    ]
},
{
    "conditions": ["catalyst system efficiency below threshold bank 2", "P0430", "catalytic converter inefficiency"],
    "bullets": [
        "- Condition: Catalyst System Efficiency Below Threshold (Bank 2)",
        "- Likely Issue: Catalytic converter failure or sensor problem",
        "- Related Issue: Emission issues and check engine light",
        "- Suggestion: Inspect converter and sensors; repair or replace"
    ]
},
{
    "conditions": ["intake air temperature sensor circuit low input", "P0112", "IAT sensor low voltage"],
    "bullets": [
        "- Condition: Intake Air Temperature Sensor Circuit Low Input",
        "- Likely Issue: Sensor failure or wiring fault",
        "- Related Issue: Incorrect air intake temperature readings affecting engine performance",
        "- Suggestion: Test sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["idle air control valve stuck open", "P0506", "idle control valve fault"],
    "bullets": [
        "- Condition: Idle Air Control Valve Stuck Open",
        "- Likely Issue: Faulty IAC valve or carbon buildup",
        "- Related Issue: High idle speed, rough idling",
        "- Suggestion: Clean or replace IAC valve"
    ]
},
{
    "conditions": ["exhaust gas recirculation valve stuck open", "P0402", "EGR valve stuck open"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Valve Stuck Open",
        "- Likely Issue: Stuck or malfunctioning EGR valve",
        "- Related Issue: Rough idle, engine stalling, increased emissions",
        "- Suggestion: Clean or replace EGR valve"
    ]
},
{
    "conditions": ["throttle actuator control module communication fault", "P2109", "throttle control module error"],
    "bullets": [
        "- Condition: Throttle Actuator Control Module Communication Fault",
        "- Likely Issue: Communication failure between throttle module and ECU",
        "- Related Issue: Reduced throttle response or limp mode",
        "- Suggestion: Inspect wiring and connectors; replace module if necessary"
    ]
},
{
    "conditions": ["fuel injector circuit malfunction bank 1", "P0201", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Circuit Malfunction (Bank 1)",
        "- Likely Issue: Faulty injector or wiring issue",
        "- Related Issue: Misfires, rough engine operation",
        "- Suggestion: Test injector and wiring; repair or replace"
    ]
},
{
    "conditions": ["engine misfire detected bank 1", "P0301", "cylinder 1 misfire"],
    "bullets": [
        "- Condition: Engine Misfire Detected (Cylinder 1)",
        "- Likely Issue: Ignition, fuel, or compression issue in cylinder 1",
        "- Related Issue: Rough engine, reduced power",
        "- Suggestion: Inspect spark plugs, fuel injectors, compression; repair as needed"
    ]
},
{
    "conditions": ["engine misfire detected bank 2", "P0302", "cylinder 2 misfire"],
    "bullets": [
        "- Condition: Engine Misfire Detected (Cylinder 2)",
        "- Likely Issue: Ignition, fuel, or compression issue in cylinder 2",
        "- Related Issue: Engine roughness and power loss",
        "- Suggestion: Check spark plugs, injectors, compression; fix problems"
    ]
},
{
    "conditions": ["engine coolant thermostat malfunction", "engine overheating risk"],
    "bullets": [
        "- Condition: Engine Coolant Thermostat Malfunction",
        "- Likely Issue: Stuck thermostat causing poor coolant flow",
        "- Related Issue: Engine overheating or poor warm-up",
        "- Suggestion: Replace thermostat and inspect cooling system"
    ]
},
{
    "conditions": ["camshaft position actuator circuit malfunction", "P0010", "camshaft actuator fault"],
    "bullets": [
        "- Condition: Camshaft Position Actuator Circuit Malfunction",
        "- Likely Issue: Faulty actuator or wiring problem",
        "- Related Issue: Poor engine performance and fuel economy",
        "- Suggestion: Test actuator and wiring; repair or replace"
    ]
},
{
    "conditions": ["throttle position sensor circuit low input", "P0122", "throttle position sensor low voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit Low Input",
        "- Likely Issue: Wiring fault or sensor degradation",
        "- Related Issue: Poor throttle response",
        "- Suggestion: Inspect wiring and sensor; replace if needed"
    ]
},
{
    "conditions": ["mass air flow sensor circuit low input", "P0102", "MAF sensor low voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Low Input",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Lean fuel condition and poor performance",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["oxygen sensor circuit malfunction bank 1 sensor 1", "P0130", "oxygen sensor fault"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit Malfunction (Bank 1 Sensor 1)",
        "- Likely Issue: Faulty oxygen sensor or wiring",
        "- Related Issue: Poor fuel economy, increased emissions",
        "- Suggestion: Test sensor and wiring; replace sensor if faulty"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit malfunction", "P0500", "vehicle speed sensor fault"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty speed sensor or wiring",
        "- Related Issue: Speedometer failure, transmission shift issues",
        "- Suggestion: Inspect sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["evaporative emission system purge control valve circuit malfunction", "P0443", "EVAP purge valve fault"],
    "bullets": [
        "- Condition: EVAP System Purge Control Valve Circuit Malfunction",
        "- Likely Issue: Faulty purge valve or wiring",
        "- Related Issue: Fuel vapor leak and emissions issues",
        "- Suggestion: Test valve and wiring; repair or replace"
    ]
},
{
    "conditions": ["exhaust gas recirculation flow insufficient detected", "P0401", "EGR flow fault"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Flow Insufficient Detected",
        "- Likely Issue: Clogged or faulty EGR valve",
        "- Related Issue: Engine knocking, emissions increase",
        "- Suggestion: Clean or replace EGR valve"
    ]
},
{
    "conditions": ["throttle position sensor circuit high input", "P0123", "throttle position sensor high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit High Input",
        "- Likely Issue: Wiring issue or sensor malfunction",
        "- Related Issue: Erratic throttle behavior",
        "- Suggestion: Inspect wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["mass air flow sensor circuit high input", "P0103", "MAF sensor high voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit High Input",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Rich fuel condition and poor engine performance",
        "- Suggestion: Test and replace sensor or repair wiring"
    ]
},
{
    "conditions": ["intake manifold runner control stuck open", "P2004", "intake manifold runner fault"],
    "bullets": [
        "- Condition: Intake Manifold Runner Control Stuck Open",
        "- Likely Issue: Stuck actuator or valve",
        "- Related Issue: Reduced engine power and efficiency",
        "- Suggestion: Inspect actuator; clean or replace valve"
    ]
},
{
    "conditions": ["secondary air injection system malfunction", "P0410", "secondary air injection fault"],
    "bullets": [
        "- Condition: Secondary Air Injection System Malfunction",
        "- Likely Issue: Faulty air injection pump or valves",
        "- Related Issue: Emission control inefficiency",
        "- Suggestion: Diagnose system; repair or replace components"
    ]
},
{
    "conditions": ["engine coolant temperature sensor circuit low input", "P0113", "ECT sensor low voltage"],
    "bullets": [
        "- Condition: Engine Coolant Temperature Sensor Circuit Low Input",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Incorrect coolant temperature readings affecting engine control",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["engine misfire detected bank 3", "P0313", "cylinder misfire fault"],
    "bullets": [
        "- Condition: Engine Misfire Detected (Bank 3)",
        "- Likely Issue: Ignition or fuel delivery issue in bank 3 cylinders",
        "- Related Issue: Rough running, reduced power",
        "- Suggestion: Inspect ignition and fuel systems; repair or replace faulty parts"
    ]
},
{
    "conditions": ["camshaft position sensor circuit malfunction bank 2", "P0347", "camshaft sensor fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit Malfunction (Bank 2)",
        "- Likely Issue: Faulty sensor or wiring problem",
        "- Related Issue: Engine timing errors and misfires",
        "- Suggestion: Inspect sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["knock sensor circuit malfunction bank 1", "P0325", "knock sensor fault"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Malfunction (Bank 1)",
        "- Likely Issue: Defective knock sensor or wiring",
        "- Related Issue: Engine knocking and reduced performance",
        "- Suggestion: Test sensor and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["fuel pressure regulator control circuit malfunction", "P0197", "fuel pressure regulator fault"],
    "bullets": [
        "- Condition: Fuel Pressure Regulator Control Circuit Malfunction",
        "- Likely Issue: Faulty fuel pressure regulator or wiring",
        "- Related Issue: Poor fuel pressure regulation causing engine issues",
        "- Suggestion: Inspect regulator and wiring; replace faulty components"
    ]
},
{
    "conditions": ["coolant thermostat circuit malfunction", "P0128", "coolant thermostat fault"],
    "bullets": [
        "- Condition: Coolant Thermostat Circuit Malfunction",
        "- Likely Issue: Stuck thermostat or faulty sensor",
        "- Related Issue: Engine running too cold or overheating",
        "- Suggestion: Test thermostat and sensor; replace as needed"
    ]
},
{
    "conditions": ["transmission input speed sensor circuit malfunction", "P0715", "input speed sensor fault"],
    "bullets": [
        "- Condition: Transmission Input Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Transmission shifting problems and erratic behavior",
        "- Suggestion: Inspect sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["transmission output speed sensor circuit malfunction", "P0720", "output speed sensor fault"],
    "bullets": [
        "- Condition: Transmission Output Speed Sensor Circuit Malfunction",
        "- Likely Issue: Defective sensor or wiring issue",
        "- Related Issue: Speedometer errors and transmission problems",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["fuel injector circuit high", "P0201", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Circuit High Voltage (Cylinder 1)",
        "- Likely Issue: Wiring short or faulty injector",
        "- Related Issue: Engine misfire or poor performance",
        "- Suggestion: Check wiring and injector; repair or replace"
    ]
},
{
    "conditions": ["vehicle stability control system malfunction", "C1234", "VSC system fault"],
    "bullets": [
        "- Condition: Vehicle Stability Control System Malfunction",
        "- Likely Issue: Faulty sensors or module in VSC system",
        "- Related Issue: Loss of traction control and vehicle stability",
        "- Suggestion: Diagnose sensors and control module; repair or replace"
    ]
},
{
    "conditions": ["rear oxygen sensor heater circuit malfunction bank 2 sensor 2", "P1158", "rear O2 sensor heater fault"],
    "bullets": [
        "- Condition: Rear Oxygen Sensor Heater Circuit Malfunction (Bank 2 Sensor 2)",
        "- Likely Issue: Faulty heater circuit or wiring",
        "- Related Issue: Emissions control and sensor function impairment",
        "- Suggestion: Inspect wiring and sensor; replace if necessary"
    ]
},
{
    "conditions": ["mass air flow sensor circuit low input", "P0102", "MAF sensor low voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Low Input",
        "- Likely Issue: Dirty sensor or wiring problem",
        "- Related Issue: Lean running condition and performance issues",
        "- Suggestion: Clean sensor; inspect wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["oxygen sensor circuit no activity detected bank 1 sensor 1", "P0130", "oxygen sensor circuit fault"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit No Activity Detected (Bank 1 Sensor 1)",
        "- Likely Issue: Open or short circuit in oxygen sensor wiring",
        "- Related Issue: Poor fuel economy and emissions control",
        "- Suggestion: Inspect wiring harness and sensor; repair or replace"
    ]
},
{
    "conditions": ["evaporative emission control system purge flow insufficient", "P0443", "evap purge flow fault"],
    "bullets": [
        "- Condition: EVAP Emission Control System Purge Flow Insufficient",
        "- Likely Issue: Blocked purge valve or faulty solenoid",
        "- Related Issue: Fuel vapor emissions and check engine light",
        "- Suggestion: Test purge valve operation; replace if malfunctioning"
    ]
},
{
    "conditions": ["engine coolant temperature sensor low voltage", "P0115", "ECT sensor fault"],
    "bullets": [
        "- Condition: Engine Coolant Temperature Sensor Low Voltage",
        "- Likely Issue: Faulty sensor or wiring short",
        "- Related Issue: Incorrect engine temperature reading affecting performance",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["throttle position sensor high voltage", "P0123", "throttle sensor high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor High Voltage",
        "- Likely Issue: Faulty sensor or wiring causing high signal",
        "- Related Issue: Erratic throttle behavior and engine hesitation",
        "- Suggestion: Inspect throttle sensor and wiring; replace sensor if faulty"
    ]
},
{
    "conditions": ["exhaust gas recirculation flow insufficient", "P0401", "EGR flow fault"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Flow Insufficient",
        "- Likely Issue: Clogged EGR valve or faulty sensor",
        "- Related Issue: Increased emissions and rough idle",
        "- Suggestion: Clean or replace EGR valve; test sensor function"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit malfunction", "P0500", "VSS fault"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Malfunction",
        "- Likely Issue: Defective sensor or wiring issues",
        "- Related Issue: Speedometer failure and transmission shifting problems",
        "- Suggestion: Check sensor and wiring; replace if necessary"
    ]
},
{
    "conditions": ["idle speed control circuit malfunction", "P0505", "idle speed control fault"],
    "bullets": [
        "- Condition: Idle Speed Control Circuit Malfunction",
        "- Likely Issue: Faulty idle air control valve or circuit",
        "- Related Issue: Unstable idle and stalling",
        "- Suggestion: Test IAC valve and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["fuel tank pressure sensor circuit high voltage", "P0453", "fuel tank pressure sensor fault"],
    "bullets": [
        "- Condition: Fuel Tank Pressure Sensor Circuit High Voltage",
        "- Likely Issue: Sensor malfunction or wiring short",
        "- Related Issue: EVAP system failure and fuel vapor leaks",
        "- Suggestion: Inspect sensor and wiring; replace faulty components"
    ]
},
{
    "conditions": ["transmission range sensor circuit malfunction", "P0705", "transmission range sensor fault"],
    "bullets": [
        "- Condition: Transmission Range Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring causing improper gear detection",
        "- Related Issue: Transmission shifting and starting issues",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["intake air temperature sensor low voltage", "P0112", "intake air temp sensor fault"],
    "bullets": [
        "- Condition: Intake Air Temperature Sensor Low Voltage",
        "- Likely Issue: Sensor failure or wiring short to ground",
        "- Related Issue: Engine running rich due to wrong temperature reading",
        "- Suggestion: Inspect sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["camshaft actuator circuit malfunction", "P0011", "camshaft timing fault"],
    "bullets": [
        "- Condition: Camshaft Actuator Circuit Malfunction",
        "- Likely Issue: Faulty actuator or wiring",
        "- Related Issue: Poor engine timing and performance",
        "- Suggestion: Inspect camshaft actuator and wiring; repair or replace"
    ]
},
{
    "conditions": ["mass air flow sensor circuit high voltage", "P0101", "MAF sensor performance fault"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit High Voltage",
        "- Likely Issue: Dirty sensor or electrical problem",
        "- Related Issue: Poor air-fuel mixture and engine hesitation",
        "- Suggestion: Clean sensor and check wiring; replace if necessary"
    ]
},
{
    "conditions": ["throttle actuator control module power relay fault", "P2108", "throttle relay fault"],
    "bullets": [
        "- Condition: Throttle Actuator Control Module Power Relay Fault",
        "- Likely Issue: Faulty power relay or wiring",
        "- Related Issue: Loss of throttle control and limp mode",
        "- Suggestion: Check relay and wiring; replace relay if defective"
    ]
},
{
    "conditions": ["exhaust gas recirculation valve stuck open", "P0403", "EGR valve fault"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Valve Stuck Open",
        "- Likely Issue: Faulty valve or carbon buildup",
        "- Related Issue: Rough idle and increased emissions",
        "- Suggestion: Clean or replace EGR valve"
    ]
},
{
    "conditions": ["intake manifold runner control stuck closed", "P2002", "intake manifold runner fault"],
    "bullets": [
        "- Condition: Intake Manifold Runner Control Stuck Closed",
        "- Likely Issue: Faulty runner control valve or actuator",
        "- Related Issue: Reduced engine power and efficiency",
        "- Suggestion: Inspect and replace actuator or valve as needed"
    ]
},
{
    "conditions": ["secondary air injection system pump circuit malfunction", "P0410", "secondary air injection pump fault"],
    "bullets": [
        "- Condition: Secondary Air Injection System Pump Circuit Malfunction",
        "- Likely Issue: Faulty pump or wiring problem",
        "- Related Issue: Emissions control failure and check engine light",
        "- Suggestion: Test pump and wiring; repair or replace"
    ]
},
{
    "conditions": ["knock sensor circuit malfunction bank 2", "P0326", "knock sensor fault"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Malfunction (Bank 2)",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Engine knocking and potential damage",
        "- Suggestion: Test sensor and wiring; replace if needed"
    ]
},
{
    "conditions": ["oxygen sensor circuit high voltage bank 2 sensor 1", "P0136", "oxygen sensor high voltage"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit High Voltage (Bank 2 Sensor 1)",
        "- Likely Issue: Sensor stuck rich or wiring problem",
        "- Related Issue: Poor fuel economy and emissions",
        "- Suggestion: Inspect sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["evaporative emission control system leak detected large leak", "P0456", "EVAP system large leak"],
    "bullets": [
        "- Condition: EVAP Emission Control System Leak Detected (Large Leak)",
        "- Likely Issue: Loose fuel cap or damaged EVAP hose",
        "- Related Issue: Fuel vapor leaks and emissions failure",
        "- Suggestion: Tighten fuel cap and inspect hoses; repair leaks"
    ]
},
{
    "conditions": ["engine misfire detected bank 1", "P0301", "engine misfire fault"],
    "bullets": [
        "- Condition: Engine Misfire Detected (Bank 1)",
        "- Likely Issue: Faulty spark plugs, ignition coil, or fuel injector",
        "- Related Issue: Rough engine operation, increased emissions",
        "- Suggestion: Inspect spark plugs, coils, and injectors; replace faulty parts"
    ]
},
{
    "conditions": ["fuel pressure regulator control circuit low", "P1251", "fuel pressure regulator low signal"],
    "bullets": [
        "- Condition: Fuel Pressure Regulator Control Circuit Low",
        "- Likely Issue: Low voltage signal to fuel pressure regulator solenoid",
        "- Related Issue: Inconsistent fuel delivery, engine hesitation",
        "- Suggestion: Check wiring and regulator; repair or replace as needed"
    ]
},
{
    "conditions": ["mass air flow sensor circuit low voltage", "P0102", "MAF sensor low voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Low Voltage",
        "- Likely Issue: Dirty sensor or wiring short to ground",
        "- Related Issue: Poor engine performance, stalling",
        "- Suggestion: Clean sensor and check wiring; replace sensor if faulty"
    ]
},
{
    "conditions": ["throttle position sensor low voltage", "P0121", "throttle sensor low voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Low Voltage",
        "- Likely Issue: Wiring short or sensor fault",
        "- Related Issue: Engine hesitation and poor throttle response",
        "- Suggestion: Inspect wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["camshaft position sensor circuit malfunction bank 1", "P0340", "camshaft position sensor fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit Malfunction (Bank 1)",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Engine timing problems, misfires",
        "- Suggestion: Check sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["intake air temperature sensor high voltage", "P0113", "intake air temp sensor high voltage"],
    "bullets": [
        "- Condition: Intake Air Temperature Sensor High Voltage",
        "- Likely Issue: Wiring open circuit or sensor fault",
        "- Related Issue: Incorrect air temperature readings affecting engine control",
        "- Suggestion: Inspect wiring and sensor; replace if necessary"
    ]
},
{
    "conditions": ["evaporative emission control system leak detected small leak", "P0455", "EVAP system leak"],
    "bullets": [
        "- Condition: EVAP Emission Control System Leak Detected (Small Leak)",
        "- Likely Issue: Cracked hose or loose fuel cap",
        "- Related Issue: Fuel vapor leaks and emissions issues",
        "- Suggestion: Inspect fuel system for leaks; tighten or replace fuel cap"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit low voltage", "P0503", "vehicle speed sensor low voltage"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Low Voltage",
        "- Likely Issue: Wiring short or sensor failure",
        "- Related Issue: Incorrect speedometer readings, transmission shifting faults",
        "- Suggestion: Check wiring and sensor; repair or replace as necessary"
    ]
},
{
    "conditions": ["knock sensor circuit malfunction bank 1", "P0325", "knock sensor fault"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Malfunction (Bank 1)",
        "- Likely Issue: Faulty sensor or wiring issue",
        "- Related Issue: Engine knocking, poor performance",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["exhaust gas recirculation sensor circuit malfunction", "P0402", "EGR sensor fault"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Increased emissions, engine performance issues",
        "- Suggestion: Inspect sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["oxygen sensor heater circuit malfunction bank 2 sensor 2", "P0157", "oxygen sensor heater fault"],
    "bullets": [
        "- Condition: Oxygen Sensor Heater Circuit Malfunction (Bank 2 Sensor 2)",
        "- Likely Issue: Faulty heater circuit or wiring",
        "- Related Issue: Poor sensor operation, increased emissions",
        "- Suggestion: Check sensor heater and wiring; replace sensor if faulty"
    ]
},
{
    "conditions": ["catalyst system efficiency below threshold bank 1", "P0420", "catalyst efficiency fault"],
    "bullets": [
        "- Condition: Catalyst System Efficiency Below Threshold (Bank 1)",
        "- Likely Issue: Faulty catalytic converter or oxygen sensors",
        "- Related Issue: Failed emissions test, poor fuel economy",
        "- Suggestion: Inspect catalytic converter and sensors; replace as needed"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit high", "P0711", "transmission fluid temp sensor high voltage"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit High",
        "- Likely Issue: Sensor malfunction or wiring short to voltage",
        "- Related Issue: Transmission shifting problems and overheating",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["pressure control solenoid A performance", "P0741", "pressure control solenoid fault"],
    "bullets": [
        "- Condition: Pressure Control Solenoid A Performance",
        "- Likely Issue: Faulty solenoid or wiring",
        "- Related Issue: Transmission slipping or harsh shifting",
        "- Suggestion: Inspect solenoid and circuit; replace if faulty"
    ]
},
{
    "conditions": ["torque converter clutch circuit malfunction", "P0740", "torque converter clutch fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Malfunction",
        "- Likely Issue: Faulty TCC solenoid or wiring",
        "- Related Issue: Transmission slipping and fuel inefficiency",
        "- Suggestion: Test TCC solenoid; clean or replace as necessary"
    ]
},
{
    "conditions": ["shift solenoid B electrical malfunction", "P0756", "shift solenoid fault"],
    "bullets": [
        "- Condition: Shift Solenoid B Electrical Malfunction",
        "- Likely Issue: Wiring or solenoid failure",
        "- Related Issue: Improper gear shifts",
        "- Suggestion: Inspect wiring and solenoid; repair or replace"
    ]
},
{
    "conditions": ["transmission component slipping", "P1870", "transmission slipping"],
    "bullets": [
        "- Condition: Transmission Component Slipping",
        "- Likely Issue: Worn internal components or low fluid",
        "- Related Issue: Loss of power and inconsistent gear engagement",
        "- Suggestion: Check transmission fluid level and quality; inspect internal parts"
    ]
},
{
    "conditions": ["fuel injector circuit malfunction bank 1", "P0201", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Circuit Malfunction (Bank 1)",
        "- Likely Issue: Faulty injector or wiring problem",
        "- Related Issue: Engine misfire and poor performance",
        "- Suggestion: Test injector and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["intake manifold tuning valve control circuit", "P2015", "intake manifold valve fault"],
    "bullets": [
        "- Condition: Intake Manifold Tuning Valve Control Circuit Fault",
        "- Likely Issue: Faulty valve or wiring",
        "- Related Issue: Reduced engine power and drivability issues",
        "- Suggestion: Inspect valve and wiring; repair or replace as needed"
    ]
},
{
    "conditions": ["evaporative emission control system leak detected", "P0456", "EVAP leak fault"],
    "bullets": [
        "- Condition: EVAP Emission Control System Leak Detected",
        "- Likely Issue: Leak in EVAP system components or hoses",
        "- Related Issue: Fuel vapor leakage and emission failures",
        "- Suggestion: Perform smoke test; repair leaks and replace faulty parts"
    ]
},
{
    "conditions": ["engine coolant temperature sensor circuit low", "P0117", "engine coolant sensor low voltage"],
    "bullets": [
        "- Condition: Engine Coolant Temperature Sensor Circuit Low",
        "- Likely Issue: Faulty coolant temp sensor or wiring short to ground",
        "- Related Issue: Engine overheating or poor fuel mixture control",
        "- Suggestion: Inspect sensor wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit malfunction", "P0500", "vehicle speed sensor fault"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or damaged wiring",
        "- Related Issue: Speedometer failure and transmission shift problems",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["throttle position sensor circuit high", "P0122", "throttle sensor high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit High Voltage",
        "- Likely Issue: Open circuit or sensor fault",
        "- Related Issue: Poor throttle response and engine hesitation",
        "- Suggestion: Inspect sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["mass air flow sensor circuit intermittent", "P0101", "MAF sensor performance fault"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Intermittent",
        "- Likely Issue: Dirty or failing MAF sensor",
        "- Related Issue: Erratic engine performance and fuel economy issues",
        "- Suggestion: Clean MAF sensor; replace if performance does not improve"
    ]
},
{
    "conditions": ["oxygen sensor circuit no activity detected bank 1 sensor 1", "P0130", "oxygen sensor inactivity"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit No Activity Detected (Bank 1 Sensor 1)",
        "- Likely Issue: Open or shorted wiring, faulty oxygen sensor",
        "- Related Issue: Increased emissions and poor fuel efficiency",
        "- Suggestion: Test wiring and sensor; replace oxygen sensor if faulty"
    ]
},
{
    "conditions": ["evaporative emission control system purge control valve circuit", "P0443", "EVAP purge valve fault"],
    "bullets": [
        "- Condition: EVAP System Purge Control Valve Circuit Malfunction",
        "- Likely Issue: Faulty purge valve or wiring",
        "- Related Issue: Fuel vapor leaks and emission failures",
        "- Suggestion: Inspect purge valve and wiring; repair or replace"
    ]
},
{
    "conditions": ["intake air temperature sensor circuit low voltage", "P0112", "intake air temp sensor low voltage"],
    "bullets": [
        "- Condition: Intake Air Temperature Sensor Circuit Low Voltage",
        "- Likely Issue: Short to ground or faulty sensor",
        "- Related Issue: Incorrect air-fuel mixture leading to rough running",
        "- Suggestion: Inspect wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["camshaft position actuator circuit malfunction", "P0011", "camshaft timing fault"],
    "bullets": [
        "- Condition: Camshaft Position Actuator Circuit Malfunction",
        "- Likely Issue: Faulty variable valve timing actuator or wiring",
        "- Related Issue: Engine timing issues and reduced power",
        "- Suggestion: Check actuator and wiring; repair or replace"
    ]
},
{
    "conditions": ["fuel system too lean bank 2", "P0174", "lean fuel condition"],
    "bullets": [
        "- Condition: Fuel System Too Lean (Bank 2)",
        "- Likely Issue: Vacuum leaks, faulty injectors, or sensor errors",
        "- Related Issue: Engine hesitation, poor performance",
        "- Suggestion: Inspect vacuum lines, fuel injectors, and sensors"
    ]
},
{
    "conditions": ["knock sensor circuit low input bank 1", "P0327", "knock sensor low voltage"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Low Input (Bank 1)",
        "- Likely Issue: Faulty sensor or wiring issue",
        "- Related Issue: Engine knocking and possible damage",
        "- Suggestion: Test knock sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["exhaust gas recirculation system high flow", "P0403", "EGR circuit fault"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation System High Flow",
        "- Likely Issue: Faulty EGR valve or sensor",
        "- Related Issue: Increased emissions, engine roughness",
        "- Suggestion: Inspect and test EGR components; repair or replace"
    ]
},
{
    "conditions": ["catalyst system efficiency below threshold bank 2", "P0430", "catalytic converter fault"],
    "bullets": [
        "- Condition: Catalyst System Efficiency Below Threshold (Bank 2)",
        "- Likely Issue: Faulty catalytic converter or oxygen sensors",
        "- Related Issue: Emission test failure, poor fuel economy",
        "- Suggestion: Test converter and sensors; replace if necessary"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit low", "P0712", "transmission fluid temp sensor low voltage"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit Low",
        "- Likely Issue: Wiring short or faulty sensor",
        "- Related Issue: Transmission overheating or shifting faults",
        "- Suggestion: Check wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["shift solenoid C electrical malfunction", "P0766", "shift solenoid fault"],
    "bullets": [
        "- Condition: Shift Solenoid C Electrical Malfunction",
        "- Likely Issue: Wiring or solenoid failure",
        "- Related Issue: Improper gear shifts",
        "- Suggestion: Inspect wiring and solenoid; repair or replace"
    ]
},
{
    "conditions": ["torque converter clutch circuit electrical malfunction", "P0741", "torque converter clutch fault"],
    "bullets": [
        "- Condition: Torque Converter Clutch Circuit Electrical Malfunction",
        "- Likely Issue: Faulty TCC solenoid or wiring",
        "- Related Issue: Transmission slipping and fuel inefficiency",
        "- Suggestion: Test TCC solenoid; clean or replace as necessary"
    ]
},
{
    "conditions": ["fuel injector control circuit open bank 2", "P0202", "fuel injector fault"],
    "bullets": [
        "- Condition: Fuel Injector Control Circuit Open (Bank 2)",
        "- Likely Issue: Broken wiring or faulty injector",
        "- Related Issue: Engine misfire and rough idle",
        "- Suggestion: Inspect wiring and injector; repair or replace"
    ]
},
{
    "conditions": ["idle speed control circuit malfunction", "P0505", "idle control fault"],
    "bullets": [
        "- Condition: Idle Speed Control Circuit Malfunction",
        "- Likely Issue: Faulty idle air control valve or wiring",
        "- Related Issue: Rough idle or stalling",
        "- Suggestion: Inspect valve and wiring; repair or replace"
    ]
},
{
    "conditions": ["evaporative emission control system leak detected large leak", "P0456", "EVAP leak fault"],
    "bullets": [
        "- Condition: EVAP Emission Control System Leak Detected (Large Leak)",
        "- Likely Issue: Large leak in EVAP system, cracked hoses",
        "- Related Issue: Fuel vapor leaks and emission failures",
        "- Suggestion: Perform smoke test; repair or replace faulty components"
    ]
},
{
    "conditions": ["power steering pressure sensor circuit low", "P1551", "power steering sensor low voltage"],
    "bullets": [
        "- Condition: Power Steering Pressure Sensor Circuit Low",
        "- Likely Issue: Wiring short to ground or sensor fault",
        "- Related Issue: Reduced power steering assist",
        "- Suggestion: Inspect sensor wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["exhaust gas recirculation flow insufficient", "P0401", "EGR flow insufficient"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation (EGR) Flow Insufficient",
        "- Likely Issue: Blocked EGR passages or faulty EGR valve",
        "- Related Issue: Increased NOx emissions and engine knocking",
        "- Suggestion: Clean EGR valve and passages; replace valve if defective"
    ]
},
{
    "conditions": ["intake manifold runner control stuck closed", "P2004", "intake manifold runner fault"],
    "bullets": [
        "- Condition: Intake Manifold Runner Control Stuck Closed",
        "- Likely Issue: Faulty runner control valve or actuator",
        "- Related Issue: Reduced engine power and poor fuel efficiency",
        "- Suggestion: Inspect actuator and control wiring; repair or replace"
    ]
},
{
    "conditions": ["vehicle speed sensor signal intermittent", "P0502", "vehicle speed sensor low input"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Signal Intermittent",
        "- Likely Issue: Loose wiring or failing sensor",
        "- Related Issue: Transmission shifting problems and speedometer errors",
        "- Suggestion: Check wiring connectors; test and replace sensor if needed"
    ]
},
{
    "conditions": ["mass air flow sensor circuit low input", "P0102", "MAF sensor low voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Low Input",
        "- Likely Issue: Dirty sensor or wiring short to ground",
        "- Related Issue: Lean fuel mixture and engine performance issues",
        "- Suggestion: Clean MAF sensor; inspect wiring and replace sensor if faulty"
    ]
},
{
    "conditions": ["fuel pressure regulator control circuit malfunction", "P1256", "fuel pressure regulator fault"],
    "bullets": [
        "- Condition: Fuel Pressure Regulator Control Circuit Malfunction",
        "- Likely Issue: Faulty regulator or electrical control issue",
        "- Related Issue: Irregular fuel pressure causing engine hesitation",
        "- Suggestion: Test regulator and wiring; repair or replace as necessary"
    ]
},
{
    "conditions": ["cylinder misfire detected bank 3", "P0303", "cylinder 3 misfire"],
    "bullets": [
        "- Condition: Cylinder Misfire Detected (Bank 3)",
        "- Likely Issue: Faulty spark plug, injector, or compression issue",
        "- Related Issue: Rough engine idle and increased emissions",
        "- Suggestion: Inspect spark plugs, ignition coils, and injectors; perform compression test"
    ]
},
{
    "conditions": ["turbocharger boost control range/performance", "P0234", "turbo overboost"],
    "bullets": [
        "- Condition: Turbocharger Boost Control Range/Performance Fault",
        "- Likely Issue: Wastegate stuck closed or boost sensor error",
        "- Related Issue: Engine overboost condition risking damage",
        "- Suggestion: Inspect wastegate actuator and sensors; repair or replace"
    ]
},
{
    "conditions": ["knock sensor circuit high input bank 2", "P0337", "knock sensor high voltage"],
    "bullets": [
        "- Condition: Knock Sensor Circuit High Input (Bank 2)",
        "- Likely Issue: Shorted wiring or faulty sensor",
        "- Related Issue: Engine knocking and potential damage",
        "- Suggestion: Test sensor and wiring; replace if defective"
    ]
},
{
    "conditions": ["catalytic converter temperature sensor circuit malfunction", "P0421", "catalyst temperature sensor fault"],
    "bullets": [
        "- Condition: Catalytic Converter Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring issues",
        "- Related Issue: Incorrect emission control system readings",
        "- Suggestion: Inspect sensor and wiring; replace sensor if necessary"
    ]
},
{
    "conditions": ["transmission range sensor circuit high input", "P0705", "transmission range sensor fault"],
    "bullets": [
        "- Condition: Transmission Range Sensor Circuit High Input",
        "- Likely Issue: Shorted wiring or faulty range sensor",
        "- Related Issue: Incorrect gear selection and shifting problems",
        "- Suggestion: Check wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["fuel injector circuit low", "P0200", "fuel injector circuit malfunction"],
    "bullets": [
        "- Condition: Fuel Injector Circuit Low",
        "- Likely Issue: Wiring short or faulty injector",
        "- Related Issue: Engine misfire and poor performance",
        "- Suggestion: Inspect wiring and injector; repair or replace"
    ]
},
{
    "conditions": ["intake air temperature sensor circuit high input", "P0113", "intake air temp sensor high voltage"],
    "bullets": [
        "- Condition: Intake Air Temperature Sensor Circuit High Input",
        "- Likely Issue: Open circuit or faulty sensor",
        "- Related Issue: Rich fuel mixture and engine stalling",
        "- Suggestion: Check wiring and sensor; replace if needed"
    ]
},
{
    "conditions": ["evaporative emission system purge flow fault", "P0449", "EVAP purge flow fault"],
    "bullets": [
        "- Condition: EVAP System Purge Flow Fault",
        "- Likely Issue: Faulty purge valve or line blockage",
        "- Related Issue: Increased emissions and fuel vapor leaks",
        "- Suggestion: Inspect purge valve and hoses; clean or replace"
    ]
},
{
    "conditions": ["camshaft position sensor circuit intermittent", "P0340", "camshaft sensor fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit Intermittent",
        "- Likely Issue: Loose wiring or failing sensor",
        "- Related Issue: Engine misfires and poor performance",
        "- Suggestion: Inspect wiring and sensor; replace if defective"
    ]
},
{
    "conditions": ["coolant thermostat stuck open", "P0128", "coolant thermostat fault"],
    "bullets": [
        "- Condition: Coolant Thermostat Stuck Open",
        "- Likely Issue: Thermostat failed to close",
        "- Related Issue: Engine running too cold affecting efficiency",
        "- Suggestion: Replace thermostat"
    ]
},
{
    "conditions": ["secondary air injection system relay fault", "P0410", "secondary air injection fault"],
    "bullets": [
        "- Condition: Secondary Air Injection System Relay Fault",
        "- Likely Issue: Faulty relay or wiring issue",
        "- Related Issue: Emissions system malfunction",
        "- Suggestion: Test relay and wiring; replace if necessary"
    ]
},
{
    "conditions": ["battery positive voltage low", "P0562", "low battery voltage"],
    "bullets": [
        "- Condition: Battery Positive Voltage Low",
        "- Likely Issue: Weak battery or charging system issue",
        "- Related Issue: Starting problems and electrical faults",
        "- Suggestion: Test battery and alternator; replace battery if needed"
    ]
},
{
    "conditions": ["abs pump motor relay fault", "C0265", "ABS pump relay malfunction"],
    "bullets": [
        "- Condition: ABS Pump Motor Relay Fault",
        "- Likely Issue: Faulty relay or wiring",
        "- Related Issue: Reduced ABS functionality",
        "- Suggestion: Check relay and wiring; replace relay if defective"
    ]
},
{
    "conditions": ["tire pressure sensor malfunction", "C2121", "TPMS sensor fault"],
    "bullets": [
        "- Condition: Tire Pressure Monitoring System (TPMS) Sensor Malfunction",
        "- Likely Issue: Faulty sensor or battery failure",
        "- Related Issue: Incorrect tire pressure warnings",
        "- Suggestion: Replace TPMS sensor or battery"
    ]
},
{
    "conditions": ["transmission fluid temperature too high", "P0715", "transmission overheating"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Too High",
        "- Likely Issue: Overheating transmission due to fluid issues",
        "- Related Issue: Premature transmission wear or failure",
        "- Suggestion: Check fluid level and quality; service transmission cooling system"
    ]
},
{
    "conditions": ["engine coolant temperature sensor circuit low", "P0117", "engine coolant sensor low voltage"],
    "bullets": [
        "- Condition: Engine Coolant Temperature Sensor Circuit Low Voltage",
        "- Likely Issue: Short to ground or faulty sensor",
        "- Related Issue: Engine overheating or incorrect temperature reading",
        "- Suggestion: Inspect wiring and sensor; replace if needed"
    ]
},
{
    "conditions": ["mass air flow sensor circuit high input", "P0101", "MAF sensor performance issue"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit High Input",
        "- Likely Issue: Wiring short or dirty sensor",
        "- Related Issue: Rich fuel mixture, poor performance",
        "- Suggestion: Clean sensor and check wiring; replace if faulty"
    ]
},
{
    "conditions": ["oxygen sensor circuit low voltage bank 1 sensor 2", "P0134", "oxygen sensor no activity"],
    "bullets": [
        "- Condition: Oxygen Sensor Circuit No Activity Detected (Bank 1 Sensor 2)",
        "- Likely Issue: Faulty oxygen sensor or wiring problem",
        "- Related Issue: Increased emissions and poor fuel economy",
        "- Suggestion: Test sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["intake air temperature sensor circuit low input", "P0112", "intake air temp sensor low voltage"],
    "bullets": [
        "- Condition: Intake Air Temperature Sensor Circuit Low Input",
        "- Likely Issue: Short to ground or faulty sensor",
        "- Related Issue: Engine performance issues due to incorrect air temp readings",
        "- Suggestion: Inspect wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["evaporative emission system leak large detected", "P0455", "large EVAP system leak"],
    "bullets": [
        "- Condition: EVAP System Leak Detected (Large Leak)",
        "- Likely Issue: Loose or missing gas cap, or damaged EVAP components",
        "- Related Issue: Fuel vapor loss and emission control failure",
        "- Suggestion: Check gas cap and EVAP hoses; replace faulty parts"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit no signal", "P0501", "vehicle speed sensor no signal"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit No Signal",
        "- Likely Issue: Faulty sensor or wiring break",
        "- Related Issue: Transmission shifting and speedometer issues",
        "- Suggestion: Inspect sensor wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["throttle position sensor circuit high input", "P0123", "throttle sensor high voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit High Input",
        "- Likely Issue: Open circuit or faulty sensor",
        "- Related Issue: Throttle control problems, engine hesitation",
        "- Suggestion: Check wiring and sensor; replace if needed"
    ]
},
{
    "conditions": ["knock sensor circuit low input bank 1", "P0325", "knock sensor low voltage"],
    "bullets": [
        "- Condition: Knock Sensor Circuit Low Input (Bank 1)",
        "- Likely Issue: Open circuit or faulty sensor",
        "- Related Issue: Engine knocking and poor performance",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["catalyst system efficiency below threshold bank 2", "P0430", "catalytic converter efficiency low"],
    "bullets": [
        "- Condition: Catalyst System Efficiency Below Threshold (Bank 2)",
        "- Likely Issue: Failing catalytic converter or oxygen sensor issue",
        "- Related Issue: Increased emissions and failed emissions tests",
        "- Suggestion: Inspect catalytic converter and sensors; replace if faulty"
    ]
},
{
    "conditions": ["transmission control module internal fault", "P0717", "TCM internal fault"],
    "bullets": [
        "- Condition: Transmission Control Module Internal Fault",
        "- Likely Issue: TCM hardware or software failure",
        "- Related Issue: Erratic shifting or transmission limp mode",
        "- Suggestion: Scan and reprogram or replace TCM"
    ]
},
{
    "conditions": ["fuel level sensor circuit malfunction", "P0463", "fuel level sensor fault"],
    "bullets": [
        "- Condition: Fuel Level Sensor Circuit Malfunction",
        "- Likely Issue: Faulty sensor or wiring issues",
        "- Related Issue: Incorrect fuel gauge readings",
        "- Suggestion: Check sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["crankshaft position sensor circuit no signal", "P0336", "crankshaft sensor no signal"],
    "bullets": [
        "- Condition: Crankshaft Position Sensor Circuit No Signal",
        "- Likely Issue: Broken wiring or failed sensor",
        "- Related Issue: Engine no start or stalling",
        "- Suggestion: Inspect wiring; replace sensor if faulty"
    ]
},
{
    "conditions": ["air conditioning refrigerant pressure sensor malfunction", "P0551", "A/C pressure sensor fault"],
    "bullets": [
        "- Condition: A/C Refrigerant Pressure Sensor Malfunction",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: A/C system not functioning properly",
        "- Suggestion: Test sensor and wiring; replace sensor if defective"
    ]
},
{
    "conditions": ["exhaust gas temperature sensor circuit malfunction", "P2097", "exhaust temperature sensor fault"],
    "bullets": [
        "- Condition: Exhaust Gas Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Sensor failure or wiring problem",
        "- Related Issue: Emissions and engine efficiency issues",
        "- Suggestion: Inspect sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["transmission fluid pressure sensor circuit low", "P0712", "transmission fluid pressure sensor low voltage"],
    "bullets": [
        "- Condition: Transmission Fluid Pressure Sensor Circuit Low",
        "- Likely Issue: Short to ground or sensor malfunction",
        "- Related Issue: Transmission pressure irregularities",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["electronic throttle control system voltage low", "P2103", "ETC system voltage low"],
    "bullets": [
        "- Condition: Electronic Throttle Control System Voltage Low",
        "- Likely Issue: Wiring or sensor power supply fault",
        "- Related Issue: Throttle control issues and limp mode",
        "- Suggestion: Inspect wiring and connectors; repair or replace components"
    ]
},
{
    "conditions": ["intake valve control solenoid circuit malfunction", "P2135", "intake valve solenoid fault"],
    "bullets": [
        "- Condition: Intake Valve Control Solenoid Circuit Malfunction",
        "- Likely Issue: Faulty solenoid or wiring problem",
        "- Related Issue: Poor engine performance and emissions",
        "- Suggestion: Test solenoid and wiring; replace if defective"
    ]
},
{
    "conditions": ["rear oxygen sensor circuit slow response bank 1 sensor 2", "P0138", "rear O2 sensor slow response"],
    "bullets": [
        "- Condition: Rear Oxygen Sensor Circuit Slow Response (Bank 1 Sensor 2)",
        "- Likely Issue: Contaminated or failing sensor",
        "- Related Issue: Increased emissions and fuel consumption",
        "- Suggestion: Replace oxygen sensor"
    ]
},
{
    "conditions": ["fuel injector control circuit high", "P0201", "fuel injector circuit high voltage"],
    "bullets": [
        "- Condition: Fuel Injector Control Circuit High",
        "- Likely Issue: Wiring short to voltage or faulty injector",
        "- Related Issue: Engine misfire and rough running",
        "- Suggestion: Inspect wiring and injector; repair or replace"
    ]
},
{
    "conditions": ["camshaft position sensor circuit intermittent", "P0340", "camshaft position sensor fault"],
    "bullets": [
        "- Condition: Camshaft Position Sensor Circuit Intermittent",
        "- Likely Issue: Loose wiring or faulty sensor",
        "- Related Issue: Engine misfires, poor timing",
        "- Suggestion: Inspect wiring and sensor; replace if needed"
    ]
},
{
    "conditions": ["evaporative emission system purge flow fault", "P0443", "EVAP purge valve fault"],
    "bullets": [
        "- Condition: Evaporative Emission System Purge Flow Fault",
        "- Likely Issue: Faulty purge valve or wiring",
        "- Related Issue: Fuel vapor leaks and increased emissions",
        "- Suggestion: Test valve and wiring; replace if defective"
    ]
},
{
    "conditions": ["barometric pressure sensor circuit range/performance", "P0108", "barometric pressure sensor fault"],
    "bullets": [
        "- Condition: Barometric Pressure Sensor Circuit Range/Performance",
        "- Likely Issue: Faulty sensor or wiring",
        "- Related Issue: Engine load calculation errors",
        "- Suggestion: Check sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit intermittent", "P0503", "vehicle speed sensor intermittent fault"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit Intermittent",
        "- Likely Issue: Loose wiring or failing sensor",
        "- Related Issue: Erratic speedometer and shifting problems",
        "- Suggestion: Inspect wiring; replace sensor if needed"
    ]
},
{
    "conditions": ["secondary air injection pump circuit malfunction", "P0410", "secondary air injection pump fault"],
    "bullets": [
        "- Condition: Secondary Air Injection Pump Circuit Malfunction",
        "- Likely Issue: Pump failure or wiring issue",
        "- Related Issue: Emission control inefficiency",
        "- Suggestion: Test pump and wiring; replace if defective"
    ]
},
{
    "conditions": ["oil pressure sensor circuit low input", "P0521", "oil pressure sensor low voltage"],
    "bullets": [
        "- Condition: Oil Pressure Sensor Circuit Low Input",
        "- Likely Issue: Wiring short to ground or faulty sensor",
        "- Related Issue: Incorrect oil pressure readings",
        "- Suggestion: Inspect wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["intake manifold runner control circuit malfunction", "P2004", "intake manifold runner fault"],
    "bullets": [
        "- Condition: Intake Manifold Runner Control Circuit Malfunction",
        "- Likely Issue: Faulty actuator or wiring problem",
        "- Related Issue: Poor engine performance",
        "- Suggestion: Test actuator and wiring; repair or replace"
    ]
},
{
    "conditions": ["fuel pressure regulator control circuit high", "P1251", "fuel pressure regulator high voltage"],
    "bullets": [
        "- Condition: Fuel Pressure Regulator Control Circuit High",
        "- Likely Issue: Wiring short to voltage or faulty regulator",
        "- Related Issue: Rich fuel condition",
        "- Suggestion: Check wiring and regulator; repair or replace"
    ]
},
{
    "conditions": ["coolant temperature sensor circuit intermittent", "P0115", "coolant temperature sensor intermittent"],
    "bullets": [
        "- Condition: Coolant Temperature Sensor Circuit Intermittent",
        "- Likely Issue: Loose wiring or failing sensor",
        "- Related Issue: Erratic temperature readings",
        "- Suggestion: Inspect wiring and sensor; replace if necessary"
    ]
},
{
    "conditions": ["transmission fluid temperature sensor circuit high", "P0710", "transmission fluid temp sensor high voltage"],
    "bullets": [
        "- Condition: Transmission Fluid Temperature Sensor Circuit High",
        "- Likely Issue: Open circuit or faulty sensor",
        "- Related Issue: Incorrect transmission temperature monitoring",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["exhaust gas recirculation temperature sensor circuit malfunction", "P0403", "EGR temperature sensor fault"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Temperature Sensor Circuit Malfunction",
        "- Likely Issue: Sensor failure or wiring issue",
        "- Related Issue: Emission control problems",
        "- Suggestion: Inspect sensor and wiring; replace if faulty"
    ]
},
{
    "conditions": ["fuel tank pressure sensor circuit low input", "P0452", "fuel tank pressure sensor low voltage"],
    "bullets": [
        "- Condition: Fuel Tank Pressure Sensor Circuit Low Input",
        "- Likely Issue: Short to ground or faulty sensor",
        "- Related Issue: EVAP system leak detection errors",
        "- Suggestion: Check wiring and sensor; repair or replace"
    ]
},
 {
        "conditions": [
            "engine won't start",
            "car won’t turn over",
            "engine no crank",
            "starter motor silent",
            "no response when key turned",
            "clicking noise when starting"
        ],
        "bullets": [
            "- Condition: Engine Won't Start",
            "- Likely Issues: Dead battery, faulty starter motor, bad ignition switch",
            "- Related Issue: Battery voltage low, corroded terminals",
            "- Suggestion: Check battery charge and connections; test starter and ignition switch"
        ]
    },
    {
        "conditions": [
            "engine stalls while driving",
            "engine cuts out suddenly",
            "car dies while moving",
            "engine loses power randomly",
            "stalling at low speed"
        ],
        "bullets": [
            "- Condition: Engine Stalls While Driving",
            "- Likely Issues: Fuel delivery problems, faulty ignition coils, clogged fuel filter",
            "- Related Issue: Dirty throttle body, vacuum leaks",
            "- Suggestion: Inspect fuel system, ignition components, and vacuum hoses; clean throttle body"
        ]
    },
    {
        "conditions": [
            "rough idling",
            "engine vibrates at idle",
            "idle surges up and down",
            "car jerks at idle",
            "uneven engine RPM"
        ],
        "bullets": [
            "- Condition: Rough Idling",
            "- Likely Issues: Vacuum leaks, dirty idle air control valve, faulty spark plugs",
            "- Related Issue: Faulty mass airflow sensor, clogged fuel injectors",
            "- Suggestion: Inspect vacuum system, clean or replace IAC valve; check ignition and fuel systems"
        ]
    },
    {
        "conditions": [
            "engine overheating",
            "temperature gauge rises quickly",
            "steam from radiator",
            "radiator fan not working",
            "coolant warning light"
        ],
        "bullets": [
            "- Condition: Engine Overheating",
            "- Likely Issues: Faulty thermostat, coolant leak, water pump failure",
            "- Related Issue: Radiator blockage, failed cooling fan",
            "- Suggestion: Check coolant level and leaks; test thermostat, water pump, radiator fan operation"
        ]
    },
    {
        "conditions": [
            "check engine light on",
            "engine warning light on dash",
            "malfunction indicator lamp lit",
            "CEL illuminated",
            "check engine warning active"
        ],
        "bullets": [
            "- Condition: Check Engine Light On",
            "- Likely Issues: Sensor failures (O2, MAF, TPS), ignition faults, emission system problems",
            "- Related Issue: Loose gas cap, catalytic converter issues",
            "- Suggestion: Scan for DTC codes; address sensor or system faults accordingly"
        ]
    },
    {
        "conditions": [
            "car won’t accelerate",
            "engine revs but no speed increase",
            "slow to gain speed",
            "acceleration delayed",
            "car sluggish when pressing gas"
        ],
        "bullets": [
            "- Condition: Car Won’t Accelerate",
            "- Likely Issues: Transmission slipping, clogged catalytic converter, faulty fuel pump",
            "- Related Issue: Dirty throttle body, MAF sensor fault",
            "- Suggestion: Check transmission fluid level; inspect fuel delivery and exhaust systems"
        ]
    },
    {
        "conditions": [
            "transmission slipping",
            "engine revs but car slows down",
            "gear slips randomly",
            "car loses power on acceleration",
            "transmission jerks when accelerating"
        ],
        "bullets": [
            "- Condition: Transmission Slipping",
            "- Likely Issues: Low transmission fluid, worn clutch (manual), faulty torque converter (auto)",
            "- Related Issue: Transmission filter clog, valve body malfunction",
            "- Suggestion: Check fluid level and condition; service or repair transmission components"
        ]
    },
    {
        "conditions": [
            "transmission won’t shift",
            "car stuck in one gear",
            "transmission won’t change gear",
            "gear lever stuck",
            "automatic won’t shift up or down"
        ],
        "bullets": [
            "- Condition: Transmission Won’t Shift",
            "- Likely Issues: Transmission control module failure, low fluid level, shift solenoid failure",
            "- Related Issue: Worn clutch, mechanical linkage problems",
            "- Suggestion: Scan transmission module; check fluid and mechanical linkages; repair or replace faulty parts"
        ]
    },
    {
        "conditions": [
            "clutch slipping (manual transmission)",
            "engine revs but no speed increase",
            "slipping clutch when accelerating",
            "clutch pedal feels soft",
            "burning smell from clutch"
        ],
        "bullets": [
            "- Condition: Clutch Slipping (Manual Transmission)",
            "- Likely Issues: Worn clutch disc, oil contamination on clutch plates, improper clutch adjustment",
            "- Related Issue: Pressure plate failure, release bearing issues",
            "- Suggestion: Inspect clutch assembly; replace worn components; adjust clutch pedal free play"
        ]
    },
    {
        "conditions": [
            "car pulling to one side",
            "steering wheel off center",
            "car drifts left or right",
            "uneven brake wear",
            "vehicle veers on straight road"
        ],
        "bullets": [
            "- Condition: Car Pulling to One Side",
            "- Likely Issues: Wheel misalignment, uneven tire pressure, stuck brake caliper",
            "- Related Issue: Suspension damage, worn steering components",
            "- Suggestion: Perform wheel alignment; check tire pressure; inspect brakes and suspension"
        ]
    },
    {
        "conditions": [
            "brake pedal feels spongy",
            "soft brake pedal",
            "brakes feel mushy",
            "brake pedal goes to floor",
            "air in brake lines"
        ],
        "bullets": [
            "- Condition: Spongy Brake Pedal",
            "- Likely Issues: Air in brake lines, brake fluid leak, master cylinder failure",
            "- Related Issue: Worn brake pads, caliper issues",
            "- Suggestion: Bleed brake system; inspect for leaks; replace faulty components"
        ]
    },
    {
        "conditions": [
            "brake noise (squeaking/grinding)",
            "squeal when braking",
            "grinding sound under brake",
            "metal scraping noise",
            "brakes make noise when applied"
        ],
        "bullets": [
            "- Condition: Brake Noise (Squeaking/Grinding)",
            "- Likely Issues: Worn brake pads, damaged rotors, stuck calipers",
            "- Related Issue: Brake dust accumulation, brake hardware wear",
            "- Suggestion: Inspect brake pads and rotors; clean or replace components as needed"
        ]
    },
    {
        "conditions": [
            "ABS light on",
            "ABS warning on dashboard",
            "ABS light stays lit",
            "anti lock brake light active",
            "ABS system malfunction"
        ],
        "bullets": [
            "- Condition: ABS Light On",
            "- Likely Issues: Faulty wheel speed sensor, ABS module failure, wiring issues",
            "- Related Issue: Damaged ABS pump, blown fuse",
            "- Suggestion: Diagnose ABS codes; inspect sensors and wiring; repair or replace faulty parts"
        ]
    },
    {
        "conditions": [
            "battery won’t hold charge",
            "car battery dies quickly",
            "battery drains overnight",
            "battery voltage drops",
            "battery light on dash"
        ],
        "bullets": [
            "- Condition: Battery Won’t Hold Charge",
            "- Likely Issues: Faulty alternator, parasitic drain, old battery",
            "- Related Issue: Corroded terminals, loose battery cables",
            "- Suggestion: Test alternator output; check for electrical drains; replace battery if needed"
        ]
    },
    {
        "conditions": [
            "car won’t start, clicking noise",
            "starter clicks but no crank",
            "clicking sound when turning key",
            "engine won’t turn over",
            "clicking relay noise"
        ],
        "bullets": [
            "- Condition: Car Won’t Start, Clicking Noise",
            "- Likely Issues: Weak battery, faulty starter motor, bad starter solenoid",
            "- Related Issue: Corroded battery terminals, poor electrical connections",
            "- Suggestion: Test battery voltage; inspect starter and wiring; clean terminals"
        ]
    },
    {
        "conditions": [
            "alternator failure",
            "battery light on dash",
            "car battery dies while running",
            "dim headlights when idling",
            "electrical system failure"
        ],
        "bullets": [
            "- Condition: Alternator Failure",
            "- Likely Issues: Faulty alternator diode, worn belt, bad voltage regulator",
            "- Related Issue: Battery drains, electrical accessories malfunction",
            "- Suggestion: Test alternator output; inspect drive belt; replace faulty alternator or regulator"
        ]
    },
    {
        "conditions": [
            "engine won't start",
            "car won’t turn over",
            "engine no crank",
            "starter motor silent",
            "no response when key turned",
            "clicking noise when starting"
        ],
        "bullets": [
            "- Condition: Engine Won't Start",
            "- Likely Issues: Dead battery, faulty starter motor, bad ignition switch",
            "- Related Issue: Battery voltage low, corroded terminals",
            "- Suggestion: Check battery charge and connections; test starter and ignition switch"
        ]
    },                      
    {
        "conditions": [
            "engine stalls while driving",
            "engine cuts out suddenly",
            "car dies while moving",
            "engine loses power randomly",
            "stalling at low speed"
        ],
        "bullets": [
            "- Condition: Engine Stalls While Driving",
            "- Likely Issues: Fuel delivery problems, faulty ignition coils, clogged fuel filter",
            "- Related Issue: Dirty throttle body, vacuum leaks",
            "- Suggestion: Inspect fuel system, ignition components, and vacuum hoses; clean throttle body"
        ]
    },
    {
        "conditions": [
            "rough idling",
            "engine vibrates at idle",
            "idle surges up and down",
            "car jerks at idle",
            "uneven engine RPM"
        ],
        "bullets": [
            "- Condition: Rough Idling",
            "- Likely Issues: Vacuum leaks, dirty idle air control valve, faulty spark plugs",
            "- Related Issue: Faulty mass airflow sensor, clogged fuel injectors",
            "- Suggestion: Inspect vacuum system, clean or replace IAC valve; check ignition and fuel systems"
        ]
    },
    {
        "conditions": [
            "engine overheating",
            "temperature gauge rises quickly",
            "steam from radiator",
            "radiator fan not working",
            "coolant warning light"
        ],
        "bullets": [
            "- Condition: Engine Overheating",
            "- Likely Issues: Faulty thermostat, coolant leak, water pump failure",
            "- Related Issue: Radiator blockage, failed cooling fan",
            "- Suggestion: Check coolant level and leaks; test thermostat, water pump, radiator fan operation"
        ]
    },
    {
        "conditions": [
            "check engine light on",
            "engine warning light on dash",
            "malfunction indicator lamp lit",
            "CEL illuminated",
            "check engine warning active"
        ],
        "bullets": [
            "- Condition: Check Engine Light On",
            "- Likely Issues: Sensor failures (O2, MAF, TPS), ignition faults, emission system problems",
            "- Related Issue: Loose gas cap, catalytic converter issues",
            "- Suggestion: Scan for DTC codes; address sensor or system faults accordingly"
        ]
    },
    {
        "conditions": [
            "car won’t accelerate",
            "engine revs but no speed increase",
            "slow to gain speed",
            "acceleration delayed",
            "car sluggish when pressing gas"
        ],
        "bullets": [
            "- Condition: Car Won’t Accelerate",
            "- Likely Issues: Transmission slipping, clogged catalytic converter, faulty fuel pump",
            "- Related Issue: Dirty throttle body, MAF sensor fault",
            "- Suggestion: Check transmission fluid level; inspect fuel delivery and exhaust systems"
        ]
    },
    {
        "conditions": [
            "transmission slipping",
            "engine revs but car slows down",
            "gear slips randomly",
            "car loses power on acceleration",
            "transmission jerks when accelerating"
        ],
        "bullets": [
            "- Condition: Transmission Slipping",
            "- Likely Issues: Low transmission fluid, worn clutch (manual), faulty torque converter (auto)",
            "- Related Issue: Transmission filter clog, valve body malfunction",
            "- Suggestion: Check fluid level and condition; service or repair transmission components"
        ]
    },
    {
        "conditions": [
            "transmission won’t shift",
            "car stuck in one gear",
            "transmission won’t change gear",
            "gear lever stuck",
            "automatic won’t shift up or down"
        ],
        "bullets": [
            "- Condition: Transmission Won’t Shift",
            "- Likely Issues: Transmission control module failure, low fluid level, shift solenoid failure",
            "- Related Issue: Worn clutch, mechanical linkage problems",
            "- Suggestion: Scan transmission module; check fluid and mechanical linkages; repair or replace faulty parts"
        ]
    },
    {
        "conditions": [
            "clutch slipping (manual transmission)",
            "engine revs but no speed increase",
            "slipping clutch when accelerating",
            "clutch pedal feels soft",
            "burning smell from clutch"
        ],
        "bullets": [
            "- Condition: Clutch Slipping (Manual Transmission)",
            "- Likely Issues: Worn clutch disc, oil contamination on clutch plates, improper clutch adjustment",
            "- Related Issue: Pressure plate failure, release bearing issues",
            "- Suggestion: Inspect clutch assembly; replace worn components; adjust clutch pedal free play"
        ]
    },
    {
        "conditions": [
            "car pulling to one side",
            "steering wheel off center",
            "car drifts left or right",
            "uneven brake wear",
            "vehicle veers on straight road"
        ],
        "bullets": [
            "- Condition: Car Pulling to One Side",
            "- Likely Issues: Wheel misalignment, uneven tire pressure, stuck brake caliper",
            "- Related Issue: Suspension damage, worn steering components",
            "- Suggestion: Perform wheel alignment; check tire pressure; inspect brakes and suspension"
        ]
    },
    {
        "conditions": [
            "brake pedal feels spongy",
            "soft brake pedal",
            "brakes feel mushy",
            "brake pedal goes to floor",
            "air in brake lines"
        ],
        "bullets": [
            "- Condition: Spongy Brake Pedal",
            "- Likely Issues: Air in brake lines, brake fluid leak, master cylinder failure",
            "- Related Issue: Worn brake pads, caliper issues",
            "- Suggestion: Bleed brake system; inspect for leaks; replace faulty components"
        ]
    },
    {
        "conditions": [
            "brake noise (squeaking/grinding)",
            "squeal when braking",
            "grinding sound under brake",
            "metal scraping noise",
            "brakes make noise when applied"
        ],
        "bullets": [
            "- Condition: Brake Noise (Squeaking/Grinding)",
            "- Likely Issues: Worn brake pads, damaged rotors, stuck calipers",
            "- Related Issue: Brake dust accumulation, brake hardware wear",
            "- Suggestion: Inspect brake pads and rotors; clean or replace components as needed"
        ]
    },
    {
        "conditions": [
            "ABS light on",
            "ABS warning on dashboard",
            "ABS light stays lit",
            "anti lock brake light active",
            "ABS system malfunction"
        ],
        "bullets": [
            "- Condition: ABS Light On",
            "- Likely Issues: Faulty wheel speed sensor, ABS module failure, wiring issues",
            "- Related Issue: Damaged ABS pump, blown fuse",
            "- Suggestion: Diagnose ABS codes; inspect sensors and wiring; repair or replace faulty parts"
        ]
    },
    {
        "conditions": [
            "battery won’t hold charge",
            "car battery dies quickly",
            "battery drains overnight",
            "battery voltage drops",
            "battery light on dash"
        ],
        "bullets": [
            "- Condition: Battery Won’t Hold Charge",
            "- Likely Issues: Faulty alternator, parasitic drain, old battery",
            "- Related Issue: Corroded terminals, loose battery cables",
            "- Suggestion: Test alternator output; check for electrical drains; replace battery if needed"
        ]
    },
    {
        "conditions": [
            "car won’t start, clicking noise",
            "starter clicks but no crank",
            "clicking sound when turning key",
            "engine won’t turn over",
            "clicking relay noise"
        ],
        "bullets": [
            "- Condition: Car Won’t Start, Clicking Noise",
            "- Likely Issues: Weak battery, faulty starter motor, bad starter solenoid",
            "- Related Issue: Corroded battery terminals, poor electrical connections",
            "- Suggestion: Test battery voltage; inspect starter and wiring; clean terminals"
        ]
    },
    {
        "conditions": [
            "alternator failure",
            "battery light on dash",
            "car battery dies while running",
            "dim headlights when idling",
            "electrical system failure"
        ],
        "bullets": [
            "- Condition: Alternator Failure",
            "- Likely Issues: Faulty alternator diode, worn belt, bad voltage regulator",
            "- Related Issue: Battery drains, electrical accessories malfunction",
            "- Suggestion: Test alternator output; inspect drive belt; replace faulty alternator or regulator"
        ]
    },
    {
    "conditions": [
            "engine won't start",
            "car does not crank",
            "engine fails to turn over",
            "no ignition when turning key",
            "engine no response on start"
        ],
        "bullets": [
            "- Condition: Engine Won't Start",
            "- Likely Issues: Dead battery, faulty starter motor, bad ignition switch",
            "- Related Issue: Loose battery cables, blown fuses",
            "- Suggestion: Test battery and starter; check ignition switch and wiring; replace faulty parts"
        ]
        },

    {
        "conditions": [
            "engine stalls while driving",
            "engine cuts off suddenly",
            "car dies at stop",
            "engine loses power and stops",
            "unexpected engine shutdown"
        ],
        "bullets": [
            "- Condition: Engine Stalls While Driving",
            "- Likely Issues: Fuel delivery problems, faulty sensors (MAF, TPS), ignition system faults",
            "- Related Issue: Clogged fuel filter, vacuum leaks",
            "- Suggestion: Inspect fuel system and sensors; check ignition components; clear vacuum leaks"
        ]
    },
    {
        "conditions": [
            "rough idling",
            "engine shakes at idle",
            "unstable idle RPM",
            "engine vibrates when stopped",
            "idle surges or dips"
        ],
        "bullets": [
            "- Condition: Rough Idling",
            "- Likely Issues: Dirty throttle body, faulty spark plugs, vacuum leaks",
            "- Related Issue: Malfunctioning idle air control valve, fuel injection issues",
            "- Suggestion: Clean throttle body; replace spark plugs; inspect vacuum system; service fuel injectors"
        ]
    },
    {
        "conditions": [
            "engine overheating",
            "temperature gauge high",
            "steam from engine bay",
            "coolant boiling",
            "engine temp warning light"
        ],
        "bullets": [
            "- Condition: Engine Overheating",
            "- Likely Issues: Low coolant level, faulty thermostat, radiator blockage",
            "- Related Issue: Water pump failure, cooling fan malfunction",
            "- Suggestion: Check coolant level and leaks; test thermostat and radiator; verify fan operation"
        ]
    },
    {
        "conditions": [
            "check engine light on",
            "engine warning lamp active",
            "malfunction indicator lamp lit",
            "service engine soon light",
            "engine fault warning"
        ],
        "bullets": [
            "- Condition: Check Engine Light ON",
            "- Likely Issues: Emissions system fault, sensor failure, misfires",
            "- Related Issue: Loose gas cap, catalytic converter issues",
            "- Suggestion: Scan OBD-II codes; diagnose fault; repair or replace faulty components"
        ]
    },
    {
        "conditions": [
            "car won't accelerate",
            "slow response when pressing gas",
            "lack of power when driving",
            "engine revs but no speed increase",
            "vehicle struggles uphill"
        ],
        "bullets": [
            "- Condition: Car Won't Accelerate",
            "- Likely Issues: Fuel delivery issues, transmission problems, clogged air filter",
            "- Related Issue: Faulty throttle position sensor, catalytic converter blockage",
            "- Suggestion: Inspect fuel and air systems; check transmission operation; clean or replace filters"
        ]
    },
    {
        "conditions": [
            "transmission slipping",
            "engine revs higher than speed",
            "delayed gear engagement",
            "gear shifts feel soft or inconsistent",
            "loss of acceleration power"
        ],
        "bullets": [
            "- Condition: Transmission Slipping",
            "- Likely Issues: Low transmission fluid, worn clutch (manual), solenoid faults (automatic)",
            "- Related Issue: Transmission fluid leaks, worn gear bands",
            "- Suggestion: Check fluid levels and quality; inspect clutch or solenoids; repair leaks"
        ]
    },
    {
        "conditions": [
            "transmission won't shift",
            "gearbox stuck in one gear",
            "unable to change gears",
            "automatic transmission stuck in park",
            "manual transmission stuck in gear"
        ],
        "bullets": [
            "- Condition: Transmission Won't Shift",
            "- Likely Issues: Faulty transmission control module, broken shift linkage, low fluid",
            "- Related Issue: Transmission hydraulic failure, clutch problems",
            "- Suggestion: Diagnose transmission electronics; check shift cables; inspect fluid and hydraulic systems"
        ]
    },
    {
        "conditions": [
            "clutch slipping (manual transmission)",
            "engine revs without acceleration",
            "difficulty in gear engagement",
            "burning smell from clutch",
            "loss of power transfer"
        ],
        "bullets": [
            "- Condition: Clutch Slipping (Manual Transmission)",
            "- Likely Issues: Worn clutch disc, oil contamination, misadjusted clutch cable",
            "- Related Issue: Faulty pressure plate, release bearing problems",
            "- Suggestion: Inspect clutch components; adjust or replace clutch cable; replace worn parts"
        ]
    },
    {
        "conditions": [
            "car pulling to one side",
            "steering off center",
            "uneven brake pulling",
            "vehicle drifts left or right",
            "hard to keep straight driving"
        ],
        "bullets": [
            "- Condition: Car Pulling to One Side",
            "- Likely Issues: Wheel misalignment, uneven tire pressure, stuck brake caliper",
            "- Related Issue: Suspension damage, uneven tire wear",
            "- Suggestion: Check and adjust alignment; balance tire pressures; inspect brakes and suspension"
        ]
    },
      {
        "conditions": [
            "brake pedal feels spongy",
            "soft brake pedal",
            "brake pedal sinks to floor",
            "loss of brake pressure",
            "brakes feel mushy"
        ],
        "bullets": [
            "- Condition: Spongy Brake Pedal",
            "- Likely Issues: Air in brake lines, low brake fluid, worn brake pads",
            "- Related Issue: Brake hose leaks, master cylinder failure",
            "- Suggestion: Bleed brake system; check fluid levels; inspect pads and hoses"
        ]
    },
    {
        "conditions": [
            "brake noise squeaking",
            "brakes make grinding noise",
            "squeal when braking",
            "metallic noise from brakes",
            "brakes screech loudly"
        ],
        "bullets": [
            "- Condition: Brake Noise (Squeaking/Grinding)",
            "- Likely Issues: Worn brake pads, glazed rotors, lack of lubrication",
            "- Related Issue: Brake hardware failure, stuck caliper",
            "- Suggestion: Replace brake pads; resurface or replace rotors; lubricate hardware"
        ]
    },
    {
        "conditions": [
            "battery won’t hold charge",
            "battery drains quickly",
            "car won’t start after sitting",
            "battery light on dash",
            "dead battery repeatedly"
        ],
        "bullets": [
            "- Condition: Battery Won't Hold Charge",
            "- Likely Issues: Faulty alternator, parasitic drain, old battery",
            "- Related Issue: Corroded battery terminals, bad battery cables",
            "- Suggestion: Test alternator output; check for electrical drains; clean terminals and replace battery if needed"
        ]
    },
    {
        "conditions": [
            "car won’t start clicking noise",
            "starter clicks but no crank",
            "engine doesn’t turn over",
            "rapid clicking when starting",
            "starter motor clicks but no action"
        ],
        "bullets": [
            "- Condition: Car Won’t Start, Clicking Noise",
            "- Likely Issues: Weak battery, faulty starter relay, bad starter motor",
            "- Related Issue: Loose battery connections, corroded terminals",
            "- Suggestion: Test battery voltage; check starter relay and connections; repair or replace starter"
        ]
    },
    {
        "conditions": [
            "alternator failure",
            "battery warning light",
            "car dies while running",
            "electrical systems fail",
            "dim headlights at idle"
        ],
        "bullets": [
            "- Condition: Alternator Failure",
            "- Likely Issues: Faulty alternator, broken drive belt, wiring issues",
            "- Related Issue: Dead battery, blown fuses",
            "- Suggestion: Test alternator output; inspect belt condition; repair wiring faults"
        ]
    },
    {
        "conditions": [
            "headlights flickering or dim",
            "headlights fade while driving",
            "light intensity changes",
            "dashboard lights flicker",
            "electrical flicker in lights"
        ],
        "bullets": [
            "- Condition: Headlights Flickering or Dim",
            "- Likely Issues: Loose wiring, failing alternator, bad ground connections",
            "- Related Issue: Battery issues, faulty light switches",
            "- Suggestion: Inspect wiring harness and grounds; test alternator and battery; replace faulty switches"
        ]
    },
    {
        "conditions": [
            "power steering failure",
            "steering hard to turn",
            "loss of power assist",
            "power steering fluid leak",
            "steering wheel stiff"
        ],
        "bullets": [
            "- Condition: Power Steering Failure",
            "- Likely Issues: Low power steering fluid, broken pump, belt slip",
            "- Related Issue: Faulty steering rack, leaks in system",
            "- Suggestion: Check and top up fluid; inspect pump and belts; repair leaks and faulty components"
        ]
    },
    {
        "conditions": [
            "steering wheel vibration",
            "shaking steering at speed",
            "steering wheel shakes when braking",
            "steering wobble",
            "vibrations felt through wheel"
        ],
        "bullets": [
            "- Condition: Steering Wheel Vibration",
            "- Likely Issues: Unbalanced tires, worn suspension parts, warped brake rotors",
            "- Related Issue: Bent wheels, loose steering components",
            "- Suggestion: Balance tires; inspect suspension and brakes; replace warped rotors"
        ]
    },
    {
        "conditions": [
            "suspension knocking noise",
            "clunking when driving over bumps",
            "knock from front suspension",
            "rear suspension knocking",
            "noise when turning or cornering"
        ],
        "bullets": [
            "- Condition: Suspension Knocking Noise",
            "- Likely Issues: Worn ball joints, broken sway bar links, damaged bushings",
            "- Related Issue: Loose shock absorbers, strut mount failure",
            "- Suggestion: Inspect and replace worn suspension components; tighten mounts"
        ]
    },
    {
        "conditions": [
            "uneven tire wear",
            "tires wear faster on one side",
            "bald spots on tires",
            "tire tread irregular",
            "tires worn inside or outside edges"
        ],
        "bullets": [
            "- Condition: Uneven Tire Wear",
            "- Likely Issues: Misalignment, improper tire pressure, worn suspension parts",
            "- Related Issue: Bent wheels, damaged shocks",
            "- Suggestion: Perform wheel alignment; maintain correct tire pressures; inspect suspension"
        ]
    },
{
    "conditions": ["knock sensor circuit high input bank 2", "P0330", "knock sensor high voltage"],
    "bullets": [
        "- Condition: Knock Sensor Circuit High Input (Bank 2)",
        "- Likely Issue: Wiring short to voltage or faulty sensor",
        "- Related Issue: Engine knocking and performance issues",
        "- Suggestion: Test sensor and wiring; repair or replace"
    ]
},
{
    "conditions": ["throttle position sensor circuit low input", "P0122", "throttle sensor low voltage"],
    "bullets": [
        "- Condition: Throttle Position Sensor Circuit Low Input",
        "- Likely Issue: Short to ground or faulty sensor",
        "- Related Issue: Throttle response problems",
        "- Suggestion: Inspect wiring and sensor; replace if needed"
    ]
},
{
    "conditions": ["exhaust gas recirculation valve control circuit low", "P0402", "EGR valve low voltage"],
    "bullets": [
        "- Condition: Exhaust Gas Recirculation Valve Control Circuit Low",
        "- Likely Issue: Wiring short or valve malfunction",
        "- Related Issue: Increased emissions and rough idle",
        "- Suggestion: Test wiring and valve; repair or replace"
    ]
},
{
    "conditions": ["idle speed control valve circuit malfunction", "P0505", "idle speed control fault"],
    "bullets": [
        "- Condition: Idle Speed Control Valve Circuit Malfunction",
        "- Likely Issue: Faulty valve or wiring problem",
        "- Related Issue: Irregular idle speeds",
        "- Suggestion: Inspect valve and wiring; replace if defective"
    ]
},
{
    "conditions": ["barometric pressure sensor circuit low input", "P0107", "barometric pressure sensor low voltage"],
    "bullets": [
        "- Condition: Barometric Pressure Sensor Circuit Low Input",
        "- Likely Issue: Wiring short to ground or faulty sensor",
        "- Related Issue: Engine load miscalculations",
        "- Suggestion: Check wiring and sensor; repair or replace"
    ]
},
{
    "conditions": ["mass air flow sensor circuit low input", "P0102", "MAF sensor low voltage"],
    "bullets": [
        "- Condition: Mass Air Flow Sensor Circuit Low Input",
        "- Likely Issue: Wiring short or sensor malfunction",
        "- Related Issue: Lean fuel mixture and poor performance",
        "- Suggestion: Inspect wiring and sensor; clean or replace"
    ]
},
{
    "conditions": ["vehicle speed sensor circuit high input", "P0504", "vehicle speed sensor high voltage"],
    "bullets": [
        "- Condition: Vehicle Speed Sensor Circuit High Input",
        "- Likely Issue: Wiring short to voltage or faulty sensor",
        "- Related Issue: Transmission shift and speedometer errors",
        "- Suggestion: Test wiring and sensor; repair or replace"
    ]
}
]
