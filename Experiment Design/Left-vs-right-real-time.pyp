<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="Left-vs-right-real-time" version="2.0">
	<nodes>
		<node id="0" name="Import XDF" position="(123.0, 607.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="4b7eacc7-e2ad-4eca-ac8a-e40a72aa799c" version="1.2.1" />
		<node id="1" name="Stream Data" position="(331.0, 607.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="f6faa187-6dbc-4c5d-98e9-e0254d5af240" version="1.2.1" />
		<node id="2" name="LSL Output" position="(537.0, 607.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="486f2f90-088f-4a16-9ed1-5fadbc1f11a3" version="1.4.2" />
		<node id="3" name="LSL Input" position="(110.0, 298.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="155258dd-5e7f-4840-b135-459c95d130f5" version="1.5.1" />
		<node id="4" name="Accumulate Calibration Data" position="(293.0, 298.0)" project_name="NeuroPype" qualified_name="widgets.deprecated.owaccumulatecalibrationdatamultiemit.OWAccumulateCalibrationDataMultiEmit" title="Accumulate Calibration Data" uuid="51553390-4861-459e-9cee-5359c6786b82" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="3" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWF8AAABFOi9zdHVkaWVzL2NvbGxlZ2UvSUlUIEdhbmRoaW5hZ2FyL1NFTSBJ
