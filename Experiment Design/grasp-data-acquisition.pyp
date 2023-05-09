<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="grasp-data-acquisition" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(264.0, 327.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="be23ee41-e9f7-438a-be60-3276d96309bf" version="1.5.1" />
		<node id="1" name="Time Series Plot" position="(490.0, 458.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="6125b5c6-5484-45f0-ab57-fe7fbe80cbcd" version="1.0.3" />
		<node id="2" name="Marker Stream Window" position="(501.0, 189.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owmarkerstreamwindow.OWMarkerStreamWindow" title="Marker Stream Window" uuid="4e86a6f4-45c8-41f4-bfa9-3f959f556e2e" version="1.0.1" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgOAAAAdHlwZT0nTWFya2VycydxCVgMAAAAbWF4X2Jsb2NrbGVucQpNAARY
CgAAAG1heF9idWZsZW5xC0seWAwAAABtYXhfY2h1bmtsZW5xDEsAWAgAAABtZXRhZGF0YXENfXEO
WAwAAABub21pbmFsX3JhdGVxD1gNAAAAKHVzZSBkZWZhdWx0KXEQWAkAAABvbWl0X2Rlc2NxEYlY
DwAAAHByZWFsbG9jX2J1ZmZlcnESiFgOAAAAcHJvY19jbG9ja3N5bmNxE4hYDQAAAHByb2NfZGVq
aXR0ZXJxFIlYDwAAAHByb2NfbW9ub3Rvbml6ZXEViVgPAAAAcHJvY190aHJlYWRzYWZlcRaJWAUA
AABxdWVyeXEXWAwAAAB0eXBlPSdBdWRpbydxGFgHAAAAcmVjb3ZlcnEZiFgUAAAAcmVzb2x2ZV9t
aW5pbXVtX3RpbWVxGkc/4AAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEbY3NpcApfdW5w
aWNrbGVfdHlwZQpxHFgMAAAAUHlRdDUuUXRDb3JlcR1YCgAAAFFCeXRlQXJyYXlxHkNCAdnQywAD
AAAAAAMLAAABNwAABHQAAAKpAAADDAAAAV0AAARzAAACqAAAAAAAAAAAB4AAAAMMAAABXQAABHMA
AAKocR+FcSCHcSFScSJYDgAAAHNldF9icmVha3BvaW50cSOJdS4=
</properties>
		<properties format="literal" node_id="1">{'absolute_time': False, 'always_on_top': False, 'antialiased': True, 'auto_line_colors': False, 'autoscale': True, 'background_color': '#FFFFFF', 'decoration_color': '#000000', 'downsampled': False, 'font_size': 10.0, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'line_width': 0.75, 'marker_color': '#FF0000', 'metadata': {}, 'nans_as_zero': False, 'no_concatenate': False, 'override_srate': '(use default)', 'plot_markers': True, 'plot_minmax': False, 'savedWidgetGeometry': None, 'scale': 1.0, 'set_breakpoint': False, 'show_toolbar': False, 'stream_name': '(use default)', 'time_range': 5.0, 'title': 'Time series view', 'zero_color': '#7F7F7F', 'zeromean': True}</properties>
		<properties format="literal" node_id="2">{'always_on_top': False, 'initial_dims': [50, 50, 500, 500], 'metadata': {}, 'override_srate': '(use default)', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'stream_name': 'Markers'}</properties>
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
            "node1",
            "data",
            "node3",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Unknown1"
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
                    "value": "type='Markers'"
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
                    "customized": true,
                    "type": "StringPort",
                    "value": "type='Audio'"
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
            "uuid": "be23ee41-e9f7-438a-be60-3276d96309bf"
        },
        "node2": {
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
            "uuid": "6125b5c6-5484-45f0-ab57-fe7fbe80cbcd"
        },
        "node3": {
            "class": "MarkerStreamWindow",
            "module": "neuropype.nodes.visualization.MarkerStreamWindow",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        500,
                        500
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Markers"
                }
            },
            "uuid": "4e86a6f4-45c8-41f4-bfa9-3f959f556e2e"
        }
    },
    "version": 1.1
}</patch>
</scheme>
