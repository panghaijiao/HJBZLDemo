load("@rules_cc//cc:defs.bzl", "objc_library")

package(default_visibility = [
    "//visibility:public"
])

objc_library(
    name = "oc_module",
    module_name = "OCModule",
    hdrs = glob([
        "include/**/*.h",
    ]),
    srcs = glob([
        "srcs/**/*.m",
    ]),
    copts = [
        "-iquote srcs/OCModule/include/OCModule",
    ],
    includes = ["include"],
    deps = [
        
    ],
)