SUkvQ0cgNTk5IFRoZXNpcy9HcmFzcCBFeHBlcmltZW50L2xlZnQtdnMtcmlnaHQvUDAzLnhkZnEI
WBMAAABoYW5kbGVfY2xvY2tfcmVzZXRzcQmIWBEAAABoYW5kbGVfY2xvY2tfc3luY3EKiFgVAAAA
aGFuZGxlX2ppdHRlcl9yZW1vdmFscQuIWA4AAABtYXhfbWFya2VyX2xlbnEMWA0AAAAodXNlIGRl
ZmF1bHQpcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YEgAAAHJlb3JkZXJfdGltZXN0YW1wc3EQiVgOAAAA
cmV0YWluX3N0cmVhbXNxEWgNWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRJjc2lwCl91bnBpY2ts
ZV90eXBlCnETWAwAAABQeVF0NS5RdENvcmVxFFgKAAAAUUJ5dGVBcnJheXEVQ0IB2dDLAAMAAAAA
AwsAAAFiAAAEdAAAAn4AAAMMAAABiAAABHMAAAJ9AAAAAAAAAAAHgAAAAwwAAAGIAAAEcwAAAn1x
FoVxF4dxGFJxGVgOAAAAc2V0X2JyZWFrcG9pbnRxGolYCwAAAHVzZV9jYWNoaW5ncRuJWA8AAAB1
c2Vfc3RyZWFtbmFtZXNxHIlYBwAAAHZlcmJvc2VxHYl1Lg==
</properties>
		<properties format="literal" node_id="1">{'data_dtype': 'float64', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgQAAAAbW92ZW1lbnQtbWFya2Vyc3EHWBAAAABtYXJrZXJfc291cmNl
X2lkcQhYAAAAAHEJWAwAAABtYXhfYnVmZmVyZWRxCks8WAgAAABtZXRhZGF0YXELfXEMWBcAAABu
dW1lcmljX2xhYmVsX3ByZWNpc2lvbnENSwFYGAAAAG51bWVyaWNfbWFya2VyX3ByZWNpc2lvbnEO
SwNYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFuZ2VkcQ+JWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5
cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NS5RdENvcmVxElgKAAAAUUJ5dGVBcnJh
eXETQ0IB2dDLAAMAAAAAAwwAAAD5AAAEcwAAAwwAAAMMAAAA+QAABHMAAAMMAAAAAAAAAAAHgAAA
AwwAAAD5AAAEcwAAAwxxFIVxFYdxFlJxF1gMAAAAc2VuZF9tYXJrZXJzcRiIWAkAAABzZXBhcmF0
b3JxGVgBAAAALXEaWA4AAABzZXRfYnJlYWtwb2ludHEbiVgJAAAAc291cmNlX2lkcRxoCVgFAAAA
c3JhdGVxHVgNAAAAKHVzZSBkZWZhdWx0KXEeWAsAAABzdHJlYW1fbmFtZXEfWAwAAABHcmFzcC1z
dHJlYW1xIFgLAAAAc3RyZWFtX3R5cGVxIVgDAAAARUVHcSJYEwAAAHVzZV9kYXRhX3RpbWVzdGFt
cHNxI4hYFgAAAHVzZV9udW1weV9vcHRpbWl6YXRpb25xJIl1Lg==
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgXAAAAbmFtZT0nbW92ZW1lbnQtbWFya2VycydxCVgMAAAAbWF4X2Jsb2Nr
bGVucQpNAARYCgAAAG1heF9idWZsZW5xC0seWAwAAABtYXhfY2h1bmtsZW5xDEsAWAgAAABtZXRh
ZGF0YXENfXEOWAwAAABub21pbmFsX3JhdGVxD1gNAAAAKHVzZSBkZWZhdWx0KXEQWAkAAABvbWl0
X2Rlc2NxEYlYDwAAAHByZWFsbG9jX2J1ZmZlcnESiFgOAAAAcHJvY19jbG9ja3N5bmNxE4hYDQAA
AHByb2NfZGVqaXR0ZXJxFIlYDwAAAHByb2NfbW9ub3Rvbml6ZXEViVgPAAAAcHJvY190aHJlYWRz
YWZlcRaJWAUAAABxdWVyeXEXWAoAAAB0eXBlPSdFRUcncRhYBwAAAHJlY292ZXJxGYhYFAAAAHJl
c29sdmVfbWluaW11bV90aW1lcRpHP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxG2Nz
aXAKX3VucGlja2xlX3R5cGUKcRxYDAAAAFB5UXQ1LlF0Q29yZXEdWAoAAABRQnl0ZUFycmF5cR5D
QgHZ0MsAAwAAAAADDAAAAV0AAARzAAACqAAAAwwAAAFdAAAEcwAAAqgAAAAAAAAAAAeAAAADDAAA
AV0AAARzAAACqHEfhXEgh3EhUnEiWA4AAABzZXRfYnJlYWtwb2ludHEjiXUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAwAAABiZWdpbl9tYXJrZXJxAUsKWA8AAABidWZmZXJfZHVyYXRpb25xAkdAPgAAAAAA
AFgRAAAAY2FsaWJyYXRpb25fZmlyc3RxA4hYDwAAAGNhbl9yZWNhbGlicmF0ZXEEiVgPAAAAZW1p
dF9jYWxpYl9kYXRhcQWIWBUAAABlbWl0X2lmX3VucmVwcmVzZW50ZWRxBolYEQAAAGVtaXRfcHJl
ZGljdF9kYXRhcQeIWBQAAABlbWl0X3doaWxlX2J1ZmZlcmluZ3EIiVgKAAAAZW5kX21hcmtlcnEJ
S2RYFAAAAGVxdWFsX3JlcHJlc2VudGF0aW9ucQpdcQtYCwAAAG1hcmtlcl9tb2RlcQxYDgAAAHJl
bGF0aXZlLXRpbWVzcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YDQAAAHByaW50X21hcmtlcnNxEIlYEwAA
AHNhdmVkV2lkZ2V0R2VvbWV0cnlxEWNzaXAKX3VucGlja2xlX3R5cGUKcRJYDAAAAFB5UXQ1LlF0
Q29yZXETWAoAAABRQnl0ZUFycmF5cRRDQgHZ0MsAAwAAAAAFQwAAAS0AAAasAAACjQAABUQAAAFT
AAAGqwAAAowAAAAAAAAAAAeAAAAFRAAAAVMAAAarAAACjHEVhXEWh3EXUnEYWA4AAABzZXRfYnJl
YWtwb2ludHEZiVgHAAAAdmVyYm9zZXEaiXUu
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
            "node4",
            "data",
            "node5",
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
                    "value": "E:/studies/college/IIT Gandhinagar/SEM III/CG 599 Thesis/Grasp Experiment/left-vs-right/P03.xdf"
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
            "uuid": "4b7eacc7-e2ad-4eca-ac8a-e40a72aa799c"
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
            "uuid": "f6faa187-6dbc-4c5d-98e9-e0254d5af240"
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
                    "value": "movement-markers"
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
                    "value": "Grasp-stream"
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
            "uuid": "486f2f90-088f-4a16-9ed1-5fadbc1f11a3"
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
                    "value": "name='movement-markers'"
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
            "uuid": "155258dd-5e7f-4840-b135-459c95d130f5"
        },
        "node5": {
            "class": "AccumulateCalibrationDataMultiEmit",
            "module": "neuropype.nodes.deprecated.AccumulateCalibrationDataMultiEmit",
            "params": {
                "begin_marker": {
                    "customized": true,
                    "type": "Port",
                    "value": 10
                },
                "buffer_duration": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 30.0
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
                "emit_if_unrepresented": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "emit_predict_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "emit_while_buffering": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "end_marker": {
                    "customized": true,
                    "type": "Port",
                    "value": 100
                },
                "equal_representation": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "marker_mode": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "relative-times"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
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
            "uuid": "51553390-4861-459e-9cee-5359c6786b82"
        }
    },
    "version": 1.1
}</patch>
</scheme>
