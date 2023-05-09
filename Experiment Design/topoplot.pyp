<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="topoplot" version="2.0">
	<nodes>
		<node id="0" name="Import XDF" position="(119.0, 443.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="4351fd59-be99-4b74-bab9-4dc3c21330b3" version="1.2.1" />
		<node id="1" name="Streaming TopoPlot" position="(660.0, 441.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owtopoplotviewer.OWTopoPlotViewer" title="Streaming TopoPlot" uuid="cc32e682-93de-4e61-9131-2216b1d2ce00" version="1.1.0" />
		<node id="2" name="Stream Data" position="(419.0, 440.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="b14d1227-f166-4f06-8ce2-d8becae5e83f" version="1.2.1" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="2" />
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
		<properties format="pickle" node_id="1">gAN9cQAoWAwAAABhZGRfY29sb3JiYXJxAYhYDQAAAGFsd2F5c19vbl90b3BxAolYEAAAAGJhY2tn
cm91bmRfY29sb3JxA1gFAAAAd2hpdGVxBFgKAAAAY2FudmFzX2RwaXEFS2RYDAAAAGNhbnZhc19z
aXplc3EGXXEHKEsHR0AVAAAAAAAAZVgWAAAAY29sb3JfYmFyX3RpY2tzX2xhYmVsc3EIWA0AAAAo
dXNlIGRlZmF1bHQpcQlYFgAAAGNvbG9yX2Jhcl90aWNrc192YWx1ZXNxCmgJWAsAAABjb2xvcl9y
YW5nZXELXXEMKFgDAAAAcmVkcQ1YBQAAAGdyZWVucQ5lWBAAAABjb2xvcl9yYW5nZV9jb250cQ9Y
BgAAAFJkWWxHbnEQWAoAAABkaXNrX3NjYWxlcRFLllgPAAAAaGVhZF9heGVzX3NjZmFjcRJHP/TM
zMzMzM1YCgAAAGhlYWRfY29sb3JxE1gFAAAAYmxhY2txFFgPAAAAaGVhZF9saW5lX3dpZHRocRVL
AlgLAAAAaGVhZF9vcHRpb25xFohYCAAAAGhlYWRfcmFkcRdHP+AAAAAAAABYDwAAAGhlYWRfcmlu
Z193aWR0aHEYRz98rAgxJul5WAwAAABpbml0aWFsX2RpbXNxGV1xGihLMksyTbwCTfQBZVgIAAAA
bWV0YWRhdGFxG31xHFgIAAAAcGxvdF9yYWRxHWgJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cR5j
c2lwCl91bnBpY2tsZV90eXBlCnEfWAwAAABQeVF0NS5RdENvcmVxIFgKAAAAUUJ5dGVBcnJheXEh
Q0IB2dDLAAMAAAAAAwsAAAEkAAAEdAAAArwAAAMMAAABSgAABHMAAAK7AAAAAAAAAAAHgAAAAwwA
AAFKAAAEcwAAArtxIoVxI4dxJFJxJVgOAAAAc2V0X2JyZWFrcG9pbnRxJolYDAAAAHNob3dfdG9v
bGJhcnEniVgFAAAAdGl0bGVxKFgVAAAARWxlY3Ryb2RlIE1ldHJpYyBQbG90cSlYEwAAAHVzZV9j
dXN0b21fY29sb3JtYXBxKolYDgAAAHZhbHVlX2Rpc2NyZXRlcSuJWAsAAAB2YWx1ZV9yYW5nZXEs
XXEtKEc/7mZmZmZmZkc/8AAAAAAAAGV1Lg==
</properties>
		<properties format="literal" node_id="2">{'data_dtype': 'float64', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
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
            "node3",
            "data"
        ],
        [
            "node3",
            "data",
            "node2",
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
            "uuid": "4351fd59-be99-4b74-bab9-4dc3c21330b3"
        },
        "node2": {
            "class": "TopoPlotViewer",
            "module": "neuropype.nodes.visualization.TopoPlotViewer",
            "params": {
                "add_colorbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "white"
                },
                "canvas_dpi": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "canvas_sizes": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        7,
                        5.25
                    ]
                },
                "color_bar_ticks_labels": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "color_bar_ticks_values": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "color_range": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        "red",
                        "green"
                    ]
                },
                "color_range_cont": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "RdYlGn"
                },
                "disk_scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 150
                },
                "head_axes_scfac": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.3
                },
                "head_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "black"
                },
                "head_line_width": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 2
                },
                "head_option": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "head_rad": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "head_ring_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.007
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
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "plot_rad": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
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
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Electrode Metric Plot"
                },
                "use_custom_colormap": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "value_discrete": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "value_range": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.95,
                        1.0
                    ]
                }
            },
            "uuid": "cc32e682-93de-4e61-9131-2216b1d2ce00"
        },
        "node3": {
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
            "uuid": "b14d1227-f166-4f06-8ce2-d8becae5e83f"
        }
    },
    "version": 1.1
}</patch>
</scheme>
