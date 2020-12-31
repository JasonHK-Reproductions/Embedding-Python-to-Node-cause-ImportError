{
    "targets": [
        {
            "target_name": "binding",
            "sources": ["./binding.cpp"],
            "defines": [
                "NAPI_CPP_EXCEPTIONS"
            ],
            "libraries": [
                "<!@(python3.8-config --embed --libs)"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include_dir\")",
                "<!@(python3.8-config --embed --includes | sed s/-I//g)"
            ],
            "link_settings": {
                "libraries": [
                    "<!@(python3.8-config --embed --libs)"
                ],
            },
            "cflags": [
                "-fPIC",
                "<!@(python3.8-config --embed --cflags)"
            ],
            "cflags!": [
                "-fno-exceptions"
            ],
            "cflags_cc!": [
                "-fno-exceptions"
            ]
        }
    ]
}
