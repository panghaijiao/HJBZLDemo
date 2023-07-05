#!/usr/bin/python3

"""An lldb module that registers a stop hook to set swift settings."""

import lldb
import re

# Order matters, it needs to be from the most nested to the least
_BUNDLE_EXTENSIONS = [
    ".framework",
    ".xctest",
    ".appex",
    ".bundle",
    ".app",
]

_TRIPLE_MATCH = re.compile(r"([^-]+-[^-]+)(-\D+)[^-]*(-.*)?")

_SETTINGS = {
	"arm64-apple-ios HJBZLDemo.app/HJBZLDemo": {
		"c": "-I$(PROJECT_DIR)/srcs/base/Masonry/Public -I$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin/srcs/base/Masonry/Public -I$(PROJECT_DIR)/external/rxswift~6.5.0/Sources/RxCocoaRuntime/include -I$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin/external/rxswift~6.5.0/Sources/RxCocoaRuntime/include -iquote$(PROJECT_DIR) -iquote$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin -iquote$(PROJECT_DIR)/external/rxswift~6.5.0 -iquote$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin/external/rxswift~6.5.0 -DSWIFT_PACKAGE -fmodule-map-file=$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin/srcs/base/Masonry/Masonry_library.swift.modulemap -fmodule-map-file=$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin/external/rxswift~6.5.0/RxCocoaRuntime.swift.modulemap -O0 -DDEBUG=1 -fstack-protector -fstack-protector-all -iquote$(PROJECT_DIR)/external/rxswift~6.5.0 -iquote$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin/external/rxswift~6.5.0 -iquote$(PROJECT_DIR) -iquote$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin -O0 -fstack-protector -fstack-protector-all -iquote$(PROJECT_DIR) -iquote$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin -O0 -fstack-protector -fstack-protector-all -iquote$(PROJECT_DIR) -iquote$(PROJECT_DIR)/bazel-out/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin -O0 -fstack-protector -fstack-protector-all",
		"s": [
			"$(BAZEL_OUT)/ios-arm64-min13.0-applebin_ios-ios_arm64-dbg-ST-b7b01a732717/bin/external/rxswift~6.5.0"
		]
	},
	"arm64-apple-ios-simulator HJBZLDemo.app/HJBZLDemo": {
		"c": "-I$(PROJECT_DIR)/srcs/base/Masonry/Public -I$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin/srcs/base/Masonry/Public -I$(PROJECT_DIR)/external/rxswift~6.5.0/Sources/RxCocoaRuntime/include -I$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin/external/rxswift~6.5.0/Sources/RxCocoaRuntime/include -iquote$(PROJECT_DIR) -iquote$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin -iquote$(PROJECT_DIR)/external/rxswift~6.5.0 -iquote$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin/external/rxswift~6.5.0 -DSWIFT_PACKAGE -fmodule-map-file=$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin/srcs/base/Masonry/Masonry_library.swift.modulemap -fmodule-map-file=$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin/external/rxswift~6.5.0/RxCocoaRuntime.swift.modulemap -O0 -DDEBUG=1 -fstack-protector -fstack-protector-all -iquote$(PROJECT_DIR)/external/rxswift~6.5.0 -iquote$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin/external/rxswift~6.5.0 -iquote$(PROJECT_DIR) -iquote$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin -O0 -fstack-protector -fstack-protector-all -iquote$(PROJECT_DIR) -iquote$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin -O0 -fstack-protector -fstack-protector-all -iquote$(PROJECT_DIR) -iquote$(PROJECT_DIR)/bazel-out/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin -O0 -fstack-protector -fstack-protector-all",
		"s": [
			"$(BAZEL_OUT)/ios-sim_arm64-min13.0-applebin_ios-ios_sim_arm64-dbg-ST-91e997dce7f3/bin/external/rxswift~6.5.0"
		]
	}
}

def __lldb_init_module(debugger, _internal_dict):
    # Register the stop hook when this module is loaded in lldb
    ci = debugger.GetCommandInterpreter()
    res = lldb.SBCommandReturnObject()
    ci.HandleCommand(
        "target stop-hook add -P swift_debug_settings.StopHook",
        res,
    )
    if not res.Succeeded():
        print(f"""\
Failed to register Swift debug options stop hook:

{res.GetError()}
Please file a bug report here: \
https://github.com/MobileNativeFoundation/rules_xcodeproj/issues/new?template=bug.md
""")
        return

def _get_relative_executable_path(module):
    for extension in _BUNDLE_EXTENSIONS:
        prefix, _, suffix = module.rpartition(extension)
        if prefix:
            return prefix.split("/")[-1] + extension + suffix
    return module.split("/")[-1]

class StopHook:
    "An lldb stop hook class, that sets swift settings for the current module."

    def __init__(self, _target, _extra_args, _internal_dict):
        pass

    def handle_stop(self, exe_ctx, _stream):
        "Method that is called when the user stops in lldb."
        module = exe_ctx.frame.module
        if not module:
            return

        module_name = module.file.__get_fullpath__()
        versionless_triple = _TRIPLE_MATCH.sub(r"\1\2\3", module.GetTriple())
        executable_path = _get_relative_executable_path(module_name)
        key = f"{versionless_triple} {executable_path}"

        settings = _SETTINGS.get(key)

        if settings:
            frameworks = " ".join([
                f'"{path}"'
                for path in settings.get("f", [])
            ])
            if frameworks:
                lldb.debugger.HandleCommand(
                    f"settings set -- target.swift-framework-search-paths {frameworks}",
                )
            else:
                lldb.debugger.HandleCommand(
                    "settings clear target.swift-framework-search-paths",
                )

            includes = " ".join([
                f'"{path}"'
                for path in settings.get("s", [])
            ])
            if includes:
                lldb.debugger.HandleCommand(
                    f"settings set -- target.swift-module-search-paths {includes}",
                )
            else:
                lldb.debugger.HandleCommand(
                    "settings clear target.swift-module-search-paths",
                )

            clang = settings.get("c")
            if clang:
                lldb.debugger.HandleCommand(
                    f"settings set -- target.swift-extra-clang-flags '{clang}'",
                )
            else:
                lldb.debugger.HandleCommand(
                    "settings clear target.swift-extra-clang-flags",
                )

        return True
