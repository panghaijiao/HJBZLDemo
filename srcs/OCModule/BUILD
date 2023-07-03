load("@rules_cc//cc:defs.bzl", "objc_library")

package(default_visibility = ["//visibility:public"])

objc_library(
    name = "oc_module",
    module_name = "OCModule",
    srcs = glob([
        "**/*.h",
        "**/*.m",
        "**/*.mm",
    ]),
    hdrs = glob([
        "**/*.h",
    ]),
)
