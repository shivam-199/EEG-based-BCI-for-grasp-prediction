<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="Grasp-real-time" version="2.0">
	<nodes>
		<node id="0" name="Import XDF" position="(1175.0, 65.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="cbe55b2a-a8c2-4f8d-96ee-26e086fb61b1" version="1.2.1" />
		<node id="1" name="Stream Data" position="(1351.0, 65.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="373a9037-a2ca-481e-98d0-b7da55610bd7" version="1.2.1" />
		<node id="2" name="LSL Output" position="(1503.0, 65.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="79ceeb3e-a7bf-4d34-afd5-7001e8cf4b1c" version="1.4.2" />
		<node id="3" name="LSL Input" position="(171.0, 150.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="0d294378-0847-4f24-95b8-bb766ba834dc" version="1.5.1" />
		<node id="4" name="IIR Filter" position="(681.0, 158.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter" uuid="c6450435-4950-4bbc-8421-dcbbaf6d9809" version="1.1.0" />
		<node id="5" name="Select Range" position="(552.0, 150.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owselectrange.OWSelectRange" title="Select Range" uuid="849f1216-cdc1-41b5-9f03-453cd3710f75" version="1.1.0" />
		<node id="6" name="Segmentation" position="(282.0, 373.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="60991374-82cc-4b3d-bf8b-0519f406d1a5" version="1.0.2" />
		<node id="7" name="Assign Target Values" position="(806.0, 157.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Target Values" uuid="c89b2588-c4f4-4e05-8fe7-e81a4980170c" version="1.0.1" />
		<node id="8" name="Common Spatial Patterns" position="(424.0, 364.0)" project_name="NeuroPype" qualified_name="widgets.neural.owcommonspatialpatterns.OWCommonSpatialPatterns" title="Common Spatial Patterns" uuid="52fcda12-1e3e-4121-a595-3a767a8d8929" version="1.0.0" />
		<node id="9" name="Variance" position="(558.0, 364.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="652f7c9b-cc7b-42c4-9943-62260fa7489a" version="1.0.0" />
		<node id="10" name="Logarithm" position="(698.0, 363.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="f9f46200-6461-4d37-8579-a005c64a6d48" version="1.0.0" />
		<node id="11" name="Logistic Regression" position="(838.0, 364.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="e0beb67e-120c-42f6-9a2b-2298d1b62de6" version="1.1.0" />
		<node id="12" name="Override Axis" position="(971.0, 366.0)" project_name="NeuroPype" qualified_name="widgets.neural.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="21612da2-911b-442f-aeaa-0e8e78a825ea" version="1.4.2" />
		<node id="13" name="Streaming Bar Plot" position="(1094.0, 368.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="76949984-6c05-4c4c-a0c3-96e8925c6c1d" version="1.0.3" />
		<node id="14" name="Time Series Plot" position="(384.0, 510.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="9204649c-24d6-48db-b884-90eb36ea77ca" version="1.0.3" />
		<node id="15" name="Dejitter Timestamps" position="(307.0, 150.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="56977092-c420-4767-828b-26f62320578f" version="1.0.0" />
		<node id="16" name="Accumulate Calibration Data" position="(421.0, 150.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owaccumulatecalibrationdata.OWAccumulateCalibrationData" title="Accumulate Calibration Data" uuid="281397a9-bae8-43ff-811a-e022df93813a" version="1.0.0" />
		<node id="17" name="Time Series Plot" position="(682.0, 47.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot_Filtered" uuid="31b8f30e-f09f-470f-86a5-05c059535e78" version="1.0.3" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="5" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWGcAAABFOi9zdHVkaWVzL2NvbGxlZ2UvSUlUIEdhbmRoaW5hZ2FyL1NFTSBJ
