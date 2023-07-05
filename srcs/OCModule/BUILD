load("@rules_cc//cc:defs.bzl", "objc_library")

package(default_visibility = ["//visibility:public"])

objc_library(
    name = "oc_module",
    module_name = "OCModule",
    hdrs = glob([
        "**/*.h",
    ]),
    srcs = glob([
        "**/*.h",
        "**/*.m",
    ]),
    deps = [
        "//srcs/base/Masonry:Masonry_library",
        "//srcs/SwiftModule:swift_module",
    ],
)
