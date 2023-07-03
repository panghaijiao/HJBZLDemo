load("@build_bazel_rules_apple//apple:ios.bzl", "ios_application")
load(
    "@rules_xcodeproj//xcodeproj:defs.bzl",
    "top_level_target",
    "xcodeproj",
)

objc_library(
    name = "app",
    srcs = [
         "app/AppDelegate.m",
         "app/UrlGetViewController.m",
         "app/main.m",
    ],
    hdrs = glob(["app/*.h"]),
)

ios_application(
    name = "ios-app",
    bundle_id = "com.olinone",
    families = [
        "iphone"
    ],
    infoplists = [":app/app-Info.plist"],
    launch_storyboard = "app/UrlGetViewController.xib",
    minimum_os_version = "13.0",
    visibility = ["//visibility:public"],
    deps = [
        ":app",
        "//srcs/OCModule:oc_module",
    ],
)

xcodeproj(
    name = "xcodeproj",
    build_mode = "bazel",
    project_name = "ios-app",
    tags = ["manual"],
    top_level_targets = [
        ":ios-app",
    ],
)
