load("@build_bazel_rules_apple//apple:ios.bzl", "ios_application")
load(
    "@rules_xcodeproj//xcodeproj:defs.bzl",
    "top_level_target",
    "xcodeproj",
)

objc_library(
    name = "app",
    srcs = glob([
        "app/**/*.m",
    ]),
    hdrs = glob(["app/*.h"]),
    deps = [
        "//srcs/MixModule:mix_module",
    ],
)

ios_application(
    name = "HJBZLDemo",
    bundle_id = "com.olinone.HJBZLDemo",
    families = [
        "iphone"
    ],
    infoplists = [":app/app-Info.plist"],
    launch_storyboard = "app/LaunchScreen.storyboard",
    minimum_os_version = "13.0",
    provisioning_profile = "App_custom.mobileprovision",
    visibility = ["//visibility:public"],
    deps = [
        ":app",
    ],
)

xcodeproj(
    name = "xcodeproj",
    build_mode = "bazel",
    project_name = "HJBZLDemo",
    tags = ["manual"],
    top_level_targets = [
        top_level_target(":HJBZLDemo", target_environments = ["device", "simulator"]),
    ],
)