SUkvQ0cgNTk5IFRoZXNpcy9HcmFzcCBFeHBlcmltZW50L0V4cGVyaW1lbnRhbCBEYXRhL0VFRy9Q
MDIueGRmcQhYEwAAAGhhbmRsZV9jbG9ja19yZXNldHNxCYhYEQAAAGhhbmRsZV9jbG9ja19zeW5j
cQqIWBUAAABoYW5kbGVfaml0dGVyX3JlbW92YWxxC4hYDgAAAG1heF9tYXJrZXJfbGVucQxYDQAA
ACh1c2UgZGVmYXVsdClxDVgIAAAAbWV0YWRhdGFxDn1xD1gSAAAAcmVvcmRlcl90aW1lc3RhbXBz
cRCJWA4AAAByZXRhaW5fc3RyZWFtc3ERaA1YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEmNzaXAK
X3VucGlja2xlX3R5cGUKcRNYDAAAAFB5UXQ1LlF0Q29yZXEUWAoAAABRQnl0ZUFycmF5cRVDQgHZ
0MsAAwAAAAADCwAAAWIAAAR0AAACfgAAAwwAAAGIAAAEcwAAAn0AAAAAAAAAAAeAAAADDAAAAYgA
AARzAAACfXEWhXEXh3EYUnEZWA4AAABzZXRfYnJlYWtwb2ludHEaiVgLAAAAdXNlX2NhY2hpbmdx
G4lYDwAAAHVzZV9zdHJlYW1uYW1lc3EciVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="literal" node_id="1">{'data_dtype': 'float64', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgTAAAAR3Jhc3BTdHJlYW0tbWFya2Vyc3EHWBAAAABtYXJrZXJfc291
cmNlX2lkcQhYAAAAAHEJWAwAAABtYXhfYnVmZmVyZWRxCks8WAgAAABtZXRhZGF0YXELfXEMWBcA
AABudW1lcmljX2xhYmVsX3ByZWNpc2lvbnENSwFYGAAAAG51bWVyaWNfbWFya2VyX3ByZWNpc2lv
bnEOSwNYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFuZ2VkcQ+JWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NS5RdENvcmVxElgKAAAAUUJ5dGVB
cnJheXETQ0IB2dDLAAMAAAAAAwwAAAD5AAAEcwAAAwwAAAMMAAAA+QAABHMAAAMMAAAAAAAAAAAH
gAAAAwwAAAD5AAAEcwAAAwxxFIVxFYdxFlJxF1gMAAAAc2VuZF9tYXJrZXJzcRiIWAkAAABzZXBh
cmF0b3JxGVgBAAAALXEaWA4AAABzZXRfYnJlYWtwb2ludHEbiVgJAAAAc291cmNlX2lkcRxoCVgF
AAAAc3JhdGVxHVgNAAAAKHVzZSBkZWZhdWx0KXEeWAsAAABzdHJlYW1fbmFtZXEfWAsAAABHcmFz
cFN0cmVhbXEgWAsAAABzdHJlYW1fdHlwZXEhWAMAAABFRUdxIlgTAAAAdXNlX2RhdGFfdGltZXN0
YW1wc3EjiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEkiXUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgaAAAAbmFtZT0nR3Jhc3BTdHJlYW0tbWFya2VycydxCVgMAAAAbWF4X2Js
b2NrbGVucQpNAARYCgAAAG1heF9idWZsZW5xC0seWAwAAABtYXhfY2h1bmtsZW5xDEsAWAgAAABt
ZXRhZGF0YXENfXEOWAwAAABub21pbmFsX3JhdGVxD1gNAAAAKHVzZSBkZWZhdWx0KXEQWAkAAABv
bWl0X2Rlc2NxEYlYDwAAAHByZWFsbG9jX2J1ZmZlcnESiFgOAAAAcHJvY19jbG9ja3N5bmNxE4hY
DQAAAHByb2NfZGVqaXR0ZXJxFIlYDwAAAHByb2NfbW9ub3Rvbml6ZXEViVgPAAAAcHJvY190aHJl
YWRzYWZlcRaJWAUAAABxdWVyeXEXWAoAAAB0eXBlPSdFRUcncRhYBwAAAHJlY292ZXJxGYhYFAAA
AHJlc29sdmVfbWluaW11bV90aW1lcRpHP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
G2NzaXAKX3VucGlja2xlX3R5cGUKcRxYDAAAAFB5UXQ1LlF0Q29yZXEdWAoAAABRQnl0ZUFycmF5
cR5DQgHZ0MsAAwAAAAADDAAAAV0AAARzAAACqAAAAwwAAAFdAAAEcwAAAqgAAAAAAAAAAAeAAAAD
DAAAAV0AAARzAAACqHEfhXEgh3EhUnEiWA4AAABzZXRfYnJlYWtwb2ludHEjiXUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEc/uZmZmZmZmkc/4AAAAAAAAEsDR0AMAAAAAAAAZVgLAAAAaWdu
b3JlX25hbnNxB4lYCAAAAG1ldGFkYXRhcQh9cQlYBAAAAG1vZGVxClgIAAAAYmFuZHBhc3NxC1gQ
AAAAb2ZmbGluZV9maWx0ZmlsdHEMiVgFAAAAb3JkZXJxDVgNAAAAKHVzZSBkZWZhdWx0KXEOWAkA
AABwYXNzX2xvc3NxD0dACAAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEQY3NpcApfdW5w
aWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJyYXlxE0NCAdnQywAD
AAAAAAMLAAABjgAABHQAAAJSAAADDAAAAbQAAARzAAACUQAAAAAAAAAAB4AAAAMMAAABtAAABHMA
AAJRcRSFcRWHcRZScRdYDgAAAHNldF9icmVha3BvaW50cRiJWAoAAABzdG9wX2F0dGVucRlHQEkA
AAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBQAAAHNwYWNlcQRYCAAAAG1ldGFkYXRhcQV9cQZY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAADDAAAAacAAARzAAACXgAAAwwA
AAGnAAAEcwAAAl4AAAAAAAAAAAeAAAADDAAAAacAAARzAAACXnELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD11xEChLAEsBSwJLA0sESwVLBksHSwhLCUsKSwtLDEsNSw5LD0sQSxFLEksTSxRLFUsW
SxdLGEstSy5LL0swSzFLMkszSzRLNUs2SzdLOEs5SzpLO0s8Sz1LPks/ZVgOAAAAc2V0X2JyZWFr
cG9pbnRxEYlYBAAAAHVuaXRxElgHAAAAaW5kaWNlc3ETdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiFgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgIAAAAbWV0YWRhdGFxA31xBFgPAAAAb25saW5lX2Vwb2NoaW5ncQVYDQAAAG1hcmtlci1s
b2NrZWRxBlgNAAAAc2FtcGxlX29mZnNldHEHSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCGNz
aXAKX3VucGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ1LlF0Q29yZXEKWAoAAABRQnl0ZUFycmF5cQtD
QgHZ0MsAAwAAAAACxgAAALwAAAcWAAADGwAAAscAAADiAAAHFQAAAxoAAAAAAAAAAAeAAAACxwAA
AOIAAAcVAAADGnEMhXENh3EOUnEPWA4AAABzZWxlY3RfbWFya2Vyc3EQXXERWA4AAABzZXRfYnJl
YWtwb2ludHESiVgLAAAAdGltZV9ib3VuZHNxE11xFChHv9AAAAAAAABHP/gAAAAAAABlWAcAAAB2
ZXJib3NlcRWIdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYGwAAAEFjdGlvbkJl
Zy1wYWxtSW4tTGVmdC1DbG9zZXEHSwBYHAAAAEFjdGlvbkJlZy1wYWxtSW4tUmlnaHQtQ2xvc2Vx
CEsAWBoAAABBY3Rpb25CZWctcGFsbUluLUxlZnQtT3BlbnEJSwFYGwAAAEFjdGlvbkJlZy1wYWxt
SW4tUmlnaHQtT3BlbnEKSwFYHQAAAEFjdGlvbkJlZy1wYWxtRG93bi1MZWZ0LUNsb3NlcQtLAFge
AAAAQWN0aW9uQmVnLXBhbG1Eb3duLVJpZ2h0LUNsb3NlcQxLAFgcAAAAQWN0aW9uQmVnLXBhbG1E
b3duLUxlZnQtT3BlbnENSwFYHQAAAEFjdGlvbkJlZy1wYWxtRG93bi1SaWdodC1PcGVucQ5LAVgb
AAAAQWN0aW9uQmVnLXBhbG1VcC1MZWZ0LUNsb3NlcQ9LAFgcAAAAQWN0aW9uQmVnLXBhbG1VcC1S
aWdodC1DbG9zZXEQSwBYGgAAAEFjdGlvbkJlZy1wYWxtVXAtTGVmdC1PcGVucRFLAVgbAAAAQWN0
aW9uQmVnLXBhbG1VcC1SaWdodC1PcGVucRJLAXVYDgAAAG1hcHBpbmdfZm9ybWF0cRNYBgAAAGNv
bXBhdHEUWAgAAABtZXRhZGF0YXEVfXEWWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRdjc2lwCl91
bnBpY2tsZV90eXBlCnEYWAwAAABQeVF0NS5RdENvcmVxGVgKAAAAUUJ5dGVBcnJheXEaQ0IB2dDL
AAMAAP/////////3AAAHgAAABAYAAAJHAAADCwAABX0AAAPzAAAAAAIAAAAHgAAAAAAAAAAdAAAH
fwAABAVxG4VxHIdxHVJxHlgOAAAAc2V0X2JyZWFrcG9pbnRxH4lYEQAAAHN1cHBvcnRfd2lsZGNh
cmRzcSCJWAsAAAB1c2VfbnVtYmVyc3EhiVgHAAAAdmVyYm9zZXEiiXUu
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAoAAABjb25kX2ZpZWxkcQFYCwAAAFRhcmdldFZhbHVlcQJYDwAAAGluaXRpYWxpemVf
b25jZXEDiFgIAAAAbWV0YWRhdGFxBH1xBVgDAAAAbm9mcQZLBFgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXEHY3NpcApfdW5waWNrbGVfdHlwZQpxCFgMAAAAUHlRdDUuUXRDb3JlcQlYCgAAAFFCeXRl
QXJyYXlxCkNCAdnQywADAAAAAAMLAAABpwAABHQAAAI5AAADDAAAAc0AAARzAAACOAAAAAAAAAAA
B4AAAAMMAAABzQAABHMAAAI4cQuFcQyHcQ1ScQ5YDgAAAHNldF9icmVha3BvaW50cQ+JdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWAgAAABtZXRhZGF0YXEFfXEGWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQdjc2lwCl91bnBpY2tsZV90eXBlCnEIWAwAAABQeVF0NS5RdENvcmVxCVgKAAAA
UUJ5dGVBcnJheXEKQ0IB2dDLAAMAAAAAAwwAAAHOAAAEcwAAAjcAAAMMAAABzgAABHMAAAI3AAAA
AAAAAAAHgAAAAwwAAAHOAAAEcwAAAjdxC4VxDIdxDVJxDlgOAAAAc2V0X2JyZWFrcG9pbnRxD4l1
Lg==
</properties>
		<properties format="literal" node_id="10">{'base': '(use default)', 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYDQAA
ACh1c2UgZGVmYXVsdClxBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABk
b250X3Jlc2V0X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWA8AAABmZWF0dXJlX3Nj
YWxpbmdxClgEAAAAbm9uZXELWAwAAABpbmNsdWRlX2JpYXNxDIhYDwAAAGluaXRpYWxpemVfb25j
ZXENiFgJAAAAbDFfcmF0aW9zcQ5oBVgIAAAAbWF4X2l0ZXJxD0tkWAgAAABtZXRhZGF0YXEQfXER
WAoAAABtdWx0aWNsYXNzcRJYBAAAAGF1dG9xE1gJAAAAbnVtX2ZvbGRzcRRLBVgIAAAAbnVtX2pv
YnNxFUsBWA0AAABwcm9iYWJpbGlzdGljcRaIWAsAAAByYW5kb21fc2VlZHEXTTkwWAsAAAByZWd1
bGFyaXplcnEYWAIAAABsMnEZWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRpjc2lwCl91bnBpY2ts
ZV90eXBlCnEbWAwAAABQeVF0NS5RdENvcmVxHFgKAAAAUUJ5dGVBcnJheXEdQ0IB2dDLAAMAAAAA
BLIAAAHWAAAGGwAAAtIAAASzAAAB/AAABhoAAALRAAAAAAAAAAAHgAAABLMAAAH8AAAGGgAAAtFx
HoVxH4dxIFJxIVgNAAAAc2VhcmNoX21ldHJpY3EiWAgAAABhY2N1cmFjeXEjWA4AAABzZXRfYnJl
YWtwb2ludHEkiVgGAAAAc29sdmVycSVYBAAAAGF1dG9xJlgJAAAAdG9sZXJhbmNlcSdHPxo24usc
Qy1YCQAAAHZlcmJvc2l0eXEoSwB1Lg==
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4hYDAAAAGN1c3RvbV9sYWJlbHEEWAAAAABxBVgIAAAAZGVj
aW1hbHNxBksDWAkAAABpbml0X2RhdGFxB11xCChYBAAAAE9wZW5xCVgFAAAAQ2xvc2VxCmVYCwAA
AGpvaW5fZm9ybWF0cQtYBQAAAHtuZXd9cQxYEQAAAGtlZXBfb3RoZXJfYXJyYXlzcQ2JWAoAAABr
ZWVwX3Byb3BzcQ6JWAgAAABtZXRhZGF0YXEPfXEQWAgAAABuZXdfYXhpc3ERWAcAAABmZWF0dXJl
cRJYCAAAAG9sZF9heGlzcRNYBwAAAGZlYXR1cmVxFFgMAAAAb25seV9zaWduYWxzcRWIWBMAAABz
YXZlZFdpZGdldEdlb21ldHJ5cRZjc2lwCl91bnBpY2tsZV90eXBlCnEXWAwAAABQeVF0NS5RdENv
cmVxGFgKAAAAUUJ5dGVBcnJheXEZQ0IB2dDLAAMAAAAABE8AAAF5AAAFuAAAAqcAAARQAAABnwAA
BbcAAAKmAAAAAAAAAAAHgAAABFAAAAGfAAAFtwAAAqZxGoVxG4dxHFJxHVgOAAAAc2V0X2JyZWFr
cG9pbnRxHolYCQAAAHZlcmJvc2l0eXEfSwB1Lg==
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWA8AAABhdXRvX2Jhcl9jb2xvcnNxAolYBAAAAGF4
aXNxA1gHAAAAZmVhdHVyZXEEWBAAAABiYWNrZ3JvdW5kX2NvbG9ycQVYBwAAACNGRkZGRkZxBlgJ
AAAAYmFyX2NvbG9ycQdYAQAAAGJxCFgJAAAAYmFyX3dpZHRocQlHP9UeuFHrhR9YCQAAAGZvbnRf
c2l6ZXEKR0AkAAAAAAAAWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksyTbwCTfQBZVgOAAAAaW5z
dGFuY2VfZmllbGRxDVgNAAAAKHVzZSBkZWZhdWx0KXEOWA4AAABsYWJlbF9yb3RhdGlvbnEPWAgA
AAB2ZXJ0aWNhbHEQWAgAAABtZXRhZGF0YXERfXESWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRNj
c2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENvcmVxFVgKAAAAUUJ5dGVBcnJheXEW
Q0IB2dDLAAMAAAAAAwwAAAFJAAAEcwAAArwAAAMMAAABSQAABHMAAAK8AAAAAAAAAAAHgAAAAwwA
AAFJAAAEcwAAArxxF4VxGIdxGVJxGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYDAAAAHNob3dfdG9v
bGJhcnEciVgLAAAAc3RyZWFtX25hbWVxHWgOWAUAAAB0aXRsZXEeWAAAAABxH1gRAAAAdXNlX2xh
c3RfaW5zdGFuY2VxIIhYBwAAAHZlcmJvc2VxIYlYCAAAAHlfbGltaXRzcSJdcSMoSs7///9LMmV1
Lg==
</properties>
		<properties format="literal" node_id="14">{'absolute_time': False, 'always_on_top': False, 'antialiased': True, 'auto_line_colors': False, 'autoscale': True, 'background_color': '#FFFFFF', 'decoration_color': '#000000', 'downsampled': False, 'font_size': 10.0, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'line_width': 0.75, 'marker_color': '#FF0000', 'metadata': {}, 'nans_as_zero': False, 'no_concatenate': False, 'override_srate': '(use default)', 'plot_markers': True, 'plot_minmax': False, 'savedWidgetGeometry': None, 'scale': 1.0, 'set_breakpoint': False, 'show_toolbar': False, 'stream_name': '(use default)', 'time_range': 5.0, 'title': 'Time series view', 'zero_color': '#7F7F7F', 'zeromean': True}</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYCAAAAG1ldGFkYXRhcQR9cQVYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUKcQdYDAAAAFB5UXQ1LlF0Q29yZXEIWAoAAABRQnl0
ZUFycmF5cQlDQgHZ0MsAAwAAAAADCwAAAbUAAAR0AAACKwAAAwwAAAHbAAAEcwAAAioAAAAAAAAA
AAeAAAADDAAAAdsAAARzAAACKnEKhXELh3EMUnENWA4AAABzZXRfYnJlYWtwb2ludHEOiVgOAAAA
d2FybXVwX3NhbXBsZXNxD0r/////dS4=
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAwAAABiZWdpbl9tYXJrZXJxAVgdAAAAQWN0aW9uQmVnLXBhbG1Eb3duLUxlZnQtQ2xv
c2VxAlgRAAAAY2FsaWJyYXRpb25fZmlyc3RxA4hYDwAAAGNhbl9yZWNhbGlicmF0ZXEEiVgPAAAA
ZW1pdF9jYWxpYl9kYXRhcQWIWBEAAABlbWl0X3ByZWRpY3RfZGF0YXEGiFgKAAAAZW5kX21hcmtl
cnEHWB4AAABBY3Rpb25CZWctcGFsbURvd24tUmlnaHQtQ2xvc2VxCFgLAAAAbWFya2VyX21vZGVx
CVgHAAAAbWFya2Vyc3EKWAgAAABtZXRhZGF0YXELfXEMWA0AAABwcmludF9tYXJrZXJzcQ2IWBMA
AABzYXZlZFdpZGdldEdlb21ldHJ5cQ5jc2lwCl91bnBpY2tsZV90eXBlCnEPWAwAAABQeVF0NS5R
dENvcmVxEFgKAAAAUUJ5dGVBcnJheXERQ0IB2dDLAAMAAAAAAwwAAAGaAAAEcwAAAmsAAAMMAAAB
mgAABHMAAAJrAAAAAAAAAAAHgAAAAwwAAAGaAAAEcwAAAmtxEoVxE4dxFFJxFVgOAAAAc2V0X2Jy
ZWFrcG9pbnRxFolYBwAAAHZlcmJvc2VxF4l1Lg==
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAkAAABmb250X3NpemVxC0dAJAAAAAAAAFgM
AAAAaW5pdGlhbF9kaW1zcQxdcQ0oSzJLMk28Ak30AWVYCgAAAGxpbmVfY29sb3JxDlgHAAAAIzAw
MDAwMHEPWAoAAABsaW5lX3dpZHRocRBHP+gAAAAAAABYDAAAAG1hcmtlcl9jb2xvcnERWAcAAAAj
RkYwMDAwcRJYCAAAAG1ldGFkYXRhcRN9cRRYDAAAAG5hbnNfYXNfemVyb3EViVgOAAAAbm9fY29u
Y2F0ZW5hdGVxFolYDgAAAG92ZXJyaWRlX3NyYXRlcRdYDQAAACh1c2UgZGVmYXVsdClxGFgMAAAA
cGxvdF9tYXJrZXJzcRmIWAsAAABwbG90X21pbm1heHEaiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEbY3NpcApfdW5waWNrbGVfdHlwZQpxHFgMAAAAUHlRdDUuUXRDb3JlcR1YCgAAAFFCeXRlQXJy
YXlxHkNCAdnQywADAAAAAAMLAAABAQAABHQAAALfAAADDAAAAScAAARzAAAC3gAAAAAAAAAAB4AA
AAMMAAABJwAABHMAAALecR+FcSCHcSFScSJYBQAAAHNjYWxlcSNHP/AAAAAAAABYDgAAAHNldF9i
cmVha3BvaW50cSSJWAwAAABzaG93X3Rvb2xiYXJxJYlYCwAAAHN0cmVhbV9uYW1lcSZoGFgKAAAA
dGltZV9yYW5nZXEnR0AUAAAAAAAAWAUAAAB0aXRsZXEoWBAAAABUaW1lIHNlcmllcyB2aWV3cSlY
CgAAAHplcm9fY29sb3JxKlgHAAAAIzdGN0Y3RnErWAgAAAB6ZXJvbWVhbnEsiHUu
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node1",
            "data",
            "node2",
            "data"
        ],
        [
            "node2",
            "data",
            "node3",
            "data"
        ],
        [
            "node6",
            "data",
            "node5",
            "data"
        ],
        [
            "node6",
            "data",
            "node18",
            "data"
        ],
        [
            "node5",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node7",
            "data"
        ],
        [
            "node7",
            "data",
            "node9",
            "data"
        ],
        [
            "node7",
            "data",
            "node15",
            "data"
        ],
        [
            "node9",
            "data",
            "node10",
            "data"
        ],
        [
            "node10",
            "data",
            "node11",
            "data"
        ],
        [
            "node11",
            "data",
            "node12",
            "data"
        ],
        [
            "node12",
            "data",
            "node13",
            "data"
        ],
        [
            "node13",
            "data",
            "node14",
            "data"
        ],
        [
            "node4",
            "data",
            "node16",
            "data"
        ],
        [
            "node16",
            "data",
            "node17",
            "data"
        ],
        [
            "node17",
            "data",
            "node6",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/studies/college/IIT Gandhinagar/SEM III/CG 599 Thesis/Grasp Experiment/Experimental Data/EEG/P02.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "cbe55b2a-a8c2-4f8d-96ee-26e086fb61b1"
        },
        "node10": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "652f7c9b-cc7b-42c4-9943-62260fa7489a"
        },
        "node11": {
            "class": "Logarithm",
            "module": "neuropype.nodes.elementwise_math.Logarithm",
            "params": {
                "base": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f9f46200-6461-4d37-8579-a005c64a6d48"
        },
        "node12": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "feature_scaling": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "none"
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "l1_ratios": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "multiclass": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "random_seed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 12345
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "e0beb67e-120c-42f6-9a2b-2298d1b62de6"
        },
        "node13": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Open",
                        "Close"
                    ]
                },
                "join_format": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "{new}"
                },
                "keep_other_arrays": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_props": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "21612da2-911b-442f-aeaa-0e8e78a825ea"
        },
        "node14": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "auto_bar_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.33
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "vertical"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "y_limits": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        -50,
                        50
                    ]
                }
            },
            "uuid": "76949984-6c05-4c4c-a0c3-96e8925c6c1d"
        },
        "node15": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "9204649c-24d6-48db-b884-90eb36ea77ca"
        },
        "node16": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "56977092-c420-4767-828b-26f62320578f"
        },
        "node17": {
            "class": "AccumulateCalibrationData",
            "module": "neuropype.nodes.machine_learning.AccumulateCalibrationData",
            "params": {
                "begin_marker": {
                    "customized": true,
                    "type": "Port",
                    "value": "ActionBeg-palmDown-Left-Close"
                },
                "calibration_first": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "can_recalibrate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "emit_calib_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "emit_predict_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "end_marker": {
                    "customized": true,
                    "type": "Port",
                    "value": "ActionBeg-palmDown-Right-Close"
                },
                "marker_mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "markers"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "print_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "281397a9-bae8-43ff-811a-e022df93813a"
        },
        "node18": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "31b8f30e-f09f-470f-86a5-05c059535e78"
        },
        "node2": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "log_progress": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "373a9037-a2ca-481e-98d0-b7da55610bd7"
        },
        "node3": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "GraspStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "GraspStream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "79ceeb3e-a7bf-4d34-afd5-7001e8cf4b1c"
        },
        "node4": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "ch0",
                        "ch1",
                        "ch2",
                        "ch3",
                        "ch4",
                        "ch5",
                        "ch6",
                        "ch7",
                        "ch8",
                        "ch9",
                        "ch10",
                        "ch11",
                        "ch12",
                        "ch13",
                        "ch14",
                        "ch15",
                        "ch16",
                        "ch17",
                        "ch18",
                        "ch19",
                        "ch20",
                        "ch21",
                        "ch22",
                        "ch23",
                        "ch24",
                        "ch25",
                        "ch26",
                        "ch27",
                        "ch28",
                        "ch29",
                        "ch30",
                        "ch31",
                        "ch32",
                        "ch33",
                        "ch34",
                        "ch35",
                        "ch36",
                        "ch37",
                        "ch38",
                        "ch39",
                        "ch40",
                        "ch41",
                        "ch42",
                        "ch43",
                        "ch44",
                        "ch45",
                        "ch46",
                        "ch47",
                        "ch48",
                        "ch49",
                        "ch50",
                        "ch51",
                        "ch52",
                        "ch53",
                        "ch54",
                        "ch55",
                        "ch56",
                        "ch57",
                        "ch58",
                        "ch59",
                        "ch60",
                        "ch61",
                        "ch62",
                        "ch63"
                    ]
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='GraspStream-markers'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "type='EEG'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "0d294378-0847-4f24-95b8-bb766ba834dc"
        },
        "node5": {
            "class": "IIRFilter",
            "module": "neuropype.nodes.signal_processing.IIRFilter",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "design": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "butter"
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        3,
                        3.5
                    ]
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "offline_filtfilt": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "pass_loss": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 3.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "c6450435-4950-4bbc-8421-dcbbaf6d9809"
        },
        "node6": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "apply_time_selection_to_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        0,
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16,
                        17,
                        18,
                        19,
                        20,
                        21,
                        22,
                        23,
                        24,
                        45,
                        46,
                        47,
                        48,
                        49,
                        50,
                        51,
                        52,
                        53,
                        54,
                        55,
                        56,
                        57,
                        58,
                        59,
                        60,
                        61,
                        62,
                        63
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "849f1216-cdc1-41b5-9f03-453cd3710f75"
        },
        "node7": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "online_epoching": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "marker-locked"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": true,
                    "type": "ListPort",
                    "value": []
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        -0.25,
                        1.5
                    ]
                },
                "verbose": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "60991374-82cc-4b3d-bf8b-0519f406d1a5"
        },
        "node8": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "ActionBeg-palmDown-Left-Close": 0,
                        "ActionBeg-palmDown-Left-Open": 1,
                        "ActionBeg-palmDown-Right-Close": 0,
                        "ActionBeg-palmDown-Right-Open": 1,
                        "ActionBeg-palmIn-Left-Close": 0,
                        "ActionBeg-palmIn-Left-Open": 1,
                        "ActionBeg-palmIn-Right-Close": 0,
                        "ActionBeg-palmIn-Right-Open": 1,
                        "ActionBeg-palmUp-Left-Close": 0,
                        "ActionBeg-palmUp-Left-Open": 1,
                        "ActionBeg-palmUp-Right-Close": 0,
                        "ActionBeg-palmUp-Right-Open": 1
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c89b2588-c4f4-4e05-8fe7-e81a4980170c"
        },
        "node9": {
            "class": "CommonSpatialPatterns",
            "module": "neuropype.nodes.neural.CommonSpatialPatterns",
            "params": {
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nof": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 4
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "52fcda12-1e3e-4121-a595-3a767a8d8929"
        }
    },
    "version": 1.1
}</patch>
</scheme>
